# Module: technical drawing

Construction: perspective, proportion, light and shadow, ellipses. Load with `core/`. Use for drawings, paintings, concept art, AI-generated images and renders that depict 3D space.

Every rule here is **MUST-BE-RIGHT**: unless the brief asks for a stylised or impossible space, an error is a failure, not a style choice. Each rule also says whether a tool could check it automatically:
- **Auto: yes** - a script can measure it reliably.
- **Auto: partly** - a script can flag candidates; a person or bot confirms by eye.
- **Auto: no** - judge by eye with the stated test.

Format: **What / Why / Check / Fix / Auto / Source**. Tools are in `tools/` (see `tools/README.md`). Measure at zoom before calling a failure.

---

## Perspective

### TD-PER-1. One horizon (eye level) per picture
- **What:** The horizon line is the viewer's eye level. There is exactly one, and every set of parallel horizontal edges converges to a vanishing point on it.
- **Why:** Two eye levels make the ground tilt and objects look pasted in.
- **Check:** Extend receding horizontal edges (tops of boxes, kerbs, tables). Their vanishing points should all land on one horizontal line.
- **Fix:** Draw the horizon first; redraw the edges that miss it.
- **Auto:** partly. Line detection (e.g. Hough/LSD) plus vanishing-point fitting can find the horizon and flag edges whose VPs fall off it: `tools/vp.py` (detect segments, group them by eye, then fit). Organic shapes give few straight edges, so a bot confirms.
- **Source:** Gurney, *Eye Level* series [S22]; Robertson & Bertling, *How to Draw* [S24].

### TD-PER-2. Figures on the same ground plane share the eye-level line
- **What:** If the viewer stands on the same flat ground as standing people of similar height, their heads (eyes) line up near the horizon regardless of distance.
- **Why:** It is the fastest way to catch figures at the wrong scale for their distance.
- **Check:** Draw the horizon. Do standing adults' eyes sit on or near it? If the eye level is at someone's waist, is it at the waist of every similar figure?
- **Fix:** Rescale the figure so the horizon crosses it at the same body point as the others.
- **Auto:** partly. A pose/keypoint detector can find eyes and feet; compare their heights to the horizon. Seated, sloped or child figures need a human eye.
- **Source:** Gurney, *Eye Level* series [S22].
- **Example pair:** Gurney's eye-level posts show crowds where the horizon cuts every adult at the same height (correct) against figures that grow or shrink at random as they recede (incorrect) [S22].

### TD-PER-3. Verticals stay vertical unless three-point perspective is intended
- **What:** In one- and two-point perspective, vertical edges are truly vertical. If they converge, they converge to one third vanishing point, consistently.
- **Why:** A few leaning verticals read as a drawing error, not a dramatic angle.
- **Check:** Measure the angle of every vertical edge. All ~90°, or all converging to one point above or below?
- **Fix:** Pick one system and redraw the outliers.
- **Auto:** yes for buildings and objects with straight edges (angle measurement; `tools/vp.py`, group `v`); partly elsewhere.
- **Source:** Robertson & Bertling, *How to Draw* [S24].

### TD-PER-4. Foreshortening matches distance
- **What:** Equal real lengths get shorter as they recede, and the spacing of repeated items (fence posts, tiles, windows) shrinks steadily toward the vanishing point.
- **Why:** Even spacing on a receding plane flattens it; random spacing makes it wobble.
- **Check:** Use the diagonal method: diagonals through a receding rectangle's corners locate its true centre. Does the drawn middle post sit there?
- **Fix:** Space repeats with diagonals (or measuring lines), not by eye.
- **Auto:** partly. With a detected VP, spacing ratios of repeated elements can be tested.
- **Source:** Robertson & Bertling, *How to Draw* [S24].

### TD-PER-5. Keep the subject inside the cone of vision
- **What:** The important forms sit within about a 60° cone around the centre of vision (roughly 30° each side of the line of sight). Vanishing points for a box are far enough apart that its near corner is not sharper than 90°.
- **Why:** Outside the cone, forms stretch and corners look too sharp: wide-angle distortion that looks like a mistake unless intended.
- **Check:** Find the centre of vision and the two vanishing points. Does any important form sit near the frame edge and look stretched? Is the near corner of a box on the ground plane drawn sharper than a right angle?
- **Fix:** Move the vanishing points further apart (step the viewer back), or crop so the subject stays near the centre.
- **Auto:** partly. With detected VPs, VP spacing relative to the frame can be measured.
- **Source:** Vandruff, perspective course (cone of vision, station point) [S75]; Robertson & Bertling, *How to Draw* [S24].

## Proportion

### TD-PRO-1. Proportions are measured, not guessed
- **What:** Use a unit (the head for figures, a key dimension for objects) and check the main lengths against it.
- **Why:** Small errors compound; a body built by eye drifts long or short.
- **Check:** For a standing adult, count head-heights (about 7.5 for an average adult, ~8 for an idealised figure). Check landmarks: the crotch near the halfway mark, the knee roughly midway down the leg.
- **Fix:** Re-block the figure with a head-unit scale before detailing.
- **Auto:** partly. Keypoint detectors can estimate limb ratios on clear poses; foreshortened limbs and stylised characters need a bot or human.
- **Source:** Proko, *Human Proportions* (Loomis-based) [S25]; Loomis, *Figure Drawing for All It's Worth* [S26].
- **Note:** Stylised work (chibi, heroic, cartoon) sets its own proportion. The rule is then *consistency with the chosen canon*, not realism. Ask Gaz which canon applies.

### TD-PRO-2. Left and right agree
- **What:** Paired features (eyes, ears, shoulders, wheels, table legs) obey the same perspective and size rules.
- **Why:** Mismatched pairs are the most common construction error in drawings and AI images.
- **Check:** Flip the image (core loop). Draw a line through each pair: do the lines converge to the same VP as the head or object?
- **Fix:** Construct a centre line and the pair's alignment line, then redraw.
- **Auto:** partly (landmark detection on faces works well; elsewhere confirm by eye).
- **Source:** Gurney, *Getting a Fresh Eye* (flip/mirror) [S7]; Robertson & Bertling [S24].

## Light and shadow

### TD-LIT-1. One key light, one direction
- **What:** Every form is lit from the same main direction, and every cast shadow points away from that light.
- **Why:** Mixed light directions are the fastest way to make a scene look composited.
- **Check:** Mark the light side and the terminator (light-to-shadow transition) on several forms. Do they agree? Do cast shadows all fall the same way? For a nearby light, lines from object to shadow tip should meet near the light's ground position.
- **Fix:** Pick the light position; repaint the outliers.
- **Auto:** partly. Shadow-direction lines can be traced and tested for convergence; soft or multiple lights need a human eye.
- **Source:** Gurney, *Light and Form* parts 1-2 [S20, S21].

### TD-LIT-2. Light family and shadow family stay separate
- **What:** The darkest light area is lighter than the lightest shadow area (except highlights and occlusion accents). Reflected light lifts a shadow but keeps it in the shadow family.
- **Why:** When reflected light gets as bright as the light side, the form loses solidity.
- **Check:** Greyscale + posterise to two values. Does the light/shadow split follow the terminator on every form?
- **Fix:** Pull reflected light down; keep the core shadow just past the terminator; darken occlusion where forms touch.
- **Auto:** yes for the two-value split itself (posterise and compare with a mask); deciding which side *should* be lit needs the light direction.
- **Source:** Gurney, *Light and Form* part 2 (core shadow, reflected light, occlusion) [S21]; Gurney, *How Many Values?* [S5].
- **Example pair:** Gurney points to an over-modelled art-school drapery study (every tonal step in every fold, so it looks academic) against Rubens' *Daniel*, where reflected light fills the shadow side but stays clearly in the shadow family [S21].

### TD-LIT-3. Cast shadows sit on the ground
- **What:** Objects touching a surface have a dark contact (occlusion) shadow at the touch point; cast shadows start at the object's base.
- **Why:** Without it objects float.
- **Check:** Zoom on every contact point (feet, table legs, cups).
- **Fix:** Add the darkest small accent at the contact and connect the cast shadow to the base.
- **Auto:** partly.
- **Source:** Gurney, *Light and Form* part 2 [S21]; Robertson & Bertling, *How to Render* (constructing cast shadows in perspective) [S72].

## Ellipses and construction

### TD-ELL-1. The minor axis follows the surface's axis
- **What:** A circle in perspective is an ellipse whose minor axis lines up with the axis through the circle's centre (the axle of a wheel, the centre line of a cylinder), which itself points to that axis's vanishing point.
- **Why:** Tilted ellipses make wheels wobble and cups lean.
- **Check:** Draw the minor axis of each ellipse (the line through its narrowest width). Does it coincide with the cylinder's centre line / axle?
- **Fix:** Draw the axis first, then the ellipse square to it.
- **Auto:** yes. Ellipse fitting (e.g. OpenCV `fitEllipse`) gives the minor-axis angle; compare it with the detected axis line (`tools/ellipse.py --axis`).
- **Source:** Drawabox Lesson 1, *Ellipses* [S23]; Robertson & Bertling, ch. 5 *Ellipses and Rotations* [S24]; Bartlett, *The Bad Ellipse* [S31].

### TD-ELL-2. Ellipse degree changes with position
- **What:** The further a circle is from eye level (or from the centre of vision), the more open its ellipse. Along a horizontal cylinder or a stack of rings, the degree changes steadily.
- **Why:** Identical ellipses along a long form make it look flat.
- **Check:** Measure minor/major ratio of each ellipse along the form. Does it change in one direction, steadily?
- **Fix:** Open ellipses progressively away from the eye level.
- **Auto:** yes (fit and compare ratios; `tools/ellipse.py`; half-visible ellipses give an approximate degree).
- **Source:** Drawabox Lesson 1 (the "same degree on every cross-section" mistake is shown explicitly) [S23].
- **Example pair:** The Drawabox ellipse lesson shows a cylinder drawn with every cross-section at the same degree (incorrect) next to one whose ellipses open up toward the ends (correct) [S23].

### TD-ELL-3. Ellipses are smooth and symmetrical
- **What:** No points at the ends of the major axis, no flat sides; both halves mirror across both axes.
- **Why:** A pointed ellipse reads as a lemon, not a circle.
- **Check:** Fold test across the minor and major axes. Look at the ends.
- **Fix:** Redraw with the whole arm, ghosting the motion first.
- **Auto:** yes (residual from fitted ellipse; `tools/ellipse.py` end check, tested only on synthetic shapes so far).
- **Source:** Drawabox Lesson 1 [S23]; Bartlett [S31].

### TD-CON-1. Build from simple forms before detail
- **What:** Boxes, cylinders, spheres first; detail last.
- **Why:** Detail on wrong construction can't be rescued.
- **Check:** Can you see (or reconstruct) the underlying simple forms, and do they obey TD-PER and TD-ELL?
- **Fix:** Redraw the construction layer, then re-apply detail.
- **Auto:** no.
- **Source:** Robertson & Bertling [S24]; Loomis [S26].

### TD-CON-2. Moved to illustration as ILL-10 (gesture before structure), 2026-11-01.

## Myths and weak claims
- **"Eight heads tall is correct":** eight heads is an idealised or heroic proportion. Average adults are about 7.5 heads (TD-PRO-1) [S25]. Use whichever the brief calls for, consistently.
- **"Stretched edges are just how perspective looks":** they usually mean the subject is outside the cone of vision (TD-PER-5) [S75].
- **"Ellipses have pointed ends":** they never do, at any degree [S31].
