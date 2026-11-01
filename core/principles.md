# Core principles

These apply to every kind of visual work. Check them before any module rule. Each rule has an ID (cite it in critiques, e.g. `CORE-2`) and five parts: **What / Why / Check / Fix / Source**.

---

## CORE-1. One clear hierarchy
- **What:** The viewer should see things in the order you intend: one main thing, then a few supporting things, then the rest.
- **Why:** If everything shouts, nothing is heard. Viewers give up or look at the wrong thing.
- **Check:** Blur or squint (see `critique-loop.md`). Write down the first three things you notice. Do they match the intended order? Count how many elements are "big": more than two is a warning.
- **Fix:** Make the main thing bigger, higher-contrast, or given more space. Turn the rest *down* rather than the hero *up*.
- **Source:** NN/g, *Visual Hierarchy in UX* and *5 Principles of Visual Design* [S1, S2].
- **Example pair:** NN/g contrasts Spotify's home screen (clear groups, one section leads even when blurred) with a busy retail page where every block has the same size and weight and the eye has nowhere to start [S1].

## CORE-2. Value before colour
- **What:** Get the lights and darks working first. Colour sits on top of a value structure; it cannot rescue a weak one.
- **Why:** Hierarchy and readability come mostly from light-dark contrast, not hue. Colour-blind viewers, small thumbnails and print all strip colour away.
- **Check:** Convert to greyscale. Does the main subject still read? Can you sort the image into 2-4 value groups?
- **Fix:** Group values into a light family and a dark family; save the strongest light-against-dark for the focal point. Avoid "middle-value mumbling" (everything mid-grey).
- **Exception:** very light sketch or line work (high-key pencil, construction drawings) is a deliberate exception when the brief calls for it. The subject must still read at thumbnail size (CORE-10).
- **Source:** Gurney, *How Many Values?* and *Cure for Middle Value Mumbling* [S5, S6]; WCAG 1.4.3 (contrast is measured on luminance, not hue) [S3].
- **Example pair:** Gurney describes Pyle's *Travels of the Soul*: lights welded into one mass, darks into one shadow, strong impact. Compare a student scene where every object has its own mid-tone and nothing groups [S5, S6].

## CORE-3. Contrast where it matters, nowhere else
- **What:** Use contrast (value, size, colour, sharpness, detail) to mark what is different or important. Keep it quiet elsewhere.
- **Why:** Contrast is the eye's magnet. Spread evenly, it becomes noise.
- **Check:** List where the highest contrast sits. Is it on the focal point / primary action? Is there a high-contrast accident somewhere unimportant (a bright patch at the edge, a loud icon)?
- **Fix:** Lower contrast on the accident; concentrate it at the focus. Limit yourself to about three levels of emphasis.
- **Source:** NN/g, *5 Principles of Visual Design* (contrast) and *Visual Hierarchy* (no more than ~3 contrast variations) [S1, S2].

## CORE-4. Spacing groups things
- **What:** Things that belong together sit closer together than things that don't. Space between groups is larger than space inside them.
- **Why:** People read closeness as meaning (Gestalt proximity). Even spacing everywhere hides the structure.
- **Check:** Measure gaps: is the gap between a label and its field smaller than between two fields? Between a heading and its text smaller than between sections?
- **Fix:** Use a small spacing scale (e.g. 4/8/16/24/32...) and give each gap a role: inside a group, between groups, between sections.
- **Source:** NN/g, *Visual Hierarchy* (grouping) [S1]; Material 3 spacing [S9]; Gestalt laws of proximity, common region and similarity, as collected in *Laws of UX* [S61].
- **Example pair:** NN/g praises a checkout form where headers hug their fields and chunks are separated, and criticises a 2017 US tax form where tight, even spacing makes it unclear which "Last name" belongs to whom [S1, S2].

## CORE-5. Align to something
- **What:** Every element should line up with something else: a grid column, an edge, a baseline, a perspective line.
- **Why:** Near-misses (2-5 px off, a figure almost on the horizon) look like mistakes. Clear alignment reads as intent.
- **Check:** Draw (or imagine) vertical and horizontal lines through edges. Look for things that are *almost* aligned.
- **Fix:** Snap them to the line, or move them clearly off it so the break looks deliberate.
- **Source:** Butterick, *Maxims of Page Layout* ("relate each new element to existing elements") [S10].

## CORE-6. Colour with a job
- **What:** Use a limited palette where each colour has a role (accent, background, warning, a light source, a mood). 
- **Why:** Too many equally strong colours flatten hierarchy and look accidental.
- **Check:** Count the saturated colours. Can you say what each one is for? In UI, is colour the *only* signal for anything (a fail)?
- **Check, in place:** Judge each colour where it sits, not as a swatch. The same colour looks different on different grounds (Albers). A warm or cool note is only warm or cool relative to its neighbours.
- **Fix:** Pick a restricted gamut; keep one accent for the most important thing; pair colour with a second cue (shape, label, icon). For unity, keep hues close and get separation from lightness. For an accent, use a small area of strong colour against a large muted one (Itten's contrast of extent).
- **Source:** NN/g, *Visual Hierarchy* (limit colours; don't rely on colour alone) [S1]; Gurney, gamut masking [S11]; Albers, *Interaction of Color* [S47]; Itten's seven contrasts [S48]; Schloss & Palmer on colour pairs [S41].

## CORE-7. Type that reads
- **What:** Few sizes with clear steps between them, comfortable line length, enough contrast.
- **Why:** Text is usually the bulk of a page and the first thing to break at small sizes.
- **Check:** How many type sizes? (Three to five is plenty.) Body line length 45-90 characters, ideally around 65? Line spacing about 120-145% of the type size? Text contrast at least 4.5:1 (3:1 for large text)?
- **Fix:** Get the body text right first, because it is most of the page. Then pick other sizes from one scale, set a max width on text blocks, and darken the text or lighten its ground.
- **Source:** Butterick, *Line Length* and *Typography in Ten Minutes* [S12, S53]; Bringhurst, comfortable measure (66 characters ideal) [S52]; Material 3 type scale [S13]; WCAG 1.4.3 [S3].

## CORE-8. Restraint and intent
- **What:** Every element should earn its place. If you can't say why something is there, remove it or quiet it.
- **Why:** Each extra element competes with the important ones.
- **Check:** For each element ask "what does this do for the viewer?" Try hiding it: is the piece worse without it?
- **Fix:** Cut, merge, or push to the background. Simplify before you add.
- **Source:** NN/g heuristic #8, *Aesthetic and Minimalist Design* [S4]; Butterick, *Maxims* ("keep it simple", "don't fear white space") [S10]; signal-to-noise, Lidwell et al. [S69]; processing fluency, Reber et al. [S37].

## CORE-9. Consistency
- **What:** Same thing, same look. Different thing, visibly different look.
- **Why:** Inconsistency makes viewers wonder whether a difference means something. In pictures, inconsistent light or perspective breaks belief.
- **Check:** Find two things that should match (two buttons, two shadows, two figures' eye levels). Do they?
- **Fix:** Use tokens/styles in UI; one light direction and one horizon in pictures.
- **Source:** NN/g heuristic #4 [S4]; Butterick, *Maxims* [S10].

## CORE-10. Reads at its real size
- **What:** Judge work at the size people will meet it: thumbnail, phone, poster across a room.
- **Why:** Detail that reads at 100% zoom disappears at feed size; big shapes and values are what survive.
- **Check:** View at thumbnail size (about 150-200 px wide) and at the real display size. Is the idea still clear?
- **Fix:** Strengthen big shapes and value groups; drop or soften detail that only exists up close.
- **Source:** Gurney, *Getting a Fresh Eye* (reducing glass, mirror at distance) [S7, S8].

## CORE-11. Balance by visual weight
- **What:** The picture or screen feels settled unless the brief wants tension. Weight comes from size, darkness or contrast, saturation, isolation, and distance from the centre.
- **Why:** An unexplained heavy side looks like an accident. A centred, symmetrical layout is already balanced; an off-centre one with a counterweight is too. Neither is the default: judge by intent.
- **Check:** Flip the image horizontally (critique-loop test 3). Does one side suddenly feel heavier? Is a small, intense element off to one side balanced by anything?
- **Fix:** Move the weight toward the centre or the frame's main axes, or add a counterweight (a smaller, darker or more saturated element on the other side). Keep the placement the work chose (centred or off-centre) unless it fights the intent.
- **Source:** Arnheim, *Art and Visual Perception* (structural skeleton, visual weight) [S70]; Palmer & Guidi, goodness of fit in rectangles (centre and axes are the "good" positions) [S71]; evidence on centring and thirds is weak either way [S43, S44].

---

**Myths:** golden ratio, the rule of thirds as a law, colour-emotion claims and similar ideas are covered in `evidence.md`. Don't use them as reasons for a fix.
