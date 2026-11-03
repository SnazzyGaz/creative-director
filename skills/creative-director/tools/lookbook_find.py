#!/usr/bin/env python3
"""Shortlist lookbook looks for a brief without loading the whole tag file.

    python3 tools/lookbook_find.py --use poster --mood bold --energy high --avoid children [--max-out 3]
                                   [--skip LB-014,LB-040] [--established] [--limit 8] [--full]
    python3 tools/lookbook_find.py --colour "#c5040f,#ed6322" [--use poster]   # nearest palettes (CIELAB distance)
    python3 tools/lookbook_find.py --like LB-010 [--skip ...]                 # more like this: visual neighbours

Matches words (case-insensitive, at the start of a word) in `use` and `theme` (--use), `mood` (--mood), `energy`
(--energy: one step off is kept but ranked lower; high against low is dropped). Drops looks whose `avoid_for` mentions any
--avoid, --mood or --use word, looks in --skip (your recent-use log) and, with
--max-out N, looks above that out_there level. Partial-read looks sort last and are marked. Prints one line per look
(ID, name, energy, out_there, sheet, hint); --full adds hallmarks by layer, avoid_for, care, colours and Getty AAT term.
--colour ranks by the distance (CIELAB dE) from each given hex to the nearest of a look's dominant colours.
--like ID lists that look's nearest_looks, then looks that list it as a neighbour, with the same filters.
Search quality is scored by modules/lookbook/tests/score_find.py."""
import argparse, json, pathlib, re

LB = pathlib.Path(__file__).resolve().parents[1] / "modules/lookbook/looks.json"

def words(s): return [w.strip().lower() for w in (s or "").split(",") if w.strip()]

def has(word, text):
    """Word-start match, so 'gin' finds 'gin labels' but not 'packaging'; plurals still match ('festival' -> 'festivals')."""
    return re.search(r"(?<![a-z])" + re.escape(word), text) is not None

def hex_lab(h):
    h = h.strip().lstrip("#"); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    M = [[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]]
    x, y, z = (sum(M[r][k] * c[k] for k in range(3)) / w for r, w in zip(range(3), (0.95047, 1.0, 1.08883)))
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    return (116 * f(y) - 16, 500 * (f(x) - f(y)), 200 * (f(y) - f(z)))

def colour_distance(query, look):
    """Mean over the query colours of the dE76 to the look's nearest dominant colour (lower is closer)."""
    cols = [hex_lab(c) for c in look.get("colours") or []]
    if not cols: return None
    qs = [hex_lab(q) for q in query]
    return sum(min(sum((a - b) ** 2 for a, b in zip(q, c)) ** 0.5 for c in cols) for q in qs) / len(qs)

def find(looks, use="", mood="", energy="", avoid="", skip="", max_out=5, established=False, limit=8, colour="", like=""):
    """Return the ranked shortlist (list of look dicts). Used by main() and modules/lookbook/tests/score_find.py."""
    query = [c for c in (colour or "").split(",") if c.strip()]
    like = (like or "").strip().upper()
    byid = {l["id"]: l for l in looks}
    if like and like not in byid: raise SystemExit(f"unknown look {like}")
    near = {}
    if like:
        for i, n in enumerate(byid[like].get("nearest_looks") or []): near[n] = i
        for l in looks:
            if like in (l.get("nearest_looks") or []) and l["id"] not in near: near[l["id"]] = 3 + (l.get("nearest_looks") or []).index(like)
    use, mood, energy, avoid = words(use), words(mood), words(energy), words(avoid)
    skip = {s.strip().upper() for s in skip.split(",") if s.strip()}
    scored = []
    for l in looks:
        if l["id"] in skip or (established and l["kind"] != "established"): continue
        if like and l["id"] not in near: continue
        if isinstance(l.get("out_there"), int) and l["out_there"] > max_out: continue
        if any(has(w, l.get("avoid_for", "").lower()) for w in avoid + mood + use): continue   # a subject, mood or use the look warns against
        le = l.get("energy", "").lower()
        if energy and le not in energy and not (le == "medium" or "medium" in energy): continue   # high vs low: drop; one step off: keep, rank lower
        hay_use = (l.get("use", "") + " " + l.get("theme", "")).lower()
        moods = " ".join(l.get("mood", [])).lower()
        s = sum(has(w, hay_use) for w in use) * 2 + sum(has(w, moods) for w in mood) + (1 if energy and le in energy else 0)
        if (use or mood) and s - (1 if energy and le in energy else 0) == 0: continue
        if like: key = near[l["id"]]
        elif query:
            d = colour_distance(query, l)
            if d is None: continue
            key = d - 2 * s                                  # colour first; a use or mood hit breaks near-ties
            l = dict(l, _dE=round(d, 1))
        else: key = -s
        scored.append((l.get("read_status") == "partial", key, l["id"], l))
    return [x[3] for x in sorted(scored, key=lambda x: x[:3])[:limit]]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--use", default=""); ap.add_argument("--mood", default=""); ap.add_argument("--energy", default="")
    ap.add_argument("--avoid", default="", help="words from the brief's subject or audience to test against avoid_for")
    ap.add_argument("--skip", default="", help="comma-separated IDs used recently")
    ap.add_argument("--max-out", type=int, default=5); ap.add_argument("--established", action="store_true")
    ap.add_argument("--limit", type=int, default=8); ap.add_argument("--full", action="store_true")
    ap.add_argument("--colour", "--color", default="", help="comma-separated hex colours to match against each look's dominant colours")
    ap.add_argument("--like", default="", help="a look ID: list its visual neighbours")
    a = ap.parse_args()
    looks = json.loads(LB.read_text())["looks"]
    res = find(looks, a.use, a.mood, a.energy, a.avoid, a.skip, a.max_out, a.established, a.limit, a.colour, a.like)
    for l in res:
        flag = "  [partial read: not a lead direction]" if l.get("read_status") == "partial" else ""
        extra = f" | dE {l['_dE']} {' '.join(l.get('colours') or [])}" if "_dE" in l else ""
        print(f"{l['id']} {l['name']} | energy {l.get('energy')} | out_there {l.get('out_there')} | {l['sheet']} {l.get('panel','')}{extra}{flag}")
        print(f"    hint: {l.get('hint')}")
        if a.full:
            for k, v in l["hallmarks"].items():
                if v: print(f"    {k}: {v}")
            print(f"    avoid for: {l.get('avoid_for')}")
            if l.get("care"): print(f"    care: {l['care']}")
            if l.get("colours"): print(f"    colours: {' '.join(l['colours'])}")
            if l.get("nearest_looks"): print(f"    more like this: {', '.join(l['nearest_looks'])}")
            if l.get("getty_aat"): print(f"    Getty AAT: {l['getty_aat']['label']} ({l['getty_aat']['url']})")
    if not res: print("no match: loosen --use/--mood, or start from the brief alone")

if __name__ == "__main__":
    main()
