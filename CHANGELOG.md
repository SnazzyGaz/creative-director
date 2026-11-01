# Changelog

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
