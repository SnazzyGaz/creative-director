## Critique: README.md, round 1

**Brief:** front page of the repo on GitHub. For people and agents deciding in a few seconds whether to use it. The one idea: "an agent can judge its own visual work with cited rules, lightly". Seen at ~1012 px on desktop and ~390 px on a phone, light and dark themes. Must-keeps: section order from the request, no badge walls or emoji, value obvious in 5 seconds (CD-1).
**Criteria judged against:** CORE-3, CORE-5, CORE-10, UI-2, UI-3, UI-7, ILL-11, UI-10.
**Evidence looked at:** `round-01-1280.png`, `round-01-390.png` (GitHub's own markdown renderer via `gh api markdown`, with github-markdown-css, headless Chrome); `tools/look.py` on the 1280 render.

### Brief check (CD-1, CD-5)
- Answers the brief: yes. Banner, pitch and before/after strip fit in the first screen at 1280. Must-keeps intact: yes.

### Test results (evidence)
- Squint/blur: the banner title and the strip lead, then the H2s. Intended order.
- Thumbnail: at 390 the banner subtitle is ~7 px tall and the loop diagram's labels ~4-5 px. Neither readable.
- Flip/mirror: no imbalance worth noting; the banner's drawing sits right, the type left.
- Greyscale: three value groups (page white, cream panels, dark photos and type). 86% of pixels in the lightest bin, so the strip carries the contrast.
- Crop/edges: the images sit directly on the next text block; at 390 the strip's caption collides with the strip.

### Meets criteria
- CORE-3: one focal point per screen: the title, then the strip.
- UI-7 / ILL-11: restrained palette (paper, ink, one rust accent), one serif and one sans, no gradients, glow or emoji.
- CORE-8: no badge wall; the hero image is the only decoration.

### Needs improvement (ranked)
1. [BLOCKER] CORE-10 / UI-10 not met. Banner subtitle and loop labels unreadable at 390 px (measured: ~7 px and ~5 px cap height). Fix: shorten the banner subtitle and enlarge it; drop the loop's sub-lines and enlarge the step names.
2. [IMPROVEMENT] CORE-5 / UI-3 not met. The three `<picture>` blocks get no bottom margin, so text sits on the image edge, and the caption overlaps the strip at 390. Fix: wrap each picture in a `<p>` so it takes the standard paragraph spacing.
3. [IMPROVEMENT] UI-2 not met. The three-column Usage table wraps the trigger phrases letter-group by letter-group at 390 (`+` alone on a line). Fix: two columns, trigger phrase under the mode name.

### Next round
- Apply the 3 fixes, rebuild the images (`docs/assets/src/build.py`), re-render at 1280 and 390, compare.

### Questions for the owner
- The strip stays 3-up on phones (small but recognisable). A stacked phone variant is possible; worth the extra asset?
