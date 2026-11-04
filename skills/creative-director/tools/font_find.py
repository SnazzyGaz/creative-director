#!/usr/bin/env python3
"""Shortlist fonts from the library for a brief without reading the whole catalogue.

    python3 tools/font_find.py --mood warmth,craft [--genre heritage] [--use menu] [--avoid "long text"] [--limit 8] [--full]
    python3 tools/font_find.py --pairs "Playfair Display"      # what the catalogue pairs with a family
    python3 tools/font_find.py --list                          # the mood words and the genre (theme) ids

--mood matches the family's mood tags (fonts/catalogue.json `mood_vocabulary`); --genre matches theme ids or names
(word start, so "slab" finds "western-slab"); --use matches words in the family's `good_for` and its themes' `use`.
--avoid drops families whose `avoid` line mentions any given word. Families matching more of the asked moods rank first.
Prints one line per family (name, themes, moods, good for); --full adds avoid, pairs, axes, weights and the path.
Mood tags are craft judgement written for this repo, not research findings (fonts/README.md)."""
import argparse, json, pathlib, re

CAT = pathlib.Path(__file__).resolve().parents[1] / "fonts/catalogue.json"

def words(s): return [w.strip().lower() for w in (s or "").split(",") if w.strip()]

def has(word, text):
    return re.search(r"(?<![a-z])" + re.escape(word), text.lower()) is not None

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--mood"); ap.add_argument("--genre"); ap.add_argument("--use"); ap.add_argument("--avoid")
    ap.add_argument("--pairs"); ap.add_argument("--list", action="store_true"); ap.add_argument("--full", action="store_true")
    ap.add_argument("--limit", type=int, default=8)
    a = ap.parse_args(argv)
    cat = json.loads(CAT.read_text())
    themes = {t["id"]: t for t in cat["themes"]}
    fams = cat["families"]
    if a.list:
        print("moods:", ", ".join(cat["mood_vocabulary"]))
        print("genres:", ", ".join(f"{t['id']} ({t['name']})" for t in cat["themes"]))
        return 0
    if a.pairs:
        f = next((f for f in fams if f["family"].lower() == a.pairs.lower()), None)
        if not f: print(f"no family named {a.pairs!r}"); return 1
        print(f"{f['family']} pairs with: {', '.join(f.get('pairs_with') or []) or 'none listed'}")
        return 0
    moods, genres, uses, avoid = words(a.mood), words(a.genre), words(a.use), words(a.avoid)
    out = []
    for f in fams:
        fthemes = [themes[t] for t in f.get("themes", []) if t in themes]
        if genres and not any(has(g, t["id"].replace("-", " ") + " " + t["name"]) for g in genres for t in fthemes):
            continue
        usetext = (f.get("good_for") or "") + " " + " ".join(t.get("use", "") for t in fthemes)
        if uses and not any(has(u, usetext) for u in uses):
            continue
        if avoid and any(has(w, f.get("avoid") or "") for w in avoid):
            continue
        score = sum(m in (f.get("moods") or []) for m in moods)
        if moods and not score:
            continue
        out.append((-score, f["family"], f))
    out.sort(key=lambda r: (r[0], r[1]))
    if not out: print("no match; try fewer words or --list"); return 1
    for _, _, f in out[: a.limit]:
        print(f"{f['family']} | {', '.join(f.get('themes', []))} | {', '.join(f.get('moods') or [])} | {f.get('good_for', '')}")
        if a.full:
            ax = ", ".join(f"{k} {v[0]:g}-{v[1]:g}" for k, v in (f.get("axes") or {}).items()) or "static " + ",".join(map(str, f.get("static_weights") or []))
            print(f"    avoid: {f.get('avoid', '')} | pairs: {', '.join(f.get('pairs_with') or [])} | {ax} | {f.get('path', '')} ({f.get('licence', '')})")
    if len(out) > a.limit: print(f"... {len(out) - a.limit} more (raise --limit)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
