"""score.py: tally filled-in scoring sheets against the key, once judging has closed.

  python3 examples/blind-test/score.py --key KEY.json scoring-owner.csv [scoring-other.csv ...]

Each judge is reported on their own, the owner of the work first; nothing is pooled across judges.
Per brief, the two sheets (same pair, sides swapped) are read together: the same image picked on both
counts as a pick for that condition; different picks, or "same", count as a tie (the choice followed position
or there was no preference). With 8 briefs, a one-sided sign test over the briefs that were not ties gives
p < 0.05 only at 7 of 8 or 8 of 8 for one condition; anything less is reported as no clear result.
"""
import argparse, csv, json, math, collections

def sign_p(k, n):  # one-sided P(X >= k), X ~ Binomial(n, 0.5)
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--key", required=True); ap.add_argument("csv", nargs="+"); a = ap.parse_args()
    key = json.load(open(a.key)); img = key["images"]; sheets = {s["sheet"]: s for s in key["sheets"]}
    judges = collections.OrderedDict()
    for path in a.csv:
        for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
            if r["sheet"] and r["preferred_id"].strip():
                judges.setdefault((r["judge"] or path, r["judge_type"]), []).append(r)
    order = sorted(judges, key=lambda j: j[1] != "owner")
    for j in order:
        picks = collections.defaultdict(list)
        for r in judges[j]:
            pid = r["preferred_id"].strip().upper()
            brief = sheets[r["sheet"]]["brief"]
            picks[brief].append(img[pid]["condition"] if pid in img else "same")
        res = {}
        for b, p in sorted(picks.items()):
            res[b] = p[0] if len(p) == 2 and p[0] == p[1] and p[0] != "same" else "tie" if len(p) == 2 else "incomplete"
        w = sum(v == "with" for v in res.values()); wo = sum(v == "without" for v in res.values())
        n = w + wo; k = max(w, wo)
        lead = "with the skill" if w > wo else "without the skill" if wo > w else "neither"
        print(f"\n{j[0]} ({j[1] or 'judge'}): with {w}, without {wo}, ties {sum(v == 'tie' for v in res.values())}, incomplete {sum(v == 'incomplete' for v in res.values())}")
        print("  per brief: " + ", ".join(f"{b} {v}" for b, v in res.items()))
        print(f"  sign test: {k} of {n} for {lead}, one-sided p = {sign_p(k, n):.3f}" + ("" if n and sign_p(k, n) < 0.05 else "  (no clear result)"))

if __name__ == "__main__":
    main()
