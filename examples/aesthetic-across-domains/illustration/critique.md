## Critique: "The long way home" picture-book spread, round 1 (the before)

**Brief:** a double-page spread for a picture book, printed at two A4 pages landscape (about 594 x 210 mm spread, 16:9 art here), read aloud to children aged 4-7. Story line on this spread (must appear, set in type): "Every evening, Nell and Biscuit walked the long way home, past the harbour wall." Must-keeps: Nell (about seven, yellow raincoat), Biscuit (small scruffy brown dog), the harbour wall, evening, room for the line of text. Done when the line reads easily, the pair lead the spread, and nothing important falls in the fold.
**Intent (AES-0):** purpose: carry one line of a bedtime-style story [brief] / audience: children 4-7 and the adult reading [brief] / mood: quiet, cosy, routine; "every evening" is a habit, not an event [inferred from the text] / style: painted picture-book illustration [inferred] / focal experience: the two friends walking home together [inferred] / polish: finished print art [brief] / must-keeps: as above [brief].
**Criteria judged against:** CORE-2, CORE-3, ILL-2, ILL-6, ILL-11, TD-LIT-1, LAY-5, TYPE-3, TYPE-10, UI-6 (contrast maths applied to print), AES-2, AES-3, AES-6, AES-7, CHAR-9, CHAR-10.
**Evidence looked at:** `before.jpg` (2560x1440), `look-before.jpg`, `anatomy-before/sheet.jpg`, chroma and contrast numbers from `../src/common.py`.

### Brief check (CD-1, CD-5)
- Answers the brief: partly. Both characters, the wall and evening are there; the text is set but crosses the fold.
- Content not in the brief: lighthouse, seagull, spired town on a cliff, street lamp, flowers. Not wrong in a first draft; each adds detail that competes with the pair.

### Test results
- Blur: the sun and its reflection lead (blur grid peak 2.6 at the centre-right cell); Nell sits in a 1.6-1.8 cell, so she comes second.
- Thumbnail: girl readable; dog merges with the cobbles; the text is unreadable.
- Flip: the eye still goes to the sunset first.
- Greyscale: three value groups spread evenly across the frame; the figures share the mid group with the town and boats.
- Crop and edges: the generator drew a book's fold line down the middle; a boat and the sun's reflection sit on it.

### Anatomy pass (CHAR-9, CHAR-10)
- Inventory: one girl (one hand visible, the other in her pocket), one dog, one seagull (background).
- `anatomy-before/sheet.jpg` | A2-A7 leash hand | PASS | fist round the lead handle, traced up the right sleeve.
- pocket hand | A3 | PASS | hand inside the pocket, sleeve continuous.
- face | A8 | PASS | eyes match.
- dog | A9 | PASS | four legs, one tail, eyes match.
- No anatomy blockers in the before.

### Meets criteria
- CHAR-9, CHAR-10: pass (above).
- CD-1: the story line is set as given, no invented text.

### Findings: MEASURED
- LAY-5 (MUST-BE-RIGHT): the text block spans x = 573-1987 of 2560, so it crosses the fold at x = 1280; "walked" sits in the gutter. **Blocker.**
- TYPE-3 / UI-6 maths: white text on the sky, line 1 is 5.85:1 on the mean ground but **1.72:1** against the brightest cloud behind it; line 2 is 3.67:1 mean, **1.41:1** worst. Large text needs 3:1. **Blocker** where it falls on the bright cloud.
- TD-LIT-1 (MUST-BE-RIGHT), checked by eye at 2x: the sun is low and behind the boats (centre-right, back light), yet Nell's face and coat are lit from the front-left and the lamp throws its own warm light. Two key lights with different directions. **Blocker.**
- ILL-11: four generic-look tells (glaring sunset, detail everywhere, saturated purple-orange grading, sparkling water). Chroma: mean C* 29.2, 26.8% of pixels above C* 40, so saturation is spread over the whole frame rather than kept for the raincoat.
- CORE-3 / ILL-2: blur peak on the sun, not the pair (numbers above).
- TYPE-10: Chewy is catalogued for cartoon titles and short display; this is a sentence read aloud. Display face for running text.

### Findings: INTERPRETED
- AES-7: feature: a blazing sunset, a castle-like town and a lighthouse. Effect: reads as a spectacular evening, not "every evening"; the routine and the friendship are lost. Trade-off: quieter light loses first-glance wow. Confidence: high.
- AES-6: feature: stock "magical harbour" props. Effect: swap the text for any seaside story and the picture still fits. Trade-off: fewer props means fewer things for a child to spot. Confidence: medium.
- AES-2: feature: the pair are large but share contrast and detail with everything else. Effect: no clear winner at a glance. Trade-off: lifting them means turning the rest down. Confidence: high.
- AES-1: feature: the wall runs out of the left edge; Nell faces right but stands on the left page with the town behind her. Effect: no path to "home"; the page turn has no pull. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] TD-LIT-1. One key light: the afterglow after sunset on the right; figures lit only from that side; no lamp glow.
2. [BLOCKER] LAY-5, TYPE-3. Text moves to a plain area of sky on the left page, clear of the fold, dark ink at 4.5:1 or better against the worst pixel; nothing important in the middle 12% of the width.
3. [IMPROVEMENT] CORE-3, ILL-2, AES-2. The pair lead: placed against plain sky on the right page, the rest of the frame turned down in contrast and detail.
4. [IMPROVEMENT] ILL-11, AES-3. One muted blue-grey family; saturation kept for the raincoat; the warm glow and lit windows echo it.
5. [IMPROVEMENT] AES-7, AES-6, AES-1, ILL-6. The habit, not a show: the wall curves towards a few cottages (home), the pair walk towards them (and the page turn); remove lighthouse, gull, lamp, flowers and spires. Removal only; nothing added.
Text type: [edit] TYPE-10, set in Fredoka (catalogued for picture books) at reading weight.

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: at a glance it says "two friends walking home" instead of "sunset". Caused by: one light from the right, plain sky around the pair, a path that ends at home, muted palette. Cost: less first-glance spectacle; fewer things for a child to find; the figures are smaller in the frame. Preference: strong; it held with sides swapped.
- Additions: none. Everything in the after is in the brief or the before (cottages were the before's town, simplified). Items removed: lighthouse, gull, lamp, flowers, spires.

### Questions for the owner
- Biscuit now trots just ahead of Nell; in the before he walked beside her. Is either relationship part of the story?
- Fredoka at weight 500 or a book serif for the running text? Both are defensible for read-aloud books.

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [regenerate] TD-LIT-1: two lights (sun behind, face lit from the front-left, lamp glow). One light: the afterglow on the right; figures lit from that side only.
2. [edit] LAY-5, TYPE-3: the text crosses the fold and drops to 1.4:1 on the bright cloud. Move it to plain sky on the left page in dark ink, at least 4.5:1, and keep the fold clear.
3. [regenerate] CORE-3, AES-2: the sunset wins the blur test. Put Nell and Biscuit against plain sky on the right page and turn the rest down.
4. [regenerate] ILL-11, AES-3: saturation everywhere. One muted blue-grey family; the raincoat is the one strong colour.
5. [regenerate] AES-7, AES-6: reads as a spectacle, not "every evening". Wall leads to the cottages they walk towards; remove lighthouse, gull, lamp, flowers, spires.
Also possible (not needed): a book serif for the text. OK to go ahead with 1-5?
