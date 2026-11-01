# Module: character and anatomy

Figures, faces and hands in drawings, paintings, 3D characters and AI-generated images. Load with `core/`, `technical-drawing/` (TD-PRO-1 and TD-PRO-2 set the measuring habit) and `illustration/` (ILL-10 gesture). This module adds the body-specific checks.

Format: **What / Why / Check / Fix / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults. Every check is something you can count, measure or compare on the image, at 200% zoom where small. Choices of style (how cartoony, how idealised, how cute) are taste calls for the owner of the work; the rules only ask that the choice is made and kept.

Why it matters: people are expert face and body readers. Small errors that would pass in a chair or a tree read as wrong, sick or eerie in a person, and broken hands and eyes are among the most noticed signs that an image is AI-generated [S110, S141].

---

### CHAR-1. Pick a proportion system and keep it
- **What:** Decide the figure's height in heads and hold it across the piece and the set. Rough guides: average adult about 7-7.5 heads, idealised 8, heroic 8.5-9, children and stylised figures fewer (a toddler about 4, many cartoon styles 2-5).
- **Why:** A figure drifting between systems (a realistic body with a cartoon head, or one character changing height across panels) reads as an error, not a style.
- **Check:** Measure the head (chin to crown) and count it into the full height. Do figures of the same age and type in one piece or series agree within about half a head?
- **Fix:** Adjust the drifting figure to the chosen system; record the system on a character sheet for sets.
- **Source:** Loomis, *Figure Drawing for All It's Worth* [S134]; TD-PRO-1.

### CHAR-2. Landmarks line up (MUST-BE-RIGHT for realistic figures)
- **What:** In a standing realistic adult: crotch near the halfway mark of the height; with arms hanging, wrists near crotch level and fingertips around mid-thigh; elbows near the navel or waist; knee about midway between hip joint and sole; shoulder width about 2 heads (often less in women). Upper arm and forearm about the same length.
- **Why:** These landmarks are what viewers sense even without training; when two are off, the figure looks broken.
- **Check:** Draw horizontal lines through the landmarks and compare. On a bent or foreshortened limb, compare segment lengths along the limb, allowing for perspective (TD-PER-3).
- **Fix:** Correct the one or two landmarks that are off; lengthen or shorten at the joints, not mid-bone.
- **Source:** Loomis [S134]; Goldfinger, *Human Anatomy for Artists* [S142]; Hampton, *Figure Drawing: Design and Invention* [S135].

### CHAR-3. Hands are countable and built right (MUST-BE-RIGHT)
- **What:** Each visible hand has the right number of digits for the design (five for realistic; a consistent four is a valid cartoon convention), the thumb on the correct side for a left or right hand, fingers bending only at their joints and only towards the palm, and lengths in order (middle longest; index and ring similar; little finger ending near the ring finger's last joint). Hand length is about the face from chin to hairline.
- **Why:** Hands are the most frequent and most noticed anatomy error in generated images [S141, S110].
- **Check:** At 200%, count digits per hand, including hidden ones that should be implied. For each hand, say which arm it belongs to and whether the thumb is on the right side. Check for extra joints, merged fingers, or fingers passing through held objects. Compare hand length with the face.
- **Fix:** Repaint or regenerate the hand alone (inpaint) with a simpler pose: a fist, a hand partly hidden, or an object held. Use a photo or a 3D hand as reference rather than guessing.
- **Source:** Narasimhaswamy et al., *HanDiffuser* [S141]; Kellogg Insight / Groh [S110]; Hampton [S135].

### CHAR-4. Faces: placement and matched eyes (MUST-BE-RIGHT for the eyes)
- **What:** In an adult head seen front-on, the eyes sit near the halfway line of the head; the gap between the eyes is about one eye width; the ears lie between brow and nose base; the mouth's corners fall roughly under the pupils. Both eyes match in size, shape and highlight direction, and look at the same point.
- **Why:** Mismatched eyes are a common AI-image tell and a main trigger of eeriness in realistic faces: abnormal eyes in a realistic face were rated far more unpleasant than the same change in a less realistic face [S136].
- **Check:** Draw the centre line through the face and the eye line across. Compare the two eyes (mirror one over the other in perspective). Do the catchlights point the same way as the key light? Do the irises point at one target? Count teeth only if the mouth is open: a row of uniform, too-many teeth is a tell.
- **Fix:** Correct the odd eye to match the other in perspective; align gaze; simplify teeth.
- **Source:** Loomis [S134]; Seyama & Nagayama [S136]; Kellogg Insight / Groh [S110].

### CHAR-5. Keep one level of realism
- **What:** Skin, eyes, hair and proportion share one level of realism. Stylised proportions (big eyes, big head) belong with stylised rendering; photo-real rendering needs realistic proportions.
- **Why:** The uncanny effect is strongest when cues disagree, such as realistic skin with doll-sized or enlarged eyes [S136]. Reviews find the most consistent support for this mismatch explanation, not for one universal curve [S138].
- **Check:** List the realism level of skin, eyes, hair, hands and proportion. Do any two disagree clearly?
- **Fix:** Move the outlier towards the rest (usually: make the eyes and proportions realistic, or simplify the rendering).
- **Source:** Seyama & Nagayama [S136]; Mori, MacDorman & Kageki [S137]; Kätsyri et al. [S138].

### CHAR-6. Weight and gesture
- **What:** The figure has a line of action (ILL-10) and stands where it can balance: in a standing pose, a plumb line from the pit of the neck lands on or between the supporting feet. With weight on one leg, the hips tilt up on that side and the shoulders tilt the other way (contrapposto).
- **Why:** Off-balance figures look like they're falling or floating, even when every part is correct.
- **Check:** Drop the plumb line. Is it over the support? If weight is on one leg, do hips and shoulders tilt in opposite directions? Are both feet on the ground plane (TD-PER-1)?
- **Fix:** Shift the hips over the support, or add the movement that explains the imbalance (a step, a lean on something).
- **Source:** Hampton [S135]; Loomis [S134]; ILL-10.

### CHAR-7. Every limb starts and ends somewhere (MUST-BE-RIGHT)
- **What:** Count limbs and follow each from shoulder or hip to hand or foot. No extra, missing, fused or swapped limbs; no limb merging into another person, clothing or furniture; held objects are gripped by a hand you can trace.
- **Why:** Fused and extra limbs are classic generated-image failures and make the image unusable for most purposes.
- **Check:** For each person: 2 arms, 2 legs (or reasons why not). Trace each one. At overlaps between people, which body does each limb belong to?
- **Fix:** Inpaint the region with a clearer pose (separate the figures, reduce overlaps); if more than one limb is wrong, regenerate or rework the figure (core loop section 4b).
- **Source:** Kellogg Insight / Groh [S110]; [S141].

### CHAR-8. Stylisation is deliberate and consistent
- **What:** Stylised choices (big heads and eyes, tiny feet, elongated limbs) follow the brief and stay the same across every image of the same character: proportions, colours, costume details, marks.
- **Why:** Bigger heads, larger eyes and rounder faces measurably raise cuteness ratings (the baby schema) [S140], so they're a valid tool, but only when they're the intended effect. In a series, any drift reads as a different character.
- **Check:** Put all images of the character side by side: same head count, eye size relative to head, colours (sample them), costume details? List the differences.
- **Fix:** Make a one-page character sheet (front, side, colours, head count) and correct each image to it. How stylised to go is the owner's call.
- **Source:** Glocker et al. [S140]; CHAR-1.

## Zoom audit for generated figures

Run at 200% on every person in an AI image. One line each; any "no" is a finding under the rule shown.

| Check | Rule |
|---|---|
| Digits counted, thumbs on the right side | CHAR-3 |
| Eyes match; gaze converges; catchlights agree with the light | CHAR-4, TD-LIT-1 |
| Limbs traced end to end; none fused or extra | CHAR-7 |
| Earrings, glasses arms, collars and sleeves match left to right | TD-PRO-2 |
| Teeth, text on clothing, and background people not melted | CHAR-4, ILL-11 |
| Feet on the ground plane; shadows agree | CHAR-6, TD-LIT-3 |

---

## Myths

- **"Eight heads is the correct human."** It's an idealised standard; average adults are nearer 7-7.5 [S134]. See TD-PRO-1.
- **"Beautiful faces follow the golden ratio" (the "phi mask").** There's no good evidence; tests of golden-ratio preference are weak in general [S38]. Averageness and symmetry have modest effects on attractiveness, and that's what the research supports [S139].
- **"Perfect symmetry looks best."** Preference for symmetry is modest, and mirror-perfect faces can look artificial [S139]. Check that features *match*; don't mirror whole faces.
- **"The uncanny valley is one universal curve."** The evidence for a single curve is mixed; mismatched realism cues are the best-supported trigger [S138]. Use CHAR-5 rather than "make it less realistic".
