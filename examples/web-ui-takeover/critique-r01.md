## Critique: Crumb & Co landing page, round 1

**Brief:** see `brief.md`. Pre-orders for weekend bread; neighbours on phones; one idea: order by Thursday, collect Saturday. Must-keeps: name, pre-order action, hours, address, brand orange #E8743B, the three loaves.
**Criteria judged against:** CD-1, CD-5, CORE-1, CORE-3, CORE-5, CORE-6, CORE-7, CORE-8, CORE-10, UI-1, UI-4, UI-5, UI-6, UI-8, UI-10, UX-1, UX-6.
**Evidence looked at:** round-01-390.png, round-01-1280.png, round-01-zoom200.png (tools/shot.sh); look-r01.png (tools/look.py, 390 px); contrast-r01.txt (tools/contrast.py, 11 pairs).

### Brief check (CD-1, CD-5)
- Answers the brief: no. The Thursday/Saturday idea is buried in the fourth sentence of a purple box with 1.43:1 contrast. Must-keeps present in the code: yes, all six. Visible on a phone: no (hours and address are off-screen to the right at 390 px).

### Test results (evidence)
- Squint/blur: the name and the yellow loaves box lead. The pre-order box and its button do not register.
- Thumbnail: only "Crumb" survives. No action is visible.
- Flip/mirror: boxes overlap at random offsets; one is rotated -4 deg. No shared edge.
- Greyscale: the background gradient spans the full value range left to right, so every element sits on a changing ground. Pre-order box is one flat mid grey with its text inside it.
- Crop/edges: at 390 px the pre-order box and the hours box are cut by the right edge (fixed 1250 px layout). Large empty area below the boxes on desktop.

### Meets criteria
- None of the rules in scope is met in full. The name is the largest text on the page (part of CORE-1), which is worth keeping.

### Needs improvement (ranked, biggest first, max 5)
1. [BLOCKER] UX-1 not met. Pre-order flow cannot be completed: "Submit" and "Go" are spans with no target, and on a phone the pre-order box is clipped off-screen. Fix: one real pre-order link/button, in the normal flow, visible at 390 px.
2. [BLOCKER] UI-6 not met. 11 of 11 measured text pairs fail (worst: footer 1.13:1; pre-order text 1.43:1; best: "click" 2.91:1). Fix: one light ground, dark text, brand orange used only where it passes or on large text.
3. [BLOCKER] UI-10 / CORE-10 not met. Fixed 1250 px wrapper and absolute positioning: content overflows at 390 px and at 200% zoom. Fix: single-column flow layout with max-width.
4. [IMPROVEMENT] UI-1 / CORE-7 not met. Six typefaces in use (Courier Prime, Pacifico, Bungee, Lobster, Special Elite, Comic Neue; Creepster was requested but is not installed and fell back to a serif). Fix: one display face plus one text face.
5. [IMPROVEMENT] CORE-1 / UI-4 / CORE-6 / UX-6 not met. No order of reading; four button colours with no roles; nine nav items for a one-page bakery; copy is filler ("Artisanal Synergy"). Fix: name, the one idea, the action, then loaves, then hours; plain copy from the brief.

### Take-over check (4b)
- Three MUST-BE-RIGHT failures at once (UX-1, UI-6, UI-10). Fails thumbnail and blur outright. Unusable for its stated purpose. **Take over: full rework.**
- Rework keeps every must-keep (CD-5): name, pre-order action, hours, address, #E8743B, the three loaves.

### Questions for the owner
- Is there a real ordering system to link to, or should the button open an email/phone order?
- Any brand typeface? The rework will use a serif display face and a sans text face as a placeholder pair.
