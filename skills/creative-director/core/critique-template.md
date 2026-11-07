# Critique template

Keep it short; omit inapplicable tests, not finding labels or the fix-level decision. An unprompted hand-off sends only the sign-off blurb (FLOW-1); delivery uses FLOW-3. A remake adds the brief in `first-principles.md`.

```markdown
## Critique: <piece>, round <n>

**Owner summary**
- Verdict: <keep / improve / the original is better / none good enough; why>
- Top changes: <now -> after; rule ID or brief line, at most 3>
- Questions: <owner choices>

**Idea and feeling:** <one sentence each>
**Brief:** <brief.json; purpose, audience, format/size, fixed copy/counts, must-keeps, success>
**Intent (AES-0):** <mood, style, focal experience, polish; each [brief] or [inferred]>
**Criteria:** <applicable rule IDs and explicit brief conditions>
**Evidence:** <render names, sizes, crop paths, measurements/tools>
**Selection:** <4–8 rough IDs; same-model fresh-context comparison; strongest differences/trade-offs; top 2–3 shown; owner's pick; or n/a: existing-work edit/consult>

### Brief check (CD-1, CD-5, CD-7)
- Answers the brief: <yes/partly/no, evidence>. Must-keeps: <intact/list>.
- Copy: <each exact line and occurrence count, as rendered vs briefed; match/slip>.
- Fixed object counts: <one tick per item on a 2x crop; expected vs observed>.
- Unverified conditions: <list; not called passes>.

### Look and measured checks
- cd.py check / autocheck: <report path; PASS/FAIL/FLAG/SKIP, numbers and thresholds>.
- Blur: <what leads>. Thumbnail: <what survives>.
- Mirror: <deviations>. Greyscale: <value groups>. Crop/edges: <contacts>.
- Sitting right (COMP-19..25): <rotate, cover half, edge sweep; flags intended/keep/fix, why; never centre by default>.
- Whitespace (LAY-10): <largest intended gap; bands/dead zones >1.5x; whole-layout review after image swap>.
- Anatomy (CHAR-9): <inventory incl. partial/background figures; each 2–4x crop, trace/count, PASS/FAIL; any fail blocks; or n/a>.
- Viewing distance / series / motion checks: <when applicable>.
- Energy: <skip: brief reason / full, structure or light: named intent line; EN findings>. Medium alone does not trigger it.

### Preserve
- <what works and its evidence; do not fix this away>

### Findings (ranked by effect; max 5)
1. [rule-backed | intent-backed | exploratory] [MEASURED | INTERPRETED] [BLOCKER | IMPROVEMENT | OPTION]
   Basis: <existing rule ID + threshold OR exact brief line OR exploratory question>.
   Observation: <visible feature, where; measured value or interpreted effect>.
   Provenance: <tool/measurement, rule lookup/path, or visual read + render/crop>.
   Confidence: <high/medium/low; why, including evidence limits>.
   Proposed change: <smallest effective intervention>. Trade-off: <what it costs>.
2. ...
- Only verified mandatory failures block. Exploratory never blocks. Interpretation is not a measured failure; state trade-offs rather than choosing neatness by default.

### Intervention decision (required before changes)
- Level: <edit / recompose / art-direct / reconceive / rebuild / explore>.
- Why this level: <why a smaller change is insufficient; idea and must-keeps protected>.
- Authority: <signed-off request or pending; reconception needs approval and roughs-then-pick>.

### Comparison (AES-9, AES-10)
- Stronger for the brief: <original / previous / latest / earlier rough / none good enough>.
- Visible difference and cause: <...>. Cost: <...>. Preference: <strong/marginal; swap-sides result>.
- Decision: <keep/refine/revert/stop: the original is better>. Remaining blockers: <none/list; preference does not waive them>.
- Additions: <none/list; [inferred] is not permission; brief line or sign-off, else remove>.

### Next round or stop
- <up to 3 changes, re-render, verify each applied, repeat measurements/anatomy as needed>.
- <stop reason; no forced polish, routine round 3 / maximum 5>.
- Deliberate exceptions: <ID or brief condition; approved reason>.

### Sign-off blurb (unprompted hand-off only; send, wait)
1. [edit|regenerate] [finding label] <rule ID or brief line>: <evidence; visible change>.
Also possible (not needed): <one line or omit>. OK to go ahead?

### Delivery (FLOW-3; result first)
1. <signed-off point>: done / not done, <final-render evidence or reason>.
QA (pass/fail/n.a./unverified): construction/light · anatomy · type/contrast · whitespace · sitting right · marks · real-subject crops · copy/counts/facts · additions · neutral whites · energy (or skipped: intent reason) · medium-specific gates.
<Latest and previous renders; what remains and why; owner questions; verdict labelled self-judged.>
```
