## Critique: allotment seed swap poster, round 1 (the before)

**Brief:** a type-only A3 portrait poster for the noticeboard and gate of an allotment site (Hollin Lane Allotments is made up for this example). Text given: "Seed Swap", Hollin Lane Allotments, Saturday 14 March 2027, 10:00 to 13:00, in the hut; bring spare seeds and take some home; envelopes provided; free; tea in the hut. No pictures. Done when someone walking past the gate knows what and when from across the path, and the rest reads up close.
**Intent (AES-0):** purpose: get plot-holders and neighbours to turn up [brief] / audience: allotment holders, many older, reading outdoors [inferred] / mood: friendly, homemade but sure of itself [inferred] / style: typographic poster [brief] / focal experience: "seed swap, Saturday" from across the path [brief] / polish: home-printed A3 [inferred] / must-keeps: the text above [brief].
**Criteria judged against:** CD-1, CORE-1, CORE-4, CORE-5, CORE-6, LAY-1, LAY-2, LAY-3, LAY-7, TYPE-1, TYPE-3, TYPE-6, TYPE-9, TYPE-10, UI-6 (contrast maths applied to print), AES-1, AES-2, AES-3, AES-10.
**Evidence looked at:** `before.png` (1754 x 2480, A3 at 150 dpi), `look-before.jpg`, `far-view.png`, text boxes and the bare gradient from `src/make_before.py`.

### Brief check (CD-1, CD-5)
- Answers the brief: mostly. All the given facts are there.
- Content not in the brief: "Join us for our annual" (nobody said it is annual), "cake", "All welcome!", "Don't miss out!", "Fellow gardeners". Each is a claim or a promise the organisers did not make.

### Test results
- Far read (LAY-7, 10%): "SEED SWAP!" reads; the date line is a smudge of white on olive; the details are gone.
- Blur: the grid peaks at 1.1 on the headline row, then drops to 0.3 for everything below; the date has no more pull than the venue.
- Greyscale: white text on a ground that gets lighter towards the bottom, so the lower lines fade exactly where the details are.
- Squint: the lower 29% of the sheet is empty yellow.

### Anatomy pass (CHAR-9, CHAR-10)
- Type only; no figures. Not applicable.

### Meets criteria
- TYPE-1: one family.
- The headline is the biggest thing on the sheet.

### Findings: MEASURED
- UI-6 maths on print (TYPE-3): white text against the bare gradient behind each line, mean: headline 3.67:1, venue 3.02:1, **date 2.78:1, time 2.55:1, details 2.09-2.32:1**. The drop shadow helps a little up close and blurs at distance. Details need 4.5:1, large lines 3:1. **Blocker** for the when and the details.
- CD-1, AES-10 (MUST-BE-RIGHT): five phrases not in the brief ("annual", "cake", "All welcome!", "Don't miss out!", "fellow gardeners"). **Blocker.**
- LAY-7, CORE-1: headline cap height 39.8 mm and the date 14.4 mm on a 420 mm sheet; the date is the same size as the venue and the time. Three levels collapse into two.
- LAY-2: text ends at y = 1735 of 2480; the bottom 29% is unused while the details are set at 6.3 mm caps.
- TYPE-6: the details are long all-caps lines in a condensed display face (Bebas has no lower case), centred, 44 characters wide, with no extra tracking.

### Findings: INTERPRETED
- AES-3: feature: green-to-yellow gradient. Effect: says "nature" generically and costs contrast; it is the only idea on the sheet. Trade-off: it is bright and noticeable from far off. Confidence: high.
- AES-1, CORE-5: feature: every line centred. Effect: ragged both sides, no edge for the eye to return to; the block of details reads as a paragraph of shouting. Confidence: medium.
- TYPE-9: feature: Bebas Neue, exclamation marks, gradient. Effect: the common "event poster" template; nothing says allotment. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] UI-6, TYPE-3. Solid paper ground and one dark ink, 4.5:1 or better everywhere; no shadows.
2. [BLOCKER] CD-1, AES-10. Use only the brief's words; remove "annual", "cake", "All welcome!", "Don't miss out!", "fellow gardeners".
3. [IMPROVEMENT] LAY-7, CORE-1, AES-2. Three levels: "SEED SWAP" filling the measure for the far read; the date as the second level in the one accent colour; time, place and details as one near-read block.
4. [IMPROVEMENT] LAY-1, LAY-2, CORE-5, AES-1. Flush left on a 12-column grid with 22 mm margins; use the full height; one rule under the site name.
5. [IMPROVEMENT] TYPE-6, TYPE-9, AES-3. Details in sentence case in a text face; drop exclamation marks; two inks only (deep green for text, tomato red for the date).
Text type: [edit] TYPE-10, Antonio for the headline and date (condensed poster face with real lower case, catalogued for posters), Cabin for the details (warm humanist sans catalogued for outdoorsy and craft brands).

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: what and when read from the far view; before, only "what" did. Caused by: 110 mm headline caps, a red date at 31 mm, solid ground. Cost: the after is calmer and less "event-like"; the headline takes so much room that the details are smaller than before (5.9 mm caps against 6.3 mm); the two inks need a colour printer for the red (in black only, the date still reads by size). Preference: strong; held with sides swapped.
- Additions: none. "Sat" and "10:00 to 13:00" restate the brief; the rule under the site name is a layout element.

### Questions for the owner
- Should "cake" go back if there will be cake?

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [edit] UI-6: the date and details fall to 2.1-2.8:1 on the gradient. Solid paper, dark ink, 4.5:1 or better.
2. [edit] CD-1, AES-10: five phrases not in the brief. Remove them.
3. [relayout] LAY-7, CORE-1: date the same size as the venue. Headline fills the measure; date second, in one accent; one detail block.
4. [relayout] LAY-1, CORE-5: centred and the bottom 29% empty. Flush left on a 12-column grid, full height.
5. [edit] TYPE-6, AES-3: all-caps details, exclamations, gradient. Sentence case in Cabin, no exclamations, two inks.
Also possible (not needed): a second, black-only print version. OK to go ahead with 1-5?
