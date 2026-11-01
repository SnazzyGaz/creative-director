# The critique loop: render, look, critique, fix, re-render

**Purpose:** a light touch. The loop nudges a bot's output (a 3D model, drawing, generated image, UI or flow) toward what people measurably prefer, while keeping its intent and what already works. It is not a rebuild. Make the smallest changes with the biggest effect, and stop once the work is clearly better.

Always look at a fresh render or screenshot. Never assume from your own code or prompt.

```
make -> render -> LOOK (5 tests) -> CRITIQUE (criteria, ranked) -> FIX up to 3 -> re-render -> compare
         ^                                                                                    |
         +----------------------- repeat only while it is clearly improving ------------------+
```

## Why bother (evidence, not taste)

- People judge visual appeal within about 50 ms, and those judgements are stable [S36].
- Perceived visual complexity is the strongest single predictor of that first impression; high complexity is liked least [S35]. Simplifying is usually the highest-impact fix.
- Attractive work is perceived as more usable and earns tolerance for minor problems, but not for serious ones [S34]. So: fix blockers first, then polish lightly.

## 0. Brief (creative-direction.md)

- Before making, have the brief (CD-1) and the direction (CD-2). For an open brief, compare 2-3 rough options first (CD-3).
- The first critique point each round is: does it answer the brief and audience, and are the must-keeps intact (CD-1, CD-5)?

## 1. Render

- Render at the size people will see it, plus a thumbnail. For UI, screenshot at phone and desktop widths, and at 200% zoom (`tools/shot.sh`).
- For 3D, run the cheap measured checks first (`modules/3d/`), then one contact sheet.
- Keep every round: `round-01.png`, `round-02.png`... for side-by-side comparison.

## 2. Look: five quick tests

Artists use these to get a "fresh eye", because the maker grows used to their own mistakes [S7, S8].

| Test | How (bot version) | What it reveals |
|---|---|---|
| **Squint / blur** | Gaussian blur ~5-10 px at screen size (more for big images) | Hierarchy and grouping: what leads when detail is gone [S1] |
| **Thumbnail** | Shrink to ~150-200 px wide | Whether the idea survives at feed or icon size |
| **Flip / mirror** | Mirror horizontally (upside down too, for pictures) | Drawing errors, lopsided balance, tilts you no longer see [S7] |
| **Greyscale** | Desaturate by perceived lightness (luminance or OKLCH L, not HSL L) | Value structure; colour doing work that value should do [S5] |
| **Crop / edges** | Inspect each edge and corner; try a tighter crop | Tangents, frame contacts, dead space, stray bright spots |

`tools/look.py` makes all five as one contact sheet, with value stats. Record one factual line per test (what was observed), e.g. "Blur: the badge top-right leads; the headline is second."

## 3. Critique

Use `critique-template.md`. Tone: neutral and factual, like a doctoral supervisor reviewing a chapter. Every point is judged against a named criterion, never personal preference.

- **State the criteria first.** List the rule IDs in scope (e.g. `CORE-1, CORE-2, TD-PER-1, ILL-2`).
- **Cite a rule ID on every point.** If no rule supports a point, it is not a critique point; put it under "Questions for Gaz".
- **No myths as reasons.** Don't justify a fix with the golden ratio, the rule of thirds as a law, or colour-emotion claims. Cite a preference study only if it fits the case (`evidence.md`).
- **Meets criteria.** Record what is met, with evidence. This is a record of what to preserve, not encouragement.
- **Needs improvement, ranked biggest first.** Rank by effect on the whole. Structure (hierarchy, perspective, composition, flow) before surface (texture, polish, micro-spacing). Five at most.
- **Blockers vs improvements.** Only **MUST-BE-RIGHT** failures are blockers: perspective, anatomy/proportion, light consistency, contrast/accessibility minimums, a main flow that can't be completed, 3D build defects. Everything else is an improvement, optional by nature.
- **Measure at zoom before calling a failure.** For ellipses, verticals, alignment and edges, look at 2x or more, or use the tool (`tools/vp.py`, `tools/ellipse.py`, `tools/contrast.py`). A call made at normal size is a candidate, not a finding.
- **Specific and actionable.** Where (region, element, coordinates), the observed evidence, the rule, and one concrete fix.
- **No padding, no harshness.** No approval or disapproval adjectives ("lovely", "weak", "terrible"), no hedging. Describe what is observed against the criterion.

Register example:
- Not: "The lighting is a bit confusing and the face feels weak."
- But: "CORE-3 not met. Highest value contrast is at the top-right sky, not the face (focal point per brief). Fix: lower the sky one value step; place the lightest light on the face."

## 4. Fix and re-render: light touch

- **Preserve intent.** Don't change the subject, style, mood, palette concept or layout concept. Those belong to the brief and to Gaz.
- **At most ~3 changes per round**, blockers first, then the highest-ranked improvements.
- **Smallest effective change.** Adjust a value step, a size, a gap, an edge. Don't restyle the piece to fix one corner. Prefer removing to adding.
- Re-run the five tests and compare with the previous round side by side. If a change made it worse or broke something that met a criterion, revert it.
- **Check each fix applied.** Compare the new render with the fix as written. Image generators often skip or drift on edits. A fix that didn't apply counts as not done; retry it or report it.
- Keep a one-line log per round: what changed, which rule, result.

## 4b. Nudge or take over

The light-touch rules assume the work is basically sound. If it isn't, drop the cap and rework it properly.

Take over (full rework or redo) when any of these is true:
- Three or more MUST-BE-RIGHT failures at once, or one that breaks the whole piece (e.g. no consistent horizon, anatomy that reads as broken, a main flow that can't be completed, a 3D model that fails build checks).
- It fails the thumbnail and blur tests outright: no readable focal point or hierarchy at all.
- Fixing it with three-change rounds would take more than three rounds.
- It is unusable for its stated purpose.
- A rework still keeps the brief's idea and must-keeps (CD-5). Re-read the brief before regenerating.

Note: take-over fires easily on AI-generated images, which often break perspective or construction outright. That's expected. Regenerating with the construction spelled out is cheap, but it is where the subject drifts, so check CD-5 first in the next critique.

When taking over: keep the brief's intent (subject, mood, purpose), say plainly that it is a rework and which triggers fired, then run the normal loop on the new version. Otherwise, nudge.

## 5. When to stop

Stop when any of these is true. "Clearly better" is enough; don't chase perfection.

- No MUST-BE-RIGHT failures remain and the top-ranked improvements are done.
- The latest round is not clearly better than the one before (side-by-side test).
- Remaining points are questions no rule settles.
- The next fix would change the brief or something Gaz made or approved.
- Round 3 is reached for a routine piece (round 5 at most for anything). Report rather than polish.

**Hand-off to Gaz:** latest and previous render, the criteria judged, what was changed (with rule IDs), what was left and why, and the specific questions for him. Never call work "finished" on taste; he makes that call.
