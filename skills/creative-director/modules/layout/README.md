# Module: layout, print and social

Fixed-frame layouts: social cards and posts, link previews, thumbnails, posters, slides and print. Load with `core/`; add `typography/` for any text and `brand/` for anything with a name on it. Web pages that scroll and reflow are `web-ui/`.

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults.

Why it matters: most social images are first seen as a small tile in a moving feed, where appeal is judged in about 50 ms [S36]. The job of the layout is to survive that glance and the platform's crop.

---

### LAY-1. Build on a grid
- **What:** Divide the frame into columns (and rows for posters and slides), with margins and gutters from one spacing unit. Text blocks and images start and end on grid lines.
- **Why:** Shared edges make a layout read as one ordered thing; near-miss alignments look like errors (CORE-4).
- **Check:** Overlay the grid (or list the left x and top y of every block). Any edges that almost match but don't (bands: COMP-24)?
- **Fix:** Snap near-misses to the same line. Common starting grids: 12 columns for 16:9, 6 for square and 4:5, 4 for 9:16.
- **Grade:** Craft wisdom.
- **Source:** Müller-Brockmann, *Grid Systems* [S60]; UI-4.

### LAY-2. Margins that breathe, and are even
- **What:** Outer margins at least about 5% of the short side (more on posters and covers). Equal on left and right unless the asymmetry is deliberate; nothing important touches the edge by accident.
- **Why:** Content crammed against the frame looks cropped, and platforms round corners and overlay buttons near edges.
- **Check:** Measure the smallest distance from text and key shapes to each edge, in pixels and as a % of the short side.
- **Fix:** Shrink or cut content rather than the margin. Set the margin as a token and use it for every edge.
- **Grade:** Craft wisdom.
- **Source:** Müller-Brockmann [S60]; Lupton [S54].

### LAY-3. One focal point, one reading order
- **What:** One element clearly leads (usually the image or headline). Then a short path: headline, support, sign-off (logo or link). On a social card, three text elements is usually the most that works.
- **Why:** A feed tile gets a glance. With two competing focal points, neither lands (CORE-1).
- **Check:** Blur and thumbnail tests (`tools/look.py`). What is seen first, second, third? Is that the order the brief needs? Count text elements.
- **Fix:** Scale up the lead element; cut the rest to the essentials; move secondary text to the post body or caption.
- **Grade:** Partly supported (CORE-1).
- **Source:** CORE-1; NN/g, *Visual Hierarchy* [S1].

### LAY-4. Export at the platform's size and ratio
- **What:** Use the platform's recommended size and ratio (table below). Export at the full recommended width; never upscale a small render.
- **Why:** Wrong ratios get cropped or padded; small images get blurred or shown as tiny thumbnails.
- **Check:** Read the file's pixel size, ratio and file size against the table.
- **Fix:** Re-render at the right size. Lay out once at the largest size, then make the other crops deliberately, not by auto-crop.
- **Grade:** Standard (platform specs).
- **Source:** the platform docs cited in the table.

**Platform specs, checked 1 November 2026.** Platforms change these often; re-check the cited page before relying on them.

| Placement | Recommended | Ratio | Notes | Source |
|---|---|---|---|---|
| X post, single image | 1600 × 900 (or 1200 × 675) | 16:9 | Single images from about 2:1 to 3:4 show uncropped on mobile; others are centre-cropped. Up to 4 images. | [S124, S130] |
| X link card (`summary_large_image`) | 1200 × 600 | 2:1 | Min 300 × 157, max 4096 × 4096, under 5 MB; no SVG. | [S123] |
| LinkedIn image post | 1080 wide; 1080 × 1080 or 1080 × 1350 | 3:1 to 4:5 | Under 5 MB; outside the range is centre-cropped. | [S126] |
| LinkedIn link preview | 1200 × 627 | 1.91:1 | Minimum for the large preview. | [S126] |
| Instagram feed | 1080 × 1350 | 4:5 | 3:4 (1080 × 1440) stays uncropped when posted in the app; the profile grid shows 3:4, trimming about 34 px off each side of a 4:5 post. | [S125, S130] |
| Instagram story / reel | 1080 × 1920 | 9:16 | Keep text out of roughly the top 14%, bottom 35%, sides 6% (practitioner guidance). | [S130] |
| YouTube thumbnail | 3840 × 2160 recommended; 1280 × 720 is fine | 16:9 | Min 640 wide; under 2 MB from mobile, 50 MB from desktop. The duration badge sits bottom right. | [S127] |
| GitHub social preview | 1280 × 640 | 2:1 | Under 1 MB; PNG, JPG or GIF. Uploaded by hand in repo Settings. | [S128] |
| Open Graph (`og:image`, Facebook and most chat apps) | 1200 × 630 | 1.91:1 | Min 600 × 315 for the large preview; set `og:image:width` and `height`. | [S129] |

### LAY-5. Key content inside the safe area (MUST-BE-RIGHT)
- **What:** Text, faces, logos and the focal point sit where no crop, rounded corner, avatar, button, caption bar or duration badge can cover them.
- **Why:** A headline cut off by the grid crop or a play badge makes the piece fail at its one job.
- **Check:** Draw the platform's crops on the image: centre crops to 1:1, 3:4 and 1.91:1 for any image that may be reused; the 9:16 overlay zones; the bottom-right badge zone on thumbnails. Does any key element cross a line?
- **Fix:** Pull key elements towards the centre; keep a margin of at least 6-8% of the short side free of text; make separate crops instead of one compromise.
- **Grade:** Standard (platform specs).
- **Source:** [S125, S127, S130]; LAY-2.

### LAY-6. Legible at feed size (MUST-BE-RIGHT for the main message)
- **What:** The main message (headline, or the face or object that is the point) reads when the image is shown at about 400 px wide, a typical phone feed width.
- **Why:** That is the size most people see it at; the full-size file is what only the designer sees.
- **Check:** Scale the export to 400 px wide. Is the headline readable without zoom? Measure its x-height: about 6 px or more (TYPE-3). Does the idea survive the thumbnail test at 200 px wide?
- **Fix:** Fewer, bigger words; stronger value contrast between text and ground (UI-6 ratios apply to text in images too); remove detail that turns to noise.
- **Grade:** Partly supported (legibility research); the feed-size test is craft.
- **Source:** Lindgaard et al. [S36]; Legge & Bigelow [S114]; UI-6.

### LAY-7. Posters: read at distance, then up close
- **What:** A poster has two reading distances: the far glance (one image and the headline) and the near read (details). Design the far layer first.
- **Why:** People decide whether to approach from across the room; small type can't do that job.
- **Check:** View the poster at about 10% of its size (roughly how a 50 cm-wide poster looks from 5 m). Do the image and headline still read? Is the detail text set together, not scattered?
  **Signage and A-boards (viewing-distance check):** write down the printed size and the distances it is read from (a pavement board: headline and price from 3-5 m, body from about 1-1.5 m). Convert each key line's cap height from pixels to millimetres at print size and compare with the distance. A practical working minimum is cap height ≈ distance ÷ 250 (12-20 mm for 3-5 m). The sign industry's best-case figure, head-on in good light, is about distance ÷ 360; signs seen at an angle or in passing need far more, about distance ÷ 120 [S179, S180]. Report each line as "reads to X m".
- **Fix:** Enlarge the headline and simplify the image; group details into one block on the grid. On signage, cut words before shrinking the type that must read from the pavement.
- **Grade:** Standard (sign-industry guidance) for the size rule; the two-distance test is craft.
- **Source:** Müller-Brockmann [S60]; CORE-1; United States Sign Council Foundation [S179, S180].

### LAY-8. Slides: one point each, with signals
- **What:** One message per slide, stated as the title (a sentence, not a topic label). Remove decoration that doesn't explain. Text a room can read: about 24 pt or more at 1920 × 1080, at most about six short lines. Highlight what the speaker is talking about.
- **Why:** People learn more when extraneous material is cut (coherence) and when the key items are signalled; text that duplicates speech word for word can hurt (redundancy) [S132]. Dense slides become documents nobody reads [S133].
- **Check:** Can the slide's point be read from its title alone? Count lines and the smallest size. Is there clip art, a stock photo or a template ornament with no job?
- **Fix:** Rewrite titles as claims; split crowded slides; move detail to speaker notes or a handout.
- **Grade:** Partly supported (multimedia-learning experiments [S132]).
- **Source:** Mayer, *Multimedia Learning* [S132]; Duarte, *slide:ology* [S133].

### LAY-9. Print files: bleed, resolution, colour (MUST-BE-RIGHT for print)
- **What:** Anything that runs off the edge extends 3 mm (0.125 in) past the trim (the bleed). Text and key elements stay at least 3-5 mm inside the trim. Images are at least 300 ppi at final printed size (line art higher). Colour is converted with the printer's CMYK profile, or spot colours are named; deep blacks for large areas use the printer's rich-black mix; small text stays 100% K.
- **Why:** Trimming is not exact; without bleed you get white slivers, and without a safe margin text gets cut. Low-res images print soft; RGB colours shift when converted late.
- **Check:** Read the document setup (bleed, trim, margins). Compute ppi: image pixels ÷ printed inches. Check the output intent or profile of the PDF and that fonts are embedded.
- **Fix:** Extend backgrounds into the bleed; re-source or re-render low-res images (don't upsample and call it 300); export PDF/X with the printer's profile, or ask the printer.
- **Grade:** Standard (print production; the printer's spec wins).
- **Source:** Adobe InDesign user guide (bleed, slug, printing) [S131]; ask the printer for their spec, which overrides these defaults.

### LAY-10. Whitespace is distributed on purpose (squint for dead zones)
- **What:** Every empty area is either a margin, a gap between groups, or deliberate focal space (room the subject looks or moves into, a quiet field that frames the one message). Related items sit closer to each other than to anything else, so each group reads as one unit. No empty band or block is much larger than the largest intended gap between groups unless it is deliberate and said so. After any image swap, crop change or regenerate, re-review the **whole** layout, not only the changed element: new imagery changes where the space is.
- **Why:** People group by nearness and shared region [S175, S176]; consistent gaps read as structure, a stray large gap as something missing [S177, S178]. This rule is the measure; the idea (active versus dead space) lives in COMP-23.
- **Check:**
  1. **Measure rows:** list the empty horizontal bands between groups. Flag any band larger than about 1.5× the largest intended inter-group gap that isn't marked as deliberate.
  2. **Squint for 2-D dead zones:** blur the piece (or view it at thumbnail size). Look for empty blocks *inside* a row, e.g. between a small item at the left and a small item at the right of the same row. A row scan alone can't see these. Flag any block whose short side exceeds about 1.5× the largest intended gap, unless it is a symmetric flank of a centred group or declared focal space.
  3. **After any image change:** re-run 1 and 2 on the full piece and write one line on what moved.
  `tools/whitespace.py IMAGE [--intended Y0-Y1]` does 1 and 2 and draws a squint sheet; treat its PASS as "review by eye", not as approval.
- **Fix:** Pull each group together, then share out the space between groups evenly; enlarge or regroup the content that sits next to a dead zone (put small items on one line, align them to a shared centre line, let the main element fill its field); move or re-crop the image so the subject sits one gap from the type; or name the space as deliberate in the critique and keep it. Big, deliberate empty fields are valid and often the strongest choice: the flag is for space with no job, not for space itself (COMP-23). Fixing a dead zone never means centring the layout by default.
- **Grade:** Proximity grouping: well supported. The 1.5x dead-zone threshold: self-chosen craft number.
- **Source:** Wertheimer [S175]; Palmer [S176]; NN/g on proximity [S177]; White [S178]; LAY-3; COMP-23 to COMP-25.

### LAY-11. Commit to one axis: symmetric or asymmetric
- **What:** Decide whether the layout is built on a central axis (centred, symmetric, formal) or on edges (flush left or right, asymmetric, active), and keep each group consistent. Mixing centred and flush blocks at random gives many weak alignment lines.
- **Why:** Tschichold's later work defended the centred classical page; his earlier *New Typography* argued for asymmetry; both are coherent systems [S211]. What fails is the unsystematic mix (CORE-5).
- **Check:** List the alignment axes in use (left edges, right edges, centre lines). More than three in one group, or a centred heading over a flush-left block with no reason?
- **Fix:** Pick one axis per group; centre only short, symmetrical material; snap the rest to the grid (LAY-1).
- **Grade:** Craft wisdom.
- **Source:** Tschichold [S211]; Müller-Brockmann [S60]; Lupton [S54]; CORE-5; COMP-17.

### LAY-12. Margins from a system, with the optical centre a little high
- **What:** Derive margins from one rule (a single unit, a ratio, or a classic book canon) and keep them consistent across pages. When a block is centred vertically, place it slightly above the true centre, and make the bottom margin at least as large as the top; equal top and bottom space looks bottom-heavy.
- **Why:** Book canons (Van de Graaf, Tschichold's 2:3 page with margins about 2:3:4:6) give consistent, generous margins [S211]. The slightly high optical centre is an old printing rule [S205] with only a small perceptual basis; evidence and limits: COMP-22.
- **Check:** Measure the four margins. Do they follow one rule? For a vertically centred block, is it at the true centre (often reads low) or a little above (a few percent of the page height)?
- **Fix:** Move the block up slightly; enlarge the bottom margin; set margins from the system, not by eye per page.
- **Grade:** Canons: traditional craft. Optical centre: craft wisdom with a small perceptual basis. "Margins must follow the golden ratio": myth (COMP-16).
- **Source:** Tschichold and the page canons [S211]; Gress on the optical centre [S205]; Drain & Reuter-Lorenz [S264]; LAY-2; COMP-16.

### LAY-13. Group with space and alignment first; add boxes and rules last
- **What:** Make groups with proximity and alignment before reaching for borders, background panels or divider lines. Add a box only where space can't do the job (dense data, mixed content).
- **Why:** A shared boundary is a strong grouping cue that can override proximity [S176], so unnecessary boxes create false groups and clutter. Proximity alone usually suffices [S177, S250].
- **Check:** For each box, rule or panel, imagine it removed: does the grouping still read from space? If yes, the box is decoration.
- **Fix:** Remove the box and widen the gap between groups (LAY-10); keep boxes for real containers.
- **Grade:** Well supported (grouping principles).
- **Source:** Palmer [S176]; NN/g [S177]; Wagemans et al. [S250]; CORE-4; LAY-10.

### LAY-14. Reading patterns are effects to design for, not templates
- **What:** Design for scanning: clear headings, front-loaded words, short groups, and a strong visual hierarchy. Don't place content to fit a "Z-pattern", "F-pattern" or "Gutenberg diagram" template.
- **Why:** Eye-tracking shows the F-shaped scan is what people do with *unformatted* walls of text, and good formatting prevents it [S259]. The other templates are teaching sketches with little direct test.
- **Check:** At blur and at thumbnail, do headings and key words stand out in the order you want? Do the first two words of each line or item carry meaning?
- **Fix:** Add headings, bold key phrases sparingly, front-load words, break text into groups. Use hierarchy (CORE-1), not a template.
- **Grade:** F-pattern as a symptom: well supported. Z, F and Gutenberg templates as layout laws: contested.
- **Source:** Pernice, NN/g [S259]; CORE-1; LAY-3.

### LAY-15. Text over images needs a quiet zone and a contrast check on the worst pixels (MUST-BE-RIGHT where the text carries the message)
- **What:** Place text on an image only over a calm, even area, or add a scrim, overlay or panel. Check contrast against the *worst* part of the background behind the text, not its average.
- **Why:** Busy, uneven backgrounds make text hard to read and can fail contrast at some letters while passing on average [S260]. W3C lists text over background images that fails contrast as a common failure [S260].
- **Check:** Crop the region behind each line of text. Sample its lightest and darkest pixels (for light text, the lightest pixel matters most; for dark text, the darkest) and run `tools/contrast.py` against the text colour: ≥ 4.5:1 (≥ 3:1 for large text). Squint: is the area behind the text busy (strong edges, many tones)?
- **Fix:** Move the text to the calm area, re-crop the image to make one, add a scrim or gradient, or put the text on a solid panel.
- **Grade:** Well supported (WCAG; usability research).
- **Source:** NN/g on text over images and W3C failure F83 [S260]; WCAG [S3]; UI-6; LAY-6.

### LAY-16. Covers: title, image and author name each get their place
- **What:** On a book or album cover, the title has its own clear zone that doesn't fight the focal image, and the author name sits in a balanced position, usually centred on a centred cover, in a colour that reads (often white on a dark picture). A name tucked into a bottom corner of an otherwise centred cover looks like an afterthought. The styling signals the genre: a literary classic and a pulpy young-adult novel are set differently, so check which one the cover says (EN-2 item 8).
- **Why:** In the repo's blind test the owner of the work marked down a cover whose title fought the moon (S35) and a picture-book author name set bottom-left (S46), and read one novel cover as "pulpy YA" and the other as "a true classic" (S40). Internal evidence, one judge.
- **Check:** At thumbnail, does the title read without competing with the main image? Is the author name on the cover's axis (LAY-11) and legible? Name the genre the cover signals in two words: does it match the book?
- **Fix:** Give the title a calm band; move the author name onto the axis, usually centred, and switch it to the better of black or white (CV-10); change type and colour to match the genre (TYPE-10).
- **Grade:** Craft wisdom; the examples are internal evidence (owner taste).
- **Source:** LAY-11; TYPE-10; CV-10; `examples/blind-test/RESULTS.md`.

### LAY-17. Menus, signage and timetables: plain, high contrast, easy to scan
- **What:** Information people scan at a distance and in passing (menu boards, wayfinding, opening times, price lists) works best plain: a clear grid, high contrast, items and prices that line up, sizes that read from where people stand (LAY-7). Plain here is the aim, not "slop" and not a lack of nerve. Energy is a light pass at most (EN-1).
- **Why:** Reading distance sets the type size [S179, S180]; scanning favours clear headings and lined-up items (LAY-14). In batch 5 a balanced, high-contrast menu board without the skill beat the with-skill version, and the owner called it "effective for its job" (S55). Internal evidence, one judge.
- **Check:** From the expected distance (LAY-7), can each item and its price be found in a few seconds? Do prices align? Is any decoration costing legibility?
- **Fix:** Simplify to one grid, raise contrast, align prices, cut decoration before shrinking type.
- **Grade:** Standard for the size rule (LAY-7); the rest is craft wisdom with one internal case.
- **Source:** LAY-7; LAY-14; United States Sign Council Foundation [S179, S180].

### LAY-18. Multi-panel pieces fail as a whole when one panel fails
- **What:** In a step-by-step infographic, a comic strip, a storyboard or a set of icons, every panel is checked on its own (anatomy, objects, text, step order). One broken panel (a wrong hand, a missing step, garbled text) fails the whole piece, however clean the rest.
- **Why:** Readers follow steps in order; one wrong step breaks the instruction. In batch 4 a less dense, readable with-skill hand-washing infographic lost because its third panel failed badly (S43). Internal evidence, one judge.
- **Check:** Crop and check each panel at 2-4x, one line per panel (CHAR-9 for any hands).
- **Fix:** Regenerate or redraw the failed panel only, then re-check the set for consistency (BRAND-6).
- **Grade:** Procedure.
- **Source:** CHAR-9; FP-3; BRAND-6; `examples/blind-test/RESULTS.md`.

---

## Myths

- **"Put text on the thirds lines."** See `core/evidence.md`; the effect is weak. Use the grid and the platform's safe area instead.
- **"72 dpi is for screen."** Screens show pixels; only pixel size matters on screen. The ppi number matters for print only.
- **"One image fits all platforms."** Ratios run from 2:1 to 9:16. Make deliberate crops.
