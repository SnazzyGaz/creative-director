#!/usr/bin/env python3
"""whites.py: how white are the whites? Measures the lightest 0.5% of every blind-test image (CV-11).

  python3 examples/blind-test/whites.py [--images examples/blind-test/images]

Uses tools/autocheck.py's white_point(): luma at the 99.5th percentile (0-255), and the median channel spread
(max - min) and blue minus red of the pixels at or above it. Reports each arm, the pairs brief by brief, and
the with-skill images split by whether their prompt named a cream, off-white or warm-white ground or type.
The images are not in git; whoever has them can re-run this."""
import argparse, json, pathlib, re, sys
import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from autocheck import white_point, WHITE_MIN, TOP_SPREAD  # noqa: E402

WARM = re.compile(r"cream|off-white|off white|warm white|pale warm|ivory|parchment|warm paper", re.I)

def summary(label, vals):
    v = np.array(vals)
    print(f"  {label}: n {len(v)}, median luma {np.median(v[:, 0]):.1f}, median spread {np.median(v[:, 1]):.0f}, "
          f"median blue minus red {np.median(v[:, 2]):+.0f}, under {WHITE_MIN}: {(v[:, 0] < WHITE_MIN).sum()}, "
          f"under 240: {(v[:, 0] < 240).sum()}, spread over {TOP_SPREAD}: {(v[:, 1] > TOP_SPREAD).sum()}")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--images", type=pathlib.Path, default=HERE / "images"); a = ap.parse_args()
    briefs = {b["id"]: b for b in json.load(open(HERE / "briefs.json"))}
    m = {}
    for bid in briefs:
        for c in ("with", "without"):
            f = a.images / f"{bid}-{c}.jpg"
            if not f.exists(): sys.exit(f"missing {f}")
            m[bid, c] = white_point(np.asarray(Image.open(f).convert("RGB")).astype(float))
    print("lightest 0.5% of each image")
    for c in ("with", "without"): summary(c + " the skill", [m[b, c] for b in briefs])
    lo = sum(m[b, "with"][0] < m[b, "without"][0] - 1 for b in briefs); hi = sum(m[b, "with"][0] > m[b, "without"][0] + 1 for b in briefs)
    print(f"  pairs: with-skill white lower in {lo} briefs, higher in {hi}, within 1 in {len(briefs) - lo - hi}")
    warm = [b for b in briefs if WARM.search(briefs[b]["with"])]
    print(f"with-skill prompts naming cream, off-white or warm white: {len(warm)} of {len(briefs)} "
          f"(plain briefs naming it: {sum(bool(WARM.search(briefs[b]['without'])) for b in briefs)})")
    summary("named it", [m[b, "with"] for b in warm])
    summary("did not", [m[b, "with"] for b in briefs if b not in warm])

if __name__ == "__main__":
    main()
