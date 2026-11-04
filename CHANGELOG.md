# Changelog

## Unreleased

- **Font library to 107 families in 29 themes** (`fonts/`): 46 new open-licence families (all SIL OFL 1.1, unmodified from google/fonts, licence file in every folder) and 11 new themes: heritage / badge slab (Clarendon and wood-type slabs for pubs, saloons and crests), blackletter, brutalist / grotesk display, variable expressive display, rounded friendly sans, stencil / industrial, signage / DIN-like, wide / extended display, high-contrast modern serif, warm old-style text serif and script / brush signage, plus gap fills in art deco, geometric and grotesk. Every family now carries mood tags from one fixed list (trust, calm, warmth, play, speed, power, precision, luxury, elegance, heritage, craft, rebellion, menace, nostalgia, tech, romance, authority), and `CATALOGUE.md` opens with a "By mood" index; the tags are craft judgement, not research. Variable fonts where they exist; italics kept only for text and workhorse families. The font zip on the assets-v1 release grows from 9.2 to 16.4 MB (`tools/fetch_assets.py` unchanged); git gains only licences, the catalogue and specimen sheets. TYPE-10 points to the mood index. No rule changes.
- **Idea first** (`core/creative-direction.md`): a short guidance note, not a rule: start from the idea, then use the rules to edit and sharpen it rather than to generate it. No rule IDs or checks change.
- **Style bleed showcase** (README, after Before and after; `examples/lookbook-strength/`): four showcase 3 sheets, each a base render beside one look at 20, 50 and 80%, with a one-line caption on which level won and why: LOW END, Cold Open and Torsion Dance at 80% (the look's structure carried the brief's idea; Cold Open with creep), Page not found at 50% (80% crept into a fake desktop). Picked by the owner of the work; one render per level, not blind. 1,600 px web JPEGs (about 90-245 KB). No rule changes.

## v0.9.8 (3 November 2026)

**Lookbook strength: 20-50% by default, strong only on purpose, and people keep who they are.** Three new rules in `modules/lookbook/README.md`, from the showcase 3 strength test: 21 briefs, each a base render beside one look at 20, 50 and 80%. The new rules are internal evidence: owner-judged, a small sample (one render per level), not blind. No budget was raised.

- **LOOK-1, default 20-50%** (craft wisdom): hint to leaning is the default range, for looks drawn at random too. This replaces "start at hint" and folds in the earlier proposal to cap random looks at medium. In showcase 3, 20-50% was best on 15 of 21 (50% on 14, 20% on 1), 80% on 5, the base on 1; the owner of the work judged 20-50% the sweet spot.
- **LOOK-2, strong only on purpose** (craft wisdom): ~80% only when the look's structure carries the brief's own idea (a red poster block as a redaction bar), or on request; first check for subject creep (the look's subject replacing the brief's, 9 of 15 random pulls) and prop stripping (the brief's props and twists dropped).
- **LOOK-3, keep an invented person's skin tone and identity** (procedure, care rule): portrait and figure looks never flatten a person into the look's palette (seen with LB-SD15 at 80%). The care flags line points to it, and LB-SD15's `care` field carries it (repo only; the breeder's row and sheet caption are unchanged, so a later sync needs the same line in the breeder).
- **Pointers.** The dial table drops "(default)" from hint; `core/which-modules.md` (lookbook row: "20-50%, LOOK-1"; token table refreshed) and `core/commands.md` (bolder: strong only per LOOK-2) follow. README's lookbook row notes the default range.
- **Evidence note.** New `examples/lookbook-strength/README.md`: a text summary of the test and its tally. No showcase 3 images are in the repo.
- **Before and after across domains** (README, gallery, `examples/showcase/`, released here): six labelled pairs, each a plain-brief baseline beside the full v0.9.7 loop: a book cover, a packaging label, a character, a logo, a poster and an exploded view. One sample per side, words by the image model. The owner of the work picked these six from ten pairs. They are illustrative, not test evidence; the blind test remains the evidence. The pairs are 1,400 px web JPEGs (about 80-230 KB).
- **Budgets after.** Always-on 6,453 of 6,500 (unchanged); with the template 7,935 of 8,000; lookbook README 1,821 of 6,000 (up from 1,289); commands 1,192; which-modules 2,183.

## v0.9.7 (3 November 2026)

**Screens need soul; exact copy and counts; batch 8 gaps answered; room made in the budgets; lookbook to 320 looks.** The review list after batch 8, done in full. The new rules answer gaps seen in one judge's batch 8 notes: internal evidence, untested until a new batch is judged. No budget cap was raised.

- **Room in the budgets first.** The "moved to" stubs are gone; a new `docs/RETIRED-IDS.md` lists every retired or merged rule ID and where it went. The energy pass and the critique loop were tightened. The film references (reading lists and myths) moved to a new optional `modules/film/notes.md` (799 tokens); the film README ends with an index of the `edit.md` rule IDs.
- **Screens need soul** (new UI-12, craft wisdom, untested; SRC-36 and SRC-34 as partial support): a named mood and one expressive move on screens that sell or greet. The energy pass now covers web heroes, landing pages, pricing sections and app home and summary screens (checkout steps skip it). The screen route in `core/which-modules.md` loads web-ui, ux and the energy pass, with the lookbook optional; a screen load is about 15,400.
- **Exact copy and counts** (new CD-7, MUST-BE-RIGHT; procedure, internal evidence, untested): every string the brief fixes reads letter for letter on the render, and every number it fixes is counted. A new blocker in the critique loop, the template's QA line, the lite file and AGENTS step 3. ILL-6 and INF-6 now point to it.
- **New rules from batch 8:** BRAND-9, logos and mascots one step of metaphor past the literal (also in ILL-17, with story across the pages); BRAND-10, packaging branding with character; CHAR-11, props as briefed (MUST-BE-RIGHT where the brief names the prop or action; anatomy crops gain A12); LAY-16 adds author-name contrast on covers, at least 4.5:1 on the worst pixels via LAY-15.
- **Rules generalised and merged.** Single-test rules now state the general case with the test as an example, with honest grades (LAY-17, ILL-6, EN-2 items, among others). INF-3 merged into LAY-18 (every panel checked, each different, the set one flow); INF-6's copy check moved to CD-7. CV-10 and CV-11 were reviewed and left as they are.
- **One home for numbers.** Touch-target sizes live in UI-5 only; the notes files point there. Source tags are now SRC-### everywhere (sheets keep S##, briefs B##).
- **Docs.** Energy-pass figures brought up to date (all 100 briefs 59-40-1, one-sided p = 0.035, meeting the 59-of-100 bar; batch 8 20-10, p = 0.049). The routing table is shorter (27 rows). `docs/PROPOSED-REPO.md` is marked historical. README gains a three-line "Start here" and corrected bundle sizes (about 12k and 93k tokens). The token table in `core/which-modules.md` is refreshed. RESULTS.md maps each batch 8 gap to its new rule.
- **Lookbook batches 7 to 12**, synced from the breeder with `tools/lookbook_sync.py`:
  - **Looks:** 320 live, up from 196. 124 added, all established: LB-115 to LB-234 (116; LB-139, LB-144, LB-149 and LB-162 were rejected at draft review in the breeder and never compiled, so those IDs are unused) and LB-SD10 to LB-SD17 (8 contemporary figure-illustration looks). A new family, F9 fine-art movements (62 looks), plus more ornamental, print, pop, digital and technique looks. Nothing retired; the two retired IDs (LB-064, LB-R02R22) stay retired.
  - **Tags:** every new look has `nearest_looks` and `colours`; existing looks' neighbours were re-derived (98 changed). `getty_aat` stays on the earlier looks (new ones below). LB-102's hallmark wording was tidied in the breeder. Dedup in the breeder: one flag, LB-232 against LB-SD12 on dHash only (CLIP 0.18), a round dish against a splash portrait, kept as distinct.
  - **Sheets:** 81 sheets (up from 45). The 36 new ones are 1,000 px JPEGs like the rest (about 13 MB of sheets in git); the 45 existing sheets are unchanged.
  - **Search** (`tests/score_find.py`): violations 0. Recall@8 on the 32 existing briefs fell from 0.979 to 0.958: in five briefs (b01, b13, b25, b29, b31) one expected look was pushed out of the top 8 by new looks. New brief b33 (calm smart-home app screens) for the new interface looks; recall@8 over all 33 is 0.949.
  - **Getty AAT:** 36 more established looks carry a `getty_aat` era term (63 in all, up from 27), each checked on its vocab.getty.edu page on 3 November 2026 (record type concept, Styles and Periods facet, preferred term). Looks renamed on purpose, named by technique, or with no matching AAT term (for example Neo-primitivism and biomorphic abstraction) stay blank.
  - **Brief expectations reviewed:** b01, b13, b25, b29 and b31 each add the new looks whose own `use` names the brief's use and whose mood fits (LB-SD11; LB-160, LB-232; LB-234; LB-224, LB-218; LB-199); the original expected looks still fit and stay. Recall@8 over 33 briefs is now 0.932 (from 0.949), violations 0. Known weakness, not hidden: for b13 (family restaurant) the search still ranks two looks whose avoid-for names "children's", because it does not link "family" to "children's".
  - **Full-size sheets:** `creative-director-lookbook-full.zip` on the assets-v1 release now holds all 81 sheets and the index (26.3 MB); `SHA256SUMS.txt` updated.
- **Budgets after.** Always-on 6,453 of 6,500 (down from 6,497); with the template 7,935 of 8,000; AGENTS 1,364; principles 1,929; loop 3,160; template 1,482; lite 2,498 of 2,500; layout 5,974 of 6,000; film 5,887; energy pass 2,761 (down from 3,347).

## v0.9.6 (3 November 2026)

**Infographics: layout first, charts designed in, an illustration budget; warmth by choice.** Batch 7, ten infographic briefs on v0.9.5, went 3 to 7 against the skill (p = 0.17 for the other side, no clear result). v0.9.5 overcorrected batch 6's "sterile": the losses were called way over-illustrated and unbalanced, a graphic that doesn't belong, charts that look cheap and pasted on, samey steps, an amateurish hero title, too demonstrative (photoreal), with two missing lines and an inhaler shown without its spacer. Its code charts were the accurate ones; the layouts around them lost. All 70 briefs: 39 to 30 with 1 tie (one-sided p = 0.17), short of the 43-of-70 bar set in advance; infographics over batches 6 and 7, 7 to 13. The new rules are internal evidence from one judge, untested. No budget was raised.

- **New `modules/layout/infographics.md` (INF-1 to INF-6).** INF-1, layout first: hierarchy, grid and reading path before any art; the chart, map or diagram is the hero, in the piece's own palette, line weight, corners and type. Two recipes: build in code with spot art, or generate the full design with the chart area styled in and replace only the data marks. Integration checks: no white box behind the chart, no labels cut by strokes, matching palette and type, no collisions. INF-2, an illustration budget: one spot illustration or one icon set, no larger than the information; simplified icons for secondary facts; no full scene behind data; no photoreal unless asked. INF-3: each step or period visibly different, with connectors. INF-4, chart type fits the data: part of a whole as a pie or donut of six slices at most, comparisons as bars, always drawn from the data. INF-5: a hero title with hierarchy logic. INF-6 (blocker): every required line present, and safety and medical steps checked against the brief.
- **Energy from structure** (`core/energy-pass.md`): EN-4 rewritten. Infographics get a structure pass, energy from layout, type, colour and a focal chart, not from illustration; EN-1 moves them out of the full pass. EN-3's grade carries the batch 7 numbers.
- **White means white, unless warmth is chosen** (CV-11, lite file): neutral white stays the default for notices, UI, data and clinical pieces; a warm paper is a named exception where context, brand, era or mood calls for it. `tools/autocheck.py --warm "reason"` passes a light, warm white (luma 228 or more, spread 45 or less, warm) and still flags grey. Autocheck tests 12/12.
- **Chart tools** (`tools/datagraphic.py`): `donut` (from the data, clockwise, transparent hole, warns above six slices) and `check-donut` (slice shares against the data); `check-panel` flags a flat panel pasted behind a chart; `bars` gains rounded corners; `route` moves labels off the line. Datagraphic tests 13/13.
- **Routing and gates.** `core/which-modules.md`: the infographic row loads `infographics.md` with the structure pass; token table refreshed; an infographic load is about 23,900. LAY-19 points to INF-1. The loop's blockers add LAY-19 and INF-6; `tools/check_budgets.py` adds the infographic load; the bundle and skill include the new file.
- **Sources** S337 (Cleveland and McGill 1984, graphical perception: position and length read more accurately than angle and area) and S338 (Spence and Lewandowsky 1991: pies do as well as bars for proportions). Bibliography: "Honest charts".
- **Blind test write-up.** Key 7 published (`sha256sum -c` passes for all seven); `scoring-owner.csv` adds S69-S78; RESULTS.md covers batch 7, its notes, the chart measurements and the honest count. README, `llms.txt`, examples and the kit README carry it.
- **AGENTS.md** drops its list of agent brand names to stay agent-neutral and inside the always-on budget.
- **Budgets after.** Always-on 6,497 of 6,500 (unchanged); with the template 7,987 of 8,000; lite 2,496 of 2,500; layout 5,924 of 6,000 (down from 5,939); infographics 1,739 of 4,500; energy pass 3,347 of 4,500.

## v0.9.5 (3 November 2026)

**Infographics: richer, never a slide, never chaos; charts drawn from the data.** Batch 6, ten infographic briefs on v0.9.4, went 4 to 6 against the skill (p = 0.38 for the other side, no clear result). The losses were called sterile, "like a PowerPoint slide" or too basic (four), repetitive (one) and busy and chaotic (one); the wins were cleaner and punchier, with stable characters. All 60 briefs: 36 to 23 with 1 tie (one-sided p = 0.059), one win short of the 37-of-60 bar set in advance, so the overall result is no longer clear. The new rules are graded as internal evidence from one judge, untested until batch 7 is judged. No budget was raised.

- **Infographics get the full energy pass** (`core/energy-pass.md`, new EN-4; EN-1 widened). Judge as the commissioner would: information right first, then appeal. Write a one-sentence art direction with a style with personality and an emotional register that fits the issuer. "Clean" means easy to read, not bare. The line between rich and chaotic is a check: one illustration style, one reading path, one hero and at most two secondary focal points, no filler or repeated pictures, text on calm ground, then a slide-template test and a chaos test.
- **Every panel shows something different** (LAY-18): the detail its step is about, with the same people, objects and setting throughout (S64 lost for one picture repeated in every panel).
- **Charts, maps and routes are drawn in code** (new LAY-19, MUST-BE-RIGHT where numbers or a route carry the message). New `tools/datagraphic.py`: `bars` and `route` draw from a JSON spec (bars exactly to scale; a loop that closes at start = finish, with a bridge drawn at every river crossing), `composite` fits the layer into a box reserved in generated art, and `check-bars` measures bar lengths in any image against the data, failing beyond 2%. Tests: `tools/tests/datagraphic_cases.py` (8/8), added to CI. In batch 6, neither generated bar chart was to scale (the skill's overstated small bars by up to 12.5 points), and neither fun-run map closed its loop or showed its bridge.
- **Routing.** `core/which-modules.md` gains an infographics row; the energy-pass row covers infographics of every kind.
- **Source** S336 (Pandey et al. 2015: truncated axes and other distortions change what readers judge). Bibliography: "Honest charts".
- **Blind test write-up.** Key 6 published (`sha256sum -c` passes for all six); `scoring-owner.csv` adds S59-S68; RESULTS.md covers batch 6, its notes, the chart finding and the honest overall count. README, `llms.txt` and the kit README carry it.
- **After the tag: README tidied.** The opening now says what the skill is, how to install and use it, and lists the modules in a table. Blind-test detail moved to a short *Blind test* section lower down that gives the headline result and links to `examples/blind-test/RESULTS.md`.
- **After the tag: blind-test batch 7 drawn.** Ten more infographic briefs (B61-B70) against v0.9.5, sheets S69-S78. The key is hashed in `KEY-SHA256.txt` and not published. On the with side, charts and routes were drawn in code and composited (see the kit README). Waiting to be judged.
- **Budgets after.** Always-on 6,497 of 6,500 (unchanged); with the template 7,987 of 8,000; template 1,490 of 1,500; lite 2,497 of 2,500; layout 5,939 of 6,000; energy pass 3,181 of 4,500. The new rules went into on-demand files only.

## v0.9.4 (3 November 2026)

**Blind test finished; rules from the owner's batch 4 and 5 notes, and white means white.** Batch 4 went 6 to 4 for the skill and batch 5, a replication on the unchanged v0.9.3 skill, 8 to 2 (p = 0.055). Batches 3 to 5, after the energy pass: 22 to 7 with 1 tie (p ≈ 0.004). All 50 briefs: 32 to 17 with 1 tie (p = 0.022), which meets the 32-of-50 bar set in advance. One judge, and the later batches aren't independent of the rule-writing, so the new rules are graded as the owner's taste and internal blind-test evidence, not research. No budget was raised.

- **Read the brief exactly.** CD-1 (`core/creative-direction.md`), ILL-6 and the loop's intent model: count what the brief fixes ("it" is one); background facts set the mood and need not be drawn or printed; think about print cost. New UI-11: no invented product screens in finished work.
- **Genre, mood and gesture.** Energy pass items 7 and 8, AES-11, TYPE-10 (a title as loud as the mood), CHAR-6 (traits through pose, not props or text), new ILL-17 (picture books need life, not clinical polish), new LAY-16 (covers: title zone, author name on the axis, styling that signals the genre).
- **Plain where plain works.** EN-1 gives menus, signage and timetables a light pass at most; new LAY-17 covers them. Item 5: an instruction the art implies also goes in the text.
- **Things that look broken.** New LAY-18 (one broken panel fails a multi-panel piece) and COMP-24 item 7 (blocks that look misprinted). CV-10 adds small text at a distance, and no outline stroke or text glow to rescue a value clash.
- **Slop and sterile.** EN-3 names the glowing, over-detailed chocolate-box look and adds an honest check for sterile results.
- **White means white.** New CV-11: paper, grounds and white type default to neutral white; cream or warm white only when the brief asks. `tools/autocheck.py` gains a `whites` check: the lightest 0.5% of an image FLAGs below luma 248 or above a channel spread of 12, and `--white-box` areas meant to be white FAIL below 248 or above a spread of 8. Four new test cases (autocheck 10/10). The critique template and lite file carry the check. A scan of the prompt guidance found no default cream wording to change; the historical example prompts are records and stay as written.
- **Blind test write-up.** Keys 4 and 5 published (`sha256sum -c` passes for all five); `scoring-owner.csv` adds S39-S58; RESULTS.md covers all five batches, the losses, the sterile notes and the off-white finding. New `examples/blind-test/whites.py`: with-skill whites had a median luma of 248.3 against 251.9, lower in 26 of 50 pairs, and 25 with-skill prompts had asked for cream or off-white.
- **Budgets after.** Always-on 6,497 of 6,500; with the template 7,987 of 8,000; template 1,490 of 1,500; lite 2,497 of 2,500. Small trims in the loop and lite file made the room.

## v0.9.3 (3 November 2026)

**Blind test judged; rules tightened from the owner's batch 3 notes.** Batch 3 went 8 to 1 for the skill with 1 tie (p = 0.020), but it isn't independent of batches 1 and 2, its maker saw both arms, and most picks were slight. Overall: 18 to 11 with 1 tie over 30 briefs (p = 0.13, no clear result). The notes moved from "sterile versus slop" to concept, figure-ground, issuer marks and plain notices; this release adds rules for those, graded as internal evidence from one judge. No budget was raised.

- **Issuer mark on official pieces** (`modules/brand/` BRAND-4, energy pass item 6). Use the issuer's real mark from its file, with the name at the top as the official say-so, not as advertising. If there's no file, ask for it or leave a labelled slot ("[Issuer] logo: official file needed") and flag it as open in the critique. Never invent a crest (BRAND-8), and don't use a characterless text-only header: without the mark a notice reads as amateur.
- **Subject on ground, text on colour.** New CV-10 in `modules/colour-value/`, plus energy pass items 1 and 3: the subject must separate from its ground in value at a distance, and text on saturated colour gets both black and white checked, keeping the higher contrast. On batch 3's red header, white measures 4.74:1 and black 4.43:1.
- **Concept fit.** New energy pass item 8 and a CD-3 bullet in `core/creative-direction.md`: the idea fits the category and its sensory cues, not just the brand name, and gets checked for unwanted readings. Item 7 adds that a fun event shows the activity and the people, not an empty place.
- **Hooks.** The critique loop's energy line, the critique template's QA line (CV-10, BRAND-4) and the lite file carry short versions. The loop trimmed two phrases (in FLOW-1 and FLOW-3's Why) to stay inside the always-on budget (6,492 of 6,500); the template is 1,492 of 1,500 and the lite file 2,488 of 2,500.
- **Sources** S334 (Piqueras-Fiszman and Spence 2015: a review finding that packaging colour, pictures and labels set taste expectations) and S335 (Somers, a practitioner note on how the WCAG 2 ratio can favour black text on orange and red where many readers find white easier). Bibliography: "Category cues and contrast on colour".
- **Blind test results.** New `examples/blind-test/RESULTS.md`: all three batches, sign tests per batch and overall, strengths, the sterile-versus-slop finding, the energy pass, batch 3's caveats, the gaps found and every judgement. The owner's picks are in `scoring-owner.csv`, with the reasons paraphrased. The three keys are now published next to `KEY-SHA256.txt`, and `sha256sum -c` passes for all three. README, `llms.txt` and the kit README carry the result.
- **score.py** handles ties explicitly: `SAME` or `tie` counts as a tie, and an ID not in the keys warns on stderr and counts as a tie.

## v0.9.2 (3 November 2026)

**Content freeze, one exception.** Batches 1 and 2 of the blind test are judged by the owner of the work: a tie, 10 to 10 over 20 briefs (5 to 3 for the skill in batch 1, 7 to 5 against it in batch 2; no clear result). Where the version without the skill won, the owner's notes mostly named its eye-catch, energy or obvious call to action. This release adds one rule in response and a third batch to test it; other new content still waits.

- **Energy pass.** New `core/energy-pass.md` (EN-1 to EN-3), loaded on demand. It runs after the accuracy and clarity checks pass, and only where it applies: a full pass for posters, covers, packaging, heroes, social cards, picture books, character art and public infographics; a light pass for notices, dashboards and data infographics; skipped for forms, tables, legal or medical text, settings and accessibility-critical UI, where "quieter" (CMD-2) wins. Seven checkable items: one focal hook at thumbnail size, confident display type with real hierarchy, purposeful colour, movement or scale contrast, an obvious call to action, the issuer's own name or mark on official pieces (never an invented one), and a mood that matches the brief's warmth. Guardrails: energy comes from structure, not texture; no clutter, no added copy, no over-rendered grain or speckle, no generic layout tropes; one or two fixes at a time. A "sterile vs slop" table names the failure on each side. Graded as procedure with internal evidence (the 10 to 10 tie, one judge), partly supported by S332 and S333.
- **Wiring.** Short hooks in `core/critique-loop.md` (LOOK step, FLOW-3 QA gates), `AGENTS.md` (on-demand list, step 3), `core/critique-template.md` (QA line), the lite file, `core/commands.md` (CMD-1 points to it for work that is correct but plain), `core/which-modules.md` (task row, check order, token counts), `llms.txt`, README and the prompt bundle. Two non-essential phrases were cut from the critique loop so the always-on set stays inside its 6,500-token budget (now 6,492); no budget was raised.
- **Sources** S332 (Pieters, Wedel and Batra 2010: feature complexity hurts attention to ads, design complexity helps) and S333 (Pieters and Wedel 2004: the picture draws attention whatever its size; attention to text grows with its size). Bibliography section 6.
- **Blind test batch 3.** 10 new briefs (B21-B30: 2 posters, an infographic, a picture-book cover and spread, a coffee bag, a web hero, 2 official notices, a character concept), written after the energy pass and before any image was made, each with its exact copy. Made the same way (GenerateImage, one call each, first output kept, same aspect ratio); the with-skill prompts follow the energy pass. One sheet per brief (S29-S38); the new key's salted SHA-256 is in `KEY-SHA256.txt`, the key stays out of the repo, and `scoring.csv`, `SCORING.md`, `score.py` and the outside-model prompt cover 38 sheets. **Batch 3 is not judged yet.** It isn't independent of batches 1 and 2: the rule it tests was written after reading the owner's notes on them.

## v0.9.1 (3 November 2026)

**Content freeze.** No new rules or modules until the blind test below has been judged; until then only fixes (broken links, wrong facts, failing checks).

- **Blind test kit.** New `examples/blind-test/`: 8 earlier briefs (3 posters, 3 illustrations, 2 UI screens), each made with and without the skill by the same image model (GenerateImage, one call each, first output kept). `blind.py` shuffles them into 16 judging sheets (each pair twice, sides swapped, random IDs); the key stays out of the repo, with its salted SHA-256 committed first. A scoring form (`SCORING.md`, `scoring.csv`), a prompt for outside models, and `score.py`, which reports each judge separately, the owner of the work first, with a sign test. Images and sheets are not in git. **Not judged yet: no results.**
- **Hero poster fix (r4).** In the aesthetic poster the double bass sat almost against the lamp post; one image edit slid it left (gap about 10 px to about 33 px at 864 px wide), still inside the lamp's light and lit from the lamp side (TD-LIT-1). Everything outside the edited area, type included, is unchanged pixel for pixel. Hero, side-by-side, look sheet and README baseline images rebuilt; before and after in `examples/anatomy-sweep/`.
- **Token budgets in CI.** New `tools/check_budgets.py`: always-on set at most 6,500 tokens, lite 2,500, each module README 6,000, every other rule file 4,500 (tiktoken `cl100k_base`). The GitHub Action fails if one is over.
  - `modules/composition/`: Sitting right (COMP-19 to 25) moved to `sitting-right.md`; README 8,787 → 5,662 tokens.
  - `modules/film/`: colour and grading, editing, composition in motion, sound, on-screen text, look vocabulary and myths moved to `edit.md`; README 9,998 → 5,801 tokens. No rule removed; every ID kept.
  - `lite/`: tightened, 3,100 → 2,340 tokens, every rule ID kept. Reworded throughout for length; some asides and examples were dropped (for example "list the rule IDs in scope first"). The full rules in `core/` and `modules/` are unchanged.
- **CI runs every test suite** (autocheck, balance, ellipse, grid, intersect, whitespace, lookbook search) on each push.
- **intersect.py needed scipy.** Without it, trimesh's proximity calls failed and every check passed silently. scipy is now in `tools/requirements.txt` and the tool exits with a message if it's missing.
- **Smaller repo.** A fresh clone went from about 279 MB to about 103 MB (`.git` 144 MB → 48 MB). Example images over 150 KB are now smaller copies (at most 1,000 px) at the same paths, lookbook sheets 1,000 px wide, and the font files left git. Full-size originals, the fonts and a git bundle of the old history are on the [assets-v1 release](https://github.com/SnazzyGaz/creative-director/releases/tag/assets-v1); `tools/fetch_assets.py` puts them back. History was rewritten to drop the old large files, so **commit hashes changed: re-clone** rather than pull. Releases and their downloads are unchanged. Images the tests read stay at full size.

## v0.9.0 (3 November 2026)

New optional module: **film** (`modules/film/`), for a cinematographer or editor bot, or any agent that makes or judges video, generated clips, animation, storyboards, shot lists or edits.

- **Story first.** `story.md` (FILM-STORY-0 to 11) is the core: name the beat, then check every choice (size, angle, lens, light, colour, movement, cut, sound, music, text) against it. It covers framing as emotional distance and power, colour scripts and palette arcs, light changes as beats, movement as subjectivity, score and source music, counterpoint, leitmotif, silence and sound bridges, suspense and withholding (the bomb under the table), reaction shots and point of view, motifs and rhymes, and contrast and affinity.
- **Craft rules.** `README.md` (42 rules): shot grammar (size, angle, perspective from distance, focus, aspect ratio and safe areas, headroom), continuity (180° line, 30° rule, eyelines, screen direction, match on action, physical continuity) as conventions with deliberate breaks recorded, camera movement and shutter, motivated light with one key direction across a scene (links TD-LIT-1), ratios and latitude, grading (one look, shot matching, skin, colour pipeline; links CV rules), editing (Murch's priorities, eye-trace across cuts, shot length, J and L cuts, an honest Kuleshov, transitions), composition in motion (balance is only a flag, never a push to centre), sound sync and loudness, titles and subtitles, flashing and captions.
- **Generated video.** `generated.md` (FILM-GEN-1 to 10): frame-sampling QC with contact sheets (ffmpeg commands, no new tool), identity drift, anatomy on sampled frames, morphing objects, physics, flicker, light across shots, invented text, camera geometry and the generic generated look, plus a 12-step checklist.
- **Review and template.** `review.md`: watch in motion at delivered size with sound before judging frames (FILM-REV-1), shot lists, storyboards reviewed as plans, and a film critique template.
- **Crossover map.** `crossover.md`: rules that apply as they are, rules that change in motion, and film-only rules.
- **Myths.** Thirds as law, the golden ratio, 24 fps as sacred, shallow focus as "cinematic", teal and orange always, "film look" as grain and bars, the strong Kuleshov legend, wide lenses distort, fixed colour meanings, never cross the line, faster cutting is better, Murch's percentages as measured.
- **New blockers** (critique loop): flashing above the WCAG 2.3.1 threshold (FILM-ACC-1); key direction within a continuous scene (FILM-LIT-1); identity, anatomy and invented text in generated video (FILM-GEN-2, -3, -8).
- **Sources** S267 to S331: craft books, attention and editing research, film-style corpus studies, Kuleshov replications, music-and-film psychology, colour-emotion work with its cultural caveats, subtitle, flashing, safe-area and loudness standards, video-model benchmarks, and trade press and practitioner pages (graded as such). Bibliography section 6a; five silent-era films added to the reference library.
- One small hand-written SVG (`modules/film/diagrams/axis-180-30.svg`, 3 KB) shows the 180° line and the 30° rule from above; the text stands without it, and the skill folder leaves it out. No generated images or clips.
- Wiring: `AGENTS.md` module table, `core/which-modules.md` task rows and token counts, lite file, README, `llms.txt`, the full prompt bundle (now includes the film module's extra files) and the skill description.

## v0.8.2 (3 November 2026)

Install support for any agent. No rule changes.

- **Portable skill folder.** New `skills/creative-director/`, a self-contained skill in the open Agent Skills format (agentskills.io): `SKILL.md` plus `core/`, `modules/`, `lite/`, the design tools and the font catalogue, about 0.8 MB with no images. One copy installs in Hermes Agent (`hermes skills install SnazzyGaz/creative-director/skills/creative-director`), Claude, Codex, Gemini CLI, Cursor, GitHub Copilot (`gh skill install`), Devin/Windsurf, Cline and the other agents `npx skills add` supports. It is generated by `tools/package_skill.py` from the root files, so `AGENTS.md`, `core/` and `modules/` stay the one source; `--check` fails if the folder is out of date, and a GitHub Action runs it on every push. The skill zip is now zipped from this folder.
- **Root `SKILL.md` removed.** Skill installers treat a root `SKILL.md` as the whole repo being one skill, which would pull in about 135 MB of examples, images and fonts. The skill is now only in `skills/creative-director/`.
- **Single-file prompt bundles.** New `tools/build_bundle.py` writes `dist/creative-director-prompt.md` (the always-on core, template and commands, about 9,000 tokens) and `dist/creative-director-prompt-full.md` (core and every module, about 63,000 tokens) for chat assistants with no file access. Both are release assets; the lite file is still the smallest option.
- **Pointer files.** New `GEMINI.md`. `CLAUDE.md` and `GEMINI.md` now import `AGENTS.md` with `@`, and the Cursor rule and Copilot instructions point to it; none carry rules of their own.
- **Install guide.** New [`docs/install.md`](docs/install.md): per-agent steps for Hermes Agent, Claude (claude.ai, Claude Code, Projects), Codex, Cursor, Gemini CLI, GitHub Copilot, Devin/Windsurf, Cline, Aider, Grok Bot, and any other LLM, each with the file paths from that agent's own docs. The README's Install section now links to it.
- The skill leaves out the maintainer scripts (`lookbook_sync.py`, the packaging scripts) and the test suites. They stay in the repo. This keeps the folder clear of Hermes Agent's install scanner, which blocks community skills with any high-severity finding.

## v0.8.1 (3 November 2026)

Lookbook batches 2 to 6, synced from the breeder with `tools/lookbook_sync.py`. No rule changes.

- **Looks:** 196 live, up from 132. 64 added: LB-067 to LB-114 (48 established looks), LB-SD01 to LB-SD09 (9 contemporary figure-illustration looks), and 7 new wildcards (LB-R07R22 to LB-R07R24, LB-R08R01, LB-R08R13, LB-R08R14, LB-R08R18). Nothing retired this time; the two retired IDs (LB-064, LB-R02R22) are unchanged. New families: contemporary figure illustration, fine-art movements, digital and internet, and technique and medium.
- **Tags:** every new look has `nearest_looks` and `colours`. `getty_aat` stays on the same 27 looks; new established looks are blank until each ID is checked on vocab.getty.edu. LB-103 is marked partial (its offset colour barely shows). LB-102's hallmarks now note that its raised, photographed-patch 3D quality is kept on purpose: dimensionality is a separate trait that can be borrowed on its own.
- **Sheets:** 45 sheets (up from 24), 1200 px JPEGs; the module is about 16 MB, well under the 50 MB point where sheets move to release assets.
- **Search test:** 6 briefs added for the new families (32 in all). recall@8 0.974 on the old 26 briefs before and after the sync, 0.979 on all 32; violations 0.
- The share check and the name check were clean.

## v0.8.0 (2 November 2026)

Five additions: a one-command auto check, a scored lookbook search, "more like this" and colour search, era terms for established looks, and three one-word commands.

- **Auto check (`tools/autocheck.py`).** One command, no judgement, on an image or a web page (file or URL). Every check prints PASS, FAIL, FLAG or SKIP with its rule ID, the measured value and the rule's own threshold, as a short report plus JSON (`--out DIR` also saves the screenshots and overlays). Pages (Playwright): contrast against the worst ground pixels behind each text run, using a second screenshot with the text hidden (UI-6, LAY-15); minimum text size (TYPE-3); number of type sizes and near-duplicates (TYPE-2); line length (TYPE-4); line spacing (TYPE-5); spacing scale and near-miss gaps or uneven gutters (CORE-4, COMP-24); text crowding the frame (COMP-24); dead space (LAY-10); balance (COMP-19); touch targets and text size at 390 px (UI-5, TYPE-3); sideways scroll and clipped text at 200% zoom (UI-10). Images: dead space, balance, edges and the safe margin (LAY-5, COMP-24), print resolution (LAY-9), and contrast inside given `--text-box` areas; text checks it cannot do from pixels are SKIP with the reason. It reuses `contrast.py`, `whitespace.py` and `balance.py`. Balance is only ever "FLAG: intended?" and never suggests centring. Exit 1 on any FAIL. Tests: `tools/tests/autocheck_cases.py`, 6/6 (four image and two page fixtures). Wired in as the first part of the loop's Look step (`core/critique-loop.md`), in `AGENTS.md` step 3 and `tools/README.md`.
- **Lookbook search test set.** `modules/lookbook/tests/briefs.json`: 26 generic briefs, each with the looks that should shortlist and looks that must not. `score_find.py` scores `tools/lookbook_find.py` on recall@8 and avoid-for violations. Before: 0.955 recall@8 with 2 violations; now 0.974 with 0 (recall@5 0.925 -> 0.944). Changes: words match at the start of a word (so "gin" no longer matches "packaging"); a look whose `avoid_for` names one of the brief's use words is dropped; energy one step off is kept but ranked lower, high against low is still dropped.
- **More like this, and colours.** Each look now has `nearest_looks` (the three most similar renders, by cosine similarity of the breeder's cached image embeddings) and `colours` (3-5 dominant hex values from the render, k-means in CIELAB). **Field change:** wildcards used to carry their breeding parents in `nearest_looks`; those moved to a new `bred_from` field. `tools/lookbook_sync.py` derives all of this on every sync (and `--enrich-only` re-derives it without pulling a batch). `lookbook_find.py` gains `--like LB-xxx` and `--colour "#hex,..."`; a look's own palette finds it first 99% of the time.
- **Era terms.** An optional `getty_aat` field (Getty Art & Architecture Thesaurus ID, preferred term and link) on 27 of the 65 established looks, Styles and Periods terms only (movements and periods, never people or works). Each ID was checked on its vocab.getty.edu page (concept, facet F.FL, label as written). The other 38 established looks are blank on purpose: technique-named looks, looks with no close AAT term, and looks given a generic name on purpose. Wildcards never get one. The mapping lives in `modules/lookbook/getty_aat.json`; credited in `SOURCES.md` (S266, ODC-By 1.0) and the README.
- **Bolder, quieter, distill (`core/commands.md`, CMD-1 to CMD-3).** What each one-word ask means, with checkable lines tied to rule IDs: bolder raises contrast, scale difference and commitment and a lookbook look's strength by one notch; quieter lowers noise, saturation and ornament and the strength by one notch; distill removes elements until the one job still works. All three keep the Sitting right guard: never centre or symmetrise to get there. Referenced from `AGENTS.md` step 0 and the task table in `core/which-modules.md`.
- **Load.** The always-on set grows from about 6,160 to 6,300 tokens (auto check line in the loop and `AGENTS.md`; `commands.md` loads only when asked). Token table recounted; `llms.txt`, `tools/README.md`, `tools/requirements.txt` (playwright) and the lookbook README and UPDATING steps updated.

## v0.7.0 (2 November 2026)

**New optional module: `modules/lookbook/`.** A searchable reference of established looks for starting new work, never a rule source. Core rules and modules always win over a look.

- **Batch 1:** 132 live looks: 65 historic and technique-based looks (LB-001 to LB-066) and 67 wildcards (LB-R…). Each has use, mood, energy, avoid-for, hallmarks by layer (palette, type, mark-making, composition, subject), a one-line hint, an out-there score (1-5), read status and any care note. Two IDs are retired (LB-064, LB-R02R22) and are never reused.
- **Files:** `looks.json` and `looks.csv` (the tag file), `index.png`, and 24 sheets of six looks each in `sheets/` (1200 px JPEGs, about 10 MB in all). Every example is our own render from that look's rules; no look is tied to a real artist, studio, community or specific work.
- **How it is used** (`README.md`): from-scratch briefs get two or three lookbook directions with IDs, at most one concept in three; work that passes but feels generic borrows one layer at hint strength; a described vibe maps to the nearest look. Never on fixes or edits. A strength dial (hint ~20% by default, leaning ~50%, strong ~80%, full) and guards against habit: a recent-use log, fit before novelty, no partial-read looks as a lead, care flags. Cite as `LB-014 Suprematism at ~20%`.
- **Tools:** `tools/lookbook_find.py` shortlists looks from the tag file by use, mood and energy. `tools/lookbook_sync.py` folds in a new batch from the breeder folder: copies only shareable files, filters to live looks, keeps retired IDs, runs the name check. `modules/lookbook/UPDATING.md` has the steps.
- **Wiring:** a row in the `AGENTS.md` module table and in `core/which-modules.md` (README 946 tokens; the tag file is searched, not loaded). The always-on set is unchanged (`AGENTS.md` grows by one table row). The skill zip carries the README, `looks.json` and the tools but no images.

## v0.6.0 (2 November 2026)

A top-to-bottom tidy: one home per rule, a much smaller always-on load, and an honest grade on every rule. No rule was renumbered; a merged rule leaves a "Moved to" line under its old ID.

- **Smaller load.** Always loaded is now `AGENTS.md`, `core/principles.md` and `core/critique-loop.md`: about 6,100 tokens (7,600 with the critique template), down from about 17,300 for `AGENTS.md` plus the everyday `core/` files. A social card (with layout and typography) drops from about 24,600 to 16,200 tokens. The rest of `core/` loads only when the job needs it, and `AGENTS.md` has a one-glance table of which module to load when.
- **Interaction flow merged into the loop.** FLOW-1 to FLOW-5 (sign-off, apply, "just fix it", take over, delivery) now sit inside the loop step they belong to in `core/critique-loop.md`, with the blocker list at the top. `core/interaction-flow.md` keeps only the diagram and a pointer.
- **Seven merges, one home each.** ILL-4 and ILL-9 to colour-value (CV-1, CV-2, CV-4, CV-5, CV-7); UI-1 and UI-2 to typography (TYPE-2 to TYPE-5, TYPE-13), which is now the one home for type numbers; UI-3 to CORE-4 (the spacing scale); COMP-7 (*ma*) to COMP-23; COMP-21 (weight and the lever) to COMP-2. The near-miss bands live in COMP-20 and COMP-24 only.
- **Grades on every rule.** Two grades added to the legend in `core/evidence.md`: *Standard* (geometry, optics or a published spec such as WCAG) and *Procedure* (a working method). All 174 live rules now carry a grade, per rule or per file (CD, FP and FLOW are procedures).
- **Contradictions fixed.** Body leading is 1.3-1.5 everywhere (up to 1.6 on long measures); typography no longer claims every number agrees; CD-1 says six lines; AES-6 no longer counts centring as a tell; a disputed Material type-ratio claim went with UI-1; CORE-8 now credits the right study authors.
- **Cuts.** Eleven Example lines (several named real brands) and the template's worked example removed; duplicated legends, viewing-test lists and the "quick questions" in `which-modules.md` removed; long Why lines trimmed. `SKILL.md` and the Cursor rule now just point at `AGENTS.md`; `tools/package_skill.py` builds the zip's `SKILL.md` from `AGENTS.md` alone.
- **Housekeeping.** README images now use Newsreader from the font library; Fraunces removed from the library (61 families). Two broken font paths fixed, S147 cited in AES-9, token table recounted, `llms.txt` and `lite/` updated to match. The *Sitting right* guard is unchanged: flag only accidental imbalance; fix with a counterweight or a firmer asymmetry; never centre or symmetrise by default.

## v0.5.1 (2 November 2026)

- **Sitting right: the broken-balance pass (new COMP-19 to COMP-25).** A pre-delivery judgement call that asks "does anything sit weirdly?". It flags only balance and placement that read as accidental, unresolved or lopsided by mistake.
  - Asymmetric, off-centre, flush-left and tension-driven work is stated to be valid and often better. Balance means equilibrium of weights, not symmetry. Every check is a flag that asks "intended?", never an auto-fix, and each rule says: never centre or symmetrise by default to satisfy this check. Broken balance is fixed with a counterweight or a firmer asymmetry.
  - COMP-19: broken balance versus asymmetry.
  - COMP-20: make intent read (commit, avoid near-misses).
  - COMP-21: weight factors and the lever (Poore, Ross, Dow, Arnheim, McManus, Hübner & Fillinger).
  - COMP-22: top-heavy and bottom-heavy, the slightly high visual centre, the inward bias and the ecological vertical bias (Palmer et al., Sammartino & Palmer).
  - COMP-23: active versus dead space (strengthens LAY-10).
  - COMP-24: the edge and alignment sweep (floating, crammed, tangents, near-alignments, uneven gutters, optical versus mathematical centring, overshoot).
  - COMP-25: run the pass and let the owner decide.
  - Tests table: squint, thumbnail at 5%, mirror, rotate 180°, cover half, the gap measure, `balance.py` and the edge sweep.
- COMP-2 and CORE-11 fixes reordered: a counterweight or a firmer asymmetry first, and moving to the centre is rarely the fix. `balance.py` readings reworded ("weights near equilibrium", "a flag, not a fault").
- The pass is added to the critique loop, the critique template, the delivery QA line, `lite/`, `AGENTS.md`, `SKILL.md`, `README.md` and `which-modules.md`. LAY-10 now cross-links COMP-23 to COMP-25. There is a new myth line, "balance means symmetry or centring". New source S265 (Material Design icon keylines).

## v0.5.0 (2 November 2026)

A compendium of design taste: composition, balance, colour and beauty, from the classic books, East Asian aesthetics and empirical aesthetics. Every new rule carries an evidence grade.

- **Evidence grades.** A four-level legend in `core/evidence.md`: well supported, partly supported, craft wisdom, contested / myth. Twelve new findings rows and a new myths block (golden ratio in depth, leading lines, Z/F/Gutenberg templates, rule of odds, right-side heaviness, colour-wheel schemes, Goethe area ratios, complementaries as most harmonious, Birkhoff's measure, fractal authentication, golden margins).
- **New `modules/composition/` (COMP-1 to COMP-18).** Skeleton and the near-miss, steelyard weighing, faces and text as weight, the eye path, lead room, figure and ground, empty space (ma), dominance, unity with variety, transition, rhythm, tension, big masses, detail at three distances, order for complexity, proportion families, symmetry and direction. It also has the studio viewing tests (thumbnail, squint, mirror, upside down, distance, quadrant lines).
- **New `modules/colour-value/` (CV-1 to CV-9).** Value key and range, notan in two and three values, the equal-lightness trap, the peephole test, harmony by a shared dimension, chroma budget, one colour of light, distance and contrast, colour-vision deficiency. It deepens CORE-6, ILL-4 and ILL-9 rather than repeating them.
- **Added to existing modules.** ILL-13 to ILL-16 (thumbnail structures, depth planes, inner framing, camera for the story); LAY-11 to LAY-15 (one axis, margins from a system, space before boxes, reading patterns as effects, text over images); TYPE-11 to TYPE-14 (vertical rhythm, paragraphs, rag and hyphenation, optical adjustments); AES-11 (most advanced yet acceptable) and AES-12 (shared taste is low for art, so the owner of the work decides).
- **New `tools/balance.py`.** It weighs each pixel by its contrast with the background and reports the visual centre of mass against the frame centre, with a heatmap sheet. It never fails, because off-centre can be intended. Tests: `tools/tests/balance_cases.py`, 6/6.
- **New `BIBLIOGRAPHY.md`.** An annotated reading list with links to public-domain full texts. Sources S181-S264 in `SOURCES.md`: 27 public-domain classics, 9 modern references and 48 empirical papers.
- Cross-links from CORE-6, CORE-11, ILL-1, ILL-2, ILL-4, LAY-10 and AES-1 to the new rules. `which-modules.md` gains composition and colour-value rows, and the token counts have been recounted. `AGENTS.md`, `SKILL.md`, `README.md`, `llms.txt`, `lite/` and `tools/README.md` are updated.

## v0.4.3 (2 November 2026)

- **Whitespace is distributed on purpose (new LAY-10).** Every empty area must be a margin, a gap between groups, or named focal space.
  - The check measures empty horizontal bands, then squints for 2-D dead zones *inside* a row, such as the gap between a small item on the left and a small item on the right. A row scan and a hierarchy check can both miss that.
  - Anything larger than about 1.5× the largest intended gap is flagged unless it is declared deliberate or is the symmetric flank of a centred group.
  - After any image swap, re-crop or regenerate, the **whole** layout is re-reviewed, not only the new image. This is also added to the AES-10 re-check, `core/critique-template.md`, the delivery QA line, the MUST-BE-RIGHT list in `lite/`, `AGENTS.md`, `SKILL.md` and the Cursor rule.
  - New `tools/whitespace.py`: band ratios, the largest empty region against the layout's own gaps and margins, `--intended` ranges, `--axis left|right` for flush layouts, and a squint sheet. Exit 1 on FAIL; a PASS means "look by eye". Tests: `tools/tests/whitespace_cases.py`, 5/5 synthetic and 3/3 example images.
  - Sources S175-S178: Wertheimer, Palmer, NN/g and White.
- **Design for the real medium (FP-2).** Line 1 of the step-back names the real medium and how the piece is seen. It must not be the incidental framing of the reference, such as a camera-roll crop, screenshot or chat preview. Constraints are never inferred from how a reference was captured.
- **Facts (FP-3).** Transcribe every fact word for word before designing. Then check dates against weekdays, sums, spellings, URLs and prices, and flag contradictions and unsourced claims as questions. Disclaimers and small print survive.
- **Imagery from the subject (new FP-9, new ILL-12).**
  - New imagery starts from a subject sheet: what the subject physically is, real references, and an art-direction line. It is not a re-description of the old picture.
  - Real subjects, food above all, must pass 2-4× crops for structure, tiling or mesh, each component, material and light, and invented marks. ILL-12 is MUST-BE-RIGHT for food.
- **Viewing distance (LAY-7).** Signage and A-boards get a millimetre check: cap height ≈ distance ÷ 250, with the sign-industry legibility index as the basis. Sources S179-S180: United States Sign Council Foundation.
- **Logo handling (BRAND-4) and series (BRAND-6).**
  - Only three kinds of cleaning are allowed: a background knockout, a faithful trace or a one-colour silhouette. All three are verified with an overlay check against the source.
  - When no file exists, the trademark name is set in plain text; it is never drawn.
  - A series gets a set-level pass: logo size and position, margins, header and footer device, palette logic and type logic.
- **Date fix in the seed-swap examples.** The weekday is now correct (Saturday 13 March 2027) in the poster and the first-principles remake, and every affected image has been re-rendered. The "known issue" note has been removed.
- **Case study: `examples/case-study-may-specials/`.** One third-party sidewalk sign, used only as a teaching example with no affiliation. It contains the original, the brief, the concepts, the final and a before-after. The write-up shows the lessons in action: first-principles brief, real medium, viewing-distance table, imagery crops, the LAY-10 failure and fix, plain-text names and fact transcription. It is self-judged. This is the only example that names a real piece. The gallery gains a card.
- `FP-1 to FP-9` references updated throughout; token counts in `which-modules.md` recounted; `tools/README.md` and `llms.txt` updated.

## v0.4.2 (2 November 2026)

- **First-principles remake (FP-1 to FP-8).** New `core/first-principles.md`, a mode for when the owner of the work asks for something "from scratch", "redo", "rejig", "start over" or "reimagine".
  - It steps back before drawing: what the piece is and where it is seen, who it is for, its one job, the feeling, the given facts word for word, what must survive and what was incidental, and how done is judged.
  - It checks the given facts against each other and never invents.
  - It sends a 5-8 line brief from first principles for sign-off.
  - It makes 2-3 concepts that differ in structure, not only style (a one-sentence structure test), recommends one against the brief and drops the others with reasons.
  - It builds the chosen concept and runs the full loop: anatomy (CHAR-9), light (TD-LIT-1), type and contrast, marks, additions, and a side-by-side with the original and any light-touch fix (AES-9).
  - The light touch stays the default without a trigger word, and a take-over (section 4b) is not a remake.
  - Wired into `AGENTS.md`, `SKILL.md`, the skill zip's modes and description, `core/interaction-flow.md` (ask table, diagram, mode mapping), `core/which-modules.md`, `core/critique-template.md` (new *Brief from first principles* section), `core/critique-loop.md`, `core/creative-direction.md`, `lite/`, `llms.txt`, the Cursor rule and the README.
  - Sources S163-S169: Rand, Schön, Dorst, the d.school, IDEO Design Kit and two by Dubberly.
- **Official logos and marks (BRAND-4 widened, new BRAND-8).**
  - BRAND-4 now covers every official mark: the client's own logo, and also sports teams, sponsors, crests and partners. The default is to include the official mark, at good quality, from the owner's file, the brand's own site or press kit, or Wikimedia Commons checked against the brand, and to use it unaltered.
  - A mark is never redrawn, restyled or AI-generated. A labelled placeholder is only a last resort, when no faithful source exists.
  - BRAND-8 (blocker): check generated images for invented logos and garbled lettering on jerseys, bottles, packaging and signs. Regenerate those surfaces plain, then composite the official file in if the brief calls for it.
  - Added to the MUST-BE-RIGHT list, the delivery QA line, FP-8, `AGENTS.md`, `SKILL.md` and `lite/`.
  - Sources S170-S174: USPTO, the Trade Marks Act 1994 s.10, Spotify and Mastercard brand guidelines, and Wikimedia Commons on non-copyright restrictions.
- **Example: `examples/first-principles-remake/`.** The seed-swap poster from the aesthetic-across-domains set, rebuilt from the brief.
  - It includes the original, the step-back brief, three concept thumbnails (seed packet, Bring / Take, calendar), the remake, a labelled side-by-side with the light-touch fix, a three-up, a far read at 10% and a critique. Fonts: Bricolage Grotesque and Hanken Grotesk; the concepts use Alfa Slab One with Zilla Slab, and Jost with Literata.
  - The fact check found that the brief's "Saturday 14 March 2027" is a Sunday. The remake holds the weekday back for the owner, and the earlier poster's README now notes the issue.
  - It is self-judged. Gallery gains a card and a `first-principles` filter.
- Token counts in `which-modules.md` updated.

### Also in this release (previously unreleased, 1 November 2026)

- **Hero lighting fixes (TD-LIT-1).** Aesthetic poster: after two more image edits (the first rejected, kept in `src/`), the bass now stands in the lamp's light, lit from the lamp side with its shadow falling away, and is drawn as a double bass (sloped shoulders) rather than a violin; type unchanged, contrast re-checked (all pass). It is `poster-aes-r3.jpg`; the round 2 art is kept. Middle "with the skill" fox cover: the art prompt had asked for a glowing book, which lit the fox's face from below against the low sun; one edit made the book plain paper (`fox-with-r3.jpg`, old art kept as `src/fox-art-r1-glowing-book.jpg`), contrast re-checked. Side-by-sides, look sheets, gallery text and the README hero (light and dark) rebuilt; the hero's "known fault" caption replaced with what was fixed.
- **Anatomy sweep.** New `examples/anatomy-sweep/`: CHAR-9/10 run over every image in `examples/` and the hero, with crops for the fixed images. No delivered, with-skill or aesthetic-layer image failed; without, before and input images are noted, not changed.
- **Aesthetic layer across domains.** New `examples/aesthetic-across-domains/`: seven worked examples (picture-book illustration, exploded technical drawing, web landing page, three-screen app flow, type-only poster, Blender perfume product shot, Mauna Loa CO2 chart). Each has a plausible before, a critique in the template (measured vs interpreted, ranked fixes with rule IDs, Additions, sign-off blurb), an after with every point applied, a delivery checklist and a labelled side-by-side, plus an index and overview image. Fonts are chosen per brief from `fonts/` (TYPE-10) and recorded. Anatomy pass on the figures. Sources S158-S162 (ISO 128-2, ISO 6433, WCAG 2.5.8, the UK DMCC Act 2024, NOAA GML data). Gallery gains the seven cards and an `aesthetic-critique` filter.
- `examples/baseline-comparison/src/compose.py` takes an optional `fox` or `poster` argument to render just one.

## v0.4.1 (1 November 2026)

- **Interaction flow (FLOW-1 to FLOW-5).** New `core/interaction-flow.md`: what the creative director is good for, how it reads the ask, and a mermaid diagram of the flow. Work handed over with no specific ask now gets a short sign-off blurb of only the imperative changes (ranked, rule ID, what will change, tagged [edit] or [regenerate]) and nothing is applied until the owner signs off. After sign-off every signed-off point is applied, with regeneration when an edit can't do it; each point and the light, anatomy and type blockers are re-checked; the result is delivered with a done / not done line per point. "Just fix it" skips the sign-off, not the checks; a take-over is named as a redo up front. Prompted by a generated book cover that came back lightly edited with a paragraph of critique that neither the edit nor a later redo fully applied. Added to the critique loop (steps 0a and 3b, hand-off), the critique template (*Sign-off blurb*, *Delivery checklist*), `AGENTS.md`, `SKILL.md`, the Cursor rule, `lite/`, `llms.txt`, the skill zip's modes and the README.
- **Font library and TYPE-10.** New `fonts/`: 60 free families (SIL OFL 1.1 or Apache 2.0, unmodified from google/fonts, licence file in every folder) in 18 themes, plus Fraunces and Instrument Sans listed from `docs/assets/src/fonts/`. `catalogue.json` and `CATALOGUE.md` give per family the themes, licence, source, axes or weights, good for, avoid and pairings; `fonts/build.py` renders a specimen sheet per theme and an overview. New rule TYPE-10: pick type from the theme catalogue to suit the brief's genre and tone, and don't reuse one family across unrelated briefs (sources S154-S157). The skill zip carries the catalogue (no font files). Token counts in `which-modules.md` updated.

Changes after a third outside review (by Claude, consulted by the owner).

- **Anatomy pass (CHAR-9, CHAR-10): a delivery gate.** Whenever a person, hand or animal is in the frame, crop each hand, limb join, face and animal head at 2x-4x and record one pass/fail line per check: hand count, finger count, trace to the shoulder on the correct side, thumb side, grip (Napier's power and precision grips), joint direction, merges and extras, eyes and teeth, animal counts. Any fail blocks delivery; the whole pass re-runs after every image edit. Replaces the optional zoom audit. Added to the critique loop (step 2b, fix and stop rules), the critique template (*Anatomy pass* section), `which-modules.md`, `AGENTS.md` and `lite/`. CHAR-3 gains a grip check. New tool `tools/anatomy_crops.py`; new example `examples/character-anatomy-pass/` (a delivered cover with an orphan hand that light, edge and type checks had passed). Sources S149-S153.

- **Aesthetic layer: restyle, don't add story.** New working rule in `modules/aesthetic-critique/` and in AES-10: an aesthetic change may restyle what the brief gives (light, palette, composition, crop, texture, finish, type styling) but may not add characters, creatures, objects, text or claims unless the brief leaves room or the owner signs off; additions are marked [inferred] and listed. AES-10's check now lists every new visible element and re-checks light direction (TD-LIT-1). Critique template gains an *Additions* line; the lite file gains one sentence.
- **Hero fixes.** Aesthetic fox cover re-made (one image edit): robin and fireflies removed, book no longer glows, one key light from the low sun (sun side lighter on fox head, body and trunk), fox larger; contrast re-checked (title 9.07:1, author 5.68:1 worst). Round 1 kept as `fox-aes-r1.jpg`. Aesthetic poster: one edit to put the bass inside the lamp's light with double-bass proportions failed (rejected attempt kept in `src/`), so the poster is unchanged and its TD-LIT-1 fault is captioned in the README hero.
- **Reference set audit.** Pieces 01, 03, 04 and 12 (07 borderline) labelled as breaking the new AES-10 rule for added content (torch beam, moth, suitcase, satchel, bookmark, dome glow, dot field). Not regenerated.
- **Equal effort.** The unequal-rounds disclosure is now a callout at the top of the reference set and the benchmark README; the protocol now requires both conditions to get the same number of rounds and image budget.
- **README.** Install (Grok Bot, Claude, other tools) moved up under the hero; the Claude upload steps re-checked against Anthropic's help page (Customize > Skills > + > + Create skill > Upload a skill; code execution on in Settings > Capabilities) and linked; "Correctness and quality" cut to two lines plus a collapsed section.

- `examples/aesthetic-benchmark/reference-set/` (was `blind-ab-01/`): blind judging dropped; now an open, labelled reference set of 12 pieces (no skill / rules / rules + aesthetic layer), answer key, briefs and making log published. Originally:: blind A/B run 01, 12 briefs across 12 media, rules only vs rules plus the aesthetic module, made and blinded by Grok Bot, not yet judged. Judging sheet, printable form, prompt for outside model judges, sides-swapped second pass. Answer key and sources withheld; their salted SHA-256 hashes are committed for later checking.
- Benchmark protocol: commit a salted key hash before judging; same start and equal effort between conditions, or report the confound.

## v0.4.0 (1 November 2026)

An aesthetic layer, built from an outside review by an AI reviewer the owner consulted. The review's point: the rules make work correct, but correct isn't the same as good, and the baseline showed it (the with-skill poster lost on atmosphere). Its proposal was paraphrased and adapted here, not copied.

**New module: `modules/aesthetic-critique/`** (about 2,050 tokens, no new blockers)
- AES-0 intent model at step 0: purpose, audience, mood, style, focal experience, degree of polish, must-keeps, each marked [brief] or [inferred]; five questions to tell a deliberate choice from an accident.
- AES-1 to AES-8, short diagnostic prompts (visible feature, effect, action), cross-linked to the existing rules rather than repeating them: composition and rhythm, emphasis, colour intelligence, shape language, craft, originality and specificity, emotional and narrative charge, coherence and art direction.
- AES-9 pairwise judgement as the verdict: which version is stronger for the brief, the strongest difference, what caused it, what it costs, strong or marginal (checked by swapping sides), and "none is good enough" allowed. No averaged scores.
- AES-10 revision with a regression check: one or two aesthetic changes at a time; keep, refine or revert; measured checks re-run.

**Core**
- `critique-loop.md`: intent model at step 0; measured vs interpreted findings in step 3; aesthetic changes compared side by side in step 4.
- `critique-template.md`: an intent line, separate MEASURED and INTERPRETED findings sections (only measured ones block; disagreements are stated, not settled toward neatness) and a comparison section.
- `which-modules.md`: routing row and quick question for aesthetic-critique; token table recounted.
- `AGENTS.md`, `SKILL.md`, the Claude Skill zip and `lite/` updated to match.

**References and testing**
- `docs/references.md`: 27 public works (museum collections, the V&A, Tate, Rijksmuseum, award-winning books and games, design systems) across composition, colour, shape, storytelling, restraint, art direction, stylisation, rule-breaking, polished-but-generic and rough-but-effective, each with a short note. Links only; no images copied. Links checked 1 Nov 2026. One gap stated: no reputable archive of exemplary product renders was found.
- `examples/aesthetic-benchmark/`: a blind A/B protocol (rules only vs rules plus the module; anonymised, side-swapped pairs; pairwise preference, brief fidelity, distinctiveness, coherence, revision success, regression rate, technical compliance, inter-rater agreement; a blind original-vs-revised test). Not yet run.
- One demo, **one sample, self-judged, not evidence**: the v0.3.1 poster with its atmosphere won back (night street, lamp at true scale; one image call, type set in code). All contrast checks pass. Verdict: stronger on atmosphere; costs stated (busier, title second at blur, bass just outside the drawn light).
- Six sources added (S143-S148): comparative judgement, the consensual assessment technique, model-judge position bias, a text-to-image preference dataset, Krippendorff's alpha.

**Other**
- README: short "Correctness and quality" section. Gallery: one card (24). `tools/README.md` lists `package_skill.py`.

## v0.3.1 (1 November 2026)

Response to an outside review of the repo.

**README**
- Plain pitch at the top: the skill gives restraint and accuracy, not flair, and says where it loses.
- New hero: the with-and-without baseline (light and dark, built by `docs/assets/src/build.py baseline`, checked at 390 px). The three earlier before/after pairs are folded under it.
- Link row near the top: gallery, Grok Bot install, Claude Skill zip, lite version. New "Install in Claude" section (claude.ai, Claude Code, Projects).

**Baseline redone (`examples/baseline-comparison/`)**
- The with-skill fox cover and jazz poster are now complete pieces: new art generated with no text, then all type set in code (`src/compose.py`, Fraunces and Instrument Sans) using only the brief's facts, judged against TYPE, LAY and CORE rules, 2 rounds (cover) and 3 rounds (poster). The poster's glow blob is gone. Without-skill versions unchanged.
- Honest result: the with-skill versions win on accuracy, hierarchy and legibility, and still lose on first-impression energy and atmosphere. The earlier art-only versions are kept as `*-image-only.jpg`.

**Claude Skill package**
- `tools/package_skill.py` builds `creative-director-skill.zip`: `creative-director/` with `SKILL.md` (frontmatter checked against Anthropic's Agent Skills rules; body is the full `AGENTS.md` instructions plus the three modes), `core/`, `modules/`, `lite/`, `tools/`, `SOURCES.md`, `LICENSE`. No examples or images. Attached to this release.

**Cross-model**
- Two outside pilot runs added under `examples/cross-model/runs/`, both labelled **contaminated, not a score** (each model had read the rubric first):
  - `claude-opus-5.5-2026-11-01` (claude.ai): loaded the repo, ran `vp.py` and `ellipse.py` itself, cited correct rule IDs, made a take-over rework that passes contrast (lowest 6.11:1) and 390 px, and asked owner questions.
  - `gpt-6-2026-11-01-pilot` (ChatGPT): with and without answers written in one chat; no tools run, so no measurements. Its HTML rework was rendered and checked here (`VERIFY.md`): passes contrast, 390 px and 200% text.
- What they suggest: the baselines already found most faults (4 or 5 of 5); the skill added structure (blockers first, rule IDs, brief kept intact, confidence stated) and, with the tools, measured numbers. A clean, blind run is still wanted. The kit now warns not to let the model read `RUBRIC.md` or `examples/` first.

**Housekeeping**
- `PROPOSED-REPO.md` and `DECISIONS.md` moved to `docs/`.
- Gallery: baseline cards updated, two pilot-run cards added (23 cards).
- Repo About, homepage (gallery) and topics set.

## v0.3.0 (1 November 2026)

**New modules**
- `modules/typography/` (TYPE-1..9): pairing, one scale, size floors, measure, leading, tracking at display sizes, hierarchy, typesetting details, the generic AI type look. TYPE-3 is a blocker below the size floor.
- `modules/layout/` (LAY-1..9): grids, margins, focal point, platform specs for X, LinkedIn, Instagram, YouTube, GitHub and Open Graph (checked 1 November 2026, with sources), safe areas and feed-size legibility (blockers), posters, slides, print (bleed, 300 ppi, CMYK; blocker for print).
- `modules/brand/` (BRAND-1..7): reading a guide into a token sheet, colour, type, logo (blocker), voice, consistency, and working without a brand.
- `modules/character/` (CHAR-1..8): proportion systems, landmarks, hands, faces, realism level, weight, limbs, stylisation, plus a zoom audit for generated figures. Hands, eyes, limbs and realistic landmarks are blockers.

**Core**
- `core/brand-intake.md`: a seven-question intake at step 0 when the brief has no brand input, with a labelled "assumed" sheet when there are no answers. Addresses the known miss that a generic look needs brand input, not more rounds.
- `core/evidence.md`: new myths (serif vs sans, the 66-character line, word shape, golden-ratio faces, the uncanny valley as one curve, 72 dpi).
- `core/which-modules.md`: routing for the new modules; token table re-measured.
- `AGENTS.md`, `core/critique-loop.md`, `lite/`: brand intake at step 0; new blockers in the lite file.

**Examples**
- `layout-social-card`, `typography-scale`, `brand-intake`, `character-hands` (small, one per module).

**Tools**
- `tools/ellipse.py`: RANSAC fit over all edge pixels in the box (side lines no longer pull it), a new end check that flags pointed ("lemon") and flattened ends, and a tilt report. It now catches the planted lemon in `technical-drawing-takeover`, which v0.2.0 missed. Tests: `tools/tests/ellipse_cases.py`, 32/32 synthetic, 4/4 example images.
- `tools/intersect.py` (new): intersecting parts, floating parts and near-miss gaps in GLB/OBJ/STL models (trimesh, manifold3d). Names the stool's leg through the seat directly, where model-qa reported it as asymmetry. Tests: 8/8 (6 synthetic, stool broken and fixed). The stool example now ships `stool-before.glb` / `stool-after.glb`.
- `tools/grid.py` (new): layout-grid check from a screenshot: alignment lines, boxes 2-6 px off them, uneven rows (tops, steps, gaps, padding), and gaps on a 4/8 px scale. Tests: 18/18 (6 synthetic, 12 example screenshots).
- `tools/requirements.txt`: trimesh, rtree, manifold3d.

**Cross-model kit**
- `examples/cross-model/`: three tasks (web UI fix, illustration critique, technical-drawing critique) with inputs, exact prompts with and without the skill for Claude, ChatGPT and Gemini, a rubric tied to rule IDs, a results template, and `.github/ISSUE_TEMPLATE/cross-model-run.md`. No runs exist yet.

**Docs**
- `docs/gallery/`: the four new examples and the v0.3.0 ellipse check added; filters for layout, typography, brand and character.
- `docs/assets/social/card-1280x640.png`: GitHub social preview (2:1, 80 px margins on every side, 12.5% of the short side), built by `docs/assets/src/social.py github`. Answers finding 3 in `examples/layout-social-card/`. Upload it by hand in the repo's Settings > Social preview.

**Sources**: S111-S142 (32 new).

## v0.2.0 (1 November 2026)

**Examples**
- Five new stress tests across every domain: take-overs of deliberately bad work in web UI, illustration and technical drawing; nudges for a UX sign-up form and a 3D product render (real Blender renders, model-qa checks).
- `examples/common-failures/`: one small case per common agent failure (spacing, grid, type scale, icon set, SVG perspective, floating and intersecting 3D parts), with links to the larger examples for contrast, mobile layout and form errors.
- `examples/baseline-comparison/`: the same two prompts with and without the skill, same image tool, labelled. Includes a "cross-model runs wanted" note with the prompts to reproduce.
- `examples/README.md`: a detected-and-fixed table for every example and an **Honest misses** section (where the loop made things worse or a tool missed).

**Docs**
- `docs/gallery/`: a static before/after gallery, filterable by module, linking to each critique log.
- `lite/CREATIVE-DIRECTOR-LITE.md`: the loop, core rules and blockers in about 1,300 tokens.
- README: Requirements section (vision, a way to render, recommended setup) and a new banner typeface (Fraunces).
- `core/which-modules.md`: approximate token cost per module (tiktoken cl100k).
- `tools/README.md`: notes a known `ellipse.py` miss (pointed ellipses when other lines share the fit box).

## v0.1.0 (1 November 2026)

- Initial release: core principles, creative direction (CD-1..6), the critique loop and template, evidence notes and sources.
- Modules: technical drawing, illustration, web UI, UX, 3D.
- Tools: look tests, WCAG contrast, screenshots, vanishing points, ellipses, before/after.
- First examples, including the README's own critique.
- Entry points for Cursor, Claude, Codex/Gemini/Jules (AGENTS.md), Copilot and llms.txt. MIT licence.
