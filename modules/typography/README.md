# Module: typography

Choosing and setting type anywhere words appear: UI, posters, social cards, decks, covers, banners. Load with `core/`. It goes deeper than UI-1 and UI-2 in `web-ui/`, which stay the short version for screens. Where the two overlap, the numbers agree.

Format: **What / Why / Check / Fix / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults. Most checks are measurements an agent can run on computed styles or on a render.

Evidence in one line: typeface choice matters less than most people think (serif vs sans makes no reliable legibility difference [S111]), while size, measure and spacing make measurable differences [S113, S114, S117]. So spend critique on setting, not on font taste.

---

### TYPE-1. One or two families, each with a job
- **What:** Use one family, or two at most with clearly different jobs (e.g. a display face for headlines, a text face for body). A third is allowed only for a real function such as code or tabular figures.
- **Why:** Each extra family adds visual complexity, the main predictor of low first-impression appeal [S35]. Two faces that are *nearly* alike (two geometric sans) look like an error, not a choice.
- **Check:** List every computed `font-family` (or every face in the file). More than two text families? Two that differ only slightly in the same category?
- **Fix:** Drop to one family with weight and size contrast, or pair faces that differ clearly in one dimension (serif with sans, or condensed with wide) and share a similar x-height. Keep the pair's mood consistent with the brief.
- **Source:** Lupton, *Thinking with Type* [S54]; Google Fonts Knowledge, pairing [S116]; Butterick [S10].

### TYPE-2. Sizes come from one scale
- **What:** All sizes come from a single ratio from the body size. Dense UI: about 1.125 to 1.25. Editorial pages, posters and slides: about 1.25 to 1.618 (big jumps read as deliberate).
- **Why:** Sizes a few percent apart look like mistakes and flatten hierarchy.
- **Check:** Sort every size used. Divide each by the next smaller one. Any neighbouring pair with a ratio under 1.1 (except the same role)? More than about 5-6 sizes on one page?
- **Fix:** Snap each size to the nearest scale step; merge near-duplicates. The golden ratio is one option, not the right one (`core/evidence.md`).
- **Source:** Brown, *More Meaningful Typography* [S55]; Material 3 type scale [S13]; UI-1.

### TYPE-3. Text is big enough to read where it is seen (MUST-BE-RIGHT below the floor)
- **What:** Default: reading text on screen at 16 px CSS or more (17 pt on iOS), captions and labels at 12 px or more. **Blocker:** reading text under 14 px, any meaningful text under 12 px, or (in an image) text whose x-height is under about 6 px at the size the platform shows it (LAY-6).
- **Why:** Reading speed falls sharply below a critical print size [S114]. On websites, larger text (18 px and up in one study) improved readability and comprehension, with no penalty [S113].
- **Check:** Read computed `font-size` for each text role. For images: scale to the display size (e.g. 600 px wide for a phone feed) and measure the x-height in pixels.
- **Fix:** Raise the body size and rebuild the scale from it (TYPE-2); in images, cut words rather than shrink them.
- **Source:** Legge & Bigelow [S114]; Rello et al. [S113]; Apple HIG [S58]; UI-2.

### TYPE-4. Measure: 45-90 characters, about 65 ideal
- **What:** Lines of running text hold about 45-90 characters including spaces. Narrow columns (captions, sidebars) can go to about 30-40.
- **Why:** Long lines make the return sweep hard; very short lines break phrases. Speed studies favour somewhat longer lines than preference does, so the range is a comfort range, not a speed optimum [S112].
- **Check:** At desktop width, count characters on three full lines of a paragraph (or divide container width by the average character width, about 0.5 em for most text faces). **Auto:** `ch` units in CSS give this directly.
- **Fix:** `max-inline-size: 65ch` on text blocks; split wide layouts into columns or widen margins.
- **Source:** Bringhurst [S52]; Butterick, *Line Length* [S12]; Dyson [S112].

### TYPE-5. Leading follows size and measure
- **What:** Body line height about 1.4-1.6 (longer measure needs more). Headlines tighter, about 1.0-1.2. Paragraph spacing larger than line spacing.
- **Why:** Tight leading on long lines makes the eye skip lines; loose leading on headlines breaks the headline into separate lines. Users who need it must be able to set line height to 1.5 and letter spacing to 0.12 em without content breaking.
- **Check:** Read computed `line-height` per role. Does any block of 3+ lines sit below 1.3? Does any headline exceed 1.3? Apply the WCAG text-spacing override (line height 1.5, paragraph spacing 2 em, letter 0.12 em, word 0.16 em): does anything clip or overlap?
- **Fix:** Set line height per role, not one global value; use unitless line heights; avoid fixed-height text boxes.
- **Source:** Butterick [S10, S53]; WCAG 2.1 SC 1.4.12 Text Spacing [S117]; Rello et al. [S113].

### TYPE-6. Track display type tighter, small caps and all-caps looser
- **What:** Large headlines (about 40 px and up) usually need slightly negative tracking (around -0.01 to -0.03 em). All-caps and small labels need positive tracking (about +0.05 to +0.12 em). Body text stays at 0.
- **Why:** Fonts are spaced for text sizes; at display sizes the gaps look loose. Caps have no ascenders or descenders to separate them, so they crowd.
- **Check:** Render the headline at size and squint: are the gaps between letters visibly uneven (e.g. "AV", "To", "LT")? Is any all-caps label at 0 tracking? Is body text tracked at all? (It shouldn't be.)
- **Fix:** Use the font's optical size or display cut if it has one; apply tracking per role; turn on kerning (`font-kerning: normal`). Hand-kern only the visible bad pairs in a logo or headline.
- **Source:** Apple HIG, tracking tables [S58]; Google Fonts Knowledge [S116]; Butterick [S10]; Beier, *Reading Letters* [S115].

### TYPE-7. Hierarchy uses as few signals as needed
- **What:** Each level of hierarchy changes one or two properties (size, weight, colour or case), not all of them. Three levels are enough for most pages; four or more need a reason.
- **Why:** When everything is bold, large and coloured, nothing leads (CORE-1).
- **Check:** Blur test: can you name the first, second and third things read? For each text role, list how it differs from the role below. Three or more differences at once, or none that survives greyscale?
- **Fix:** Remove signals until each level is separated by one strong difference (usually size or weight). Keep colour for meaning.
- **Source:** NN/g, *Visual Hierarchy* [S1]; Lupton [S54]; CORE-1.

### TYPE-8. Typesetting details are right
- **What:** Real quotes and apostrophes (" ' not " '), en dashes for ranges, no double spaces, no widows (one word alone) on headlines, no fake bold or italic, numerals that line up in tables (`tabular-nums`), no text set on a curve or stretched unless the brief asks.
- **Why:** These are the marks readers notice without knowing why; they read as care or the lack of it.
- **Check:** Search the text for straight quotes, `--`, double spaces. Does any headline end with one short word on its own line? Is any face distorted (width not 100%)?
- **Fix:** Replace characters; use `text-wrap: balance` on headlines and `text-wrap: pretty` on paragraphs; load the real weights you use.
- **Source:** Butterick, *Practical Typography* [S10]; Bringhurst [S52].

### TYPE-9. Avoid the generic AI type look
- **What:** Common tells: Inter, Roboto or Poppins for everything with no reason; a huge centred bold headline with a grey subhead under it; gradient-filled text; every heading in title case with an emoji; all text the same weight; three sizes only, a few pixels apart; letter-spaced caps labels on every section.
- **Why:** None is wrong alone. Together they say "no one chose this" (UI-7) and make the work look like everything else [S27, S28].
- **Check:** Count the tells. Two or more: flag. For each typeface, can you name the reason it was chosen (brand, subject, legibility need)? If not, it's a default.
- **Fix:** Take type from the brand guide (BRAND-3). With none, pick a face whose voice suits the subject, then set it carefully (TYPE-2 to TYPE-6). A neutral face set well beats a distinctive face set badly. The choice of face itself is a taste call for the owner of the work.
- **Source:** Anticode [S27]; Superdesign [S28]; UI-7.

### TYPE-10. Pick type from the theme catalogue to suit the genre; don't reuse one face everywhere
- **What:** Match the display face to the brief's genre and tone, using the theme catalogue in [`fonts/CATALOGUE.md`](../../fonts/CATALOGUE.md) (62 free families in 18 themes, each with what it's good for, what to avoid and pairings). Name the theme and the reason in the critique or the log ("pulp comedy cover: Shrikhand title, Cabin author line"). Don't default to the same family across unrelated briefs, and vary type across a set of examples or a portfolio; one face in every piece reads as a house style nobody chose.
- **Why:** Readers consistently attribute personality to typefaces, and to text, so a face whose persona clashes with the content changes how the piece is read [S156, S157]. Choosing on voice is the craft advice too [S54, S116]. Repeating one face across unrelated briefs is the type form of the generic look (TYPE-9).
- **Check:** Which catalogue theme fits the brief's genre and tone? Is the chosen face from it (or is there a stated reason not)? Across the last few pieces, or across a set of examples, does one family recur where the briefs differ? The face's "avoid" line in the catalogue: does this use break it (e.g. a script in all caps, a thin deco face at text size)?
- **Fix:** Pick from the matching theme; pair with a text face from the catalogue's "pairs with" line; then set it carefully (TYPE-2 to TYPE-6). This is a default, not a blocker; the owner of the work can choose otherwise, and a brand guide (BRAND-3) wins over the catalogue.
- **Source:** Brumberger [S156]; Shaikh, Chaparro & Fox [S157]; Lupton [S54]; Google Fonts Knowledge [S116].

---

## Myths

- **"Serifs are more readable in print, sans on screen."** Controlled tests find no reliable difference between serif and sans at normal sizes [S111]. Choose on voice, x-height and spacing, not category.
- **"The ideal line length is exactly 66 characters."** 45-90 is a comfort range. Some studies find faster reading at longer lines, while people still prefer medium ones [S112].
- **"All-caps is unreadable because of word shape."** The word-shape theory is weak; caps read slower mainly because they are less familiar and take more space [S118]. Short caps labels are fine; long caps paragraphs are not.

## Quick measurements

| Check | How | Pass |
|---|---|---|
| Measure | characters per line on 3 lines | 45-90 |
| Scale | neighbouring size ratio | ≥ 1.1, one ratio |
| Body size | computed px | ≥ 16 (web) |
| Leading | line-height ÷ font-size | body 1.4-1.6, display 1.0-1.2 |
| Families | distinct `font-family` | ≤ 2 (+1 functional) |
