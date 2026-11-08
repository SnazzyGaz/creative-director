# Module: composition, balance and beauty

How a picture or page holds together: its skeleton, visual weight, the eye's path, dominance, unity and variety, rhythm, space, tension, simplicity, proportion and symmetry. It applies to illustration, painting, photography, posters and layout alike. Load with `core/`; add `colour-value/` for value and colour structure, `illustration/` for scenes, `layout/` and `typography/` for pages.

Format: **What / Why / Check / Fix / Grade / Source** (grades: `core/evidence.md`). Nothing here is MUST-BE-RIGHT: these are strong defaults, and a deliberate exception that works is recorded, not fixed (AES-0).

The older books cited here are public domain and linked in full in `BIBLIOGRAPHY.md`. Where a modern book is in copyright, the rule paraphrases it from secondary sources.

**Pre-delivery pass:** *Sitting right* (COMP-19 to COMP-25, in `sitting-right.md`) is a short check for *broken* balance and odd placement. It flags what looks accidental and asks "intended?". It never pushes work toward symmetry or centring.

The viewing tests (squint, thumbnail, mirror, rotate 180°, cover half, distance) are in `sitting-right.md` and in `core/critique-loop.md`.

---

### COMP-1. Know the frame's skeleton, and place things clearly on or clearly off it
- **What:** Every frame has a hidden structure: the centre, the vertical and horizontal axes, and the diagonals. Arnheim describes it as a field of forces [SRC-70]. A key element is either clearly *on* a structural point or line (calm, stable, "levelled") or clearly *off* it (dynamic, "sharpened"). Just missing the centre or an axis reads as an error.
- **Why:** People rate how well a shape "fits" at each spot in a frame; the centre and the axes score highest, and fit falls off in a regular way [SRC-71]. Dondis calls the near-miss in between *ambiguity*, the one state that gives the viewer nothing to resolve [SRC-208].
- **Check:** Draw the quadrant lines and both diagonals. Is each key element clearly on a structural line or clearly off it? Near-miss bands: COMP-20.
- **Fix:** Snap a near-miss onto the line, or move it decisively away. Don't nudge.
- **Grade:** Partly supported (fit ratings for simple shapes [SRC-71]; Arnheim's wider force field is theory); the near-miss advice is craft wisdom.
- **Source:** Arnheim [SRC-70]; Palmer & Guidi [SRC-71]; Dondis [SRC-208]; CORE-11; CORE-4.

### COMP-2. Weigh the picture: what makes weight, and the lever
- **What:** Balance is visual weight about the centre, like a steelyard: weight times distance on one side answers weight times distance on the other, so a small heavy thing far out can balance a large light thing near the middle. Left-right matters more than top-bottom. Weight, roughly in order of reliability:
  - **meaning:** faces, eyes, figures and words (COMP-3);
  - **position:** distance from the centre (the lever arm) and height in the frame (COMP-22);
  - **value contrast** with the surround; **size**; **saturation and warm hues**;
  - **isolation:** alone in space weighs more than the same thing in a crowd;
  - **direction:** gaze, pointing and motion add weight on the side they face;
  - **detail, texture and regular shape.**
- **Why:** Perceived balance depends mostly on position, less on size and colour [SRC-235], and a centre-of-mass measure tracks balance ratings of simple pictures, mostly through the horizontal offset [SRC-237]. Faces, text and gaze pull attention far beyond their area [SRC-239, SRC-240]. Cautions: balance and liking are only loosely linked, and in complex art first-glance balance follows grouping and recognised objects more than a weight sum [SRC-238].
- **Check:** List the five heaviest things and what makes each heavy. Run `tools/balance.py IMAGE --sheet out.png` (centroid offset, left/right and top/bottom ratios; pixels only), then correct by eye for meaning and gaze. Mirror-flip: does one version slide off the page?
- **Fix:** First ask whether the imbalance is the point (COMP-12). Otherwise pull the cheapest lever: darken, saturate, isolate or move further out a small accent on the light side, or quiet the heavy element; or commit harder to the asymmetry (COMP-20). Add a new object only with the owner's say-so (AES-0). Equilibrium is the aim, not symmetry: never centre by default (COMP-19).
- **Grade:** Partly supported for simple pictures; weak for complex art and for preference. Faces, text and gaze: well supported. The order of the other factors and the warm-hue effect: craft wisdom.
- **Source:** Poore [SRC-183]; Ross [SRC-182]; Dow [SRC-181]; Arnheim [SRC-70]; McManus et al. [SRC-235]; Hübner & Fillinger [SRC-237]; Gershoni & Hochstein [SRC-238]; Cerf et al. [SRC-239]; Friesen & Kingstone [SRC-240]; CORE-11.

### COMP-3. Faces, text and figures are heavy by nature
- **What:** Some things outweigh their size: faces (eyes above all), written words, human and animal figures, and the sharpest light-dark edge. A small face or word pulls more attention than a large plain area.
- **Why:** In free viewing, faces and text attract early fixations far above their area, even when people are not told to look for them [SRC-239]. Viewers also follow a depicted person's gaze automatically [SRC-240].
- **Check:** List every face, figure and piece of text. Does each sit where you want attention? Does a background face or a stray word (a sign, a label, a watermark) compete with the focus? At thumbnail, where does your eye go first?
- **Fix:** Remove, blur, darken or turn away a competing face or word. Put the main face or headline where the composition wants its strongest weight.
- **Grade:** Well supported.
- **Source:** Cerf, Frady & Koch [SRC-239]; Friesen & Kingstone [SRC-240]; ILL-2; LAY-3.

### COMP-4. Guide the eye with what eyes actually follow; treat lines as support
- **What:** Plan an eye path (entry, focus, pauses, exit), but build it from strong cues: contrast, faces and gaze direction, pointing, text, and isolation. Leading lines and S-curves help connect places, but they don't drive the eye on their own. On a page, rules, banners and other graphic marks can support that path when they bound a group or point to the next thing (TYPE-15).
- **Why:** Eye-tracking of paintings shows viewers returning to a few high-information regions, on a path that depends on viewer and task [SRC-241, SRC-242]. Gaze and pointing cues shift attention reliably [SRC-240]; faces win in paintings with people, contrast and colour in landscapes [SRC-243]. There is little direct evidence that leading lines on their own steer the eye.
- **Check:** Blur the work and note the first three places the eye lands. Are they the focus and the planned secondary points, in that order? Does any depicted gaze or pointing arm lead out of the frame or to nothing?
- **Fix:** Raise the focus's contrast; turn a figure's gaze toward the focus; add a secondary accent where the path should pause; cut or calm the cue that pulls off-route.
- **Grade:** Gaze cueing and contrast: well supported. "Leading lines steer the eye": craft wisdom with little direct test; the strong version ("lines force the path") is contested (see `core/evidence.md`).
- **Source:** DeAngelus & Pelz [SRC-241]; Nodine et al. [SRC-242]; Massaro et al. [SRC-243]; Friesen & Kingstone [SRC-240]; Ruskin's law of continuity [SRC-184]; AES-1.

### COMP-5. Give looking and moving things room in front
- **What:** A figure, face, vehicle or arrow that faces or moves one way needs more space in front of it than behind (lead room). Facing toward the inside of the frame reads as settled; facing out reads as leaving, which is fine only on purpose.
- **Why:** People prefer pictures where a directional object faces into the frame, the "inward bias" [SRC-218]. Preference also depends on where the object sits, and the effect is stronger for objects that clearly point or face [SRC-219].
- **Check:** For each directional element, measure the space in front of and behind it. Mirror-flip: does the flipped version feel more settled?
- **Fix:** Shift the subject toward the back edge, flip it (only if nothing in it reads backwards), or crop more behind it.
- **Grade:** Well supported.
- **Source:** Palmer, Gardner & Wickens [SRC-218]; Sammartino & Palmer [SRC-219].

### COMP-6. Design the figure and the ground together
- **What:** The figure should be the region that is smaller, enclosed, convex, symmetric or lower in the frame, and the shapes left over around it (negative shapes) should be designed as carefully as the objects. Dow's advice: spacing comes first, and good colour depends on good value pattern, which depends on good spacing [SRC-181].
- **Why:** Those cues decide what is seen as figure [SRC-250]; the lower region of a split is seen as figure more often [SRC-249]. Clear figure-ground makes an image easier to read and is liked more [SRC-37].
- **Check:** Fill the silhouettes solid and look only at the background shapes. Are they varied in size, or a set of near-identical slivers? Is anything reversible by accident (you can't tell which side is figure)?
- **Fix:** Vary the gaps; widen or close a sliver; overlap shapes decisively. If an area reads as figure when it should be ground, lighten it, open its edge or make it less convex.
- **Grade:** Well supported (figure-ground cues); "design the negative shapes" is craft wisdom built on it.
- **Source:** Wagemans et al. [SRC-250]; Vecera, Vogel & Woodman [SRC-249]; Dow [SRC-181]; Reber et al. [SRC-37]; CORE-2.

### COMP-8. One dominant in every attribute; everything else subordinate
- **What:** For each attribute (size, value, colour, direction, shape type, texture, interval), one kind dominates and the others play support. Ruskin's "principality": one feature more important than the rest, and "one light larger and brighter than the other lights" [SRC-184]. Dow's "subordination": group parts under one main part, by axis, radiation or size [SRC-181].
- **Why:** Hierarchy is how a viewer knows where to start (CORE-1). Equal competing amounts (half warm, half cool; half curves, half straights) read as indecision.
- **Check:** For each attribute, write the split: e.g. "value: 70% light, 20% mid, 10% dark; direction: mostly horizontal; shapes: mostly curved". Any attribute near 50/50 without a reason?
- **Fix:** Tip the near-even attribute to clear dominance (roughly 60-80% one kind, as a craft default, not a measured optimum). Keep the minority as accent near the focus.
- **Grade:** Craft wisdom.
- **Source:** Ruskin [SRC-184]; Dow [SRC-181]; Ross [SRC-182]; CORE-1; AES-2.

### COMP-9. Unity with variety: repeat a family, vary its members
- **What:** Build from a few families of shapes, colours and intervals that repeat, and vary each repetition in size, spacing or angle. Hutcheson put beauty at "uniformity amidst variety" [SRC-186]; Hogarth's six principles (fitness, variety, uniformity, simplicity, intricacy and quantity) work together, "mutually correcting and restraining each other" [SRC-185].
- **Why:** A review of the research concludes that order and complexity are separate dimensions that interact in appreciation, not two ends of one scale [SRC-231], so adding variety does not have to cost order. Repetition makes a form easy to see (fluency) [SRC-37]. Dow's warning: repetition without art (his examples are fences and blocks of buildings) is "like doggerel rhyme" [SRC-181].
- **Check:** List the shape families (round, angular, long), colour families and the repeated intervals. Is there any orphan (an element that belongs to no family)? Is any family a set of identical clones at equal spacing?
- **Fix:** Bring an orphan into a family (match its corner radius, colour or angle) or remove it. Vary the clones: big, medium, small; uneven intervals.
- **Grade:** Partly supported (order and complexity effects; fluency); the classic formula is tradition.
- **Source:** Hutcheson [SRC-186]; Hogarth [SRC-185]; Dow [SRC-181]; Van Geert & Wagemans [SRC-231]; Reber et al. [SRC-37]; CORE-9.

### COMP-10. Bridge strong contrasts with transition
- **What:** Where opposites meet (light and dark, straight and curved, big and small, warm and cool), let something carry the eye between them somewhere in the picture: a mid value, a gradation, a softened corner. Keep the sharpest, unbridged contrast for the focus. Dow names this principle "transition" [SRC-181]; Ross works it as gradation [SRC-182].
- **Why:** If every contrast is maximal, none leads (CORE-1); bridged contrasts hold the picture together.
- **Check:** Find the three strongest contrasts. Is the strongest at the focus? Elsewhere, is there any step between the extremes?
- **Fix:** Add a mid value or a gradation along one edge; round one corner; let the sharpest edge belong to the focus only (ILL-5).
- **Grade:** Craft wisdom.
- **Source:** Dow [SRC-181]; Ross [SRC-182]; Ruskin's laws of interchange and continuity [SRC-184]; ILL-5.

### COMP-11. Rhythm comes from measured intervals
- **What:** Choose how repeated elements are spaced. Regular intervals feel calm and formal; intervals that grow or shrink in steps (a progression) feel like movement; random intervals feel like noise. Ross describes rhythm as regular, marked movement [SRC-182].
- **Why:** The viewer reads an interval pattern as a pattern only if it has a rule.
- **Check:** Measure the gaps between repeats along the main direction. Are they equal, stepped (each one a set ratio of the last), or unrelated?
- **Fix:** Pick one: equal for calm, a progression toward the focus for movement. Make unrelated gaps follow a rule.
- **Grade:** Craft wisdom.
- **Source:** Ross [SRC-182]; Dow on repetition [SRC-181]; Crane on line and rhythm [SRC-196]; AES-1; TYPE-2.

### COMP-12. Tension on purpose, never by accident
- **What:** Tension (an element jammed near an edge, a strong diagonal, a crowded side, an unresolved gap) is a tool for unease, drama and energy. Use it where the brief wants energy; remove it where it isn't wanted. The worst state is the near-miss: almost centred, almost touching, almost level (COMP-1).
- **Why:** Off-centre and edge positions read as unstable and pulling [SRC-71, SRC-70]; Dondis contrasts deliberate sharpening with unreadable ambiguity [SRC-208].
- **Check:** List each source of tension (tangents, crowding at an edge, tilted horizon, cut-off subject). For each, is it intended by the brief's mood (AES-0)?
- **Fix:** Resolve the unintended ones (move away from the edge, level the horizon, overlap or separate tangents, ILL-1). Push the intended ones further so they read as chosen (COMP-20). The pre-delivery pass for accidental tension is COMP-19 to COMP-25.
- **Grade:** Partly supported (position-stability ratings); the use of tension is craft.
- **Source:** Dondis [SRC-208]; Arnheim [SRC-70]; Palmer & Guidi [SRC-71]; Locher & Stappers on implied dynamics [SRC-262]; ILL-1, ILL-7.

### COMP-13. Simple big shapes first: three to five masses
- **What:** The whole picture should read as a few big shapes (about three to five) before any detail. Detail lives *inside* the big shapes, and never breaks them up.
- **Why:** The gist of a scene is taken from coarse structure first, blobs before edges [SRC-244]. Gestalt research shows that the simplest grouping tends to win [SRC-250]. Appeal is judged in about 50 ms [SRC-36].
- **Check:** Blur the work hard (or view it at 120 px). Count the masses you can see. Does the main idea still read? If the blurred version is a grey mush, the structure is missing.
- **Fix:** Merge neighbouring values into fewer groups (CV-2); cut detail that crosses mass boundaries; simplify the silhouette (ILL-3).
- **Grade:** Coarse-first gist: well supported. "Three to five" is a craft number.
- **Source:** Schyns & Oliva [SRC-244]; Wagemans et al. [SRC-250]; Lindgaard [SRC-36]; Loomis [SRC-76]; Payne [SRC-210]; CORE-3; CV-2.

### COMP-14. Something to see at every viewing distance
- **What:** A strong piece gives something at three scales: big shapes from across the room, a readable arrangement at arm's length, and detail or texture close up. The big scale must always win.
- **Why:** Natural scenes have structure at many scales, and lab studies find people like fractal-like patterns of mid complexity (a fractal dimension around 1.3-1.5) on average, with real individual differences [SRC-228]. Images of art share some of these statistics with natural scenes [SRC-253].
- **Check:** View at thumbnail, at arm's length and close (or at 100% and 300% zoom). Does each step add something new? Does the close-up detail ever break the thumbnail read?
- **Fix:** Add texture or small accents inside the big shapes; or calm close detail that shows at thumbnail as noise.
- **Grade:** Partly supported (fractal preference in the lab, varying by person); the three-distance test is craft.
- **Source:** Spehar et al. [SRC-228]; Graham & Redies [SRC-253]; Hagerhall et al. [SRC-229]; LAY-7.

### COMP-15. More elements need more order
- **What:** Every time you add elements, also add order: alignment, grouping, repetition, a shared colour. Complexity is fine; complexity without order is not.
- **Why:** Order and complexity are separate dimensions that interact [SRC-231]; studies that varied only complexity gave contradictory results, partly because they ignored order. Complexity itself has several parts (number of elements, variety, irregularity), and people weigh them differently [SRC-230]. Highly complex web pages get the lowest first impressions [SRC-35].
- **Check:** Count the distinct element types and the distinct alignment lines. If types grew but alignment lines also grew, order did not keep up.
- **Fix:** Group, align to fewer lines, share one colour or shape language, or cut.
- **Grade:** Partly supported (separate factors: well argued; the best mix varies by person and stimulus).
- **Source:** Van Geert & Wagemans [SRC-231]; Nadal et al. [SRC-230]; Reinecke et al. [SRC-35]; CORE-8.

### COMP-16. Proportions from one family, for consistency, not for magic
- **What:** Choose the format and the main divisions from one family of ratios (simple ratios like 1:2, 2:3 and 3:4, √2 for paper, or the golden ratio if you like it) and reuse it. The value is consistency. No ratio makes a piece beautiful on its own.
- **Why:** Repeated proportions read as order (COMP-9). The golden-ratio beauty claim has failed repeated tests: no reliable preference for golden rectangles [SRC-220, SRC-221, SRC-38], and many famous examples rest on loose measuring [SRC-222, SRC-224]. The nautilus shell is not golden [SRC-223]. Hambidge's "dynamic symmetry" (1920) was an influential design system, but his claims about Greek practice are not established [SRC-194, SRC-224].
- **Check:** List the main ratios: format, main division, large-to-small areas. Do they come from one family? If a critique says "this follows the golden ratio, so it is beautiful", strike the claim.
- **Fix:** Bring stray proportions into the family; keep the ratio if it helps consistency, drop the claim about beauty.
- **Grade:** Consistency: craft wisdom. "Golden ratio equals beauty": myth.
- **Source:** Green [SRC-220]; Höge [SRC-221]; McManus et al. [SRC-38]; Markowsky [SRC-222]; Falbo [SRC-223]; Fischler [SRC-224]; Hambidge [SRC-194]; Vitruvius on symmetria (commensurable parts) [SRC-202]; LAY-12.

### COMP-17. Symmetry is a choice: go fully symmetric or clearly asymmetric
- **What:** Full mirror symmetry feels formal, calm, monumental and complete; asymmetry feels alive and informal. Pick one. Okakura notes that Zen-influenced art avoided symmetry because it expressed completion and repetition, and that the viewer completes what is left incomplete [SRC-199, SRC-214].
- **Why:** For abstract patterns, symmetry is the strongest single predictor of "beautiful" judgements [SRC-234]; it is also easy to process [SRC-37]. Near-symmetry (almost mirrored, with small accidental differences) looks like a mistake.
- **Check:** Mirror-flip and overlay at 50%. If the piece is almost symmetric, list the differences: are they deliberate?
- **Fix:** Make it truly symmetric (copy one half), or break the symmetry decisively (move the axis, change one side's weight clearly).
- **Grade:** Symmetry and beauty for patterns: well supported. The asymmetry tradition: craft and cultural.
- **Source:** Jacobsen & Höfel [SRC-234]; Reber et al. [SRC-37]; Okakura [SRC-199]; Parkes & Loughnane, SEP [SRC-214]; LAY-11.

### COMP-18. Direction carries reading habits
- **What:** In left-to-right reading cultures, rightward movement reads as "forward" and leftward as returning or resisting. Choose direction for what the story needs, and check the mirror image if the piece will meet a right-to-left audience.
- **Why:** Aesthetic preference for left-right direction shifts with reading habit [SRC-254], and so does how people picture events, with the actor placed on the side where reading starts [SRC-261]; lateral biases in art exist but are small and depend on the task [SRC-255, SRC-256].
- **Check:** Which way does the main movement or gaze go? Mirror-flip: does the meaning change in a way you want?
- **Fix:** Flip the arrangement (not text or anything with handedness) if the direction fights the story.
- **Grade:** Partly supported, culture-dependent. "The right side is always heavier" is contested.
- **Source:** Chokron & De Agostini [SRC-254]; Maass & Russo [SRC-261]; Levy [SRC-255]; McManus & Humphrey [SRC-256].

---

## Sitting right: the broken-balance pass (COMP-19 to COMP-25)

The pre-delivery check for *broken* balance and odd placement lives in [`sitting-right.md`](sitting-right.md): the viewing tests (squint, thumbnail, mirror, rotate 180°, cover half, gap measure, weight centroid, edge sweep) and these rules. Load it before delivery. It flags and asks "intended?"; it never centres or symmetrises by default.

- COMP-19. Flag broken balance, not asymmetry
- COMP-20. Make intent read: commit, don't hedge
- COMP-22. Top-heavy, bottom-heavy, and the centre that sits a little high
- COMP-23. Empty space is a shape with a job: active or dead
- COMP-24. Things that sit oddly: the edge and alignment sweep
- COMP-25. Run the pass, report flags, let the owner decide

## Myths and weak claims (details in `core/evidence.md`)
- **Golden ratio, golden spirals and "divine proportion" as the source of beauty:** myth (COMP-16).
- **"Leading lines force the eye":** contested; lines connect, content drives (COMP-4).
- **"Always use an odd number of objects" (rule of odds):** no direct test found; treat as a craft habit for avoiding pairs that split attention, not a rule.
- **Rule of thirds as law:** weak (ILL-1).
- **"Balance means symmetry or centring":** myth. Balance is equilibrium of weights; asymmetric and off-centre work balances by the lever (COMP-2, COMP-19).
- **An exact optical centre ("5% above the middle", "golden" margins):** myth in its exact form; the slight upward placement is craft wisdom (COMP-22).
- **Birkhoff's aesthetic measure (order ÷ complexity, 1933):** historical; its predictions did not hold up, though order and complexity remain useful dimensions (COMP-15).

Further reading, grouped and annotated: `BIBLIOGRAPHY.md`.
