# Module: colour and value

The light-dark structure of a piece (value, key, notan) and how its colours work together (contrast in place, harmony, chroma, light, distance, colour-vision deficiency). It deepens CORE-2, CORE-3 and CORE-6 and ILL-4 and ILL-9; it doesn't replace them. Load with `core/` for any picture, poster, page or palette decision; with `composition/` for structure.

Format: **What / Why / Check / Fix / Grade / Source**. Grades as in `core/evidence.md` (well supported, partly supported, craft wisdom, contested / myth). Nothing here is MUST-BE-RIGHT except where it repeats an existing blocker (text contrast, UI-6).

Measuring: `tools/look.py` gives a greyscale copy and L* statistics; `tools/contrast.py` gives WCAG ratios for colour pairs. For anything else, sample colours and convert to L* (CIELAB lightness, 0 black to 100 white) or OKLCH [S50].

---

### CV-1. Choose a value key and range on purpose
- **What:** Decide the key (high: mostly light; low: mostly dark; middle) and the range (full black to white, or compressed) for the mood the brief wants, then keep the piece inside it. The focus gets the biggest value contrast available within that key.
- **Why:** Value carries the read before colour does (CORE-2). A key that drifts (some parts high-key, some low) reads as two pictures.
- **Check:** Convert to greyscale and read the L* percentiles from `look.py`: p5, p50, p95. Is p50 where the chosen key says it should be (high key above about 65, low key below about 35, as rough guides)? Is the widest local contrast at the focus?
- **Fix:** Lift or drop the outliers into the key; compress shadows into a narrow dark range to free steps for the lights (Fowkes); keep the one full-range accent for the focus.
- **Grade:** Craft wisdom.
- **Source:** Loomis's tonal plans [S76]; Gurney, *How Many Values?* [S5]; Fowkes [S80]; Ruskin on one light larger and brighter than the rest [S184].

### CV-2. Design the notan: two and three values
- **What:** Reduce the work to two values (light and dark) and then three (light, middle, dark). The resulting pattern should be interesting on its own: varied shapes, linked darks or linked lights, and the focus at the strongest light-dark meeting. Dow treats this "notan" (Japanese for dark-light) as one of the three structural elements of art, alongside line and colour, and puts it before colour [S181].
- **Why:** Gist is taken from coarse structure first [S244]. Linked masses read as one big shape rather than scattered spots (COMP-13).
- **Check:** Threshold the greyscale at its median (2 values) and at the 33rd and 66th percentiles (3 values). Does the main idea still read? Are the darks a few connected shapes or many isolated spots? Is any important edge lost because both sides fall in one group?
- **Fix:** Merge isolated darks into a connected chain (Gurney's linking darks); push the focus's edge across the threshold; simplify a busy pattern into fewer, larger shapes.
- **Grade:** Craft wisdom, consistent with coarse-to-fine perception.
- **Source:** Dow [S181]; Gurney, *Linking Darks* [S16]; Schyns & Oliva [S244]; ILL-4; COMP-13.

### CV-3. Don't separate with hue alone: check every important edge in greyscale
- **What:** Two areas of different hue but equal lightness (equiluminant) seem to shimmer, float or lose their position, and the edge disappears in greyscale. Use that only for a deliberate glow or vibration. Every edge that carries meaning (figure against ground, text against background, a data series against its neighbour) needs a lightness step.
- **Why:** The parts of vision that handle position, depth and motion respond mainly to luminance, so equal-lightness edges are hard to locate; Livingstone shows painters using this deliberately for glow and movement [S215]. Lightness contrast also raises preference in colour pairs [S41], and contrast rules (WCAG) are luminance-based [S3].
- **Check:** View in greyscale. Does each important edge survive? For key pairs, compare L*: a difference under about 15-20 L* units usually looks weak in greyscale (a working default chosen for this repo, not a standard). For text, `tools/contrast.py` and UI-6 decide.
- **Fix:** Lighten one side and darken the other; or keep the equiluminant pair and add an outline or value step where meaning depends on it.
- **Grade:** Well supported (luminance and edge perception); the L* threshold is self-chosen.
- **Source:** Livingstone, *Vision and Art* [S215]; Schloss & Palmer [S41]; WCAG [S3]; CORE-2; UI-6.

### CV-4. Judge each colour where it sits: the peephole test
- **What:** A colour's appearance depends on what surrounds it: neighbours push each other apart in lightness, hue and saturation (simultaneous contrast). Pick and adjust colours on their real ground, at their real size, not as swatches on white.
- **Why:** Chevreul set out the law of simultaneous contrast in 1839 from his work on dyed tapestries: two colours side by side each shift toward the complement of the other [S188]. Albers built a whole course on one colour looking like two and two looking like one [S47].
- **Check:** Peephole test: punch a small hole in grey card (or crop a tiny patch digitally and place it on mid grey) and look at a colour isolated from its neighbours. Does it match what you thought you used? Look at the same colour in two places in the piece: do they look the same? Should they?
- **Fix:** Adjust the colour in place until it reads as intended; if the same brand or role colour must look the same in two places, keep its surroundings similar or tune it locally.
- **Grade:** Well supported.
- **Source:** Chevreul [S188]; Albers [S47]; Palmer, Schloss & Sammartino [S217]; CORE-6; ILL-9.

### CV-5. Harmony: hold one dimension steady, vary another in steps
- **What:** A palette feels unified when its colours share something: a narrow hue range with lightness steps, a shared lightness with hue steps, or a shared low chroma with one strong accent. Colour-wheel schemes (complementary, triadic, split-complementary) are starting points, not proof of harmony.
- **Why:** In tests, pairs rated harmonious tend to be similar in hue, and pairs that are liked tend to differ in lightness [S41]. Models built from ratings of two-colour combinations also find that similar hue and similar chroma, plus a lightness difference, predict harmony [S245]. Wheel templates come from teaching traditions and are used in graphics software [S246], but their link to people's ratings is weak.
- **Check:** Plot the palette in OKLCH or Munsell terms (hue, lightness, chroma). Which dimension is shared? Which varies, and in regular steps? Is there more than one "loud" colour?
- **Fix:** Pull stray hues into the range; step lightness evenly; mute all but one accent.
- **Grade:** Shared-hue harmony and lightness-contrast preference: well supported. Wheel geometry: craft wisdom with weak evidence.
- **Source:** Schloss & Palmer [S41]; Ou & Luo [S245]; Cohen-Or et al. [S246]; Munsell [S189]; Rood [S190]; CORE-6.

### CV-6. A chroma budget: strongest colour, smallest area, at the focus
- **What:** Spend high chroma sparingly. Strong colours take small areas near the focus; large areas are muted or neutral. Munsell's rule: when colours of unequal strength must balance, use more area of the weaker one; his example balances a bright buttercup yellow-red against twice the area of a weak violet [S189]. Itten calls this the contrast of extent [S48].
- **Why:** The most saturated patch draws the eye (CORE-3); spread everywhere, it flattens hierarchy and looks accidental.
- **Check:** Estimate the share of the picture above a chroma threshold (in OKLCH, roughly C > 0.15). Is it small (a craft default: under about 10-15%)? Is it at or near the focus? Is there a second strong-chroma area competing elsewhere?
- **Fix:** Desaturate the large areas or the competitor; shrink the strong colour; move it to the focus.
- **Grade:** Craft wisdom (Munsell's balance is a system rule, not tested on viewers). The fixed area ratios that Itten attributes to Goethe (yellow needing a third of the area of violet, and so on) are tradition with no evidence; they do not appear in the 1840 English translation of Goethe's *Theory of Colours* [S192, S48].
- **Source:** Munsell [S189]; Itten [S48]; Goethe [S192]; CORE-6.

### CV-7. One colour of light over everything
- **What:** All the colours in a scene sit under the same light, so they share its tint: everything under warm evening light leans warm, everything in shade leans toward the sky colour. A palette that ignores the light looks pasted together.
- **Why:** The visual system expects a common illuminant and judges colours relative to it (colour constancy) [S217]; painters unify a scene with one light colour, sometimes by literally glazing or tinting the whole (Gurney) [S51].
- **Check:** Sample a white or neutral in the light and the same in shadow. Do they shift the same way as the stated light (key, sky, bounce)? Does any object keep its "local" colour unchanged when everything else has shifted?
- **Fix:** Shift the outlier toward the light's tint; add a light colour overlay at low opacity to the whole and then restore the focus.
- **Grade:** Colour constancy: well supported. The painting practice: craft wisdom.
- **Source:** Gurney, *Color and Light* [S51]; Palmer, Schloss & Sammartino [S217]; Rood [S190]; ILL-9; TD-LIT-1.

### CV-8. Distance lowers contrast and sharpness
- **What:** Further away means lower value contrast, lower chroma, softer edges and a shift toward the colour of the air (usually lighter and bluer by day). Keep the strongest contrasts and sharpest edges in the foreground or at the focus.
- **Why:** Lower contrast alone makes a region look further away [S247]; blur pattern also signals depth and scale [S248]. Leonardo described aerial perspective centuries ago; Ruskin and the landscape tradition rely on it [S184].
- **Check:** Posterise to 3-4 levels and mark the depth planes. Does contrast decrease from near to far? Is there a far element with a near-level contrast or edge that jumps forward?
- **Fix:** Lighten and cool the far plane; lower its contrast and chroma; soften its edges.
- **Grade:** Well supported.
- **Source:** O'Shea, Blackburn & Ono [S247]; Held et al. [S248]; ILL-5; ILL-14.

### CV-9. Make it survive colour-vision deficiency
- **What:** Any colour distinction that carries meaning must also differ in lightness, or be backed by shape, label or pattern.
- **Why:** Red-green colour-vision deficiency affects about 8% of men and 0.5% of women of Northern European descent, with lower rates in many other groups [S252].
- **Check:** Simulate protanopia and deuteranopia (any CVD simulator), and view in greyscale. Are paired colours that mean different things still distinguishable?
- **Fix:** Separate by lightness (CV-3); add a second cue (UI-6, CORE-6).
- **Grade:** Well supported.
- **Source:** Birch [S252]; WCAG [S3]; CORE-6; UI-6.

---

## Myths and weak claims (details in `core/evidence.md`)
- **Colour-wheel schemes guarantee harmony:** weak (CV-5).
- **"Goethe's" area ratios** (via Itten) and other fixed "colour proportion" numbers: tradition only (CV-6).
- **Colour-emotion tables** (red = anger, blue = trust): context-dependent and weakly supported [S46].
- **"Complementary colours always look best together":** pairs of very different hue are rarely rated harmonious [S41]; complements are a contrast tool, not a harmony recipe.

Further reading: `BIBLIOGRAPHY.md` (Chevreul, Rood, Munsell, Ostwald, Goethe, Albers, Itten, Livingstone).
