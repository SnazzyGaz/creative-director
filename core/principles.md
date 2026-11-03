# Core principles

Apply to every kind of visual work, before any module rule. Cite by ID (e.g. `CORE-2`). Format: **What / Why / Check / Fix / Grade / Source**; grades are defined in `evidence.md`.

---

## CORE-1. One clear hierarchy
- **What:** The viewer sees things in the intended order: one main thing, a few supporting things, then the rest.
- **Why:** If everything shouts, the eye has nowhere to start.
- **Check:** Blur or squint. Write down the first three things you notice: do they match the intended order? More than two "big" elements is a warning.
- **Fix:** Give the main thing more size, contrast or space. Turn the rest down rather than the hero up.
- **Grade:** Partly supported.
- **Source:** NN/g [SRC-1, SRC-2].

## CORE-2. Value before colour
- **What:** Get the lights and darks working first; colour cannot rescue a weak value structure.
- **Why:** Hierarchy and legibility come mostly from light-dark contrast. Colour-blind viewers, thumbnails and print strip hue away.
- **Check:** Greyscale it (by luminance). Does the subject still read? Does it sort into 2-4 value groups?
- **Fix:** Group values into a light family and a dark family; save the strongest light-against-dark for the focus. Exception: high-key sketch or line work the brief asks for, provided it reads at thumbnail size (CORE-10).
- **Grade:** Partly supported; contrast is measured on luminance (Standard, WCAG).
- **Source:** Gurney [SRC-5, SRC-6]; WCAG 1.4.3 [SRC-3]. Deeper: CV-1 to CV-3.

## CORE-3. Contrast where it matters, nowhere else
- **What:** Contrast (value, size, colour, sharpness, detail) marks what is important; keep it quiet elsewhere.
- **Why:** Contrast pulls the eye. Spread evenly, it becomes noise.
- **Check:** Where is the highest contrast? On the focus or primary action? Any bright accident at an edge or on something minor?
- **Fix:** Lower the accident; concentrate contrast at the focus. About three levels of emphasis.
- **Grade:** Craft wisdom, consistent with salience research (COMP-3).
- **Source:** NN/g [SRC-1, SRC-2].

## CORE-4. Spacing groups things
- **What:** Things that belong together sit closer than things that don't. Gaps between groups are larger than gaps inside them. Spacing comes from a small scale (e.g. 4/8/16/24/32/48), each step with a role: inside a group, between groups, between sections.
- **Why:** People read closeness as belonging (proximity). Even spacing everywhere hides the structure.
- **Check:** Is a label nearer its field than the next field? A heading nearer its text than the section above? Are gaps on the scale (UI: inspect the CSS)?
- **Fix:** Snap gaps to the scale and give each gap a role.
- **Grade:** Well supported (proximity grouping); the scale itself is craft.
- **Source:** NN/g [SRC-1]; Material 3 spacing [SRC-9]; *Laws of UX* [SRC-61].

## CORE-5. Align to something
- **What:** Every element lines up with something: a column, an edge, a baseline, a perspective line.
- **Why:** Near-misses read as mistakes; clear alignment reads as intent.
- **Check:** Run lines through edges; look for things *almost* aligned. Bands and thresholds: COMP-20 (to the frame's lines), COMP-24 (between elements).
- **Fix:** Snap to the line, or move clearly off it.
- **Grade:** Craft wisdom; see COMP-24 for the evidence on edge fit.
- **Source:** Butterick [SRC-10].

## CORE-6. Colour with a job
- **What:** A limited palette where each colour has a role (accent, ground, warning, a light source, a mood).
- **Why:** Many equally strong colours flatten hierarchy and look accidental.
- **Check:** Count the saturated colours: can you say what each is for? Is colour the only signal for anything (a fail in UI)? Judge colour in place, not as a swatch (CV-4).
- **Fix:** Restrict the gamut; one accent for the most important thing; pair colour with a second cue (shape, label, icon).
- **Grade:** Craft wisdom; "not colour alone" is Standard (WCAG 1.4.1).
- **Source:** NN/g [SRC-1]; Gurney [SRC-11]; Albers [SRC-47]; Itten [SRC-48]; Schloss & Palmer [SRC-41]. Deeper: CV-3 to CV-6.

## CORE-7. Type that reads
- **What:** Few sizes on one scale, comfortable line length and leading, enough contrast.
- **Why:** Text is usually most of the page and the first thing to break at small sizes.
- **Check:** Three to five sizes? Body 45-90 characters per line (about 65)? Body leading about 1.3-1.5 (1.5 where WCAG text spacing applies)? Contrast at least 4.5:1, 3:1 for large text?
- **Fix:** Set the body first, then other sizes from one scale; cap the measure; darken text or lighten its ground. Detail: `modules/typography/` (TYPE-2 to TYPE-5).
- **Grade:** Partly supported (reading research); the contrast and spacing floors are Standard (WCAG).
- **Source:** Butterick [SRC-12, SRC-53]; Bringhurst [SRC-52]; WCAG 1.4.3, 1.4.12 [SRC-3, SRC-117].

## CORE-8. Restraint and intent
- **What:** Every element earns its place.
- **Why:** Each extra element competes with the important ones; lower complexity is liked better at first sight [SRC-35].
- **Check:** For each element: what does it do for the viewer? Hide it: is the piece worse?
- **Fix:** Cut, merge or push back. Simplify before adding.
- **Grade:** Partly supported (complexity and fluency research).
- **Source:** NN/g [SRC-4]; Butterick [SRC-10]; Lidwell et al. [SRC-69]; Reber et al. [SRC-37]; Reinecke et al. [SRC-35].

## CORE-9. Consistency
- **What:** Same thing, same look; different thing, visibly different.
- **Why:** Inconsistency makes viewers ask whether a difference means something; in pictures, mixed light or perspective breaks belief.
- **Check:** Find two things that should match (buttons, shadows, eye levels). Do they?
- **Fix:** Tokens and styles in UI; one light and one horizon in pictures.
- **Grade:** Craft wisdom.
- **Source:** NN/g [SRC-4]; Butterick [SRC-10].

## CORE-10. Reads at its real size
- **What:** Judge work at the size people meet it: thumbnail, phone, poster across a room.
- **Why:** Detail that reads at 100% disappears at feed size; big shapes and values survive.
- **Check:** View at about 150-200 px wide and at real display size. Is the idea still clear?
- **Fix:** Strengthen big shapes and value groups; drop detail that only exists up close.
- **Grade:** Craft wisdom, consistent with coarse-first gist (COMP-13).
- **Source:** Gurney [SRC-7, SRC-8].

## CORE-11. Balance by visual weight
- **What:** The piece feels settled unless the brief wants tension. Weight comes from size, darkness and contrast, saturation, isolation, faces and text, and distance from the centre.
- **Why:** An unexplained heavy side looks like an accident. Centred-symmetric and off-centre-with-counterweight are both balanced; neither is the default.
- **Check:** Mirror the image: does one side suddenly feel heavier? Is an intense off-side element answered by anything?
- **Fix:** Add a counterweight, or commit harder to the asymmetry so it reads as chosen. Keep the placement the work chose. Never centre or symmetrise by default.
- **Grade:** Partly supported (see COMP-2).
- **Source:** Arnheim [SRC-70]; Palmer & Guidi [SRC-71]; [SRC-43, SRC-44]. Deeper: COMP-2 (weighing, `tools/balance.py`) and the *Sitting right* pass (COMP-19 to COMP-25).

---

Myths (golden ratio, thirds as a law, colour-emotion claims) are in `evidence.md`. Never use them as reasons.
