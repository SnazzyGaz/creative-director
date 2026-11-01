# Changelog

## Unreleased (1 November 2026)

Examples and README only; nothing in the skill zip changed, so no new release.

- **Hero lighting fixes (TD-LIT-1).** Aesthetic poster: after two more image edits (the first rejected, kept in `src/`), the bass now stands in the lamp's light, lit from the lamp side with its shadow falling away, and is drawn as a double bass (sloped shoulders) rather than a violin; type unchanged, contrast re-checked (all pass). It is `poster-aes-r3.jpg`; the round 2 art is kept. Middle "with the skill" fox cover: the art prompt had asked for a glowing book, which lit the fox's face from below against the low sun; one edit made the book plain paper (`fox-with-r3.jpg`, old art kept as `src/fox-art-r1-glowing-book.jpg`), contrast re-checked. Side-by-sides, look sheets, gallery text and the README hero (light and dark) rebuilt; the hero's "known fault" caption replaced with what was fixed.
- **Anatomy sweep.** New `examples/anatomy-sweep/`: CHAR-9/10 run over every image in `examples/` and the hero, with crops for the fixed images. No delivered, with-skill or aesthetic-layer image failed; without, before and input images are noted, not changed.
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
