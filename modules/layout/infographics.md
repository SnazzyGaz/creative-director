# Infographics: information first, one designed piece (INF-1 to INF-6)

Load with the layout README for any infographic: how-to, process, data, map or route, safety, children's, fact or timeline sheet. Format: **What / Check / Fix / Why / Grade**. INF-1, INF-4 (accuracy) and INF-6 are **MUST-BE-RIGHT**; the rest are defaults.

**Why this file exists.** In the repo's blind test the owner of the work judged two infographic batches. Batch 6 (v0.9.4) went 4 to 6: the losses were sterile, "like a PowerPoint slide". Batch 7 (v0.9.5) answered with the full energy pass and went 3 to 7, worse: heavy illustration "way over-illustrated, unbalanced", charts "cut into the graphic, cheap and pasted on", a graphic that "doesn't belong", a "samey" timeline, an "amateurish" central title, a photoreal sheet that dropped text and a comic with a medical error. The winners on both sides were compact, balanced and information-dense, in one coherent style, with simplified icons for secondary facts, a clear flow between steps, each step or period visibly different, punchy type and some warmth. These rules aim at that middle. Internal evidence, one judge (`examples/blind-test/RESULTS.md`).

### INF-1. Layout first; the chart is designed in, not pasted on (MUST-BE-RIGHT for the data marks)
- **What:** Before any image, plan the information: the hierarchy (title, hero chart or diagram, two or three secondary facts, the source or action), a grid, and one reading path. The chart, map or diagram is the hero, drawn in the same visual language as the rest: the palette, line weight, corner style, type and ground. Two recipes; pick the one that looks most integrated:
  - **A. Code-built** (preferred where the data carries the piece): build the whole sheet in code (SVG, HTML or `tools/datagraphic.py` on a designed ground), with the title, text, chart and icons in one system, and generated illustration only as contained spot art placed in the grid.
  - **B. Generated, then marks replaced:** generate the full design with the chart area styled as part of it (axis, tracks or ring in the piece's colours, on its ground), then replace only the data marks with code-accurate ones in matching colours, corners and type (`bars` with `corner`, `donut`, `route`; transparent layers, no `bg`). Never a white box or panel dropped onto finished art.
- **Check:** (a) no panel or white box behind the chart unless every other block sits on the same kind of card: `datagraphic.py check-panel IMG --box` on the chart area; (b) labels are not cut by strokes, lines or art (`route` moves labels off the line and reports it); (c) the chart's colours and type are the piece's own; (d) the chart collides with no illustration; (e) the marks pass `check-bars` or `check-donut`; routes close with a bridge at each crossing (LAY-19).
- **Fix:** Re-plan the layout with the chart as the hero area; restyle the marks to the piece; move to recipe A if B keeps leaving a seam.
- **Why:** "Charts cut into the graphic and look cheap and pasted on" (S73); "the graphic doesn't belong", "very unbalanced" (S74); strokes cutting through route labels (S71).

### INF-2. Illustration budget
- **What:** One supporting spot illustration, or one consistent icon set, not both competing. Secondary facts get simplified icons. No full scene behind data, no illustration taking more area than the information, and no photoreal unless the brief asks.
- **Check:** Estimate the areas in the thumbnail: illustration ≤ information (title, chart, text and icons), and one spot at most. Are all icons one style and weight? Is anything photoreal?
- **Fix:** Shrink or crop the spot art, turn secondary pictures into icons, regenerate in a flat drawn style.
- **Why:** "Way over-illustrated, unbalanced info presentation"; the winner used "simplified icons for sub-info" (S76); a photoreal sheet was "too demonstrative" (S70).

### INF-3. Each step or period looks different, and the steps flow
- **What:** Each step, stage or time period has its own visual: a frame shape, a colour band or an icon of what changes. Visible connectors (arrows, a path, a timeline spine, transitions) carry the eye from one to the next. No samey repeats; the same people and objects across steps (LAY-18).
- **Check:** Cover the labels: can you still tell the periods or steps apart? Follow the connectors once, start to end, without a jump.
- **Fix:** Give each step its own framing or colour; draw the path between them.
- **Why:** "Framing differentiates times better; the other reads samey" (S78); "transitional flow reads better" (S75).

### INF-4. The chart type fits the data (MUST-BE-RIGHT for accuracy)
- **What:** Part of a whole (shares adding to 100%, "of every £1"): a pie or donut, six slices at most, angles exactly from the data (`datagraphic.py donut`). Comparison or ranking: bars on a common baseline. Change over time: a line or a timeline. Two numbers: two bars or a big-number pair, not a chart padded out. Always drawn from the data in code (LAY-19).
- **Check:** Name the data's job in three words (share, compare, change); does the chart type match? `check-donut` or `check-bars` passes.
- **Fix:** Redraw as the fitting type.
- **Why:** A part-of-whole budget lost as bars in a white panel to a donut that "reads nicer" (S72), though that donut was about 8 points wrong; the right type, drawn accurately, keeps both wins. Bars on a common scale are read more accurately than angles for comparison [S337], while for a part's share of the whole pies do as well as bars or better [S338].

### INF-5. A hero title with hierarchy logic
- **What:** The title is set confidently (a display face or weight, a clear size step, TYPE-2, TYPE-9) and placed by the layout's logic: top left or across the top band on the grid, tied to the hero, not plonked in the centre with nothing below it in order.
- **Check:** In the thumbnail, does the title read first or second (after the hero), and does its position follow the grid?
- **Fix:** Align it to the grid, raise the size step, cut ornaments round it.
- **Why:** "Central hero title mildly amateurish" (S75).

### INF-6. Every required word, and safety or medical steps checked (MUST-BE-RIGHT)
- **What:** Every line of the brief's copy appears, word for word (CD-1). Safety and medical steps are checked against the brief, panel by panel: what is held, where, in what order (an inhaler goes in the spacer, not the mouth; nobody stands on the ice the sheet warns against).
- **Check:** Tick each brief line off on the render. One line per panel: does the picture show what the step says, safely?
- **Fix:** Set missing copy in code; redraw the wrong panel only (LAY-18).
- **Why:** A thin-ice sheet dropped two required lines and showed people on the ice (S70); a comic showed the inhaler without its spacer (S77).

**Grade, all six:** Procedure from internal evidence, one judge, two batches; INF-4's chart-reading claims are well supported [S337, S338]. Untested until another infographic batch is judged.
