#!/usr/bin/env python3
"""Shortlist lookbook looks for a brief without loading the whole tag file.

    python3 tools/lookbook_find.py --use poster --mood bold --energy high --avoid children [--max-out 3]
                                   [--skip LB-014,LB-040] [--established] [--limit 8] [--full]

Matches words (case-insensitive substrings) in `use` and `theme` (--use), `mood` (--mood), `energy` (--energy).
Drops looks whose `avoid_for` mentions any --avoid or --mood word, looks in --skip (your recent-use log) and, with
--max-out N, looks above that out_there level. Partial-read looks sort last and are marked. Prints one line per look
(ID, name, energy, out_there, sheet, hint); --full adds hallmarks by layer, avoid_for and care."""
import argparse, json, pathlib

LB = pathlib.Path(__file__).resolve().parents[1] / "modules/lookbook/looks.json"

def words(s): return [w.strip().lower() for w in (s or "").split(",") if w.strip()]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--use", default=""); ap.add_argument("--mood", default=""); ap.add_argument("--energy", default="")
    ap.add_argument("--avoid", default="", help="words from the brief's subject or audience to test against avoid_for")
    ap.add_argument("--skip", default="", help="comma-separated IDs used recently")
    ap.add_argument("--max-out", type=int, default=5); ap.add_argument("--established", action="store_true")
    ap.add_argument("--limit", type=int, default=8); ap.add_argument("--full", action="store_true")
    a = ap.parse_args()
    looks = json.loads(LB.read_text())["looks"]
    use, mood, energy, avoid = words(a.use), words(a.mood), words(a.energy), words(a.avoid)
    skip = {s.strip().upper() for s in a.skip.split(",") if s.strip()}
    scored = []
    for l in looks:
        if l["id"] in skip or (a.established and l["kind"] != "established"): continue
        if isinstance(l.get("out_there"), int) and l["out_there"] > a.max_out: continue
        if any(w in l.get("avoid_for", "").lower() for w in avoid + mood): continue   # a wanted mood the look warns against
        if energy and l.get("energy", "").lower() not in energy: continue
        hay_use = (l.get("use", "") + " " + l.get("theme", "")).lower()
        moods = " ".join(l.get("mood", [])).lower()
        s = sum(w in hay_use for w in use) * 2 + sum(w in moods for w in mood)
        if (use or mood) and s == 0: continue
        scored.append((l.get("read_status") == "partial", -s, l["id"], l))
    for partial, neg, _, l in sorted(scored)[:a.limit]:
        flag = "  [partial read: not a lead direction]" if partial else ""
        print(f"{l['id']} {l['name']} | energy {l.get('energy')} | out_there {l.get('out_there')} | {l['sheet']} {l.get('panel','')}{flag}")
        print(f"    hint: {l.get('hint')}")
        if a.full:
            for k, v in l["hallmarks"].items():
                if v: print(f"    {k}: {v}")
            print(f"    avoid for: {l.get('avoid_for')}")
            if l.get("care"): print(f"    care: {l['care']}")
    if not scored: print("no match: loosen --use/--mood, or start from the brief alone")

if __name__ == "__main__":
    main()
