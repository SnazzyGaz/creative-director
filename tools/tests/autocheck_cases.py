#!/usr/bin/env python3
"""Fixture tests for tools/autocheck.py. Run: python3 tools/tests/autocheck_cases.py
Image cases always run; page cases need playwright + chromium and are skipped (not failed) without it."""
import json, subprocess, sys, tempfile, pathlib
HERE = pathlib.Path(__file__).resolve().parent
TOOL = HERE.parent / "autocheck.py"
FIX = HERE / "fixtures" / "autocheck"

def run(target, *extra):
    with tempfile.TemporaryDirectory() as d:
        out = pathlib.Path(d) / "r.json"
        p = subprocess.run([sys.executable, str(TOOL), str(target), "--json", str(out), *extra], capture_output=True, text=True)
        if not out.exists():
            raise RuntimeError(p.stderr[-800:])
        r = json.load(open(out)); r["_exit"] = p.returncode
        return r

def st(r):
    return {c["id"]: c["status"] for c in r["checks"]}

CASES = [
    # (name, target, extra args, expected {check id: status}, expected exit)
    ("even layout passes", "even.png", [], {"dead-space": "PASS", "balance": "PASS", "edges": "PASS", "contrast": "SKIP", "text-size": "SKIP"}, 0),
    ("dead band fails LAY-10", "deadband.png", [], {"dead-space": "FAIL"}, 1),
    ("crowded edge and lopsided weight flag", "crowded.png", [], {"edges": "FLAG", "balance": "FLAG"}, 0),
    ("text boxes: grey fails, black passes", "textboxes.png", ["--text-box", "50,50,710,110", "--text-box", "50,250,710,310"], {"contrast": "FAIL"}, 1),
    ("neutral white ground passes CV-11", "whites-neutral.png", [], {"whites": "PASS"}, 0),
    ("cream ground flags CV-11", "whites-cream.png", [], {"whites": "FLAG"}, 0),
    ("white box on neutral white passes", "whites-neutral.png", ["--white-box", "20,600,580,780"], {"whites": "PASS"}, 0),
    ("white box on cream fails", "whites-cream.png", ["--white-box", "20,600,580,780"], {"whites": "FAIL"}, 1),
    ("cream named as a warm choice passes", "whites-cream.png", ["--warm", "heritage market"], {"whites": "PASS"}, 0),
    ("grey ground still flags with --warm", "whites-grey.png", ["--warm", "cosy"], {"whites": "FLAG"}, 0),
]
PAGE_CASES = [
    ("good page: no FAIL", "good.html", [], {"contrast": "PASS", "text-size": "PASS", "type-sizes": "PASS", "measure": "PASS", "leading": "PASS", "spacing-scale": "PASS", "targets": "PASS"}, 0),
    ("bad page: hard failures", "bad.html", [], {"contrast": "FAIL", "text-size": "FAIL", "type-sizes": "FAIL", "measure": "FAIL", "leading": "FAIL", "targets": "FAIL", "spacing-scale": "FLAG", "near-miss": "FLAG", "edges": "FLAG"}, 1),
]

def main():
    ok = fail = skip = 0
    try:
        import playwright  # noqa
        cases = CASES + PAGE_CASES
    except ImportError:
        cases = CASES; skip = len(PAGE_CASES); print(f"skip {skip} page cases: playwright not installed")
    for name, f, extra, want, code in cases:
        r = run(FIX / f, *extra); got = st(r); errs = []
        for k, v in want.items():
            if got.get(k) != v: errs.append(f"{k}: want {v}, got {got.get(k)}")
        if any(c["id"] == "balance" and c["status"] == "FAIL" for c in r["checks"]): errs.append("balance must never FAIL")
        if r["_exit"] != code: errs.append(f"exit {r['_exit']} != {code}")
        if f == "textboxes.png":
            b = next(c for c in r["checks"] if c["id"] == "contrast")["boxes"]
            if [x["ok"] for x in b] != [False, True]: errs.append(f"box results {b}")
        print(("ok   " if not errs else "FAIL ") + name + ("" if not errs else ": " + "; ".join(errs)))
        ok += not errs; fail += bool(errs)
    print(f"{ok}/{ok + fail} passed" + (f", {skip} skipped" if skip else ""))
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    main()
