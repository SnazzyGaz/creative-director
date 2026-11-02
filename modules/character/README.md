# Module: character and anatomy

Figures, faces, hands and animals in drawings, paintings, 3D characters and AI-generated images. Load it whenever a person, a hand or an animal is in the frame, however small: the anatomy pass (CHAR-9) is then required. Load with `core/`, `technical-drawing/` (TD-PRO-1 and TD-PRO-2 set the measuring habit) and `illustration/` (ILL-10 gesture). This module adds the body-specific checks.

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults. Every check is something you can count, measure or compare on the image, at 200% zoom where small. Choices of style (how cartoony, how idealised, how cute) are taste calls for the owner of the work; the rules only ask that the choice is made and kept.

Why it matters: people are expert face and body readers. Small errors that would pass in a chair or a tree read as wrong, sick or eerie in a person, and broken hands and eyes are among the most noticed signs that an image is AI-generated [S110, S141].

---

### CHAR-1. Pick a proportion system and keep it
- **What:** Decide the figure's height in heads and hold it across the piece and the set. Rough guides: average adult about 7-7.5 heads, idealised 8, heroic 8.5-9, children and stylised figures fewer (a toddler about 4, many cartoon styles 2-5).
- **Why:** A figure drifting between systems (a realistic body with a cartoon head, or one character changing height across panels) reads as an error, not a style.
- **Check:** Measure the head (chin to crown) and count it into the full height. Do figures of the same age and type in one piece or series agree within about half a head?
- **Fix:** Adjust the drifting figure to the chosen system; record the system on a character sheet for sets.
- **Grade:** Craft wisdom.
- **Source:** Loomis, *Figure Drawing for All It's Worth* [S134]; TD-PRO-1.

### CHAR-2. Landmarks line up (MUST-BE-RIGHT for realistic figures)
- **What:** In a standing realistic adult: crotch near the halfway mark of the height; with arms hanging, wrists near crotch level and fingertips around mid-thigh; elbows near the navel or waist; knee about midway between hip joint and sole; shoulder width about 2 heads (often less in women). Upper arm and forearm about the same length.
- **Why:** These landmarks are what viewers sense even without training; when two are off, the figure looks broken.
- **Check:** Draw horizontal lines through the landmarks and compare. On a bent or foreshortened limb, compare segment lengths along the limb, allowing for perspective (TD-PER-3).
- **Fix:** Correct the one or two landmarks that are off; lengthen or shorten at the joints, not mid-bone.
- **Grade:** Craft wisdom (artistic anatomy).
- **Source:** Loomis [S134]; Goldfinger, *Human Anatomy for Artists* [S142]; Hampton, *Figure Drawing: Design and Invention* [S135].

### CHAR-3. Hands are countable and built right (MUST-BE-RIGHT)
- **What:** Each visible hand has the right number of digits for the design (five for realistic; a consistent four is a valid cartoon convention), the thumb on the correct side for a left or right hand, fingers bending only at their joints and only towards the palm, and lengths in order (middle longest; index and ring similar; little finger ending near the ring finger's last joint). Hand length is about the face from chin to hairline.
- **Why:** Hands are the most frequent and most noticed anatomy error in generated images [S141, S110].
- **Check:** At 200%, count digits per hand, including hidden ones that should be implied. For each hand, say which arm it belongs to and whether the thumb is on the right side. Check for extra joints, merged fingers, or fingers passing through held objects. Compare hand length with the face. For a hand that holds something, name the grip: in a power grip the fingers curl round the object and the thumb presses back from the other side; in a precision grip the object is pinched between fingertips and thumb pad [S149]. A hand that "holds" with flat, straight fingers, or with the thumb on the same side as the fingers, isn't holding.
- **Fix:** Repaint or regenerate the hand alone (inpaint) with a simpler pose: a fist, a hand partly hidden, or an object held. Use a photo or a 3D hand as reference rather than guessing.
- **Grade:** Partly supported (viewers notice hand errors [S110]); construction is craft.
- **Source:** Narasimhaswamy et al., *HanDiffuser* [S141]; Kellogg Insight / Groh [S110]; Hampton [S135]; Napier [S149].

### CHAR-4. Faces: placement and matched eyes (MUST-BE-RIGHT for the eyes)
- **What:** In an adult head seen front-on, the eyes sit near the halfway line of the head; the gap between the eyes is about one eye width; the ears lie between brow and nose base; the mouth's corners fall roughly under the pupils. Both eyes match in size, shape and highlight direction, and look at the same point.
- **Why:** Mismatched eyes are a common AI-image tell and a main trigger of eeriness in realistic faces: abnormal eyes in a realistic face were rated far more unpleasant than the same change in a less realistic face [S136].
- **Check:** Draw the centre line through the face and the eye line across. Compare the two eyes (mirror one over the other in perspective). Do the catchlights point the same way as the key light? Do the irises point at one target? Count teeth only if the mouth is open: a row of uniform, too-many teeth is a tell.
- **Fix:** Correct the odd eye to match the other in perspective; align gaze; simplify teeth.
- **Grade:** Partly supported (face perception research [S136]); placement is craft.
- **Source:** Loomis [S134]; Seyama & Nagayama [S136]; Kellogg Insight / Groh [S110].

### CHAR-5. Keep one level of realism
- **What:** Skin, eyes, hair and proportion share one level of realism. Stylised proportions (big eyes, big head) belong with stylised rendering; photo-real rendering needs realistic proportions.
- **Why:** The uncanny effect is strongest when cues disagree, such as realistic skin with doll-sized or enlarged eyes [S136]. Reviews find the most consistent support for this mismatch explanation, not for one universal curve [S138].
- **Check:** List the realism level of skin, eyes, hair, hands and proportion. Do any two disagree clearly?
- **Fix:** Move the outlier towards the rest (usually: make the eyes and proportions realistic, or simplify the rendering).
- **Grade:** Partly supported (mismatched realism cues [S138]).
- **Source:** Seyama & Nagayama [S136]; Mori, MacDorman & Kageki [S137]; Kätsyri et al. [S138].

### CHAR-6. Weight and gesture
- **What:** The figure has a line of action (ILL-10) and stands where it can balance: in a standing pose, a plumb line from the pit of the neck lands on or between the supporting feet. With weight on one leg, the hips tilt up on that side and the shoulders tilt the other way (contrapposto).
- **Why:** Off-balance figures look like they're falling or floating, even when every part is correct.
- **Check:** Drop the plumb line. Is it over the support? If weight is on one leg, do hips and shoulders tilt in opposite directions? Are both feet on the ground plane (TD-PER-1)?
- **Fix:** Shift the hips over the support, or add the movement that explains the imbalance (a step, a lean on something).
- **Grade:** Craft wisdom.
- **Source:** Hampton [S135]; Loomis [S134]; ILL-10.

### CHAR-7. Every limb starts and ends somewhere (MUST-BE-RIGHT)
- **What:** Count limbs and follow each from shoulder or hip to hand or foot. No extra, missing, fused or swapped limbs; no limb merging into another person, clothing or furniture; held objects are gripped by a hand you can trace.
- **Why:** Fused and extra limbs are classic generated-image failures and make the image unusable for most purposes.
- **Check:** For each person: 2 arms, 2 legs (or reasons why not). Trace each one. At overlaps between people, which body does each limb belong to?
- **Fix:** Inpaint the region with a clearer pose (separate the figures, reduce overlaps); if more than one limb is wrong, regenerate or rework the figure (`core/critique-loop.md` section 6).
- **Grade:** Partly supported (viewers notice limb errors [S110]).
- **Source:** Kellogg Insight / Groh [S110]; [S141].

### CHAR-8. Stylisation is deliberate and consistent
- **What:** Stylised choices (big heads and eyes, tiny feet, elongated limbs) follow the brief and stay the same across every image of the same character: proportions, colours, costume details, marks.
- **Why:** Bigger heads, larger eyes and rounder faces measurably raise cuteness ratings (the baby schema) [S140], so they're a valid tool, but only when they're the intended effect. In a series, any drift reads as a different character.
- **Check:** Put all images of the character side by side: same head count, eye size relative to head, colours (sample them), costume details? List the differences.
- **Fix:** Make a one-page character sheet (front, side, colours, head count) and correct each image to it. How stylised to go is the owner's call.
- **Grade:** Cuteness cues: well supported [S140]. Consistency: craft.
- **Source:** Glocker et al. [S140]; CHAR-1.

### CHAR-9. Anatomy pass: crop, trace, count (MUST-BE-RIGHT, delivery gate)
- **What:** Whenever a person, a hand or an animal is in the frame, run the anatomy pass below before any hand-off. Each check is done on a zoomed crop of one region, never on the whole image at a glance. Any failed line is a blocker: the work can't be delivered as it is, whatever else is right.
- **Why:** Generators still produce wrong finger counts, merged body parts and limbs that belong to no one [S150, S151], and people spot these faults readily [S150, S110]. They are small in the frame, so a whole-image look misses them; a check of light, edges and type passes them straight through.
- **Check:** The table below, one line per crop, each line pass or fail with what was seen.
- **Fix:** Edit or inpaint the failing region only, with the anatomy spelled out (which arm, which side, how many fingers, what the hand holds and how) [S151]. Then run the **whole** pass again, not only the fixed line: an edit can move, add or remove another hand. If three edits fail, regenerate the figure (`core/critique-loop.md` section 6) or report the failure; don't deliver it.
- **Grade:** Procedure.
- **Source:** Kamali et al. [S150]; Lu et al., *HandRefiner* [S151]; Napier [S149]; Bridgman [S153]; Goldfinger [S142, S152].

### CHAR-10. Animals: count and match the species (MUST-BE-RIGHT for counts)
- **What:** Each animal has the right number of eyes, legs, wings or fins for its species, in the right places; parts connect to the body; eyes match each other and catch the same light; teeth, claws and beaks are the right kind and number for the animal. Stylised animals may simplify, but consistently.
- **Why:** Viewers know common animals well, and generators duplicate or drop parts on animals as they do on people.
- **Check:** Name the species. Count eyes, limbs or fins against a photo or anatomy reference of that species. Trace each limb or fin to where it joins the body. Zoom on the eye: one pupil, round or slit as the species has it, highlight on the key-light side. If the mouth is open, look at the teeth.
- **Fix:** Edit the region with the species and the count stated; use a reference photo.
- **Grade:** Craft wisdom (animal anatomy).
- **Source:** Goldfinger, *Animal Anatomy for Artists* [S152]; Kamali et al. [S150].

## The anatomy pass (CHAR-9)

**How.** List every person, hand and animal you can find, including partial ones at the frame edge and in the background. Crop each hand, each limb join and each face or animal head at 2x-4x (`tools/anatomy_crops.py` makes the crops and a labelled sheet; by hand, any image viewer at 200%+ works). Write one line per crop. "Looks fine" without a crop doesn't count.

**Left and right.** Name sides from the figure's own point of view, then say which side of the image that is. A figure facing the viewer has its right arm on the image's left. Trace from the shoulder, not from where the hand happens to be.

| # | Check | Pass when | Rule |
|---|---|---|---|
| A1 | Hand count | Each person shows two hands, or the missing one is plainly hidden (behind a body, object or frame edge) | CHAR-7 |
| A2 | Finger count | Each visible hand: five digits for realistic work (four is a valid, consistent cartoon convention); hidden digits are plausibly hidden, not missing | CHAR-3 |
| A3 | Trace | Each hand follows back along a wrist and forearm, through an elbow, to a shoulder on the correct side of the same person; no hand without an arm, no arm ending without a hand or an occluder | CHAR-7 |
| A4 | Thumb and side | Thumb on the correct side for a left or right hand seen palm-in or palm-out | CHAR-3 |
| A5 | Grip | A held object is wrapped by curled fingers with the thumb opposing (power grip), or pinched between fingertips and thumb pad (precision grip); fingers sit on the surface, not through it [S149] | CHAR-3 |
| A6 | Joints | Elbows, knees, wrists and finger joints bend only the way they can; no extra joints; upper arm and forearm similar length | CHAR-2, CHAR-3 |
| A7 | Merges and extras | No extra or missing limbs, no limb fused with another person, clothing or object, no sleeve that changes arm partway | CHAR-7 |
| A8 | Face | Eyes match in size, shape and highlight; gaze converges (or both lids closed alike); teeth, if shown, are a believable row, not a strip | CHAR-4 |
| A9 | Animals | Eye count and pupil, limb or fin count and placement match the species; each joins the body | CHAR-10 |
| A10 | Clothing symmetry | Collars, cuffs, sleeves, earrings and glasses match left to right | TD-PRO-2 |
| A11 | Ground and shadow | Feet on the ground plane; shadows agree with the key light | CHAR-6, TD-LIT-3 |

Record it in the critique (template section *Anatomy pass*): crop file, line number, pass or fail, what was seen. A1-A9 failures are blockers; A10-A11 follow their own rules.

---

## Myths

- **"Eight heads is the correct human."** It's an idealised standard; average adults are nearer 7-7.5 [S134]. See TD-PRO-1.
- **"Beautiful faces follow the golden ratio" (the "phi mask").** There's no good evidence; tests of golden-ratio preference are weak in general [S38]. Averageness and symmetry have modest effects on attractiveness, and that's what the research supports [S139].
- **"Perfect symmetry looks best."** Preference for symmetry is modest, and mirror-perfect faces can look artificial [S139]. Check that features *match*; don't mirror whole faces.
- **"The uncanny valley is one universal curve."** The evidence for a single curve is mixed; mismatched realism cues are the best-supported trigger [S138]. Use CHAR-5 rather than "make it less realistic".
