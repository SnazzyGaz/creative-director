## Critique: Mauna Loa CO2 chart, round 1 (the before)

**Brief:** a 1600 x 1000 chart for an article on the Mauna Loa carbon dioxide record, read on phones and desktops. Data: NOAA Global Monitoring Laboratory annual means, 1959-2025 (public domain), unchanged. Must-keeps: the data and a source line. Done when a reader gets the main point without reading the article, and every label reads at the width the article shows it (800 px).
**Intent (AES-0):** purpose: show the size and steadiness of the rise [brief] / audience: general readers [brief] / mood: calm, factual [inferred] / style: editorial chart [brief] / focal experience: the line climbing [inferred] / polish: publishable [brief] / must-keeps: data, source [brief].
**Criteria judged against:** CD-1, CORE-1, CORE-3, CORE-6, CORE-8, CORE-10, TYPE-3, TYPE-7, TYPE-8, TYPE-9, TYPE-10, UI-6 (contrast maths applied to a chart), AES-2, AES-3, AES-10.
**Evidence looked at:** `before.png`, `look-before.jpg`, `src/chart.py`, and the contrast of the rainbow colours worked out from matplotlib's colour map.

### Brief check (CD-1, CD-5)
- Answers the brief: partly. The data is there, but the chart has no source line and the title gives no point.
- Content not in the brief: "Alarming increase!" with an arrow pointing at 2015, a judgement the data does not make on its own.

### Test results
- Blur: the grid is between 0.3 and 1.5 everywhere; the strongest cells are the legend and the frame, not the data.
- Greyscale: the rainbow becomes a mid-grey band that is lighter in the middle (green-yellow), so the bars look like they dip around 1990.
- Squint: a large coloured block; the rise is a slight slope at the top.

### Anatomy pass (CHAR-9, CHAR-10)
- Chart only; no figures. Not applicable.

### Meets criteria
- The data is plotted correctly and in full.

### Findings: MEASURED
- CD-1: no source line. **Blocker** (a must-keep).
- CD-1, AES-10 (MUST-BE-RIGHT): "Alarming increase!" is not in the brief. **Blocker.**
- TYPE-3, CORE-10: 67 year labels at 5 pt, rotated 90 degrees. At the 800 px article width that is about 7 px tall. **Blocker.**
- UI-6 maths: the rainbow puts 44 of 67 bars below 3:1 against the white ground (the lowest is 1.24:1). The red annotation is 4.00:1, below the 4.5:1 needed for text of that size.
- CORE-3: bars start at zero, so the 316-to-427 ppm rise uses the top 25% of the plot height. Each year also has a vertical grid line: 67 lines, plus 9 horizontal.
- CORE-8: a legend for a single series; the y label is "CO2" with no unit.

### Findings: INTERPRETED
- CORE-6, AES-3: feature: rainbow by year. Effect: the colour says "year" a second time, after the x axis, and suggests a hot-cold story the data does not tell. Confidence: high.
- CORE-1, AES-2: feature: the title "CO2 Levels Over The Years". Effect: it names the topic but not the finding, so the reader has to work out what to look at. Confidence: high.
- TYPE-9: feature: DejaVu Sans bold title, default matplotlib frame. Effect: reads as a notebook output, not a publishable chart. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] CD-1. Add the source: NOAA Global Monitoring Laboratory, Mauna Loa annual means, with the file date.
2. [BLOCKER] CD-1, AES-10. Remove "Alarming increase!" and its arrow.
3. [BLOCKER] TYPE-3, CORE-10. Year ticks every 10 years, horizontal, at 10.5 pt (about 15 px at 800 px wide).
4. [IMPROVEMENT] CORE-3, CORE-6, AES-3. One line in one accent colour (rust red, 5.58:1 on the paper colour) instead of 67 bars. The y axis runs from 300 to 440 ppm, so the rise fills about 80% of the height. A line chart does not need a zero baseline; the axis labels state the range. Light horizontal grid only.
5. [IMPROVEMENT] CORE-1, AES-2, CORE-8. A title that states what the data shows. A subtitle carrying the unit and the change in the yearly rise. Direct labels on the first and last points. No legend, no axis titles.
6. [IMPROVEMENT] TYPE-8. Subscript the 2 in CO₂ and use an en dash in ranges.
Text type: [edit] TYPE-10. Newsreader 560 (optical size 36) for the title: an editorial serif catalogued for news and long-form, made for screen reading. Source Sans 3 for everything else: a humanist sans catalogued for interfaces and data, with clear figures at small sizes.

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: the point (a steady, speeding-up rise) reads from the title and the line before any axis is read. Caused by the finding stated in the title, one accent line on a fitted axis, and direct labels. Costs:
  - The yearly values are no longer individually readable; the CSV is in `src/`.
  - The non-zero axis makes the rise look steeper than a zero-based chart. The labels state the range, but some readers will not check.
  Preference: strong; held with sides swapped.
- Additions: the title and subtitle state facts **[inferred]** from the data, not given in the brief. Both were checked against the file: every year-on-year difference is positive. The mean yearly rise was 0.86 ppm for 1960-1969 and 2.63 ppm for 2016-2025, a ratio of 3.05.

### Questions for the owner
- Should the chart also show the yearly rise as a second panel, rather than putting it only in the subtitle?

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [edit] CD-1: no source. Add NOAA GML, Mauna Loa annual means, file date.
2. [edit] CD-1, AES-10: "Alarming increase!" is not in the brief. Remove it.
3. [edit] TYPE-3: 67 year labels at about 7 px. One per decade, horizontal, about 15 px.
4. [redraw] CORE-3, CORE-6: rainbow bars from zero, 44 under 3:1. One rust line, axis 300-440, light horizontal grid.
5. [edit] CORE-1, AES-2: title names the topic. State the finding; unit and growth in a subtitle; label the end points; drop the legend.
6. [edit] TYPE-8: CO₂ subscript, en dashes.
Also possible (not needed): a second panel of the yearly rise. OK to go ahead with 1-6?
