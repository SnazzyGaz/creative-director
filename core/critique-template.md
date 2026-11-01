# Critique template

Neutral and factual. Every point cites a rule ID. No praise padding, no harshness. Light touch: preserve the intent and what meets criteria; propose at most ~3 changes per round. Copy, fill in, keep it short.

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
