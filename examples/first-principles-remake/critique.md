## Critique: seed-swap poster, first-principles remake (concept B), round 1

Self-judged by the agent that made it. No owner reviewed it.

**Brief:** see [brief.md](brief.md), 7 lines, FP-4.
**Intent (AES-0):** purpose: people come with seeds [inferred from the brief] / audience: plot-holders and neighbours [inferred] / mood: friendly, practical [inferred] / style: typographic poster [brief] / focal experience: "Bring ... Take" from across the path, then the date [inferred] / polish: home-printed A3 [inferred] / must-keeps: the given text, type only [brief].
**Criteria judged against:** FP-1..8, CD-1, CD-5, CORE-1, CORE-3, CORE-4, CORE-5, LAY-2, LAY-7, TYPE-1, TYPE-3, TYPE-10, UI-6 (contrast maths applied to print), BRAND-4, BRAND-8, AES-2, AES-9, AES-10, CHAR-9, TD-LIT-1.
**Evidence looked at:**
- `remake.png` (1754 x 2480, A3 at 150 dpi);
- `look-remake.jpg`;
- `far-view.png` (each sheet at 10%);
- the text boxes and the bare ground from `src/make_remake.py`;
- `tools/contrast.py`.

### Brief from first principles (FP-1..8)
- **Trigger (FP-1):** "rejig ... from scratch".
- **Step back and fact check (FP-2, FP-3):** see [brief.md](brief.md). One conflict was found: 14 March 2027 is a Sunday, not a Saturday. The weekday is held back.
- **Concepts (FP-5):** [concepts/concepts.jpg](concepts/concepts.jpg).
  - A: the poster is the back of a seed packet, and the variety label leads.
  - B: the sheet is split in two, Bring above and Take below, inverted. The action leads.
  - C: a March calendar with the day marked. The date leads.
  - Structure test: the three one-sentence descriptions differ without naming a font or colour. **Pass.**
- **Recommend (FP-6): B.** It puts the poster's one job, what to bring and what you get, in the far read. Those words were small print in both earlier versions.
  - Dropped A: it carries the most charm and the clearest "seeds" signal, but its details sit in a table that only reads up close. Its far read is the name alone, the same as the light-touch fix.
  - Dropped C: it makes "when" unmissable, but it spends the sheet on 31 numbers, 30 of which mean nothing. It also leans hardest on the unconfirmed weekday.

### Test results (evidence)
- **Far read (LAY-7, 10%):** "Bring", "spare seeds", "Take", "some home" and the date all read. "Seed swap" reads as a second-level heading.
- **Blur grid** (`look.py`, rows top to bottom): the peaks are 3.1-3.7 (Bring) and 3.3-3.5 (the date and Take rows). The light-touch fix peaks at 5.0 on SEED SWAP and drops to 0.7-1.0 for its bottom row (the details).
- **Greyscale:** two value groups, with a 42/53% split. The structure is the figure-ground swap itself.
- **Crop and edges:** text ends 132 px (22 mm) from every edge. "Hollin Lane Allotments" right-aligns to the rule's end. Nothing touches the frame.
- **Flip:** the heavy lower half balances the larger word above it. No tilt.

### Anatomy pass (CHAR-9, CHAR-10)
- **Inventory:** no people, hands or animals. The poster is type only. **n/a.**

### Light (TD-LIT-1)
- Flat two-ink print, with no modelled light, shading or shadows. **n/a.**

### Marks (BRAND-4, BRAND-8)
- No logo was supplied, and the brief names none. No generated imagery is used. **None present; pass.**

### Meets criteria
- **CD-1, AES-10:** only the given words. Checked line by line against the brief; nothing added.
- **CD-5:** every given fact is present. The one exception is the weekday, which is held back on purpose (FP-3) and reported here.
- **TYPE-10:** Bricolage Grotesque (`fonts/grotesk-neutral/`) for the display lines. Its 75% width at 800 weight keeps "Bring" and "Take" at one size. Hanken Grotesk for the near read. Not Fraunces, and not the faces of either earlier version.
- **CORE-5:** one left edge at the 22 mm margin for every line.

### Findings: MEASURED
- **UI-6 maths on print (TYPE-3):**
  - ink #212b1e on paper #eee4ce: 11.63:1;
  - paper on ink: 11.63:1;
  - date #a33c21 on paper: 5.15:1. The date is large text, so it needs 3:1, and it also clears 4.5:1.
  - Worst pixel equals the mean, because the grounds are solid. **Pass.**
- **Ink box heights at A3:**
  - Bring 105.8 mm; Take 86.5 mm (one font size; "Bring" has an ascender and a descender);
  - spare seeds 23.9 mm; some home 20.3 mm;
  - date 20.5 mm; Seed swap 21.2 mm;
  - time line 8.8 mm; details 8.0 mm; site name 6.8 mm.
- **LAY-7 trade-off (measured):** the date is smaller here than in the light-touch fix (20.5 mm box vs 30.6 mm caps there), and so is the event name. The remake spends its biggest type on what to do, not on what or when.

### Findings: INTERPRETED
- **AES-2:** the figure-ground inversion between the halves makes the swap itself visible. Effect: the two-way trade reads before any word does. Trade-off: about 53% of the sheet is solid dark ink, which is heavy on a home printer and may band. Confidence: medium.
- **AES-9, three-way comparison:**
  - Original: not a contender (contrast blockers, invented copy).
  - Light-touch fix: stronger on "what" and "when" at distance.
  - Remake: stronger on "what to do". It is the only version where a neighbour who has never heard of a seed swap learns what it is, and what to bring, from across the path.
  - Preference for the brief's one job: the remake, **marginal to strong**. This was not re-tested with left and right swapped.
  - "The light touch was enough" is a fair answer if the owner's audience already knows the event.

### Needs improvement (ranked)
1. **[QUESTION, blocks printing]** FP-3: the weekday. Is it Saturday 13 or Sunday 14 March 2027? Once the owner answers, add the day before the date.
2. **[IMPROVEMENT]** LAY-7: if the owner wants the date to read further, the date line has room to grow to about 200 px (24 mm) without crowding "spare seeds".
3. **[QUESTION]** Print: the solid lower half on a home printer. Options: keep it, print it at a shop, or use a light-tint version (contrast would need re-checking).

### Delivery checklist (FLOW-3)
1. **Brief from first principles (FP-4):** done. Seven lines, self-approved for the demo.
2. **Facts word for word, nothing added (FP-3, AES-10):** done. The weekday is held back and asked about.
3. **2-3 structurally different concepts, with a recommendation (FP-5, FP-6):** done. Three concepts; B recommended; A and C dropped with reasons.
4. **Full QA (FP-7):** done.

QA re-run on the final render:
- light: n/a (flat print);
- anatomy: n/a (inventory: none);
- type size and contrast: pass (lowest 5.15:1);
- marks: none;
- additions: none.
