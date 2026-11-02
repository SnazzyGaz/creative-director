# Critique template

Neutral and factual. Every point cites a rule ID. No praise padding, no harshness. Light touch: preserve the intent and what meets criteria; propose at most ~3 changes per round. Copy, fill in, keep it short. When the work was handed over with no specific ask, the reader gets the **Sign-off blurb** at the end, not the whole critique, and nothing is applied until they sign off (`interaction-flow.md`, FLOW-1). The delivery after fixes uses the **Delivery checklist**.

```markdown
## Critique: <piece name>, round <n>

**Brief:** <purpose, audience, the one idea, where and how big it is seen, must-keeps, how done is judged (CD-1)>
**Intent (AES-0):** purpose [brief] / audience [brief] / mood [inferred?] / style / focal experience / polish / must-keeps. Mark each [brief] or [inferred].
**Criteria judged against:** <rule IDs, e.g. CORE-1, CORE-2, CORE-3, CORE-10, ILL-1, TD-PER-1>
**Evidence looked at:** <render file names and sizes; tests run>

### Brief check (CD-1, CD-5)
- Answers the brief and audience: <yes / partly / no, with evidence>. Must-keeps intact: <yes / list what changed>.
- Options considered (CD-3, open briefs only): <chosen, and one line per dropped option>

### Brief from first principles (remake mode only: "from scratch", "redo", "rejig", "reimagine"; FP-1..8). Send this first, then wait.
- Trigger (FP-1): <the owner's words>
- Step back (FP-2), one line each, [brief] or [inferred]: what it is and where it is seen / who it is for / its one job / the feeling / the given facts, word for word / must survive vs incidental / success
- Fact check (FP-3): <one line per check; conflicts as questions; what is held back until answered>
- **Brief (5-8 lines, FP-4):** <what and where> · <for whom> · <one job> · <feeling> · <must survive, incl. official marks (FP-8)> · <free to change> · <judged done when> · <open questions>
- Concepts (FP-5), each with a thumbnail: A <one-line idea; what leads> / B <...> / C <...>. Structure test: <the one-sentence descriptions differ without naming a font, colour or effect: yes / no>
- Recommend (FP-6): <concept, reason citing a brief line>. Dropped: <one line each: what it does better, why it lost>. The owner picks.
- Comparison after the build (FP-7, AES-9): original vs light-touch fix (if any) vs remake: <stronger for the brief, why, cost>

### Test results (evidence)
- Squint/blur: <what leads at blur; intended element per brief>
- Thumbnail: <readable at ~200 px: yes/no, what is lost>
- Flip/mirror: <deviations observed>
- Greyscale: <number of value groups; subject/ground separation>
- Crop/edges: <tangents, frame contacts, empty regions>

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

### Sign-off blurb (unprompted hand-off only; FLOW-1). Send this, then wait. Apply nothing yet.
Imperative changes (sign off and I'll apply all of them):
1. [edit|regenerate] <RULE-ID>: <what is wrong, where>. <what will visibly change>.
2. ...
Also possible (not needed): <one line, or omit>. OK to go ahead?

### Delivery checklist (after the fixes; FLOW-3). Lead with the result, then:
1. <point> (<RULE-ID>): done / not done, <evidence or reason>.
2. ...
QA re-run on the final render: light (TD-LIT-1) <pass/fail> · anatomy (CHAR-9) <pass/fail/n.a.> · type size and contrast (TYPE-3, UI-6) <pass/fail> · marks (BRAND-4, BRAND-8) <official, source / placeholder / none / invented: fail> · additions (AES-10) <none/list>.
```

## Worked example

> **Brief:** blog header illustration, 1200x630, shown in a feed at ~300 px. Focal point: the character's face.
> **Criteria judged against:** CORE-1, CORE-2, CORE-3, CORE-10, ILL-1, ILL-2.
> **Test results:** Blur: top-right sky leads. Greyscale: character and background both fall in the mid-value group. Thumbnail: pose readable, face not.
>
> **Meets criteria**
> - ILL-3 (shape): the figure's silhouette reads as one clear action at thumbnail size.
> - CORE-6: palette limited to three hues, each with a role.
>
> **Needs improvement**
> 1. [IMPROVEMENT] CORE-2 not met. Character vs background: same value group in greyscale. Fix: darken the background behind the head one value step; keep the face in the light group.
> 2. [IMPROVEMENT] CORE-3 not met. Highest contrast is at the top-right sky, not the face. Fix: drop the sky one step; place the lightest light on the face.
> 3. [IMPROVEMENT] ILL-1 not met. Horizon sits on the exact vertical centre, dividing the frame into equal halves. Fix: move it clearly above or below centre, whichever suits the brief (no specific ratio required).
>
> **Questions for the owner:** warm or cool light family for the face?
