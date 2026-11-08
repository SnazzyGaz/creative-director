# Module: typography

Choosing and setting type anywhere words appear: UI, posters, social cards, decks, covers, banners. Load with `core/`. It is the one home for type numbers; `web-ui/` points here (former UI-1 and UI-2 merged into TYPE-2 to TYPE-5 and TYPE-13).

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults. Most checks are measurements an agent can run on computed styles or on a render.

Evidence in one line: serif versus sans makes no reliable legibility difference [SRC-111], while size, measure and spacing do [SRC-113, SRC-114, SRC-117]. Spend critique on setting and on whether the face belongs to this job (TYPE-10): voice and fit are not the same as a serif-versus-sans taste argument.

---

### TYPE-1. One or two families, each with a job
- **What:** Use one family, or two at most with clearly different jobs (e.g. a display face for headlines, a text face for body). A third is allowed only for a real function such as code or tabular figures.
- **Why:** Each extra family adds visual complexity, the main predictor of low first-impression appeal [SRC-35]. Two faces that are *nearly* alike (two geometric sans) look like an error, not a choice.
- **Check:** List every computed `font-family` (or every face in the file). More than two text families? Two that differ only slightly in the same category?
- **Fix:** Drop to one family with weight and size contrast, or pair faces that differ clearly in one dimension (serif with sans, or condensed with wide) and share a similar x-height. Keep the pair's mood consistent with the brief.
- **Grade:** Craft wisdom.
- **Source:** Lupton, *Thinking with Type* [SRC-54]; Google Fonts Knowledge, pairing [SRC-116]; Butterick [SRC-10].

### TYPE-2. Sizes come from one scale
- **What:** All sizes come from a single ratio from the body size. Dense UI: about 1.125 to 1.25. Editorial pages, posters and slides: about 1.25 to 1.618 (big jumps read as deliberate).
- **Why:** Sizes a few percent apart look like mistakes and flatten hierarchy.
- **Check:** List every computed size and weight. Sort the sizes. Divide each by the next smaller one. Any neighbouring pair with a ratio under 1.1 (except the same role)? More than about 5-6 sizes on one page?
- **Fix:** Snap each size to the nearest scale step; merge near-duplicates. The golden ratio is one option, not the right one (`core/evidence.md`).
- **Grade:** Craft wisdom.
- **Source:** Brown, *More Meaningful Typography* [SRC-55]; NN/g (about 3 sizes) [SRC-1]; *Every Layout* (one ratio for type and space) [SRC-56].

### TYPE-3. Text is big enough to read where it is seen (MUST-BE-RIGHT below the floor)
- **What:** Default: reading text on screen at 16 px CSS or more (17 pt on iOS), captions and labels at 12 px or more. **Blocker:** reading text under 14 px, any meaningful text under 12 px, or (in an image) text whose x-height is under about 6 px at the size the platform shows it (LAY-6).
- **Why:** Reading speed falls sharply below a critical print size [SRC-114]. On websites, larger text (18 px and up in one study) improved readability and comprehension, with no penalty [SRC-113].
- **Check:** Read computed `font-size` for each text role. For images: scale to the display size (e.g. 600 px wide for a phone feed) and measure the x-height in pixels.
- **Fix:** Raise the body size and rebuild the scale from it (TYPE-2); in images, cut words rather than shrink them.
- **Grade:** Partly supported (reading research); platform minimums are Standard.
- **Source:** Legge & Bigelow [SRC-114]; Rello et al. [SRC-113]; Apple HIG [SRC-58].

### TYPE-4. Measure: 45-90 characters, about 65 ideal
- **What:** Lines of running text hold about 45-90 characters including spaces. Narrow columns (captions, sidebars) can go to about 30-40.
- **Why:** Long lines make the return sweep hard; very short lines break phrases. Speed studies favour somewhat longer lines than preference does, so the range is a comfort range, not a speed optimum [SRC-112].
- **Check:** At desktop width, count characters on three full lines of a paragraph (or divide container width by the average character width, about 0.5 em for most text faces). **Auto:** `ch` units in CSS give this directly.
- **Fix:** `max-inline-size: 65ch` on text blocks; split wide layouts into columns or widen margins.
- **Grade:** Partly supported (speed and preference studies disagree; the range is a comfort range).
- **Source:** Bringhurst [SRC-52]; Butterick, *Line Length* [SRC-12]; Dyson [SRC-112].

### TYPE-5. Leading follows size and measure
- **What:** Body line height about 1.3-1.5, up to about 1.6 on long measures. Headlines tighter, about 1.0-1.2. Paragraph spacing larger than line spacing.
- **Why:** Tight leading on long lines makes the eye skip lines; loose leading on headlines breaks the headline into separate lines. Users who need it must be able to set line height to 1.5 and letter spacing to 0.12 em without content breaking.
- **Check:** Read computed `line-height` per role. Does any block of 3+ lines sit below 1.3? Does any headline exceed 1.3? Apply the WCAG text-spacing override (line height 1.5, paragraph spacing 2 em, letter 0.12 em, word 0.16 em): does anything clip or overlap?
- **Fix:** Set line height per role, not one global value; use unitless line heights; avoid fixed-height text boxes.
- **Grade:** Craft wisdom; the WCAG text-spacing override is Standard.
- **Source:** Butterick [SRC-10, SRC-53]; WCAG 2.1 SC 1.4.12 Text Spacing [SRC-117]; Rello et al. [SRC-113].

### TYPE-6. Track display type tighter, small caps and all-caps looser
- **What:** Large headlines (about 40 px and up) usually need slightly negative tracking (around -0.01 to -0.03 em). All-caps and small labels need positive tracking (about +0.05 to +0.12 em). Body text stays at 0.
- **Why:** Fonts are spaced for text sizes; at display sizes the gaps look loose. Caps have no ascenders or descenders to separate them, so they crowd.
- **Check:** Render the headline at size and squint: are the gaps between letters visibly uneven (e.g. "AV", "To", "LT")? Is any all-caps label at 0 tracking? Is body text tracked at all? (It shouldn't be.)
- **Fix:** Use the font's optical size or display cut if it has one; apply tracking per role; turn on kerning (`font-kerning: normal`). Hand-kern only the visible bad pairs in a logo or headline.
- **Grade:** Craft wisdom.
- **Source:** Apple HIG, tracking tables [SRC-58]; Google Fonts Knowledge [SRC-116]; Butterick [SRC-10]; Beier, *Reading Letters* [SRC-115].

### TYPE-7. Hierarchy uses as few signals as needed
- **What:** Each level of hierarchy changes one or two properties (size, weight, colour or case), not all of them. Three levels are enough for most pages; four or more need a reason.
- **Why:** When everything is bold, large and coloured, nothing leads (CORE-1).
- **Check:** Blur test: can you name the first, second and third things read? For each text role, list how it differs from the role below. Three or more differences at once, or none that survives greyscale? On a poster, cover or label: have neighbouring display lines flattened to one face and one alignment (TYPE-15)?
- **Fix:** Remove redundant signals until each level is separated by one strong difference (usually size or weight). Keep colour for meaning. On designed surfaces, a change of scale or style between lines is hierarchy, not clutter.
- **Grade:** Craft wisdom.
- **Source:** NN/g, *Visual Hierarchy* [SRC-1]; Lupton [SRC-54]; CORE-1.

### TYPE-8. Typesetting details are right
- **What:** Real quotes and apostrophes (" ' not " '), en dashes for ranges, no double spaces, no widows (one word alone) on headlines, no fake bold or italic, numerals that line up in tables (`tabular-nums`), no text set on a curve or stretched unless the brief asks.
- **Why:** These are the marks readers notice without knowing why; they read as care or the lack of it.
- **Check:** Search the text for straight quotes, `--`, double spaces. Does any headline end with one short word on its own line? Is any face distorted (width not 100%)?
- **Fix:** Replace characters; use `text-wrap: balance` on headlines and `text-wrap: pretty` on paragraphs; load the real weights you use.
- **Grade:** Craft wisdom (typographic convention).
- **Source:** Butterick, *Practical Typography* [SRC-10]; Bringhurst [SRC-52].

### TYPE-9. Avoid the generic AI type look
- **What:** Common tells: Inter, Roboto or Poppins for everything with no reason; a huge centred bold headline with a grey subhead under it; gradient-filled text; every heading in title case with an emoji; all text the same weight; three sizes only, a few pixels apart; letter-spaced caps labels on every section; a respectable default serif or sans chosen because it will set cleanly, with no named reason it belongs to this job; a photograph with a title parked in a safe band and the facts lined up or split into opposite corners.
- **Why:** None is wrong alone. Together they say "no one chose this" (UI-7) and make the work look like everything else [SRC-27, SRC-28].
- **Check:** Count the tells. Two or more: flag. For each typeface, can you name the reason it was chosen (brand, subject, legibility need)? If not, it's a default.
- **Fix:** Take type from the brand guide (BRAND-3). With none, pick a face whose voice suits the subject, then set it carefully (TYPE-2 to TYPE-6). A neutral face set well beats a distinctive face set badly. The choice of face itself is a taste call for the owner of the work.
- **Grade:** Craft wisdom (practitioner write-ups).
- **Source:** Anticode [SRC-27]; Superdesign [SRC-28]; UI-7.

### TYPE-10. Pick type from the theme catalogue to suit the genre; don't reuse one face everywhere
- **What:** Match the display face to the brief's genre and tone, using the theme catalogue in [`fonts/CATALOGUE.md`](../../fonts/CATALOGUE.md) (107 free families in 29 themes, each with what it's good for, what to avoid, pairings and mood tags; a "By mood" index lists families per mood); shortlist with `python3 tools/font_find.py --mood ... --genre ...` rather than reading the whole catalogue. Name the theme and the reason in the critique or the log ("pulp comedy cover: Shrikhand title, Cabin author line"). Match the title's loudness to the mood as well: a cold, measured thriller wants a quieter, tighter title than a fun run (owner's note on a batch 5 crime cover, S51). Don't pick a face because it will overlay cleanly: hone the choice to this job's purpose and fit (a playbill, a cider label and a quiet cookbook should not share one safe pair). Don't default to the same family across unrelated briefs, and vary type across a set of examples or a portfolio; repeating one overlay pair (a display serif plus a sans) is the same fault as reusing one face.
- **Why:** Readers consistently attribute personality to typefaces, and to text, so a face whose persona clashes with the content changes how the piece is read [SRC-156, SRC-157]. Choosing on voice is the craft advice too [SRC-54, SRC-116]. Repeating one face across unrelated briefs is the type form of the generic look (TYPE-9).
- **Check:** Which catalogue theme fits the brief's genre and tone? Is the chosen face from it (or is there a stated reason not)? Across the last few pieces, or across a set of examples, does one family recur where the briefs differ? The face's "avoid" line in the catalogue: does this use break it (e.g. a script in all caps, a thin deco face at text size)?
- **Fix:** Pick from the matching theme; pair with a text face from the catalogue's "pairs with" line; then set it carefully (TYPE-2 to TYPE-6). This is a default, not a blocker; the owner of the work can choose otherwise, and a brand guide (BRAND-3) wins over the catalogue.
- **Grade:** Partly supported (type-personality studies [SRC-156, SRC-157]).
- **Source:** Brumberger [SRC-156]; Shaikh, Chaparro & Fox [SRC-157]; Lupton [SRC-54]; Google Fonts Knowledge [SRC-116].

### TYPE-11. Vertical space in measured intervals
- **What:** Space between lines, paragraphs, headings and blocks comes from one unit (usually the body leading) and its multiples or simple fractions. Space above a heading is larger than below it, so the heading belongs to what follows.
- **Why:** Bringhurst: add and delete vertical space in measured intervals [SRC-212]. Consistent spacing reads as order (CORE-9); the heading rule is proximity (CORE-4).
- **Check:** List the vertical gaps (in px or pt). Are they multiples or simple fractions of the leading? Is each heading closer to its own text than to the previous block?
- **Fix:** Round gaps to the unit; move space from below headings to above them.
- **Grade:** Craft wisdom, supported by grouping research for the heading rule.
- **Source:** Bringhurst, 2.2.2 [SRC-212]; Butterick [SRC-10]; CORE-4; TYPE-5.

### TYPE-12. Paragraphs: one signal, not two
- **What:** Mark new paragraphs with an indent *or* a space between them, not both. With indents, set the first paragraph after a heading flush left, and indent the rest by at least one en (about half the type size); one em is common.
- **Why:** Both signals together over-mark the break and waste space. A first-paragraph indent marks a break where none is needed [SRC-212].
- **Check:** Are paragraphs both indented and spaced? Is the first paragraph after a heading indented?
- **Fix:** Choose one signal; remove the first-paragraph indent.
- **Grade:** Craft wisdom (typographic convention).
- **Source:** Bringhurst, 2.3.1-2.3.2 [SRC-212]; Butterick [SRC-53].

### TYPE-13. Rag and hyphenation: an even edge without holes
- **What:** Body text, and anything on a narrow measure or on the web, is set flush left, ragged right; justify only with good hyphenation and spacing, so there are no rivers or wide word gaps. A ragged edge should look like a gentle, uneven ripple, not a staircase or a big notch. Hyphenation: at least two letters before the break and three after, and no more than three hyphenated lines in a row.
- **Why:** Justified narrow columns force uneven word spaces; Bringhurst gives the hyphenation limits [SRC-212].
- **Check:** In justified text, squint for white rivers. In ragged text, look at the right edge: any line much shorter than its neighbours, or a regular pattern of short-long? Count consecutive hyphens.
- **Fix:** Switch to ragged right; turn on hyphenation with sensible limits; rewrite or rebreak the worst lines in display text by hand.
- **Grade:** Craft wisdom.
- **Source:** Bringhurst, 2.1.3, 2.4.1, 2.4.3 [SRC-212]; Butterick [SRC-53]; TYPE-8.

### TYPE-14. Optical adjustments in display type
- **What:** At display sizes, adjust by eye where the geometry is right but the look is wrong: hang quotation marks and bullets into the margin so the text edge stays straight; nudge round or pointed letters (O, A, V) past the line so they look aligned; space capitals and small caps a little wider; use titling (lining) figures with capitals and text (old-style) figures in running text where the font has them.
- **Why:** Round and pointed shapes look smaller than square ones of the same measured size, which is why typefaces are drawn with overshoot; the same correction applies to alignment when type is set large. Bringhurst gives the conventions for capitals and figures [SRC-212]; Gress covers optical corrections in letter design and spacing for even tone [SRC-205].
- **Check:** Zoom to the left edge of headlines and pull quotes: does punctuation or an O make the edge look indented? Do caps look cramped?
- **Fix:** Hang punctuation; nudge round letters; letterspace caps (TYPE-6); switch figure style.
- **Grade:** Craft wisdom (well established in type design).
- **Source:** Bringhurst, 2.1.6, 3.2.1 [SRC-212]; Gress [SRC-205]; TYPE-6; TYPE-8.


### TYPE-15. Type and graphic marks are structure, not garnish
- **What:** On posters, covers, labels, tickets and other designed surfaces, type is page architecture, not a caption parked on a picture. Neighbouring lines change scale and style enough to form a rhythm (TYPE-2, TYPE-7). Simple graphic marks — rules, banners, badges, holding shapes, small ornaments — are structure when they bound a group, lead the eye or balance a field. Do this without adding a single extra word (CD-7). Setting type in code over textless art is fine for locked wording; it is not a reason to default to "title in a safe band, facts in opposite corners." An emblem (a pebble, a sprig, a badge) stays emblem-sized; it should not swell into a large study that pushes the words aside. A label, tin or ticket should still read as that object unless the brief asked for a flat artwork.
- **Why:** Refusing invented slogans is right; throwing away the graphic system those words sat in is the fail. In comparison proofs the owner of the work found with-skill pieces flattening to a picture plus type, while without-skill pieces used type changeups and graphic marks as structure, and chose faces and colours that belonged to the job.
- **Check:** Squint. Is this a designed page, or a photograph with a caption? Do neighbouring display lines differ by a deliberate scale or style step? Point at each rule, banner, badge or ornament: does it bound, lead or balance, or is it missing because the words were cleaned? If you stripped invented copy, did the lockup, rules and grouping go with it? Are emblems still small enough to sit as marks?
- **Fix:** Rebuild the type system with only the allowed words. Change scale and style between roles. Add a rule, banner or holding shape where it groups, points or balances. Keep emblems small. Restore the object (label on a bottle, type on a tin, ticket as a ticket) if the brief is for that object. Do not invent copy to fill a mark.
- **Grade:** Craft wisdom; the comparison cases are internal evidence, one judge.
- **Source:** Müller-Brockmann [SRC-60]; Lupton [SRC-54]; TYPE-2; TYPE-7; TYPE-10; LAY-7; CD-7; CORE-1.

---

## Myths

- **"Serifs are more readable in print, sans on screen."** Controlled tests find no reliable difference between serif and sans at normal sizes [SRC-111]. Choose on voice, x-height and spacing, not category.
- **"The ideal line length is exactly 66 characters."** 45-90 is a comfort range. Some studies find faster reading at longer lines, while people still prefer medium ones [SRC-112].
- **"All-caps is unreadable because of word shape."** The word-shape theory is weak; caps read slower mainly because they are less familiar and take more space [SRC-118]. Short caps labels are fine; long caps paragraphs are not.

## Quick measurements

| Check | How | Pass |
|---|---|---|
| Measure | characters per line on 3 lines | 45-90 |
| Scale | neighbouring size ratio | ≥ 1.1, one ratio |
| Body size | computed px | ≥ 16 (web) |
| Leading | line-height ÷ font-size | body 1.3-1.5 (to 1.6 on long measures), display 1.0-1.2 |
| Families | distinct `font-family` | ≤ 2 (+1 functional) |
