# Composition: the Sitting right pass (COMP-19 to COMP-25)

On-demand part of `modules/composition/`: load it for the pre-delivery check, or on its own when only that check is needed. Format and grades as in the module README.

Before delivery, ask one question of the whole piece: **does anything sit weirdly?** This is a judgement call backed by evidence, not another placement rule. The rules in the module README (COMP-1 to COMP-18) say how to build a composition. This pass looks only for **broken** balance: something that reads as accidental, unresolved or lopsided by mistake.

**What it is not.** Balance means the visual weights are in equilibrium. It does not mean sameness, symmetry or centring. Asymmetric, off-centre, flush-left, tension-driven and dynamic compositions are fully valid and often better: a small dark accent far out can hold a big quiet mass near the middle (the steelyard, COMP-2). Every check below raises a **flag** that asks "does this look intended?". None of them is an auto-fix. When balance really is broken, the fix is usually to **commit harder to the asymmetry** or to **add a counterweight**. Moving things to the centre is rarely the fix.

**Never centre or symmetrise by default to satisfy this pass.** If the owner of the work or the brief chose the off-centre arrangement, record it as intended and move on (AES-0).

**The tests** (each takes under a minute; use at least the first four):

| Test | How | What it reveals |
|---|---|---|
| Squint / blur | Half-close the eyes, or blur until detail goes (`tools/look.py`) | Masses only: a heavy corner, a lonely element, a dead block |
| Thumbnail at 5% | View at about 5% of the real size, or about 60-120 px across | Whether the big masses settle or slide; what pulls first |
| Mirror flip | Flip left to right | Lopsidedness you had stopped seeing; a piece that only "works" one way |
| Rotate 180° | Turn it upside down | Subject meaning stops pulling, so raw weight, top-heaviness and floating elements show |
| Cover half | Cover the left half, then the right; then the top, then the bottom | Whether each half holds something, and whether one half carries all the interest by accident |
| Gap measure | Measure every empty band and block against the largest intended gap (LAY-10, `tools/whitespace.py`) | Dead space and uneven gutters |
| Weight centroid | `tools/balance.py IMAGE --sheet out.png` | Where the pixel weight sits; a prompt, not a verdict (pixels can't see faces, words or gaze) |
| Edge and alignment sweep | Zoom to 200-400% along each edge, each shared edge and each corner | Tangents, near-alignments, crammed edges, overshoot errors |

**Output.** List each flag as one line: what, where, which test found it, and the question "intended?". For each flag, either mark it intended (and keep it) or fix it with the gentlest move that commits (COMP-20). This pass sits in the critique loop's crop/edges and delivery steps (`core/critique-loop.md`), after the blockers.

### COMP-19. Flag broken balance, not asymmetry
- **What:** Look for weight that seems unresolved by mistake: one side or corner much heavier with nothing answering it, a picture that seems to slide off the frame, or a layout whose quiet side looks unfinished rather than chosen. Don't flag a clear, committed asymmetry, a deliberate tension (COMP-12) or a flush-left page (LAY-11). Dow praised a facade split into "unequal but balanced proportions", and warned that symmetry is often used in design where no regard is paid to beauty of form [S181].
- **Why:** People do register imbalance: disrupted versions of paintings were judged less balanced than the originals, by experts more than lay viewers [S236], and adults arranging elements tend to balance them [S263]. But liking follows balance only loosely (COMP-2) [S237, S238]. So an off-centre piece in equilibrium is not a problem, and a "balance score" is not a quality score.
- **Check:** Run the squint, thumbnail, mirror and rotate tests above. Flag only where your eye keeps sliding toward one side or corner with nothing to stop it, or where a half looks unfinished in the cover test. For each flag, write "intended?" and answer from the brief.
- **Fix:** If unintended, add a counterweight on the light side (small, dark, saturated, isolated or textured; COMP-2), or commit harder so the imbalance reads as tension (COMP-20). Centre only if the piece was meant to be centred and has drifted.
- **Grade:** That people notice disrupted balance: partly supported (a few studies, mostly with paintings and simple shapes). That balance raises liking: partly supported for simple displays, weak for art. That balance means symmetry or centring: myth.
- **Source:** Locher, Gray & Nodine [S236]; McManus et al. [S235]; Hübner & Fillinger; Wilson & Chatterjee [S237]; Gershoni & Hochstein [S238]; Locher, Stappers & Overbeeke [S263]; Arnheim [S70]; COMP-2, CORE-11.
- **Never centre or symmetrise by default to satisfy this check.**

### COMP-20. Make intent read: commit, don't hedge
- **What:** An off-centre, tilted or crowded arrangement looks chosen when it is decisive and looks like a mistake when it is timid. The giveaways of accident are small: almost centred, almost level, almost aligned, almost symmetric, almost touching.
- **Why:** The frame's structural lines are where placement reads as stable, and fit falls away from them in a regular way [S71]. Arnheim describes the near-miss as an unresolved tension pulling toward the nearest stable point [S70]; Dondis calls it ambiguity, the one state the viewer can't resolve [S208].
- **Check:** For each key element and line, measure its offset from the nearest structural line (centre, axis, margin, a neighbour's edge). Flag offsets of roughly 1-6% of the frame width (self-chosen band): too small to read as a decision, big enough to see. Flag a horizon or edge tilted by about 0.5-3°.
- **Fix:** Snap it exactly onto the line, or move it decisively away (more than about 8-10% of the width, self-chosen). For asymmetry, push it further: a bigger size difference, a clearer empty side, one strong counterweight.
- **Grade:** Fit ratings: partly supported. The near-miss bands: craft wisdom with self-chosen numbers.
- **Source:** Palmer & Guidi [S71]; Arnheim [S70]; Dondis [S208]; COMP-1, COMP-12, COMP-17.
- **Never centre or symmetrise by default to satisfy this check.**

### COMP-21. Moved to COMP-2 (what makes weight, and the lever), v0.6.0.

### COMP-22. Top-heavy, bottom-heavy, and the centre that sits a little high
- **What:** Height adds weight. The same element looks heavier high in the frame than low, so a layout with its mass at the top can look ready to tip, and one weighted low looks grounded. The point that *looks* like the vertical middle sits slightly above the measured middle, so content placed at the exact middle of a page or panel tends to look low. Single subjects that face or move one way want room on that side (the inward bias, COMP-5).
- **Why:** Arnheim describes the upper part of the field as heavier and the lower as able to carry more [S70]. Type designers draw the top halves of B, E, S and 8 smaller for the same reason (TYPE-14), and printers placed the main line above centre [S205]. Attention's small upward bias [S264] is a weak basis for an exact optical centre. People prefer a single object near the centre but shifted toward the side it faces [S218], and higher or lower according to where such objects usually sit (bowls low, birds high) [S219], so there is no fixed "put it low" rule.
- **Check:** Rotate 180° and cover the top half, then the bottom: does the piece feel like it will tip? Is a block that should look centred sitting at the exact geometric middle, so it reads low? Does a subject with a facing direction have more room on that side?
- **Fix:** For an accidental top-heavy look, lighten or shrink the top mass, or give the bottom a darker or larger base. Lift "centred" content slightly above the middle by eye; the 2-5% often quoted is a self-chosen range, not a measured law. Give a facing subject room in front (COMP-5). Leave a deliberately top-heavy, looming piece alone.
- **Grade:** Inward bias and the centre bias for single objects: well supported (several experiments, one lab). The ecological vertical bias: partly supported. Top-heaviness and the optical centre: craft wisdom with weak perceptual support; any exact position is a myth.
- **Source:** Arnheim [S70]; Gress [S205]; Drain & Reuter-Lorenz [S264]; Palmer, Gardner & Wickens [S218]; Sammartino & Palmer [S219]; LAY-12, TYPE-14, COMP-5.

### COMP-23. Empty space is a shape with a job: active or dead
- **What:** Empty space is **active** when it has a job: it frames the focus, gives a subject room to look or move, separates groups, or sets a mood of quiet. Give it a clear shape and a firm edge; the idea of *ma* treats the interval as part of the work [S213, S199]. It is **dead** when it is just left over: a hole between small items, a band nothing explains, a corner that pulls the eye for no reason. Big empty areas are fine and often the best part; only unexplained ones are flags.
- **Why:** Empty areas are read as shapes (COMP-6), and spacing is how people group things [S175, S176]; a stray gap reads as something missing [S177, S178].
- **Check:** Name the job of each empty area larger than the largest intended gap ("margin", "group gap", "focal field", "room in front", "quiet"). Any area without a name is a flag. Is the quiet area one shape or scraps? Numbers: the LAY-10 gap measure.
- **Fix:** Give the space a job, merge scraps into one shape, or close it by regrouping the content beside it. Don't fill it with decoration.
- **Grade:** Proximity grouping: well supported. Active versus dead space, and *ma*: craft wisdom and tradition.
- **Source:** Wertheimer [S175]; Palmer [S176]; NN/g [S177]; White [S178]; Dow [S181]; Okakura [S199]; Isozaki [S213]; LAY-10, COMP-6. Former COMP-7 merged here.

### COMP-24. Things that sit oddly: the edge and alignment sweep
- **What:** Look for seven small faults that make a piece look unfinished even when the big balance is right:
  1. **Floating:** an element that relates to nothing (no shared edge, centre line, grid line or ground). It drifts.
  2. **Crammed:** an element pressed against the frame edge or another element, with less room than its neighbours have, by accident.
  3. **Tangents:** two contours just touching, or a contour just kissing the frame edge (ILL-1).
  4. **Near-alignments:** edges or centres that are almost but not quite lined up.
  5. **Uneven gutters:** gaps that should be equal but differ by a little.
  6. **Mathematical, not optical, centring:** a circle, triangle, play icon or rounded letter centred by its bounding box looks off. Pointed and round shapes need to be a little larger than square ones to look the same size (overshoot), and a triangle centres by its visual mass, not its box.
  7. **Blocks that look misprinted:** a solid panel or band dropped into the middle of a layout, or a graphic hanging lopsided off the bottom, that reads as a printer's misregistration rather than a choice. A block needs a job and a clear relation to the grid; on official notices this reads as amateur straight away (owner's note on a batch 5 notice, S57).
- **Why:** Placements near the frame's edges rate as poor fits [S71]. Small deviations from an alignment or a repeated interval read as errors, because the regular structure is what the eye groups by [S176, S250]. Overshoot is standard practice in type and icon design: icon systems draw circles larger than squares on the same grid so they look equal [S265], and type designers let round letters overshoot the baseline and cap height (TYPE-14).
- **Check:** At 200-400% zoom, go round every edge and corner, every shared edge and every gutter. Measure where it matters. Flag:
  - edge offsets of a few pixels between things that look meant to align (about 1-8 px on a 1,000-px-wide piece, self-chosen);
  - gutters that should be equal but differ by more than about 10%;
  - any element closer to the frame than the margin system allows;
  - any contour that touches another or the frame edge without overlapping it.

  Centre round and pointed shapes by eye, not by the numbers.
- **Fix:** Snap near-alignments exactly, or offset them clearly. Equalise gutters from one spacing scale (CORE-4). Pull crammed elements off the edge to the margin, or crop through them decisively. Overlap or separate tangents. Enlarge round and pointed shapes slightly against square ones. Shift a play triangle toward its point until it looks centred.
- **Grade:** Edge fit and grouping by regular structure: partly supported. The seven faults as a list, and the pixel and percentage bands: craft wisdom with self-chosen numbers. Overshoot: established practice in type and icon design.
- **Source:** Palmer & Guidi [S71]; Palmer [S176]; Wagemans et al. [S250]; Material Design icon keylines [S265]; Bringhurst [S212]; ILL-1, CORE-4, CORE-5, LAY-1, TYPE-14.

### COMP-25. Run the pass, report flags, let the owner decide
- **What:** Before delivery, run the tests table above on the real output at its real size, plus one thumbnail. Then write the flags: each one says what, where, which test, and "intended?".
- **Why:** These are judgement calls. The evidence says people notice broken balance and odd placement. It does not say any particular asymmetric choice is wrong, and taste in art and design is far less shared than in faces or landscapes (AES-12) [S251].
- **Check:** Is every flag answered either "intended: keep" (with the reason) or "fixed: how"? Was anything centred or made symmetric only to clear a flag? If so, undo it unless the brief asked for centring.
- **Fix:** Apply only the flagged fixes the owner signs off on (FLOW-1, FLOW-2 in `core/critique-loop.md`). Re-run the squint and mirror tests after any change, and the LAY-10 whole-layout re-review after any image swap.
- **Grade:** Procedure (craft); it gathers the graded rules above.
- **Source:** COMP-19 to COMP-24; LAY-10; AES-0, AES-12; Vessel et al. [S251].
- **Never centre or symmetrise by default to satisfy this check.**

---
