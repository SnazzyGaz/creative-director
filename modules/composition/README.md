# Module: composition, balance and beauty

How a picture or page holds together: its skeleton, visual weight, the eye's path, dominance, unity and variety, rhythm, space, tension, simplicity, proportion and symmetry. It applies to illustration, painting, photography, posters and layout alike. Load with `core/`; add `colour-value/` for value and colour structure, `illustration/` for scenes, `layout/` and `typography/` for pages.

Format: **What / Why / Check / Fix / Grade / Source**. Nothing here is MUST-BE-RIGHT: these are strong defaults, and a deliberate exception that works is recorded, not fixed (AES-0).

**Evidence grades** (the same legend as `core/evidence.md`):
- **Well supported:** replicated experiments or a meta-analysis back the core claim.
- **Partly supported:** some experimental support, but narrow stimuli, small effects or mixed results.
- **Craft wisdom:** long agreement among teachers and practitioners, not tested (or not testable) in the lab. Use it as a default, not as a fact about viewers.
- **Contested / myth:** tested and not supported, or the popular version goes well beyond the evidence. Don't cite it as a reason.

The older books cited here are public domain and linked in full in `BIBLIOGRAPHY.md`. Where a modern book is in copyright, the rule paraphrases it from secondary sources.

**Pre-delivery pass:** the section *Sitting right* (COMP-19 to COMP-25) is a short check for *broken* balance and odd placement. It flags what looks accidental and asks "intended?". It never pushes work toward symmetry or centring.

**Viewing tests used below** (all quick, all from the studio tradition; Poore lists most of them in 1903 [S183]):
- **Thumbnail:** view at about 5 cm wide or 120 px.
- **Squint / blur:** half-close the eyes or blur until detail goes; only masses remain (`tools/look.py`).
- **Mirror flip:** flip left to right. Faults you had stopped seeing jump out, and a picture that only balances one way shows it.
- **Upside down:** turn it 180°. Subject matter stops pulling, so shapes and weights show.
- **Distance:** across the room, then at arm's length, then close.
- **Quadrant lines:** draw a vertical and a horizontal line through the true centre and compare the four parts.

---

### COMP-1. Know the frame's skeleton, and place things clearly on or clearly off it
- **What:** Every frame has a hidden structure: the centre, the vertical and horizontal axes, and the diagonals. Arnheim describes it as a field of forces [S70]. A key element is either clearly *on* a structural point or line (calm, stable, "levelled") or clearly *off* it (dynamic, "sharpened"). Just missing the centre or an axis reads as an error.
- **Why:** People rate how well a shape "fits" at each spot in a frame; the centre and the axes score highest, and fit falls off in a regular way [S71]. Dondis calls the near-miss in between *ambiguity*, the one state that gives the viewer nothing to resolve [S208].
- **Check:** Draw the quadrant lines and both diagonals over the work. For each key element, is it within about 2% of the frame width of a structural line (on), or clearly away from it (off)? List any that sit 2-6% off: those are the near-misses.
- **Fix:** Snap a near-miss onto the line, or move it decisively away. Don't nudge.
- **Grade:** Partly supported (fit ratings for simple shapes [S71]; Arnheim's wider force field is theory); the near-miss advice is craft wisdom.
- **Source:** Arnheim [S70]; Palmer & Guidi [S71]; Dondis [S208]; CORE-11; CORE-4.

### COMP-2. Weigh the picture: weight times distance, then mirror-flip
- **What:** Balance is visual weight around the centre, like a steelyard: a small, dark, isolated or far-out element can balance a large one near the middle. An empty half needs *something* (an accent, a texture, a gradation) to hold its side. Poore's test: with lines through the true centre, a satisfying picture balances about them, and the left-right division matters more than top-bottom [S183].
- **Why:** In fulcrum experiments, perceived balance depended mostly on an element's *position*, less on its size and colour, and integrated the whole picture, not one feature [S235]. A centre-of-mass measure tracked people's balance ratings of simple pictures, mostly through the horizontal offset [S237]. Two cautions: balance and *liking* are only loosely linked, and for complex art people's first-glance balance follows grouping, recognised objects and vertical symmetry more than a weight sum [S238]. Experts notice disrupted balance more than lay viewers [S236]. When adults arrange elements themselves, they tend to balance them about the centre and the main axes [S263].
- **Check:**
  1. Run `tools/balance.py IMAGE --sheet out.png`. It reports the weighted centroid's offset and the left/right and top/bottom weight ratios (pixels only).
  2. Mirror-flip the image. Does it still feel settled? If one version feels like it is sliding off the page, weight is lopsided.
  3. Add by eye the weights pixels can't see (COMP-3).
- **Fix:** First ask whether the imbalance is the point (COMP-12); if so, keep it and say so. Otherwise add a small counterweight far out on the light side (the steelyard), or commit harder to the asymmetry (COMP-20); darken, saturate or isolate a small accent rather than adding a big object. Move the heavy thing inward only if that is what the piece was meant to be. Equilibrium is the aim, not symmetry: never centre by default (COMP-19).
- **Grade:** Partly supported. The steelyard/centre-of-mass idea predicts balance ratings for simple pictures; it is much weaker for complex art and for preference.
- **Source:** Poore [S183]; Ross on balance and the centre of equilibrium [S182]; Arnheim [S70]; McManus et al. [S235]; Hübner & Fillinger [S237]; Locher, Gray & Nodine [S236]; Locher, Stappers & Overbeeke [S263]; Gershoni & Hochstein [S238]; CORE-11.

### COMP-3. Faces, text and figures are heavy by nature
- **What:** Some things outweigh their size: faces (eyes above all), written words, human and animal figures, and the sharpest light-dark edge. A small face or word pulls more attention than a large plain area.
- **Why:** In free viewing, faces and text attract early fixations far above their area, even when people are not told to look for them [S239]. Viewers also follow a depicted person's gaze automatically [S240].
- **Check:** List every face, figure and piece of text. Does each sit where you want attention? Does a background face or a stray word (a sign, a label, a watermark) compete with the focus? At thumbnail, where does your eye go first?
- **Fix:** Remove, blur, darken or turn away a competing face or word. Put the main face or headline where the composition wants its strongest weight.
- **Grade:** Well supported.
- **Source:** Cerf, Frady & Koch [S239]; Friesen & Kingstone [S240]; ILL-2; LAY-3.

### COMP-4. Guide the eye with what eyes actually follow; treat lines as support
- **What:** Plan an eye path (entry, focus, pauses, exit), but build it from strong cues: contrast, faces and gaze direction, pointing, text, and isolation. Leading lines and S-curves help connect places, but they don't drive the eye on their own.
- **Why:** Eye-tracking of paintings shows that viewers return again and again to a few high-information regions, and the path depends on the viewer and the task [S241, S242]. Gaze and pointing cues shift attention reliably [S240]. In paintings with people, gaze goes to the figures and faces whatever the surrounding layout; in landscapes, low-level contrast and colour guide it more [S243]. There is little direct evidence that leading lines on their own steer the eye.
- **Check:** Blur the work and note the first three places the eye lands. Are they the focus and the planned secondary points, in that order? Does any depicted gaze or pointing arm lead out of the frame or to nothing?
- **Fix:** Raise the focus's contrast; turn a figure's gaze toward the focus; add a secondary accent where the path should pause; cut or calm the cue that pulls off-route.
- **Grade:** Gaze cueing and contrast: well supported. "Leading lines steer the eye": craft wisdom with little direct test; the strong version ("lines force the path") is contested (see `core/evidence.md`).
- **Source:** DeAngelus & Pelz [S241]; Nodine et al. [S242]; Massaro et al. [S243]; Friesen & Kingstone [S240]; Ruskin's law of continuity [S184]; AES-1.

### COMP-5. Give looking and moving things room in front
- **What:** A figure, face, vehicle or arrow that faces or moves one way needs more space in front of it than behind (lead room). Facing toward the inside of the frame reads as settled; facing out reads as leaving, which is fine only on purpose.
- **Why:** People prefer pictures where a directional object faces into the frame, the "inward bias" [S218]. Preference also depends on where the object sits, and the effect is stronger for objects that clearly point or face [S219].
- **Check:** For each directional element, measure the space in front of and behind it. Mirror-flip: does the flipped version feel more settled?
- **Fix:** Shift the subject toward the back edge, flip it (only if nothing in it reads backwards), or crop more behind it.
- **Grade:** Well supported.
- **Source:** Palmer, Gardner & Wickens [S218]; Sammartino & Palmer [S219].

### COMP-6. Design the figure and the ground together
- **What:** The figure should be the region that is smaller, enclosed, convex, symmetric or lower in the frame, and the shapes left over around it (negative shapes) should be designed as carefully as the objects. Dow's advice: spacing comes first, and good colour depends on good value pattern, which depends on good spacing [S181].
- **Why:** Those cues decide what is seen as figure [S250]; the lower region of a split is seen as figure more often [S249]. Clear figure-ground makes an image easier to read and is liked more [S37].
- **Check:** Fill the silhouettes solid and look only at the background shapes. Are they varied in size, or a set of near-identical slivers? Is anything reversible by accident (you can't tell which side is figure)?
- **Fix:** Vary the gaps; widen or close a sliver; overlap shapes decisively. If an area reads as figure when it should be ground, lighten it, open its edge or make it less convex.
- **Grade:** Well supported (figure-ground cues); "design the negative shapes" is craft wisdom built on it.
- **Source:** Wagemans et al. [S250]; Vecera, Vogel & Woodman [S249]; Dow [S181]; Reber et al. [S37]; CORE-2.

### COMP-7. Empty space is a shape with a job (ma)
- **What:** Leave one quiet area on purpose and give it a clear shape, a firm edge and a role: room for the subject to breathe, the direction of movement, or a resting place for the eye. The Japanese idea of *ma* treats the interval as part of the work, not leftover space [S213]. Okakura writes that emptiness is all-powerful "because all containing" [S199].
- **Why:** Space that reads as intended separates groups and makes the focus stronger (CORE-2, LAY-10). Space that reads as forgotten (a hole between small items) looks like a mistake.
- **Check:** Squint. Point at each large empty area and say its job. If you can't, it's a dead zone (LAY-10). Is the quiet area one shape, or broken into scraps?
- **Fix:** Merge scraps of space into one shape; push content together so the space gathers in one place; or fill a space that has no job.
- **Grade:** Craft wisdom and tradition, consistent with grouping research (proximity, figure-ground).
- **Source:** Okakura [S199]; Isozaki, *Ma* [S213]; Dow on notan and spacing [S181]; White [S178]; LAY-10.

### COMP-8. One dominant in every attribute; everything else subordinate
- **What:** For each attribute (size, value, colour, direction, shape type, texture, interval), one kind dominates and the others play support. Ruskin's "principality": one feature more important than the rest, and "one light larger and brighter than the other lights" [S184]. Dow's "subordination": group parts under one main part, by axis, radiation or size [S181].
- **Why:** Hierarchy is how a viewer knows where to start (CORE-1). Equal competing amounts (half warm, half cool; half curves, half straights) read as indecision.
- **Check:** For each attribute, write the split: e.g. "value: 70% light, 20% mid, 10% dark; direction: mostly horizontal; shapes: mostly curved". Any attribute near 50/50 without a reason?
- **Fix:** Tip the near-even attribute to clear dominance (roughly 60-80% one kind, as a craft default, not a measured optimum). Keep the minority as accent near the focus.
- **Grade:** Craft wisdom.
- **Source:** Ruskin [S184]; Dow [S181]; Ross [S182]; CORE-1; AES-2.

### COMP-9. Unity with variety: repeat a family, vary its members
- **What:** Build from a few families of shapes, colours and intervals that repeat, and vary each repetition in size, spacing or angle. Hutcheson put beauty at "uniformity amidst variety" [S186]; Hogarth's six principles (fitness, variety, uniformity, simplicity, intricacy and quantity) work together, "mutually correcting and restraining each other" [S185].
- **Why:** A review of the research concludes that order and complexity are separate dimensions that interact in appreciation, not two ends of one scale [S231], so adding variety does not have to cost order. Repetition makes a form easy to see (fluency) [S37]. Dow's warning: repetition without art (his examples are fences and blocks of buildings) is "like doggerel rhyme" [S181].
- **Check:** List the shape families (round, angular, long), colour families and the repeated intervals. Is there any orphan (an element that belongs to no family)? Is any family a set of identical clones at equal spacing?
- **Fix:** Bring an orphan into a family (match its corner radius, colour or angle) or remove it. Vary the clones: big, medium, small; uneven intervals.
- **Grade:** Partly supported (order and complexity effects; fluency); the classic formula is tradition.
- **Source:** Hutcheson [S186]; Hogarth [S185]; Dow [S181]; Van Geert & Wagemans [S231]; Reber et al. [S37]; CORE-9.

### COMP-10. Bridge strong contrasts with transition
- **What:** Where opposites meet (light and dark, straight and curved, big and small, warm and cool), let something carry the eye between them somewhere in the picture: a mid value, a gradation, a softened corner. Keep the sharpest, unbridged contrast for the focus. Dow names this principle "transition" [S181]; Ross works it as gradation [S182].
- **Why:** If every contrast is maximal, none leads (CORE-1); bridged contrasts hold the picture together.
- **Check:** Find the three strongest contrasts. Is the strongest at the focus? Elsewhere, is there any step between the extremes?
- **Fix:** Add a mid value or a gradation along one edge; round one corner; let the sharpest edge belong to the focus only (ILL-5).
- **Grade:** Craft wisdom.
- **Source:** Dow [S181]; Ross [S182]; Ruskin's laws of interchange and continuity [S184]; ILL-5.

### COMP-11. Rhythm comes from measured intervals
- **What:** Choose how repeated elements are spaced. Regular intervals feel calm and formal; intervals that grow or shrink in steps (a progression) feel like movement; random intervals feel like noise. Ross describes rhythm as regular, marked movement [S182].
- **Why:** The viewer reads an interval pattern as a pattern only if it has a rule.
- **Check:** Measure the gaps between repeats along the main direction. Are they equal, stepped (each one a set ratio of the last), or unrelated?
- **Fix:** Pick one: equal for calm, a progression toward the focus for movement. Make unrelated gaps follow a rule.
- **Grade:** Craft wisdom.
- **Source:** Ross [S182]; Dow on repetition [S181]; Crane on line and rhythm [S196]; AES-1; TYPE-2.

### COMP-12. Tension on purpose, never by accident
- **What:** Tension (an element jammed near an edge, a strong diagonal, a crowded side, an unresolved gap) is a tool for unease, drama and energy. Use it where the brief wants energy; remove it where it isn't wanted. The worst state is the near-miss: almost centred, almost touching, almost level (COMP-1).
- **Why:** Off-centre and edge positions read as unstable and pulling [S71, S70]; Dondis contrasts deliberate sharpening with unreadable ambiguity [S208].
- **Check:** List each source of tension (tangents, crowding at an edge, tilted horizon, cut-off subject). For each, is it intended by the brief's mood (AES-0)?
- **Fix:** Resolve the unintended ones (move away from the edge, level the horizon, overlap or separate tangents, ILL-1). Push the intended ones further so they read as chosen (COMP-20). The pre-delivery pass for accidental tension is COMP-19 to COMP-25.
- **Grade:** Partly supported (position-stability ratings); the use of tension is craft.
- **Source:** Dondis [S208]; Arnheim [S70]; Palmer & Guidi [S71]; Locher & Stappers on implied dynamics [S262]; ILL-1, ILL-7.

### COMP-13. Simple big shapes first: three to five masses
- **What:** The whole picture should read as a few big shapes (about three to five) before any detail. Detail lives *inside* the big shapes, and never breaks them up.
- **Why:** The gist of a scene is taken from coarse structure first, blobs before edges [S244]. Gestalt research shows that the simplest grouping tends to win [S250]. Appeal is judged in about 50 ms [S36].
- **Check:** Blur the work hard (or view it at 120 px). Count the masses you can see. Does the main idea still read? If the blurred version is a grey mush, the structure is missing.
- **Fix:** Merge neighbouring values into fewer groups (CV-2); cut detail that crosses mass boundaries; simplify the silhouette (ILL-3).
- **Grade:** Coarse-first gist: well supported. "Three to five" is a craft number.
- **Source:** Schyns & Oliva [S244]; Wagemans et al. [S250]; Lindgaard [S36]; Loomis [S76]; Payne [S210]; CORE-3; CV-2.

### COMP-14. Something to see at every viewing distance
- **What:** A strong piece gives something at three scales: big shapes from across the room, a readable arrangement at arm's length, and detail or texture close up. The big scale must always win.
- **Why:** Natural scenes have structure at many scales, and lab studies find people like fractal-like patterns of mid complexity (a fractal dimension around 1.3-1.5) on average, with real individual differences [S228]. Images of art share some of these statistics with natural scenes [S253].
- **Check:** View at thumbnail, at arm's length and close (or at 100% and 300% zoom). Does each step add something new? Does the close-up detail ever break the thumbnail read?
- **Fix:** Add texture or small accents inside the big shapes; or calm close detail that shows at thumbnail as noise.
- **Grade:** Partly supported (fractal preference in the lab, varying by person); the three-distance test is craft.
- **Source:** Spehar et al. [S228]; Graham & Redies [S253]; Hagerhall et al. [S229]; LAY-7.

### COMP-15. More elements need more order
- **What:** Every time you add elements, also add order: alignment, grouping, repetition, a shared colour. Complexity is fine; complexity without order is not.
- **Why:** Order and complexity are separate dimensions that interact [S231]; studies that varied only complexity gave contradictory results, partly because they ignored order. Complexity itself has several parts (number of elements, variety, irregularity), and people weigh them differently [S230]. Highly complex web pages get the lowest first impressions [S35].
- **Check:** Count the distinct element types and the distinct alignment lines. If types grew but alignment lines also grew, order did not keep up.
- **Fix:** Group, align to fewer lines, share one colour or shape language, or cut.
- **Grade:** Partly supported (separate factors: well argued; the best mix varies by person and stimulus).
- **Source:** Van Geert & Wagemans [S231]; Nadal et al. [S230]; Reinecke et al. [S35]; CORE-8.

### COMP-16. Proportions from one family, for consistency, not for magic
- **What:** Choose the format and the main divisions from one family of ratios (simple ratios like 1:2, 2:3 and 3:4, √2 for paper, or the golden ratio if you like it) and reuse it. The value is consistency. No ratio makes a piece beautiful on its own.
- **Why:** Repeated proportions read as order (COMP-9). The golden-ratio beauty claim has failed repeated tests: no reliable preference for golden rectangles [S220, S221, S38], and many famous examples rest on loose measuring [S222, S224]. The nautilus shell is not golden [S223]. Hambidge's "dynamic symmetry" (1920) was an influential design system, but his claims about Greek practice are not established [S194, S224].
- **Check:** List the main ratios: format, main division, large-to-small areas. Do they come from one family? If a critique says "this follows the golden ratio, so it is beautiful", strike the claim.
- **Fix:** Bring stray proportions into the family; keep the ratio if it helps consistency, drop the claim about beauty.
- **Grade:** Consistency: craft wisdom. "Golden ratio equals beauty": myth.
- **Source:** Green [S220]; Höge [S221]; McManus et al. [S38]; Markowsky [S222]; Falbo [S223]; Fischler [S224]; Hambidge [S194]; Vitruvius on symmetria (commensurable parts) [S202]; LAY-12.

### COMP-17. Symmetry is a choice: go fully symmetric or clearly asymmetric
- **What:** Full mirror symmetry feels formal, calm, monumental and complete; asymmetry feels alive and informal. Pick one. Okakura notes that Zen-influenced art avoided symmetry because it expressed completion and repetition, and that the viewer completes what is left incomplete [S199, S214].
- **Why:** For abstract patterns, symmetry is the strongest single predictor of "beautiful" judgements [S234]; it is also easy to process [S37]. Near-symmetry (almost mirrored, with small accidental differences) looks like a mistake.
- **Check:** Mirror-flip and overlay at 50%. If the piece is almost symmetric, list the differences: are they deliberate?
- **Fix:** Make it truly symmetric (copy one half), or break the symmetry decisively (move the axis, change one side's weight clearly).
- **Grade:** Symmetry and beauty for patterns: well supported. The asymmetry tradition: craft and cultural.
- **Source:** Jacobsen & Höfel [S234]; Reber et al. [S37]; Okakura [S199]; Parkes & Loughnane, SEP [S214]; LAY-11.

### COMP-18. Direction carries reading habits
- **What:** In left-to-right reading cultures, rightward movement reads as "forward" and leftward as returning or resisting. Choose direction for what the story needs, and check the mirror image if the piece will meet a right-to-left audience.
- **Why:** Aesthetic preference for left-right direction shifts with reading habit [S254], and so does how people picture events, with the actor placed on the side where reading starts [S261]; lateral biases in art exist but are small and depend on the task [S255, S256].
- **Check:** Which way does the main movement or gaze go? Mirror-flip: does the meaning change in a way you want?
- **Fix:** Flip the arrangement (not text or anything with handedness) if the direction fights the story.
- **Grade:** Partly supported, culture-dependent. "The right side is always heavier" is contested.
- **Source:** Chokron & De Agostini [S254]; Maass & Russo [S261]; Levy [S255]; McManus & Humphrey [S256].

---

## Sitting right: the broken-balance pass (COMP-19 to COMP-25)

Before delivery, ask one question of the whole piece: **does anything sit weirdly?** This is a judgement call backed by evidence, not another placement rule. The rules above say how to build a composition. This pass looks only for **broken** balance: something that reads as accidental, unresolved or lopsided by mistake.

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
- **Why:** People do register imbalance. Viewers judged deliberately disrupted versions of paintings less balanced than the originals, experts more sharply than non-experts [S236]. Perceived balance in simple pictures follows weight times distance from the centre, mostly in the horizontal [S235, S237]. Adults who arrange elements themselves tend to balance them [S263]. Preference follows balance only loosely, though. For simple displays a balance score predicts liking modestly [S237]; for complex art, fast balance judgements follow grouping and recognised objects more than a weight sum [S238]. So an off-centre piece in equilibrium is not a problem, and a "balance score" is not a quality score.
- **Check:** Run the squint, thumbnail, mirror and rotate tests above. Flag only where your eye keeps sliding toward one side or corner with nothing to stop it, or where a half looks unfinished in the cover test. For each flag, write "intended?" and answer from the brief.
- **Fix:** If unintended, add a counterweight on the light side (small, dark, saturated, isolated or textured; COMP-21), or commit harder so the imbalance reads as tension (COMP-20). Centre only if the piece was meant to be centred and has drifted.
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

### COMP-21. Know what makes weight, and use the lever
- **What:** Weight, roughly in order of how reliably it works:
  - **meaning:** faces, eyes, figures and words (COMP-3);
  - **position:** distance from the centre (the lever arm), and height in the frame (COMP-22);
  - **value contrast** with the surround;
  - **size;**
  - **saturation and warm hues;**
  - **isolation:** an element alone in space weighs more than the same one in a crowd;
  - **direction:** gaze, pointing, arrows and motion add weight on the side they face;
  - **detail, texture and regular shape.**

  Balance about a fulcrum at the centre: weight times distance on one side should answer weight times distance on the other. A small heavy thing far out balances a large light thing near the middle.
- **Why:** The lever model is the classic account (Poore's steelyard [S183]; Ross's centre of equilibrium [S182]; Dow's divisions that are "unequal but balanced" [S181]; Arnheim [S70]). In fulcrum experiments, position mattered most and size and colour less [S235]. A centre-of-mass measure tracks rated balance for simple pictures [S237]. Faces, text and gaze pull attention far beyond their area [S239, S240].
- **Check:** List the five heaviest things and say what makes each heavy. Picture the frame on a fulcrum at the centre (left-right first, then top-bottom). Does any side lack an answer? Compare with `tools/balance.py`, then correct by eye for meaning and gaze.
- **Fix:** Adjust the cheapest lever: darken, saturate or isolate a small accent on the light side, or move it further out; or lighten, lower the contrast of, or move inward the heavy element. Adding a new object is the last resort, and only with the owner's say-so (AES-0).
- **Grade:** The lever / centre-of-mass model for simple pictures: partly supported. Faces, text and gaze: well supported. The ordering of the other factors and the warm-hue effect: craft wisdom.
- **Source:** Poore [S183]; Ross [S182]; Dow [S181]; Arnheim [S70]; McManus et al. [S235]; Hübner & Fillinger [S237]; Cerf et al. [S239]; Friesen & Kingstone [S240]; COMP-2, COMP-3.

### COMP-22. Top-heavy, bottom-heavy, and the centre that sits a little high
- **What:** Height adds weight. The same element looks heavier high in the frame than low, so a layout with its mass at the top can look ready to tip, and one weighted low looks grounded. The point that *looks* like the vertical middle sits slightly above the measured middle, so content placed at the exact middle of a page or panel tends to look low. Single subjects that face or move one way want room on that side (the inward bias, COMP-5).
- **Why:** Arnheim describes the upper part of the field as heavier and the lower as able to carry more [S70]. Type designers draw the top halves of B, E, S and 8 smaller for the same reason (TYPE-14), and printers placed the main line above centre [S205]. Attention has a small upward bias [S264], which is at most a weak basis for an exact optical centre. In framing studies, people preferred a single object near the centre but shifted toward the side it faces (the inward bias) [S218]. Vertically, the preferred height depended on where such objects usually sit relative to the eye: bowls lower, lamps and flying birds higher [S219]. So there is no fixed "put it low" rule.
- **Check:** Rotate 180° and cover the top half, then the bottom: does the piece feel like it will tip? Is a block that should look centred sitting at the exact geometric middle, so it reads low? Does a subject with a facing direction have more room on that side?
- **Fix:** For an accidental top-heavy look, lighten or shrink the top mass, or give the bottom a darker or larger base. Lift "centred" content slightly above the middle by eye; the 2-5% often quoted is a self-chosen range, not a measured law. Give a facing subject room in front (COMP-5). Leave a deliberately top-heavy, looming piece alone.
- **Grade:** Inward bias and the centre bias for single objects: well supported (several experiments, one lab). The ecological vertical bias: partly supported. Top-heaviness and the optical centre: craft wisdom with weak perceptual support; any exact position is a myth.
- **Source:** Arnheim [S70]; Gress [S205]; Drain & Reuter-Lorenz [S264]; Palmer, Gardner & Wickens [S218]; Sammartino & Palmer [S219]; LAY-12, TYPE-14, COMP-5.

### COMP-23. Active space or dead space
- **What:** Empty space is **active** when it has a job: it frames the focus, gives a subject room to look or move, separates groups, or sets a mood of quiet. It is **dead** when it is just left over: a hole between two small items, a band no larger idea explains, a corner that pulls the eye for no reason. Big empty areas are fine, and often the best part of a design (COMP-7). Only unexplained ones are flags.
- **Why:** Empty areas are read as shapes in their own right (figure and ground, COMP-6) and spacing is how people group things [S175, S176]. A stray large gap reads as something missing [S177, S178]. Dow and Okakura treat designed emptiness as the source of strength [S181, S199].
- **Check:** Name the job of each empty area larger than the largest intended gap ("margin", "group gap", "focal field", "room in front", "quiet"). Any area without a name is a flag. Run the LAY-10 gap measure and squint test for the numbers.
- **Fix:** Give the space a job (make it the field the focus sits in, or the room a subject faces into), or close it by regrouping the content beside it. Don't fill it with decoration.
- **Grade:** Proximity grouping: well supported. Dead versus active space: craft wisdom.
- **Source:** Wertheimer [S175]; Palmer [S176]; NN/g [S177]; White [S178]; Dow [S181]; Okakura [S199]; LAY-10, COMP-6, COMP-7.

### COMP-24. Things that sit oddly: the edge and alignment sweep
- **What:** Look for six small faults that make a piece look unfinished even when the big balance is right:
  1. **Floating:** an element that relates to nothing (no shared edge, centre line, grid line or ground). It drifts.
  2. **Crammed:** an element pressed against the frame edge or another element, with less room than its neighbours have, by accident.
  3. **Tangents:** two contours just touching, or a contour just kissing the frame edge (ILL-1).
  4. **Near-alignments:** edges or centres that are almost but not quite lined up.
  5. **Uneven gutters:** gaps that should be equal but differ by a little.
  6. **Mathematical, not optical, centring:** a circle, triangle, play icon or rounded letter centred by its bounding box looks off. Pointed and round shapes need to be a little larger than square ones to look the same size (overshoot), and a triangle centres by its visual mass, not its box.
- **Why:** Placements near the frame's edges rate as poor fits [S71]. Small deviations from an alignment or a repeated interval read as errors, because the regular structure is what the eye groups by [S176, S250]. Overshoot is standard practice in type and icon design: icon systems draw circles larger than squares on the same grid so they look equal [S265], and type designers let round letters overshoot the baseline and cap height (TYPE-14).
- **Check:** At 200-400% zoom, go round every edge and corner, every shared edge and every gutter. Measure where it matters. Flag:
  - edge offsets of a few pixels between things that look meant to align (about 1-8 px on a 1,000-px-wide piece, self-chosen);
  - gutters that should be equal but differ by more than about 10%;
  - any element closer to the frame than the margin system allows;
  - any contour that touches another or the frame edge without overlapping it.

  Centre round and pointed shapes by eye, not by the numbers.
- **Fix:** Snap near-alignments exactly, or offset them clearly. Equalise gutters from one spacing scale (CORE-4). Pull crammed elements off the edge to the margin, or crop through them decisively. Overlap or separate tangents. Enlarge round and pointed shapes slightly against square ones. Shift a play triangle toward its point until it looks centred.
- **Grade:** Edge fit and grouping by regular structure: partly supported. The six faults as a list, and the pixel and percentage bands: craft wisdom with self-chosen numbers. Overshoot: established practice in type and icon design.
- **Source:** Palmer & Guidi [S71]; Palmer [S176]; Wagemans et al. [S250]; Material Design icon keylines [S265]; Bringhurst [S212]; ILL-1, CORE-4, CORE-5, LAY-1, TYPE-14.

### COMP-25. Run the pass, report flags, let the owner decide
- **What:** Before delivery, run the tests table above on the real output at its real size, plus one thumbnail. Then write the flags: each one says what, where, which test, and "intended?".
- **Why:** These are judgement calls. The evidence says people notice broken balance and odd placement. It does not say any particular asymmetric choice is wrong, and taste in art and design is far less shared than in faces or landscapes (AES-12) [S251].
- **Check:** Is every flag answered either "intended: keep" (with the reason) or "fixed: how"? Was anything centred or made symmetric only to clear a flag? If so, undo it unless the brief asked for centring.
- **Fix:** Apply only the flagged fixes the owner signs off on (`core/interaction-flow.md`). Re-run the squint and mirror tests after any change, and the LAY-10 whole-layout re-review after any image swap.
- **Grade:** Procedure (craft); it gathers the graded rules above.
- **Source:** COMP-19 to COMP-24; LAY-10; AES-0, AES-12; Vessel et al. [S251].
- **Never centre or symmetrise by default to satisfy this check.**

---

## Myths and weak claims (details in `core/evidence.md`)
- **Golden ratio, golden spirals and "divine proportion" as the source of beauty:** myth (COMP-16).
- **"Leading lines force the eye":** contested; lines connect, content drives (COMP-4).
- **"Always use an odd number of objects" (rule of odds):** no direct test found; treat as a craft habit for avoiding pairs that split attention, not a rule.
- **Rule of thirds as law:** weak (ILL-1).
- **"Balance means symmetry or centring":** myth. Balance is equilibrium of weights; asymmetric and off-centre work balances by the lever (COMP-19, COMP-21).
- **An exact optical centre ("5% above the middle", "golden" margins):** myth in its exact form; the slight upward placement is craft wisdom (COMP-22).
- **Birkhoff's aesthetic measure (order ÷ complexity, 1933):** historical; its predictions did not hold up, though order and complexity remain useful dimensions (COMP-15).

Further reading, grouped and annotated: `BIBLIOGRAPHY.md`.
