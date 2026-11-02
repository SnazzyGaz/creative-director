# Case study: "May Specials" A-board

> **Third-party sign, used only as a teaching example.** This is a sidewalk A-board from a restaurant with no connection to this project. There is no affiliation, endorsement or commission. The original photo was supplied by the owner of the work for a critique exercise. The remake is a self-judged study, not a delivered or approved design. "Butterfinger" is a trademark of its owner; it appears here only as plain menu text. If you are the rights holder and want this removed, open an issue.

This is the only worked example in the repo that names a real piece. It shows the rules in action from start to finish: first-principles brief → imagery → viewing distance → whitespace → marks → facts. Everything below is **self-judged**.

| File | What it is |
|---|---|
| `original.jpg` | The photographed sign, perspective-corrected (the given) |
| `brief.md` | Facts transcribed, fact check, the seven step-back answers, the brief, three concepts and the recommendation |
| `concepts.png` | The three structural concepts as thumbnails; A ("Hero and strip") was chosen |
| `final.jpg` | The built remake after the full aesthetic loop and the LAY-10 whitespace fix |
| `before-after.jpg` | Original and final side by side |

## The lessons in action

**1. Step back before drawing (FP-2 to FP-6).** The sign is read in two passes: a one-second glance at 3–5 m by someone walking past, then a 1 m read if they stop. Its one job is to make the burger and its price stop people. The original gave all four items equal weight, used 11 type treatments and set the body copy at about 1.5% of the board height. The three concepts differ in structure, not only in style. A was chosen because it is the only one that gives the lead item enough size to read at 4 m.

**2. Design for the real medium (FP-2).** The medium is a 24×36 in board on a pavement (the size is [inferred] from the photo's proportions). It is not a phone screen and not the framing of the photo it arrived in. Every size decision below is made in millimetres on the board.

**3. Viewing distance (LAY-7: cap height ≈ distance / 250).** The board is 1600 px across 610 mm, so 0.381 mm/px. Cap heights were measured from the rendered fonts:

| Element | Cap height | Reads to about | Needed |
|---|---|---|---|
| Headline "MAY SPECIALS!" | 43 mm | 10.8 m | 3–5 m ✔ |
| Burger price | 35 mm | 8.9 m | 3–5 m ✔ |
| "SMASH" | 31 mm | 7.6 m | 3–5 m ✔ |
| Tots name | 25 mm | 6.2 m | 3–5 m ✔ |
| Name in footer | 22 mm | 5.4 m | 3–5 m ✔ |
| Tots price | 21 mm | 5.1 m | 3–5 m ✔ |
| Burger name | 17 mm | 4.2 m | 3–5 m ✔ |
| Burger description | 13 mm | 3.1 m | 1–1.5 m ✔ |
| Shake descriptions | 10 mm | 2.4 m | 1–1.5 m ✔ |

Everything meant for the glance reads at 4 m or more, and every description reads at the 1 m stop.

**4. Imagery from the subject (FP-9, ILL-12).** The food is built from what the menu says is in it, not from a re-description of the photo's artwork. 2–4× crops of the final were checked against the transcribed ingredients: toasted bun, smashed patties with a crust, pepper jack, jalapeño poppers, bacon, grilled green chiles and pico de gallo on the burger; tots with cheese sauce, chiles, bacon and pico. Every component is present and plausible. There is no tiling, no melted or fused shapes and no impossible geometry. The light comes from the upper left in all three images.

**5. Whitespace (LAY-10).** The first built version passed the squint test and the hierarchy check, but `tools/whitespace.py` failed it:

| | Result |
|---|---|
| Before the fix | FAIL: an 88 px band between the hero and the tots (1.74× the next largest gap), plus a 256 px dead zone at the top right of the hero (2.0× the reference gap, 3.5% of the area) |
| After the fix | PASS: the largest empty region is 1.0× the reference gap, and no band exceeds 1.5× unintentionally |

The fix moved the item block to the top of the column and put the price after the description, so it reads name → description → price. The burger moved down 10 px and the tots moved up 30 px. The whole layout was then re-reviewed, not just the area that changed.

**6. Marks (FP-8, BRAND-4).** No usable logo file existed. The only source was a small, glare-affected patch of a phone photo, so the restaurant name is set in plain type, not traced or imitated, and the brief asks the owner for the file. The third-party candy bar name is plain menu text, with no wordmark. The cups are unbranded.

**7. Facts (FP-3).** Every line was transcribed word for word before any design work, then checked against itself: prices agree everywhere, and there is no date, address, hours or phone number. Nothing was added that the original did not say.
