# Which modules to load

Always load `AGENTS.md`, `core/principles.md` and `core/critique-loop.md` (plus `core/critique-template.md` when writing a critique). Then add only what the task needs: loading everything wastes attention. A module's `notes.md` is optional depth. Not sure? Use the module table in `AGENTS.md`. Merged or retired rule IDs: `docs/RETIRED-IDS.md`.

| Task | Load |
|---|---|
| Drawing or painting from imagination, concept art, scene | technical-drawing, illustration, composition (+ colour-value) |
| "It feels off", "make it more beautiful": balance, focus, unity, space | composition (+ colour-value) |
| Palette, value plan, colour that looks wrong in place | colour-value |
| Any person, face, hand or animal, even small or partial (drawn, 3D or generated) | character (anatomy pass CHAR-9 required; props CHAR-11), technical-drawing (+ illustration) |
| Construction errors only | technical-drawing |
| Poster, cover, header, social graphic, thumbnail, link preview | layout, typography, composition (+ illustration, colour-value; brand if it carries a name; LAY-16 for covers) |
| Slide deck, print piece (flyer, packaging) | layout, typography (+ brand; BRAND-10 for packaging) |
| Infographic of any kind | layout + `layout/infographics.md` (INF rules; LAY-18 panels; LAY-19 data in code), typography, illustration (+ character, brand); structure pass (EN-4) |
| Menu board, signage, timetable, price list | layout (LAY-7, LAY-17), typography; light energy pass at most |
| Type is the point (wordmark, editorial page, type-led poster) | typography (+ layout or web-ui) |
| A named brand or product, or a brand guide | brand (+ the medium's module); no brand input: `core/brand-intake.md` at step 0 |
| Web page, landing page, pricing, app screen, dashboard (how it looks) | web-ui (UI-12 for mood) + `core/energy-pass.md` (full for heroes, pricing, app home; light for dashboards) (+ typography; brand; lookbook, optional, for the direction) |
| Sign-up, checkout, settings, multi-step task (how it works) | ux (+ web-ui); energy pass skipped |
| A whole product or prototype | web-ui, ux |
| 3D model, prop, asset, scene | 3d (+ illustration for a beauty render) |
| 3D as reference for a drawing | 3d, technical-drawing |
| Logo, mascot, icon set | brand (BRAND-9: one step past the literal), illustration, web-ui (size and contrast) |
| Storyboard, comic, carousel, image sequence | illustration (ILL-7; `notes.md` for transitions), LAY-18 (+ film `story.md`, `review.md` when it plans video shots) |
| Video, film, animation, trailer, clip, shot list | film (README + `story.md` + `review.md`; `edit.md` for grading, cutting, sound, titles; `crossover.md` when unsure) + composition, colour-value for key frames (+ typography, character) |
| Clip made or altered by a video model | film (+ `generated.md`), character, brand for any lettering |
| Mood, energy or a distinctive feel; correct but flat; choosing between versions | aesthetic-critique (+ the medium's modules, which still decide blockers) |
| From-scratch concepts; correct but generic; naming a described vibe, screens included | lookbook, optional (at most one concept in three; hint strength; never on fixes or edits) |
| Any piece that sells or greets, once the checks pass | `core/energy-pass.md`: full pass for posters, covers, packaging, logos, social cards, picture books, character art, heroes and app home screens; structure pass for infographics; light for notices, dashboards, menus; skip for forms and dense data |
| Just "bolder", "quieter" or "distill" | `core/commands.md` + the medium's modules |
| Remake from scratch ("redo", "rejig", "start over", "reimagine") | `core/first-principles.md` + the medium's modules + aesthetic-critique (AES-9); brand if it carries a mark |
| Image from an AI image model | illustration, technical-drawing; brand for any lettering (BRAND-8); character for people or animals (CHAR-9 gate); exact copy and counts (CD-7) |

## Order of checks when several modules apply

1. Core hierarchy and value (does it read at all?)
2. Blockers (perspective, proportion, anatomy pass, light, broken flows, failing contrast): the MUST-BE-RIGHT list in `core/critique-loop.md`.
3. Energy pass where it applies (`energy-pass.md`): after accuracy and clarity, never instead of them.
4. Composition and layout (`composition/` COMP-1 to 18, with the *Sitting right* pass COMP-19 to 25 in `sitting-right.md` last before delivery; `colour-value/` CV-1 to 11).
5. Surface: edges, texture, micro-spacing, polish.

## Token cost per module

Approximate: counted with tiktoken's `cl100k_base` encoding (`python3 tools/check_budgets.py --loads` prints the current numbers; v0.9.7, 3 Nov 2026). Other models tokenise differently, so expect roughly ±15%. Budgets: the always-on set 6,500, lite 2,500, a module README 6,000, any other rule file 4,500; the CI fails when a file goes over.

| File or set | Tokens |
|---|---|
| `AGENTS.md` (entry point, always) | 1,364 |
| `core/principles.md` (always) | 1,929 |
| `core/critique-loop.md` (always) | 3,160 |
| `core/critique-template.md` (when writing a critique) | 1,482 |
| `core/energy-pass.md` (eye-catch after the checks pass) | 2,761 |
| `core/commands.md` (bolder, quieter, distill) | 1,185 |
| `core/creative-direction.md` (direct mode, open briefs) | 1,706 |
| `core/first-principles.md` (remake from scratch) | 3,233 |
| `core/brand-intake.md` (no brand input) | 701 |
| `core/evidence.md` (before claiming people prefer something) | 2,961 |
| `core/which-modules.md` (this file) | 2,170 |
| `core/interaction-flow.md` (pointer and diagram only) | 724 |
| `modules/3d/` | 1,896 |
| `modules/aesthetic-critique/` | 3,160 |
| `modules/brand/` | 3,900 |
| `modules/character/` | 4,211 |
| `modules/colour-value/` | 4,205 |
| `modules/composition/` (README 5,730, COMP-1 to 18; `sitting-right.md` 3,505, COMP-19 to 25, before delivery) | 9,235 |
| `modules/film/` (README 5,887 + `story.md` 3,156 + `review.md` 1,422; `edit.md` 3,863 for grading, cutting, sound and titles; `generated.md` 2,262 for generated clips; `crossover.md` 1,375 when unsure; `notes.md` 799, optional film references) | 10,465 |
| `modules/illustration/` (+ notes 493) | 4,296 |
| `modules/lookbook/` (README only; search `looks.json` with `tools/lookbook_find.py`, never load it whole) | 1,289 |
| `modules/layout/` (README 5,974; `infographics.md` 1,611, INF-1, INF-2, INF-4 to INF-6, for any infographic) | 7,585 |
| `modules/technical-drawing/` | 3,038 |
| `modules/typography/` (+ `fonts/CATALOGUE.md` when picking type, about 7,400) | 4,063 |
| `modules/ux/` | 1,917 |
| `modules/web-ui/` (+ notes 447) | 2,755 |
| `lite/CREATIVE-DIRECTOR-LITE.md` (everything in one short file) | 2,498 |
| `BIBLIOGRAPHY.md` (reading list; not needed for a critique) | 4,736 |

Typical loads, with the always-on set and the critique template (about 8,000): a screen (web-ui + ux + energy pass) about 15,400; a social card (layout + typography) about 18,000, plus about 5,700 for the composition README and 3,500 for `sitting-right.md`; a figure (character + technical-drawing + illustration) about 19,500; a poster remake (first-principles + layout + typography + aesthetic-critique) about 24,400; an infographic (layout with `infographics.md`, typography, illustration) about 23,900; a video review (film README, `story.md` and `review.md`) about 18,400, or 24,500 with `edit.md` and `generated.md`. For a pre-delivery check alone, load just `composition/sitting-right.md` (COMP-19 to 25). If that is too much, use the lite file.
