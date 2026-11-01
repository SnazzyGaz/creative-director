# Baseline comparison: same prompt, with and without the skill

**Model / tool:** all images were made by **GenerateImage, Grok Bot's built-in image tool**, on 1 Nov 2026, at 3:4. One sample each, nothing retouched. This is a small, single-tool test (two briefs), so treat it as an illustration, not a benchmark.

- **Without the skill:** the one-line prompt, sent as is. The model drew the text into the image itself. Kept exactly as generated.
- **With the skill:** the same request run through the loop. Step 0 wrote the brief; the art was generated **with no text in it** and room left for type; then **all type was set in code** over the art ([`src/compose.py`](src/compose.py), Fraunces and Instrument Sans, both OFL), using only the brief's facts; then look tests, critique against TYPE, LAY, BRAND and CORE rules, up to 3 rounds.

The text is part of the deliverable, so the with-skill versions are the full piece: art and type.

> **Earlier version (v0.2.0 to v0.3.0):** the with-skill side was the generated image only, with no type set ([`fox-with-image-only.jpg`](fox-with-image-only.jpg), [`poster-with-image-only.jpg`](poster-with-image-only.jpg)). That was an unfair comparison (a picture against a finished cover), and the poster's lamp glow came out as a flat blob. Both were redone on 1 Nov 2026 as below.

## 1. Children's book cover

Prompt: *"A cover illustration for a children's book about a fox who loves reading."*

![](fox-side-by-side.jpg)

**Text used.** The brief gives no title or author. Title: *A Fox Who Loves Reading*, the brief's own words used as a **working title** (replace with the real one). Author: `AUTHOR NAME`, a marked placeholder. Nothing else.

| Round | Finding (rule) | Fix |
|---|---|---|
| 1 ([r1](fox-with-r1.jpg)) | Second title line "Who Loves" runs into the tree's leaves: text over busy texture (TYPE-3 legibility, CORE-2 value, UI-6 text over images) | Title 112 → 92 px so the whole block sits on plain sky |
| 2 ([r2](fox-with-r2.jpg), final) | No blockers. Title 8.97:1 and author 6.78:1 on the sky (`tools/contrast.py`); title readable at a 150 px thumbnail; fox and book are the blur-test focal point | Stopped: clearly better, no rule left to cite |

| | Without | With |
|---|---|---|
| Invented text (CD-1, CORE-8) | Title, subtitle, three labelled book spines, a signpost and a slogan card, none asked for | Working title from the brief, marked author placeholder |
| Hierarchy (TYPE-7, CORE-1) | Title, subtitle, signs and spines all compete | Title, then fox, then author |
| Type (TYPE-1) | Four styles, letters drawn by the image model | Two families, set in code, editable |
| Palette (ILL-4) | Full saturated rainbow | Fox orange and page light against sage and pale sky |
| **Still loses on** | | **Energy and age signal at a glance.** The without version shouts "children's book" in a feed; the with version is calmer and reads older. Whether that suits the age group is a question for the owner, not a rule failure. |

## 2. Event poster

Prompt: *"A poster for a neighbourhood jazz night on Friday 14 March at The Lantern, 8pm, free entry."*

![](poster-side-by-side.jpg)

**Text used.** Exactly the brief's facts: Neighbourhood Jazz Night, Friday 14 March, 8pm, The Lantern, Free entry. No act names were given, so none are set; no address.

| Round | Finding (rule) | Fix |
|---|---|---|
| 1 ([r1](poster-with-r1.jpg)) | "8pm" collides with the bass scroll, and "Night" touches it: blocker (TYPE-3, LAY-6) | Title 190 → 168 px and up 16 px; facts 46 → 40 px at 85% width |
| 2 ([r2](poster-with-r2.jpg)) | Facts clear, but the "t" of "Night" sits almost tangent to the scroll: a near-tangent that pulls the eye (crop/edges look test, ILL-1 tangents) | Title 168 → 156 px |
| 3 ([r3](poster-with-r3.jpg), final) | No blockers. Navy on paper 11.47:1. Reading order what, when, where, price. The lamp glow is now a soft radial light (the v0.2 blob is gone) | Stopped at the round limit |

| | Without | With |
|---|---|---|
| Facts (CD-1, CORE-8) | All four facts, plus an invented address ("12 Lantern Lane, Our Neighbourhood") and three invented slogans | Exactly the facts in the brief |
| Hierarchy (TYPE-7) | Title, slogans, date and footer compete; "Our neighbourhood" appears three times | One reading order |
| Type (TYPE-1) | Four styles (spaced caps, condensed, brush script, handwriting) | Two families |
| **Still loses on** | | **Atmosphere.** The without version's street at dusk is richer and more inviting at a glance. The with version is cleaner, more legible and correct, but plainer. Smaller misses: the lamp is drawn at an odd scale next to the bass, and the orange rule under the title is 2.36:1 on the paper (decorative only, carries no information, so no WCAG failure, but it is faint). |

## What this shows, honestly

- With type set properly, both with-skill pieces are now **complete, accurate and legible**: no invented facts, one reading order, two typefaces, every text pair well above 4.5:1. On accuracy and hierarchy they win outright.
- They **do not win outright on first impression.** Both without-skill versions are more vivid and atmospheric, and many people would pick them in a feed. The skill buys restraint and correctness; it doesn't add excitement on its own.
- The without versions keep their invented text and image-model lettering; that is the honest baseline, not a strawman.
- A **web UI baseline** was not run here: the same agent writing HTML "without the skill" would already have read it. See the [cross-model kit](../cross-model/).

## Files

`*-without.jpg` (baseline, as generated) · `*-with.jpg` (final) · `*-with-r1..r3.jpg` (rounds) · `*-with-image-only.jpg` (the earlier, art-only version) · `look-*.jpg` (look tests; `look-*-with.jpg` are of the finals) · `src/` (generated art without text, `compose.py`, per-round `params.py`).

Reproduce: `cd src && python3 compose.py 3` (needs google-chrome). Prompts used for the art are in [`src/PROMPTS.md`](src/PROMPTS.md).
