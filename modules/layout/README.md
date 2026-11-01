# Module: layout, print and social

Fixed-frame layouts: social cards and posts, link previews, thumbnails, posters, slides and print. Load with `core/`; add `typography/` for any text and `brand/` for anything with a name on it. Web pages that scroll and reflow are `web-ui/`.

Format: **What / Why / Check / Fix / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults.

Why it matters: most social images are first seen as a small tile in a moving feed, where appeal is judged in about 50 ms [S36]. The job of the layout is to survive that glance and the platform's crop.

---

### LAY-1. Build on a grid
- **What:** Divide the frame into columns (and rows for posters and slides), with margins and gutters from one spacing unit. Text blocks and images start and end on grid lines.
- **Why:** Shared edges make a layout read as one ordered thing; near-miss alignments look like errors (CORE-4).
- **Check:** Overlay the grid (or list the left x and top y of every block). Are there edges within about 1% of the frame width of each other that don't match exactly?
- **Fix:** Snap near-misses to the same line. Common starting grids: 12 columns for 16:9, 6 for square and 4:5, 4 for 9:16.
- **Source:** Müller-Brockmann, *Grid Systems* [S60]; UI-4.

### LAY-2. Margins that breathe, and are even
- **What:** Outer margins at least about 5% of the short side (more on posters and covers). Equal on left and right unless the asymmetry is deliberate; nothing important touches the edge by accident.
- **Why:** Content crammed against the frame looks cropped, and platforms round corners and overlay buttons near edges.
- **Check:** Measure the smallest distance from text and key shapes to each edge, in pixels and as a % of the short side.
- **Fix:** Shrink or cut content rather than the margin. Set the margin as a token and use it for every edge.
- **Source:** Müller-Brockmann [S60]; Lupton [S54].

### LAY-3. One focal point, one reading order
- **What:** One element clearly leads (usually the image or headline). Then a short path: headline, support, sign-off (logo or link). On a social card, three text elements is usually the most that works.
- **Why:** A feed tile gets a glance. With two competing focal points, neither lands (CORE-1).
- **Check:** Blur and thumbnail tests (`tools/look.py`). What is seen first, second, third? Is that the order the brief needs? Count text elements.
- **Fix:** Scale up the lead element; cut the rest to the essentials; move secondary text to the post body or caption.
- **Source:** CORE-1; NN/g, *Visual Hierarchy* [S1].

### LAY-4. Export at the platform's size and ratio
- **What:** Use the platform's recommended size and ratio (table below). Export at the full recommended width; never upscale a small render.
- **Why:** Wrong ratios get cropped or padded; small images get blurred or shown as tiny thumbnails.
- **Check:** Read the file's pixel size, ratio and file size against the table.
- **Fix:** Re-render at the right size. Lay out once at the largest size, then make the other crops deliberately, not by auto-crop.
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
- **Source:** [S125, S127, S130]; LAY-2.

### LAY-6. Legible at feed size (MUST-BE-RIGHT for the main message)
- **What:** The main message (headline, or the face or object that is the point) reads when the image is shown at about 400 px wide, a typical phone feed width.
- **Why:** That is the size most people see it at; the full-size file is what only the designer sees.
- **Check:** Scale the export to 400 px wide. Is the headline readable without zoom? Measure its x-height: about 6 px or more (TYPE-3). Does the idea survive the thumbnail test at 200 px wide?
- **Fix:** Fewer, bigger words; stronger value contrast between text and ground (UI-6 ratios apply to text in images too); remove detail that turns to noise.
- **Source:** Lindgaard et al. [S36]; Legge & Bigelow [S114]; UI-6.

### LAY-7. Posters: read at distance, then up close
- **What:** A poster has two reading distances: the far glance (one image and the headline) and the near read (details). Design the far layer first.
- **Why:** People decide whether to approach from across the room; small type can't do that job.
- **Check:** View the poster at about 10% of its size (roughly how a 50 cm-wide poster looks from 5 m). Do the image and headline still read? Is the detail text set together, not scattered?
- **Fix:** Enlarge the headline and simplify the image; group details into one block on the grid.
- **Source:** Müller-Brockmann [S60]; CORE-1.

### LAY-8. Slides: one point each, with signals
- **What:** One message per slide, stated as the title (a sentence, not a topic label). Remove decoration that doesn't explain. Text a room can read: about 24 pt or more at 1920 × 1080, at most about six short lines. Highlight what the speaker is talking about.
- **Why:** People learn more when extraneous material is cut (coherence) and when the key items are signalled; text that duplicates speech word for word can hurt (redundancy) [S132]. Dense slides become documents nobody reads [S133].
- **Check:** Can the slide's point be read from its title alone? Count lines and the smallest size. Is there clip art, a stock photo or a template ornament with no job?
- **Fix:** Rewrite titles as claims; split crowded slides; move detail to speaker notes or a handout.
- **Source:** Mayer, *Multimedia Learning* [S132]; Duarte, *slide:ology* [S133].

### LAY-9. Print files: bleed, resolution, colour (MUST-BE-RIGHT for print)
- **What:** Anything that runs off the edge extends 3 mm (0.125 in) past the trim (the bleed). Text and key elements stay at least 3-5 mm inside the trim. Images are at least 300 ppi at final printed size (line art higher). Colour is converted with the printer's CMYK profile, or spot colours are named; deep blacks for large areas use the printer's rich-black mix; small text stays 100% K.
- **Why:** Trimming is not exact; without bleed you get white slivers, and without a safe margin text gets cut. Low-res images print soft; RGB colours shift when converted late.
- **Check:** Read the document setup (bleed, trim, margins). Compute ppi: image pixels ÷ printed inches. Check the output intent or profile of the PDF and that fonts are embedded.
- **Fix:** Extend backgrounds into the bleed; re-source or re-render low-res images (don't upsample and call it 300); export PDF/X with the printer's profile, or ask the printer.
- **Source:** Adobe InDesign user guide (bleed, slug, printing) [S131]; ask the printer for their spec, which overrides these defaults.

---

## Myths

- **"Put text on the thirds lines."** See `core/evidence.md`; the effect is weak. Use the grid and the platform's safe area instead.
- **"72 dpi is for screen."** Screens show pixels; only pixel size matters on screen. The ppi number matters for print only.
- **"One image fits all platforms."** Ratios run from 2:1 to 9:16. Make deliberate crops.
