"""score.py: tally filled-in scoring sheets against the key(s), once judging has closed.

  python3 examples/blind-test/score.py --key KEY.json [--key KEY-2.json ...] scoring-owner.csv [scoring-other.csv ...]

Each batch has its own key (batch 1: S01-S16, briefs B1-B8, two sheets per brief with sides swapped; batch 2:
S17-S28, briefs B9-B20, one sheet per brief; batch 3: S29-S38, briefs B21-B30, one sheet per brief). Pass every key whose sheets were judged. Each judge is reported on
their own, the owner of the work first; nothing is pooled across judges.

One judgement per brief. Batch 1's two sheets for a brief are read as one judgement: if both were filled and
agree, that is the pick; if only one was filled (a judge who recognises the repeat may skip it), that one is
the pick; if they disagree, or the pick is "same" or "tie", it is a tie. Any other value that is not an ID
on that sheet is also counted as a tie, with a warning. A one-sided sign test runs over the briefs that
were not ties, for all briefs together and for each key's batch. With no ties, p < 0.05 needs 7 of 8,
10 of 12, 9 of 10, 15 of 20 or 20 of 30 for one condition; anything less is reported as no clear result.
"""
import argparse, csv, json, math, collections, sys

def sign_p(k, n):  # one-sided P(X >= k), X ~ Binomial(n, 0.5)
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0

def load_keys(paths):
    img, sheets, batch_of = {}, {}, {}
    for path in paths:
        key = json.load(open(path))
        for i, v in key["images"].items():
            if i in img: raise SystemExit(f"image ID {i} is in more than one key")
            img[i] = v
        for s in key["sheets"]:
            if s["sheet"] in sheets: raise SystemExit(f"sheet {s['sheet']} is in more than one key")
            sheets[s["sheet"]] = s; batch_of[s["brief"]] = path
    return img, sheets, batch_of

def judgement(p):
    if not p: return "incomplete"
    if "same" in p or len(set(p)) > 1: return "tie"
    return p[0]

def line(label, res):
    w = sum(v == "with" for v in res.values()); wo = sum(v == "without" for v in res.values())
    n = w + wo; k = max(w, wo)
    lead = "with the skill" if w > wo else "without the skill" if wo > w else "neither"
    return (f"  {label}: with {w}, without {wo}, ties {sum(v == 'tie' for v in res.values())}, "
            f"not judged {sum(v == 'incomplete' for v in res.values())}; sign test {k} of {n} for {lead}, "
            f"one-sided p = {sign_p(k, n):.3f}" + ("" if n and sign_p(k, n) < 0.05 else "  (no clear result)"))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--key", required=True, action="append")
    ap.add_argument("csv", nargs="+"); a = ap.parse_args()
    img, sheets, batch_of = load_keys(a.key)
    judges = collections.OrderedDict(); skipped = set()
    for path in a.csv:
        for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
            if r["sheet"] and r["preferred_id"].strip():
                if r["sheet"] not in sheets:
                    skipped.add(r["sheet"]); continue
                judges.setdefault((r["judge"] or path, r["judge_type"]), []).append(r)
    if skipped: print(f"skipped {len(skipped)} sheets not in the keys given: {', '.join(sorted(skipped))}", file=sys.stderr)
    for j in sorted(judges, key=lambda j: j[1] != "owner"):
        picks = {b: [] for b in batch_of}
        for r in judges[j]:
            pid = r["preferred_id"].strip().upper()
            brief = sheets[r["sheet"]]["brief"]
            if pid in ("SAME", "TIE"):
                picks[brief].append("same")
            elif pid in img and img[pid]["brief"] == brief:
                picks[brief].append(img[pid]["condition"])
            else:
                print(f"warning: {j[0]} {r['sheet']}: '{r['preferred_id']}' is not an ID on that sheet; counted as a tie", file=sys.stderr)
                picks[brief].append("same")
        res = {b: judgement(p) for b, p in sorted(picks.items(), key=lambda x: int(x[0][1:]))}
        print(f"\n{j[0]} ({j[1] or 'judge'})")
        print("  per brief: " + ", ".join(f"{b} {v}" for b, v in res.items()))
        print(line("all briefs", res))
        if len(a.key) > 1:
            for k in a.key:
                print(line(f"briefs in {k}", {b: v for b, v in res.items() if batch_of[b] == k}))

if __name__ == "__main__":
    main()
