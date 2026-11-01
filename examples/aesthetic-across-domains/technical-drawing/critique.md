## Critique: nest box exploded view, round 1 (the before)

**Brief:** an assembly sheet for a small-hole nest box (32 mm entrance) made from 15 mm board, to print at A4 landscape and pin up in a school workshop. Must show every part with its number, the eight screws and where they go, a parts list with sizes, and the order of assembly. Done when a 12-year-old with an adult can build it from the sheet alone.
**Intent (AES-0):** purpose: let someone build the box without asking [brief] / audience: pupils about 12 and a supervising adult [brief] / mood: calm, clear, trustworthy [inferred] / style: line-drawn instruction sheet [inferred from "assembly sheet"] / focal experience: see how six pieces become one box [inferred] / polish: finished print [brief] / must-keeps: part numbers, 8 screws, sizes, order [brief].
**Criteria judged against:** CD-1, CD-6, CORE-1, CORE-3, CORE-5, CORE-6, TD-PRO-1, TD-LIT-1, TYPE-3, TYPE-10, AES-2, AES-3, AES-4, AES-5.
**Evidence looked at:** `before.png` (1753x1240), `look-before.jpg`, `src/draw_before.py` (the default axis settings it kept).

### Brief check (CD-1, CD-5)
- Answers the brief: partly. Six parts and a hole are drawn; screws are shown as dots; there is no parts list with sizes and no assembly order.
- Content not in the brief: axes, grid, tick numbers, legend, a title with "Diagram" in it. Matplotlib defaults, not choices.

### Test results
- Blur: the brightest-contrast cells (1.6-1.8) are the overlapping orange front, blue base and purple side in the middle; no single part leads and the eye has no start point.
- Thumbnail: six coloured slabs in a grey box; the screws disappear.
- Greyscale: the tab10 colours collapse to near-equal mid-greys; at 50% alpha the parts behind show through, so edges cross faces everywhere.
- Squint: the grid and axis panes carry as much line as the object.

### Anatomy pass (CHAR-9, CHAR-10)
- Inventory: no figures or animals. Not applicable.

### Meets criteria
- CD-1: part names and the 32 mm hole match the brief.
- The explode directions are correct: every part moves away from the box along one axis.

### Findings: MEASURED
- TD-PRO-1 (MUST-BE-RIGHT): matplotlib's default box aspect is 4:4:3 while the limits are 450:450:500 mm, so one millimetre of height is drawn at **0.675** of one millimetre of width. The back panel (150 x 235 mm) reads nearly square. **Blocker**: a pupil cutting from this would doubt the sizes.
- CD-6 (done means the brief is met): screws are 8 scattered points (`ax.scatter`) with no shaft, no direction and no line to a part; four float in the middle of the base footprint where no panel sits. The sheet does not say where any screw goes. **Blocker** for an assembly sheet.
- CORE-5 / TYPE-3: 4 of 6 part labels sit on top of another part or an edge ("Part 2" crosses the front and the base, "Part 6" lies on the roof over the back, "Part 4" crosses the left side's edge, "Part 1" sits on blue at 50% alpha). Black 9 pt text on the blue base at 50% alpha measures about 4.3:1, below 4.5:1 for small text.
- CORE-1, AES-5: one line weight (1 pt) for edges, grid, axes and hole alike; ISO 128-2 (which replaced ISO 128-20) asks for at least two widths in a 2:1 ratio so outlines read above detail [S158].
- Brief gaps: no parts list with sizes, no assembly order.

### Findings: INTERPRETED
- AES-3: feature: six unrelated tab10 colours. Effect: colour suggests six materials or six meanings where there is one board. Trade-off: one colour per part can help matching to a list; here there is no list to match. Confidence: high.
- AES-2 / CORE-3: feature: grid, panes and ticks at the same weight as the parts. Effect: the object competes with its own coordinate system. Confidence: high.
- AES-4: feature: transparent faces. Effect: reads as a screen preview, not something to build from; nothing feels solid. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] TD-PRO-1. True proportions: an isometric projection at equal scale on all three axes, so 235 mm looks taller than 150 mm by the right amount.
2. [BLOCKER] CD-6. Every screw drawn as a screw, aimed at its hole, with a thin chain line showing the path; one balloon (7) and a quantity in the list.
3. [IMPROVEMENT] CORE-1, AES-5, AES-4. Solid opaque faces with three flat tones (lit top, front, side), thick outer outline, thin inner edges, extra-thin chain lines (4:2:1); remove axes, grid, panes and legend.
4. [IMPROVEMENT] CORE-5, TYPE-3, ISO 6433 [S159]. Numbers in circles (balloons) outside the drawing, in two aligned columns, with leader lines ending on a dot inside each part; no text on the parts.
5. [IMPROVEMENT] AES-3, CORE-6, CD-6 brief gaps. One neutral palette plus one accent kept for the screws (the only bought parts); add the parts list with sizes and a three-step order.
Text type: [edit] TYPE-10, Public Sans for the notes (catalogued as neutral and legible for UI and documents) and Martian Mono for numbers and sizes, so figures line up in the list.

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: you can see what to screw where. Caused by: true proportions, drawn screws with paths, balloons and a list. Cost: the 3D view can no longer be rotated by re-running with another angle without redrawing balloons; colour coding of parts is gone (the list does that job now). Preference: strong; held with sides swapped.
- Additions: the parts list, sizes and assembly order are asked for in the brief. The note line ("Chain lines show where each part moves to") explains a convention; it adds no content. Nothing else added.

### Questions for the owner
- Should the sizes go on the drawing as dimensions as well as in the list? The brief says "sizes"; the list covers it at less clutter.
- Pilot holes: should the sheet say to drill them? That is content, so not added.

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [redraw] TD-PRO-1: height is drawn at 0.675 of width. Switch to true isometric, equal scale on all axes.
2. [redraw] CD-6: screws are loose dots. Draw all 8 as screws aimed at their holes, with chain lines.
3. [redraw] CORE-1, AES-4: one line weight, see-through faces, grid and axes. Opaque faces in three tones, lines at 4:2:1, no axes or legend.
4. [edit] CORE-5, TYPE-3: 4 of 6 labels sit on parts. Numbered balloons in two aligned columns outside the drawing.
5. [edit] AES-3: six meaningless colours, and the list and order are missing. Neutral palette, orange only for screws; add parts list and three steps.
Also possible (not needed): dimension lines on the drawing. OK to go ahead with 1-5?
