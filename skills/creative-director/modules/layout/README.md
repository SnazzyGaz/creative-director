# Module: layout, print and social

Fixed-frame layouts: social cards and posts, link previews, thumbnails, posters, slides and print. Load with `core/`; add `typography/` for any text and `brand/` for anything with a name on it. Web pages that scroll and reflow are `web-ui/`.

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults.

Why it matters: most social images are first seen as a small tile in a moving feed, where appeal is judged in about 50 ms [SRC-36]. The job of the layout is to survive that glance and the platform's crop.

---

### LAY-1. Build on a grid
- **What:** Divide the frame into columns (and rows for posters and slides), with margins and gutters from one spacing unit. Text blocks and images start and end on grid lines.
- **Why:** Shared edges make a layout read as one ordered thing; near-miss alignments look like errors (CORE-4).
- **Check:** Overlay the grid (or list the left x and top y of every block). Any edges that almost match but don't (bands: COMP-24)?
- **Fix:** Snap near-misses to the same line. Common starting grids: 12 columns for 16:9, 6 for square and 4:5, 4 for 9:16.
- **Grade:** Craft wisdom.
- **Source:** Müller-Brockmann, *Grid Systems* [SRC-60]; UI-4.

### LAY-2. Margins that breathe, and are even
- **What:** Outer margins at least about 5% of the short side (more on posters and covers). Equal on left and right unless the asymmetry is deliberate; nothing important touches the edge by accident.
- **Why:** Content crammed against the frame looks cropped; platforms round corners and overlay buttons near edges.
- **Check:** Measure the smallest distance from text and key shapes to each edge, in pixels and as a % of the short side.
- **Fix:** Shrink or cut content rather than the margin. Set the margin as a token and use it for every edge.
- **Grade:** Craft wisdom.
- **Source:** Müller-Brockmann [SRC-60]; Lupton [SRC-54].

### LAY-3. One focal point, one reading order
- **What:** One element clearly leads (usually the image or headline). Then a short path: headline, support, sign-off (logo or link). On a social card, three text elements is usually the most that works.
- **Why:** A feed tile gets a glance. With two competing focal points, neither lands (CORE-1).
- **Check:** Blur and thumbnail tests (`tools/look.py`). What is seen first, second, third? Is that the order the brief needs? Count text elements.
- **Fix:** Scale up the lead element; cut the rest to the essentials; move secondary text to the post body or caption.
- **Grade:** Partly supported (CORE-1).
- **Source:** CORE-1; NN/g, *Visual Hierarchy* [SRC-1].

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
| X post, single image | 1600 × 900 (or 1200 × 675) | 16:9 | Single images from about 2:1 to 3:4 show uncropped on mobile; others are centre-cropped. Up to 4 images. | [SRC-124, SRC-130] |
| X link card (`summary_large_image`) | 1200 × 600 | 2:1 | Min 300 × 157, max 4096 × 4096, under 5 MB; no SVG. | [SRC-123] |
| LinkedIn image post | 1080 wide; 1080 × 1080 or 1080 × 1350 | 3:1 to 4:5 | Under 5 MB; outside the range is centre-cropped. | [SRC-126] |
| LinkedIn link preview | 1200 × 627 | 1.91:1 | Minimum for the large preview. | [SRC-126] |
| Instagram feed | 1080 × 1350 | 4:5 | 3:4 (1080 × 1440) stays uncropped when posted in the app; the profile grid shows 3:4, trimming about 34 px off each side of a 4:5 post. | [SRC-125, SRC-130] |
| Instagram story / reel | 1080 × 1920 | 9:16 | Keep text out of roughly the top 14%, bottom 35%, sides 6% (practitioner guidance). | [SRC-130] |
| YouTube thumbnail | 3840 × 2160 recommended; 1280 × 720 is fine | 16:9 | Min 640 wide; under 2 MB from mobile, 50 MB from desktop. The duration badge sits bottom right. | [SRC-127] |
| GitHub social preview | 1280 × 640 | 2:1 | Under 1 MB; PNG, JPG or GIF. Uploaded by hand in repo Settings. | [SRC-128] |
| Open Graph (`og:image`, Facebook and most chat apps) | 1200 × 630 | 1.91:1 | Min 600 × 315 for the large preview; set `og:image:width` and `height`. | [SRC-129] |

### LAY-5. Key content inside the safe area (MUST-BE-RIGHT)
- **What:** Text, faces, logos and the focal point sit where no crop, rounded corner, avatar, button, caption bar or duration badge can cover them.
- **Why:** A headline cut off by the grid crop or a play badge makes the piece fail at its one job.
- **Check:** Draw the platform's crops: centre crops to 1:1, 3:4 and 1.91:1 for reused images; the 9:16 overlay zones; the thumbnail badge zone. Does any key element cross a line?
- **Fix:** Pull key elements towards the centre; keep a margin of at least 6-8% of the short side free of text; make separate crops instead of one compromise.
- **Grade:** Standard (platform specs).
- **Source:** [SRC-125, SRC-127, SRC-130]; LAY-2.

### LAY-6. Legible at feed size (MUST-BE-RIGHT for the main message)
- **What:** The main message (headline, or the face or object that is the point) reads when the image is shown at about 400 px wide, a typical phone feed width.
- **Why:** That is the size most people see it at; the full-size file is what only the designer sees.
- **Check:** Scale the export to 400 px wide. Is the headline readable without zoom? Measure its x-height: about 6 px or more (TYPE-3). Does the idea survive the thumbnail test at 200 px wide?
- **Fix:** Fewer, bigger words; stronger value contrast between text and ground (UI-6 ratios apply to text in images too); remove detail that turns to noise.
- **Grade:** Partly supported (legibility research); the feed-size test is craft.
- **Source:** Lindgaard et al. [SRC-36]; Legge & Bigelow [SRC-114]; UI-6.

### LAY-7. Posters: read at distance, then up close
- **What:** A poster has two reading distances: the far glance (one image and the headline) and the near read (details). Design the far layer first.
- **Why:** People decide whether to approach from across the room; small type can't do that job.
- **Check:** View the poster at about 10% of its size (roughly how a 50 cm-wide poster looks from 5 m). Do the image and headline still read? Is the detail text set together, not scattered?
  **Signage and A-boards:** note the printed size and reading distances (a pavement board: headline and price from 3-5 m, body from about 1-1.5 m); convert each key line's cap height to millimetres at print size. A practical working minimum is cap height ≈ distance ÷ 250 (12-20 mm for 3-5 m). The sign industry's best-case figure, head-on in good light, is about distance ÷ 360; signs seen at an angle or in passing need far more, about distance ÷ 120 [SRC-179, SRC-180]. Report each line as "reads to X m".
- **Fix:** Enlarge the headline and simplify the image; group details into one block on the grid. On signage, cut words before shrinking the type that must read from the pavement.
- **Grade:** Standard (sign-industry guidance) for the size rule; the two-distance test is craft.
- **Source:** Müller-Brockmann [SRC-60]; CORE-1; United States Sign Council Foundation [SRC-179, SRC-180].

### LAY-8. Slides: one point each, with signals
- **What:** One message per slide, stated as the title (a sentence, not a topic label). Remove decoration that doesn't explain. Text a room can read: about 24 pt or more at 1920 × 1080, at most about six short lines. Highlight what the speaker is talking about.
- **Why:** People learn more when extraneous material is cut (coherence) and when the key items are signalled; text that duplicates speech word for word can hurt (redundancy) [SRC-132]. Dense slides become documents nobody reads [SRC-133].
- **Check:** Can the slide's point be read from its title alone? Count lines and the smallest size. Is there clip art, a stock photo or a template ornament with no job?
- **Fix:** Rewrite titles as claims; split crowded slides; move detail to speaker notes or a handout.
- **Grade:** Partly supported (multimedia-learning experiments [SRC-132]).
- **Source:** Mayer, *Multimedia Learning* [SRC-132]; Duarte, *slide:ology* [SRC-133].

### LAY-9. Print files: bleed, resolution, colour (MUST-BE-RIGHT for print)
- **What:** Anything that runs off the edge extends 3 mm (0.125 in) past the trim (the bleed). Text and key elements stay at least 3-5 mm inside the trim. Images are at least 300 ppi at final printed size (line art higher). Colour is converted with the printer's CMYK profile, or spot colours are named; deep blacks for large areas use the printer's rich-black mix; small text stays 100% K.
- **Why:** Trimming is not exact; without bleed you get white slivers, and without a safe margin text gets cut. Low-res images print soft; RGB colours shift when converted late.
- **Check:** Read the document setup (bleed, trim, margins). Compute ppi: image pixels ÷ printed inches. Check the output intent or profile of the PDF and that fonts are embedded.
- **Fix:** Extend backgrounds into the bleed; re-source or re-render low-res images (don't upsample and call it 300); export PDF/X with the printer's profile, or ask the printer.
- **Grade:** Standard (print production; the printer's spec wins).
- **Source:** Adobe InDesign user guide (bleed, slug, printing) [SRC-131]; ask the printer for their spec, which overrides these defaults.

### LAY-10. Whitespace is distributed on purpose (squint for dead zones)
- **What:** Every empty area is either a margin, a gap between groups, or deliberate focal space (room the subject looks or moves into, a quiet field that frames the one message). Related items sit closer to each other than to anything else, so each group reads as one unit. No empty band or block is much larger than the largest intended gap between groups unless it is deliberate and said so. After any image swap, crop change or regenerate, re-review the **whole** layout, not only the changed element: new imagery changes where the space is.
- **Why:** People group by nearness and shared region [SRC-175, SRC-176]; consistent gaps read as structure, a stray large gap as something missing [SRC-177, SRC-178]. This rule is the measure; the idea (active versus dead space) lives in COMP-23.
- **Check:**
  1. **Measure rows:** list the empty horizontal bands between groups. Flag any band larger than about 1.5× the largest intended inter-group gap that isn't marked as deliberate.
  2. **Squint for 2-D dead zones:** blur the piece and look for empty blocks *inside* a row (a small item left, a small item right), which a row scan misses. Flag any block whose short side exceeds about 1.5× the largest intended gap, unless it flanks a centred group or is declared focal space.
  3. **After any image change:** re-run 1 and 2 on the full piece and write one line on what moved.
  `tools/whitespace.py IMAGE [--intended Y0-Y1]` does 1 and 2 and draws a squint sheet; treat its PASS as "review by eye", not as approval.
- **Fix:** Pull each group together, then share the space between groups evenly; enlarge or regroup content next to a dead zone; move or re-crop the image so the subject sits one gap from the type; or name the space as deliberate and keep it. Big deliberate fields are valid and often strongest: the flag is for space with no job (COMP-23), and fixing it never means centring by default.
- **Grade:** Proximity grouping: well supported. The 1.5x dead-zone threshold: self-chosen craft number.
- **Source:** Wertheimer [SRC-175]; Palmer [SRC-176]; NN/g on proximity [SRC-177]; White [SRC-178]; LAY-3; COMP-23 to COMP-25.

### LAY-11. Commit to one axis: symmetric or asymmetric
- **What:** Decide whether the layout is built on a central axis (centred, symmetric, formal) or on edges (flush left or right, asymmetric, active), and keep each group consistent. Mixing centred and flush blocks at random gives many weak alignment lines.
- **Why:** Tschichold's later work defended the centred classical page; his earlier *New Typography* argued for asymmetry; both are coherent systems [SRC-211]. What fails is the unsystematic mix (CORE-5).
- **Check:** List the alignment axes in use (left edges, right edges, centre lines). More than three in one group, or a centred heading over a flush-left block with no reason?
- **Fix:** Pick one axis per group; centre only short, symmetrical material; snap the rest to the grid (LAY-1).
- **Grade:** Craft wisdom.
- **Source:** Tschichold [SRC-211]; Müller-Brockmann [SRC-60]; Lupton [SRC-54]; CORE-5; COMP-17.

### LAY-12. Margins from a system, with the optical centre a little high
- **What:** Derive margins from one rule (a single unit, a ratio, or a classic book canon) and keep them consistent across pages. When a block is centred vertically, place it slightly above the true centre, and make the bottom margin at least as large as the top; equal top and bottom space looks bottom-heavy.
- **Why:** Book canons (Van de Graaf, Tschichold's 2:3 page with margins about 2:3:4:6) give consistent, generous margins [SRC-211]. The slightly high optical centre is an old printing rule [SRC-205] with only a small perceptual basis; evidence and limits: COMP-22.
- **Check:** Measure the four margins. Do they follow one rule? For a vertically centred block, is it at the true centre (often reads low) or a little above (a few percent of the page height)?
- **Fix:** Move the block up slightly; enlarge the bottom margin; set margins from the system, not by eye per page.
- **Grade:** Canons: traditional craft. Optical centre: craft wisdom with a small perceptual basis. "Margins must follow the golden ratio": myth (COMP-16).
- **Source:** Tschichold and the page canons [SRC-211]; Gress on the optical centre [SRC-205]; Drain & Reuter-Lorenz [SRC-264]; LAY-2; COMP-16.

### LAY-13. Group with space and alignment first; add boxes and rules last
- **What:** Make groups with proximity and alignment before reaching for borders, background panels or divider lines. Add a box only where space can't do the job (dense data, mixed content).
- **Why:** A shared boundary is a strong grouping cue that can override proximity [SRC-176], so unnecessary boxes create false groups and clutter. Proximity alone usually suffices [SRC-177, SRC-250].
- **Check:** For each box, rule or panel, imagine it removed: does the grouping still read from space? If yes, the box is decoration.
- **Fix:** Remove the box and widen the gap between groups (LAY-10); keep boxes for real containers.
- **Grade:** Well supported (grouping principles).
- **Source:** Palmer [SRC-176]; NN/g [SRC-177]; Wagemans et al. [SRC-250]; CORE-4; LAY-10.

### LAY-14. Reading patterns are effects to design for, not templates
- **What:** Design for scanning: clear headings, front-loaded words, short groups, and a strong visual hierarchy. Don't place content to fit a "Z-pattern", "F-pattern" or "Gutenberg diagram" template.
- **Why:** Eye-tracking shows the F-shaped scan is what people do with *unformatted* walls of text, and good formatting prevents it [SRC-259]. The other templates are teaching sketches with little direct test.
- **Check:** At blur and at thumbnail, do headings and key words stand out in the order you want? Do the first two words of each line or item carry meaning?
- **Fix:** Add headings, bold key phrases sparingly, front-load words, break text into groups. Use hierarchy (CORE-1), not a template.
- **Grade:** F-pattern as a symptom: well supported. Z, F and Gutenberg templates as layout laws: contested.
- **Source:** Pernice, NN/g [SRC-259]; CORE-1; LAY-3.

### LAY-15. Text over images needs a quiet zone and a contrast check on the worst pixels (MUST-BE-RIGHT where the text carries the message)
- **What:** Place text on an image only over a calm, even area, or add a scrim, overlay or panel. Check contrast against the *worst* part of the background behind the text, not its average.
- **Why:** Busy, uneven backgrounds make text hard to read and can fail contrast at some letters while passing on average [SRC-260]. W3C lists text over background images that fails contrast as a common failure [SRC-260].
- **Check:** Crop the region behind each line of text. Sample its lightest and darkest pixels (for light text, the lightest pixel matters most; for dark text, the darkest) and run `tools/contrast.py` against the text colour: ≥ 4.5:1 (≥ 3:1 for large text). Squint: is the area behind the text busy (strong edges, many tones)?
- **Fix:** Move the text to the calm area, re-crop the image to make one, add a scrim or gradient, or put the text on a solid panel.
- **Grade:** Well supported (WCAG; usability research).
- **Source:** NN/g on text over images and W3C failure F83 [SRC-260]; WCAG [SRC-3]; UI-6; LAY-6.

### LAY-16. Covers: title, image and author name each get their place, and the cover signals its genre
- **What:** The title has its own clear zone that doesn't fight the focal image. The author name sits on the cover's axis (LAY-11), not tucked into a corner as an afterthought, and reads clearly: contrast measured on the worst pixels behind it, never left to busy texture such as grass, foliage or cloud (LAY-15). Type and image signal the genre and tone the book really has (EN-2 item 8).
- **Why:** Covers are read at thumbnail first. In the blind test the owner marked down a title fighting the moon (S35), an author name tucked bottom-left (S46) and one lost in grass (S101), preferred a central title (S80), and read genre from styling (S40).
- **Check:** At thumbnail, does the title read without competing? Is the author name on the axis, and does `tools/contrast.py` on its worst background pixels give ≥ 4.5:1 (≥ 3:1 large)? Name the genre the cover signals in two words: does it match the book?
- **Fix:** Give the title a calm band; move the name onto the axis and a calm area or scrim, in the better of black or white (CV-10); match type and colour to the genre (TYPE-10).
- **Grade:** Well supported for the contrast check (WCAG, LAY-15); placement and genre are craft wisdom, internal evidence, one judge.
- **Source:** LAY-11; LAY-15; TYPE-10; CV-10; `examples/blind-test/RESULTS.md`.

### LAY-17. Scanned information is plain, high contrast and lined up
- **What:** Anything read at a distance or in passing (menus, signage, timetables, price lists, opening times) works best plain: one grid, high contrast, items and values lined up, sizes that read from where people stand (LAY-7). Plain is the aim here, not a lack of nerve; energy is a light pass at most (EN-1).
- **Why:** Reading distance sets the type size [SRC-179, SRC-180]; scanning favours clear headings and aligned items (LAY-14). E.g. a plain, high-contrast menu board beat a livelier one as "effective for its job" (S55, internal evidence, one judge).
- **Check:** From the expected distance, can each item and its value be found in a few seconds? Do values align? Is decoration costing legibility?
- **Fix:** One grid, more contrast, aligned values; cut decoration before shrinking type.
- **Grade:** Standard for the size rule (LAY-7); the rest is craft wisdom, one internal case.
- **Source:** LAY-7; LAY-14; United States Sign Council Foundation [SRC-179, SRC-180].

### LAY-18. Multi-panel pieces: every panel checked, each one different, the set one flow
- **What:** In a step-by-step sheet, timeline, comic strip, storyboard or icon set, every panel is checked on its own (anatomy, objects, text, order): one broken panel fails the whole piece, however clean the rest. Each panel or period shows what is specific to it (where the cuff sits, what the dial reads), with its own frame, colour band or icon; never the same picture repeated. Visible connectors (arrows, a path, a timeline spine) carry the eye from one to the next. People, objects and setting stay the same throughout. (Merges the former INF-3.)
- **Why:** Readers follow steps in order; one wrong step breaks the instruction. E.g. a broken third panel sank a readable hand-washing sheet (S43); one image repeated in every panel lost as "repetitive, wasteful" (S64); framing told periods apart where the other read "samey" (S78); transitional flow read better (S75); stable characters won (S59). Internal evidence, one judge.
- **Check:** Crop each panel at 2-4x, one line per panel (CHAR-9 for hands): what does it show that the others don't? Same person, same object? Cover the labels: can you still tell the steps apart? Follow the connectors start to end without a jump.
- **Fix:** Regenerate or redraw the failed panel only, then re-check the set (BRAND-6); give each step its own framing or colour; draw the path between them.
- **Grade:** Procedure (checking every panel); differentiation and flow are craft wisdom, internal evidence, one judge.
- **Source:** CHAR-9; FP-3; BRAND-6; `examples/blind-test/RESULTS.md`.

### LAY-19. Charts, maps and routes are drawn from the data in code (MUST-BE-RIGHT where numbers or a route carry the message)
- **What:** Never trust an image model for numbers, bar lengths, scales or route geometry. Draw the chart or route from the data in code (`tools/datagraphic.py`, SVG or matplotlib), styled as part of the piece, never as a panel pasted on: the integration recipes and checks are INF-1 in [`infographics.md`](infographics.md), which every infographic loads. A loop route visibly closes at start = finish; every crossing of water or a road shows a bridge.
- **Why:** Distorted bars change how big readers judge a difference [SRC-336]. In batch 6 no generated chart was to scale (small bars overstated by up to 12.5 points) and neither route map closed its loop or showed its bridge; in batch 7 a generated donut was 8 points off.
- **Check:** `datagraphic.py check-bars` on the final image: every bar within 2% of its data share (`--scale-max` for a visible track). Routes: the tool reports a closed loop and bridges = crossings; labels sit by their places, in order.
- **Fix:** Redraw from the data; never edit generated bars.
- **Grade:** Well supported for honest scales [SRC-336]; the generator failures are internal evidence.
- **Source:** Pandey et al. [SRC-336]; LAY-18; `examples/blind-test/RESULTS.md`.

---

## Myths

- **"Put text on the thirds lines."** See `core/evidence.md`; the effect is weak. Use the grid and the platform's safe area instead.
- **"72 dpi is for screen."** Screens show pixels; only pixel size matters on screen. The ppi number matters for print only.
- **"One image fits all platforms."** Ratios run from 2:1 to 9:16. Make deliberate crops.
