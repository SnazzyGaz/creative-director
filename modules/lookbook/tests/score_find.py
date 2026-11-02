#!/usr/bin/env python3
"""Score tools/lookbook_find.py against briefs.json: recall@k of the 'should' looks and avoid-for violations.

    python3 modules/lookbook/tests/score_find.py [--k 8] [--verbose] [--json OUT]

recall@k: share of each brief's 'should' looks in the top k, averaged over briefs.
violations: (a) a 'should_not' look in the top k; (b) any shortlisted look whose avoid_for contains one of the
brief's avoid words or wanted moods (the search should have dropped it). Exit 1 if there is any violation."""
import argparse, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from lookbook_find import find, words, has  # noqa: E402

def score(k=8, verbose=False):
    looks = json.loads((ROOT / "modules/lookbook/looks.json").read_text())["looks"]
    briefs = json.loads((pathlib.Path(__file__).parent / "briefs.json").read_text())["briefs"]
    rec, viol, rows = [], 0, []
    for b in briefs:
        got = [l["id"] for l in find(looks, b["use"], b["mood"], b["energy"], b["avoid"], limit=k)]
        hit = [i for i in b["should"] if i in got]
        bad = [i for i in b["should_not"] if i in got]
        byid = {l["id"]: l for l in looks}
        clash = [i for i in got if any(has(w, byid[i].get("avoid_for", "").lower()) for w in words(b["avoid"]) + words(b["mood"]) + words(b["use"]))]
        r = len(hit) / len(b["should"]); rec.append(r); viol += len(bad) + len(clash)
        rows.append(dict(id=b["id"], recall=round(r, 2), missed=[i for i in b["should"] if i not in got], should_not_hits=bad, avoid_clash=clash, got=got))
        if verbose:
            print(f"{b['id']} recall {r:.2f}  missed {rows[-1]['missed']}  bad {bad + clash}  got {got}")
    # colour search sanity: a look's own palette should find that look first (self-retrieval@1, and @3)
    s1 = s3 = 0
    for l in looks:
        got_c = [x["id"] for x in find(looks, colour=",".join(l["colours"][:3]), limit=3)]
        s1 += got_c[:1] == [l["id"]]; s3 += l["id"] in got_c
    # --like sanity: every listed neighbour comes back (partial-read looks sort last, so order can shift)
    like_ok = all(set(l["nearest_looks"]) <= {x["id"] for x in find(looks, like=l["id"], limit=20)} for l in looks if l["nearest_looks"])
    return dict(k=k, briefs=len(briefs), recall_at_k=round(sum(rec) / len(rec), 3), violations=viol,
                colour_self_at1=round(s1 / len(looks), 3), colour_self_at3=round(s3 / len(looks), 3), like_ok=like_ok,
                zero_recall=[x["id"] for x in rows if x["recall"] == 0], rows=rows)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--k", type=int, default=8); ap.add_argument("--verbose", action="store_true"); ap.add_argument("--json")
    a = ap.parse_args(); r = score(a.k, a.verbose)
    print(f"lookbook_find: {r['briefs']} briefs, recall@{r['k']} = {r['recall_at_k']}, violations = {r['violations']}, zero-recall briefs: {', '.join(r['zero_recall']) or 'none'}")
    print(f"colour search: own palette finds the look first {r['colour_self_at1']:.0%}, in the top 3 {r['colour_self_at3']:.0%}; --like returns every nearest_looks entry: {r['like_ok']}")
    if a.json: json.dump(r, open(a.json, "w"), indent=1)
    sys.exit(1 if r["violations"] or not r["like_ok"] else 0)
