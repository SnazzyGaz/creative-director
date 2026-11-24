#!/usr/bin/env python3
"""check_budgets.py: token budgets for the v2 kernel and on-demand rule files.

    python3 tools/check_budgets.py           # check every budgeted file/set; exit 1 if any is over
    python3 tools/check_budgets.py --loads   # also print typical task loads

Reads kernel files and budgets from manifest.json. Uses POSIX relative paths across Windows and Linux.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

try:
    import tiktoken
    _enc = tiktoken.get_encoding("cl100k_base")
    count, METHOD = (lambda s: len(_enc.encode(s))), "tiktoken cl100k_base"
except Exception:
    count, METHOD = (lambda s: round(len(s) / 4)), "characters / 4"

ALWAYS = MANIFEST["kernel"]["always_on"]
KERNEL_CAP = MANIFEST["kernel"]["token_budget"]
MODULE_ENTRY = 6000
ON_DEMAND = 4500
SKIP = {"modules/lookbook/UPDATING.md"}

LOADS = {
    "Tier 1 fast QA (kernel only + cd.py check)": [],
    "screen (web-ui + typography)": ["modules/web-ui/README.md", "modules/typography/README.md"],
    "screen + ux flow": ["modules/web-ui/README.md", "modules/typography/README.md", "modules/ux/README.md"],
    "poster / social card (layout + typography + composition + colour-value)": [
        "modules/layout/README.md", "modules/typography/README.md",
        "modules/composition/README.md", "modules/colour-value/README.md",
    ],
    "infographic (layout + infographics + typography)": [
        "modules/layout/README.md", "modules/layout/infographics.md", "modules/typography/README.md",
    ],
    "logo (brand + logo + mark-making)": [
        "modules/brand/README.md", "modules/brand/logo.md", "modules/brand/mark-making.md",
    ],
    "figure / character (character + technical-drawing)": [
        "modules/character/README.md", "modules/technical-drawing/README.md",
    ],
    "photo (photo + character)": ["modules/photo/README.md", "modules/character/README.md"],
    "optional: writing": ["modules/writing/README.md"],
    "optional: video review (film README + story + review)": [
        "modules/film/README.md", "modules/film/story.md", "modules/film/review.md",
    ],
}


def tokens(files):
    return sum(count((ROOT / f).read_text(encoding="utf-8")) for f in files)


def rows():
    out = [
        (f"always-on kernel ({' + '.join(ALWAYS)})", tokens(ALWAYS), KERNEL_CAP),
        ("always-on kernel + critique template", tokens(ALWAYS + ["core/critique-template.md"]), KERNEL_CAP + 1500),
        ("lite/CREATIVE-DIRECTOR-LITE.md", tokens(["lite/CREATIVE-DIRECTOR-LITE.md"]), 2600),
    ]
    budgeted = {"lite/CREATIVE-DIRECTOR-LITE.md"}
    for entry in MANIFEST.get("core_files", []):
        rel = entry["path"]
        out.append((rel, tokens([rel]), entry["budget"]))
        budgeted.add(rel)

    for p in sorted((ROOT / "modules").glob("*/README.md")):
        rel = p.relative_to(ROOT).as_posix()
        out.append((rel, count(p.read_text(encoding="utf-8")), MODULE_ENTRY))
        budgeted.add(rel)

    for p in sorted([*(ROOT / "core").glob("*.md"), *(ROOT / "modules").glob("*/*.md")]):
        rel = p.relative_to(ROOT).as_posix()
        if rel in budgeted or rel in SKIP or p.name == "README.md":
            continue
        out.append((rel, count(p.read_text(encoding="utf-8")), ON_DEMAND))
    return out


def main(argv):
    over = 0
    print(f"token budgets ({METHOD})")
    for label, n, cap in rows():
        bad = n > cap
        over += bad
        print(f"{'OVER' if bad else 'ok  '}  {n:6,} / {cap:6,}  {label}")
    if "--loads" in argv:
        base = tokens(ALWAYS)
        print(f"\ntypical loads (always-on kernel = {base:,}; not enforced)")
        for label, files in LOADS.items():
            print(f"        {base + tokens(files):6,}  {label}")
    print(f"\n{over} over budget" if over else "\nall within budget")
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
