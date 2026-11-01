## Critique: README.md, round 2

**Brief:** as round 1.
**Criteria judged against:** CORE-3, CORE-5, CORE-10, UI-2, UI-3, UI-7, ILL-11, UI-10.
**Evidence looked at:** `round-02-1280.png`, `round-02-390.png`; compared with round 1.

### Fixes applied? (section 4)
1. Banner subtitle shortened to "Design judgement for AI agents" and set at 38 px (was 25 px): ~11 px tall at 390. Loop step names at 30 px, sub-lines dropped: ~8-9 px at 390. Applied.
2. Pictures wrapped in `<p>`: standard spacing below each image. Applied. The caption collision turned out to have a second cause: GitHub's CSS gives `<sub>` a line-height of 0, so a caption that wraps overprints itself. Caption is now plain text. Applied.
3. Usage table is two columns with the trigger under the mode name; no orphaned `+` at 390. Applied.

### Test results (evidence)
- Thumbnail: banner title and subtitle readable at 390; loop step names readable; the loop's side notes (~5 px) are not, but the text below the image says the same.
- Crop/edges: every image has clear space above and below.

### Also corrected
- The banner's annotation read "axis ⟂ minor", which says the opposite of TD-ELL-1. It now reads "minor axis = cylinder axis".

### Result
Clearly better at phone size, unchanged at desktop. No blockers left. Stopped.

### Questions for the owner
- Stacked phone variant of the before/after strip: not made (see round 1).
