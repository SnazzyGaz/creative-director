# Lookbook strength: how far to turn the dial

Text summary only; the images stay out of the repo. This is the internal evidence behind LOOK-1 to LOOK-3 (`modules/lookbook/README.md`). It is owner-judged, a small sample with one render per level, and not blind: treat it as craft wisdom, not a test result.

**How it was made** (v0.9.7, one image model). 21 invented briefs in varied domains, most with exact copy: posters, covers, labels, packaging, a stamp, a ticket, a tote, a skate deck, a web page, a product render, a chapter opener and others. Each brief got a **base** render (the full rules, no look) and three renders with **one** look at 20% (hint), 50% (leaning) and 80% (strong), as the strength dial defines them. Briefs 1-15 drew their look at random (`random.Random(seed).choice` over the 320 live looks, one seed per brief). Briefs 16-21 tested Family 8 (LB-SD10 to LB-SD15), one look each, two of them on briefs outside the look's `use` list. No real people. The best level per brief was picked by the agent and reviewed by the owner of the work, who judged 20-50% the sweet spot.

| Best level | Random pulls (1-15) | Family 8 (16-21) | All 21 |
|---|---|---|---|
| Base | 1 | 0 | 1 |
| 20% | 1 | 0 | 1 |
| 50% | 10 | 4 | 14 |
| 80% | 3 | 2 | 5 |

**What happened at 80%.**
- **It won where the look's structure was the brief's idea:** a game-box lid for a reading challenge, ribbon figures for a dance company called Torsion, a gallery statue glancing sideways for "Look Closer", a red poster block used as a redaction bar on a true-crime cover, and CMY circles used as speaker cones on a club poster.
- **Subject creep, 9 of 15 random pulls:** the look's own subject replaced the brief's: a crowd of creatures for a hedgehog mascot, icon-like figures on a choir ticket, a space shuttle for a skater, a fake desktop for a 404 page, among others.
- **Prop stripping, Family 8:** the family's subjects are generic (one figure, one animal, one portrait), so creep was milder, but 80% dropped the brief's props and twists to fit the look's single-subject formula (a suitcase, a quill, the lightning, the books).
- **Identity:** SD15 at 80% lightened an invented older woman's skin tone and features into its paper tone (LOOK-3).

**At 20%** the change was often too small to see; it won once, where one loud palette move was enough. Copy was exact on every render that carried text; words are by the image model, one render per level.
