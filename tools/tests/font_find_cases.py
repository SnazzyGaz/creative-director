#!/usr/bin/env python3
"""Smoke cases for tools/font_find.py: filters work and every catalogue mood finds at least one family."""
import contextlib, io, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import font_find

def run(*args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): code = font_find.main(list(args))
    return code, buf.getvalue()

cat = json.loads(font_find.CAT.read_text())
fails = 0
for m in cat["mood_vocabulary"]:
    code, out = run("--mood", m)
    if code: print("FAIL mood finds nothing:", m); fails += 1
code, out = run("--genre", "blackletter", "--limit", "50")
names = {f["family"] for f in cat["families"] if "blackletter" in f["themes"]}
if code or {l.split(" | ")[0] for l in out.splitlines() if " | " in l} != names: print("FAIL genre filter"); fails += 1
code, out = run("--mood", "warmth,craft", "--limit", "1")
first = out.splitlines()[0].split(" | ")
if not {"warmth", "craft"} <= set(first[2].split(", ")): print("FAIL ranking: best match should carry both moods"); fails += 1
code, _ = run("--pairs", "no such family")
if code != 1: print("FAIL unknown family"); fails += 1
print("font_find: all cases pass" if not fails else f"font_find: {fails} failing"); sys.exit(1 if fails else 0)
