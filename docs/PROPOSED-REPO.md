# Proposed GitHub repo (original plan)

The plan the repo was set up from. Kept for reference.

## Name and home
- Suggested: `SnazzyGaz/creative-director` (matches the folder name and the existing `model-qa` / `bot-creative-toolkit` naming: short, lower-case, hyphenated).
- Alternatives: `design-judgement`, `bot-design-critic`.

## Structure

```
creative-director/
  README.md            what it is, light-touch purpose, how bots use it
  AGENTS.md            one-page instructions for any agent (same role as in model-qa)
  skills/creative-director/SKILL.md   wrapper for agents that load "skills" (points at core/)
  core/                principles, evidence (preference research and myths), critique loop, template, which-modules
  modules/             technical-drawing, illustration, character, web-ui, ux, 3d, typography, layout, brand (each README; optional notes.md for depth)
  examples/            worked critiques (round-by-round), using generated or openly licensed images only
  tools/               optional small scripts: blur/greyscale/flip/thumbnail sheet, WCAG contrast check, ellipse fit, PBR range check, 200% zoom diff
  SOURCES.md
  CHANGELOG.md
  LICENSE
```

## Naming conventions
- Folders and files: lower-case, hyphenated (`web-ui`, `critique-loop.md`).
- Rule IDs: `CORE-n`, `TD-PER-n`, `TD-PRO-n`, `TD-LIT-n`, `TD-ELL-n`, `TD-CON-n`, `ILL-n`, `UI-n`, `UX-n`, `3D-n`. IDs are never reused or renumbered; retired rules are marked "retired" so old critiques still make sense.
- Sources: `[Sn]`, listed once in `SOURCES.md`.

## How bots load it
1. Clone or fetch raw files (no install needed; it's Markdown).
2. Read `AGENTS.md` -> `core/principles.md` -> `core/which-modules.md` -> only the modules needed (READMEs; `notes.md` and `core/evidence.md` on demand).
3. Run `core/critique-loop.md` on each render; write critiques with `core/critique-template.md`.
4. For 3D, also install `model-qa` and `bot-creative-toolkit` and follow their `AGENTS.md`.
5. Optional `tools/look.py` would produce one sheet (original | blur | greyscale | flipped | thumbnail) so a bot spends one image view per round instead of five.

## Versioning
- Tag releases (`v0.1.0` first public draft). Note rule additions/changes in `CHANGELOG.md` so bots and people can see what moved.

## Licence
- **MIT for everything** (text, scripts and examples), chosen by the maintainer on 2026-11-01 to keep it as open as possible. See `LICENSE`.
- Example images are generated for this repo; no copied images from cited sources.
- Cited works stay their authors' copyright; the repo only paraphrases and links.

## Before going public
- The maintainer reviews every rule marked as a default (non-MUST-BE-RIGHT) and the open questions in the hand-off.
- Add 2-3 worked examples from real bot output with before/after renders.
- Decide whether `tools/` ships in v0.1 or later.
