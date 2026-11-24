# Which modules to load (generated from `manifest.json`)

Always load `AGENTS.md` and `core/kernel.md` (≤ 1,600 tokens). Everything else loads on demand via `python3 tools/cd.py load --brief brief.json` or `python3 tools/cd.py rule <ID>`.

Do not edit this routing table by hand — edit `manifest.json` and run `python3 tools/cd.py generate-docs`.

## Task routes (`core-visual` and `optional-domain`)

| Route | Group | Media / Triggers | Files loaded |
|---|---|---|---|
| Poster, cover, header, social graphic, thumbnail, link preview | `core-visual` | poster, cover, book cover, album cover, picture-book cover, header | `modules/layout/README.md`, `modules/typography/README.md`, `modules/composition/README.md`, `modules/colour-value/README.md` |
| Slide deck, print piece, packaging, label | `core-visual` | slide, slide deck, slides, print, print piece, packaging | `modules/layout/README.md`, `modules/typography/README.md`, `modules/brand/README.md` |
| Infographic, chart, diagram, map, fact sheet, timeline | `core-visual` | infographic, chart, diagram, route map, map, fact sheet | `modules/layout/README.md`, `modules/layout/infographics.md`, `modules/typography/README.md` |
| Menu board, signage, timetable, price list, official notice | `core-visual` | menu, menu board, signage, sign, timetable, price list | `modules/layout/README.md`, `modules/typography/README.md` |
| Type-led piece (wordmark, editorial page, type-led poster) | `core-visual` | wordmark, editorial, editorial page, type-led, type-led poster, typography | `modules/typography/README.md`, `modules/layout/README.md` |
| Drawing, painting, illustration, concept art, scene, picture book | `core-visual` | drawing, painting, illustration, concept art, scene, picture book | `modules/illustration/README.md`, `modules/technical-drawing/README.md`, `modules/composition/README.md`, `modules/colour-value/README.md` |
| Technical drawing or construction errors only | `core-visual` | technical drawing, technical-drawing, construction, construction errors only, perspective, orthographic | `modules/technical-drawing/README.md` |
| Any person, face, hand, creature, mascot or animal | `core-visual` | character, character design, creature, creature design, portrait, animal (or `has_people_or_animals: true`) | `modules/character/README.md`, `modules/technical-drawing/README.md` |
| Photograph or photoreal image (shot or generated) | `core-visual` | photo, photograph, photography, photoreal, product photo, food photo | `modules/photo/README.md` |
| Logo, mark, emblem, crest, icon set | `core-visual` | logo, mark, emblem, crest, icon, icon set | `modules/brand/README.md`, `modules/brand/logo.md`, `modules/brand/mark-making.md` |
| Brand guide or brand identity system | `core-visual` | brand, brand guide, brand identity, identity | `modules/brand/README.md`, `core/brand-intake.md` |
| Web page, landing page, pricing section, app screen, dashboard | `core-visual` | web, web page, website, landing page, web hero, hero (or `format.kind: screen`) | `modules/web-ui/README.md`, `modules/typography/README.md` |
| Sign-up, checkout, settings, form, multi-step flow or whole product | `core-visual` | ux, flow, sign-up, signup, checkout, settings | `modules/ux/README.md`, `modules/web-ui/README.md` |
| Balance, focus, composition or colour/value review | `core-visual` | balance, composition, palette, colour, color, value | `modules/composition/README.md`, `modules/colour-value/README.md` |
| Mood, distinctiveness, aesthetic critique or version comparison | `core-visual` | aesthetic, distinctive feel, mood, critique, comparison | `modules/aesthetic-critique/README.md` |
| Variations, visual directions, style exploration | `core-visual` | variations, lookbook, directions, from-scratch concepts | `modules/lookbook/README.md` |
| Storyboard, comic, carousel or image sequence | `core-visual` | storyboard, comic, carousel, image sequence | `modules/illustration/README.md`, `modules/illustration/notes.md` |
| 3D model, prop, asset, scene or render (optional domain) | `optional-domain` | 3d, 3d model, 3d render, 3d prop, 3d scene, blender | `modules/3d/README.md` |
| Video, film, animation, trailer, shot list or generated clip (optional domain) | `optional-domain` | film, video, animation, trailer, clip, shot list | `modules/film/README.md`, `modules/film/story.md`, `modules/film/review.md` |
| Website copy, emails, replies, blurbs, microcopy (optional domain) | `optional-domain` | writing, copy, web copy, website copy, email, email reply | `modules/writing/README.md` |

## Module index

| Module | Group | Entry | Extra files | Covers |
|---|---|---|---|---|
| `layout` | `core-visual` | `modules/layout/README.md` | `infographics.md` | Fixed frames: posters, covers, social cards, slides, print, signage, packaging and infographics. Infographic recipes are less mature until Batch 9 is judged. |
| `typography` | `core-visual` | `modules/typography/README.md` | — | Type choice, scale, measure, leading, display hierarchy and font selection. |
| `composition` | `core-visual` | `modules/composition/README.md` | `sitting-right.md` | Balance, visual weight, focus, unity, space and the pre-delivery Sitting right pass. |
| `colour-value` | `core-visual` | `modules/colour-value/README.md` | — | Value grouping, colour roles, neutral whites, simultaneous contrast and CVD safety. |
| `illustration` | `core-visual` | `modules/illustration/README.md` | `notes.md` | Picture-making, focal hierarchy, silhouettes, edges, storyboards and generated-image tells. |
| `character` | `core-visual` | `modules/character/README.md` | — | People, faces, hands, animals and props, including the CHAR-9 cropped anatomy delivery gate. |
| `technical-drawing` | `core-visual` | `modules/technical-drawing/README.md` | — | Perspective, horizons, ellipses, proportion and consistent key lighting. |
| `brand` | `core-visual` | `modules/brand/README.md` | `logo.md`, `logo-notes.md`, `mark-making.md`, `clever-marks.md` | Official marks, brand systems, packaging identity and logo mark-making (LOGO-1..16). |
| `photo` | `core-visual` | `modules/photo/README.md` | — | Photographs and photoreal imagery: lens distance, camera height, light, casting and AI photo tells. |
| `web-ui` | `core-visual` | `modules/web-ui/README.md` | `notes.md` | Web and app screens: layout grids, components, states, contrast, dark mode, reflow and motion. Less mature until Batch 9 (screens and infographics) is judged. |
| `ux` | `core-visual` | `modules/ux/README.md` | — | Task flows, error recovery, defaults, keyboard focus order and alt text. Less mature until Batch 9 (screens and infographics) is judged. |
| `aesthetic-critique` | `core-visual` | `modules/aesthetic-critique/README.md` | — | Intent modelling, comparative pairwise verdicts, regression checks and novelty-typicality balance. |
| `lookbook` | `core-visual` | `modules/lookbook/README.md` | — | Optional 415 curated visual looks and clusters for controlled 20-50% style bleed on concepts/variations. |
| `writing` | `optional-domain` | `modules/writing/README.md` | — | Optional domain: website copy, emails, replies, blurbs, about pages and UI microcopy (WRITE-1..11). |
| `film` | `optional-domain` | `modules/film/README.md` | `story.md`, `review.md`, `edit.md`, `generated.md`, `crossover.md`, `notes.md` | Optional domain: cinematography, story beats, continuity, editing, grading, sound and generated-video QC. |
| `3d` | `optional-domain` | `modules/3d/README.md` | — | Optional domain: 3D models, renders, scene scale, build QA and Blender/AgX workflows. |

## Energy triggers (intent-gated only)

`core/energy-pass.md` loads only when the brief's `feeling`, `purpose`, `idea`, or `intent_tags` match an energetic intent — never from `medium` alone:

`energetic`, `energy`, `lively`, `playful`, `bold`, `kinetic`, `vibrant`, `exciting`, `dynamic`, `festive`, `celebration`, `festival`, `fete`, `concert`, `gig`, `party`, `carnival`, `comedy`, `children`, `children's`, `kids`, `youth`, `sport`, `run`, `race`, `club`, `nightlife`, `loud`, `punchy`, `dramatic`, `thriller`, `action`, `promotional`, `campaign`

## Maturity

The `web-ui` and `ux` modules, and the infographic recipes in `modules/layout/infographics.md`, are less mature than the rest. Blind-test Batch 9, which covers screens and infographics, is drawn and waiting to be judged.

## Token budgets

Run `python3 tools/check_budgets.py --loads` for live token counts. Budgets are enforced in CI on both Linux and Windows.
