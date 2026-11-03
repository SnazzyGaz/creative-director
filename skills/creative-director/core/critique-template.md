# Critique template

Copy, fill in, keep it short; drop sections that don't apply. Rules for writing it: `critique-loop.md` section 4. An unprompted hand-off sends only the **Sign-off blurb** (FLOW-1); the delivery uses the **Delivery checklist** (FLOW-3). A remake adds the brief block in `first-principles.md`.

```markdown
## Critique: <piece name>, round <n>

**Brief:** <purpose, audience, the one idea, where and how big it is seen, must-keeps, how done is judged (CD-1)>
**Intent (AES-0):** purpose [brief] / audience [brief] / mood [inferred?] / style / focal experience / polish / must-keeps. Mark each [brief] or [inferred].
**Criteria judged against:** <rule IDs, e.g. CORE-1, CORE-2, CORE-3, CORE-10, ILL-1, TD-PER-1>
**Evidence looked at:** <render file names and sizes; tests run>

### Brief check (CD-1, CD-5)
- Answers the brief and audience: <yes / partly / no, with evidence>. Must-keeps intact: <yes / list what changed>.
- Options considered (CD-3, open briefs only): <chosen, and one line per dropped option>

### Test results (evidence)
- Squint/blur: <what leads at blur; intended element per brief>
- Thumbnail: <readable at ~200 px: yes/no, what is lost>
- Flip/mirror: <deviations observed>
- Greyscale: <number of value groups; subject/ground separation>
- Crop/edges: <tangents, frame contacts, empty regions>
- Sitting right (COMP-19..25): <flags from rotate 180°, cover half, edge and alignment sweep: each "intended: keep (why)" or "fix"; nothing centred or symmetrised just to clear a flag>
- Whitespace (LAY-10): <largest intended inter-group gap; any band or 2-D dead zone over ~1.5× it (`tools/whitespace.py`), each marked deliberate or fixed; after an image swap: whole layout re-reviewed, what moved>
- Viewing distance (LAY-7, signage only): <print size; each key line's cap height in mm and "reads to X m" (≈ distance ÷ 250)>
- Set (BRAND-6, series only): <logo size/position, margins, palette and type logic shared: yes / list differences>

### Anatomy pass (CHAR-9; required when a person, hand or animal is in frame, else "n/a")
- Inventory: <people, hands, animals found, incl. partial and background ones>
- <crop file> | A<n> <check> | PASS/FAIL | <what was seen, e.g. "figure's left hand (image right): 5 digits, thumb on top, traced along yellow sleeve to left shoulder">
- Any FAIL is a BLOCKER below; re-run every line after each image edit.

### Meets criteria
- <RULE-ID>: <evidence, one line>

### Findings: MEASURED (checked with a tool or count; only these can be blockers)
- <RULE-ID>: <value measured, tool, threshold>. e.g. "UI-6: headline 8.97:1 on its background (`tools/contrast.py`), needs 4.5:1. Met."

### Findings: INTERPRETED (aesthetic reading; labelled as interpretation)
- <AES-ID>: feature <what is visible, where> -> effect <what it does to the viewer> -> trade-off <what changing it would cost>. Confidence: <high / low>.
- If a measured and an interpreted finding pull in opposite directions, write both and the trade-off. Don't settle it toward the neater option; it's the owner's call.

### Needs improvement (ranked, biggest first, max 5)
1. [BLOCKER|IMPROVEMENT] <RULE-ID> not met. <where>: <observed evidence>.
   Fix: <one concrete, smallest effective change>.
2. ...

### Comparison with the previous round or alternatives (AES-9)
- Stronger for this brief: <A / B / none good enough>. Strongest difference: <...>. Caused by: <decisions>. Cost: <what the winner gives up>. Preference: <strong / marginal; did it hold with left and right swapped?>.
- Aesthetic change this round: <one or two>. Decision: <keep / refine / revert> (AES-10). Measured checks still pass: <yes / list regressions>.
- Additions (content not in the brief or the previous version: characters, creatures, objects, text, claims): <none / list, each marked [inferred], with the brief line or owner sign-off that allows it, or "remove">.

### Deliberate exceptions (if any)
- <RULE-ID>: broken on purpose because <reason in the brief>.

### Next round
- Apply up to 3 fixes, blockers first. Re-render. Re-run tests. Compare with round <n>.
- Stop if the result is clearly better and no blockers remain.

### Questions for the owner (no rule settles these)
- <specific choice, with the options>

### Sign-off blurb (unprompted hand-off only; format in FLOW-1). Send, then wait.
1. [edit|regenerate] <RULE-ID>: <what is wrong, where>. <what will visibly change>.
Also possible (not needed): <one line, or omit>. OK to go ahead?

### Delivery checklist (after the fixes; FLOW-3). Lead with the result, then:
1. <point> (<RULE-ID>): done / not done, <evidence or reason>.
2. ...
QA re-run on the final render: light (TD-LIT-1) <pass/fail> · anatomy (CHAR-9) <pass/fail/n.a.> · type size and contrast (TYPE-3, UI-6) <pass/fail> · whitespace (LAY-10) <pass / deliberate space named / fail> · sitting right (COMP-25) <no flags / flags answered / open: list> · marks (BRAND-4, BRAND-8) <official, source, overlay check / plain-text name / placeholder / none / invented: fail> · real-subject crops (ILL-12) <pass/fail/n.a.> · facts (FP-3) <transcribed, questions open: list> · additions (AES-10) <none/list> · energy (EN-2) <full / light / skip, why; items not met>.
```
