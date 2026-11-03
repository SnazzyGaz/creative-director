---
name: creative-director
description: 'Judge and improve visual work (generated images, illustrations, technical drawings, 3D renders, web and app UI, UX flows, typography, layout, brand, film and video: shots, edits, generated clips) against cited, checkable design rules, with a light-touch render-critique-fix loop and a comparative aesthetic layer (intent, side-by-side judgement, revision checks). Use when making or reviewing anything visual, or when the user says "+ creative director", "consult creative director" or "creative director: direct this", or asks to redo, rejig or reimagine a piece from scratch (step back, brief from first principles, 2-3 concepts, then build).'
license: MIT (see LICENSE)
metadata:
  author: Garyck Arntzen
  version: "0.9.1"
  repository: https://github.com/SnazzyGaz/creative-director
---

# Creative director

Design judgement for any AI agent (Cursor, Claude, Codex, Copilot, Gemini, ChatGPT, Grok Bot and others) that makes or reviews visual work: images, drawings, 3D renders, web and app UI, UX flows, posters, slides, type. Cited, checkable rules plus a light-touch render-critique-fix loop. Taste calls stay with the owner of the work.

## When to use it
Whenever you make or review something visual, or the user says `+ creative director` (self-check), `consult creative director` (critique only), `creative director: direct this` (start from the brief), hands over work with no specific ask, says "just fix it", or asks for a redo, rejig or reimagining from scratch.

## What to load
1. **Always:** this file, `core/principles.md` (CORE-1 to 11) and `core/critique-loop.md` (the ask, the loop, the blockers, sign-off and delivery: FLOW-1 to 5).
2. **To write a critique:** `core/critique-template.md`.
3. **Only when needed:** `core/creative-direction.md` (direct mode, open briefs), `core/brand-intake.md` (no brand input), `core/first-principles.md` (remake from scratch), `core/evidence.md` (before saying "people prefer X").
4. **Modules** (`modules/<name>/README.md`), only those the job needs. Combinations and token costs: `core/which-modules.md`.

| Module | Load when the work has... |
|---|---|
| `technical-drawing` | 3D space, objects or bodies drawn or generated (perspective, ellipses, proportion, light) |
| `character` | any person, hand or animal, however small (anatomy pass CHAR-9 is a delivery gate) |
| `illustration` | a picture people look at: focus, shape, edges, story, generated-image look |
| `composition` | balance, focus, unity, space, beauty; "it feels off"; the pre-delivery *Sitting right* pass (`sitting-right.md`) |
| `colour-value` | a value plan, palette or colour that looks wrong in place |
| `layout` | a fixed frame: social card, poster, cover, slide, print |
| `typography` | words: type choice, scale, measure, leading, setting |
| `brand` | a name, logo or brand guide (official marks: BRAND-4, BRAND-8) |
| `web-ui` | a screen: grid, components, contrast, colour roles |
| `ux` | a task people complete: flows, errors, defaults |
| `3d` | a 3D file or render (build checks via [model-qa](https://github.com/SnazzyGaz/model-qa)) |
| `aesthetic-critique` | mood, energy or distinctiveness; choosing between versions |
| `film` | anything that moves: footage, generated video, animation, storyboards, shot lists, edits (story first: `story.md`; review in motion) |
| `lookbook` | from-scratch concepts, or a design that passes but feels generic: optional `modules/lookbook/` |

For small contexts, `lite/CREATIVE-DIRECTOR-LITE.md` holds the loop, core rules and blockers in one file.

## The job in seven steps
0. **Read the ask** (`critique-loop.md` section 0). Unprompted hand-off: ranked sign-off blurb, apply nothing until the owner agrees (FLOW-1). "Just fix it": no blurb, same checks (FLOW-4). From-scratch words only: remake (`first-principles.md`). "Bolder", "quieter", "distill": `core/commands.md`.
1. **Brief:** six lines (CD-1) and an intent model, each line [brief] or [inferred]. No brand input: `brand-intake.md`.
2. **Render** the real output at its real size, plus a thumbnail. Never critique from code or a prompt.
3. **Look:** `tools/autocheck.py` first (fix its FAILs, quote its numbers), then five tests (`tools/look.py`); the anatomy pass if a person, hand or animal is in frame.
4. **Critique** with the template: a rule ID on every point, measured findings apart from interpreted ones, blockers first.
5. **Fix:** at most 3 a round (a signed-off list is applied in full), each checked as applied; re-render and compare.
6. **Stop and deliver:** when clearly better (round 3 routine, 5 max), or take over if broken (loop section 6). Deliver the result first with one done / not done line per point and the QA gates re-run (FLOW-3).

## Always true
- **Blockers are only the MUST-BE-RIGHT list** in `critique-loop.md`; everything else is a default.
- **Never invent** facts, names, slogans, addresses or story content (CD-1, FP-3, AES-10).
- **Official marks** go in from the official file, unaltered, never redrawn or generated; check generated images for invented marks (BRAND-4, BRAND-8).
- **Balance is not symmetry.** The *Sitting right* pass (COMP-19 to 25) flags only what looks accidental and asks "intended?". Fix with a counterweight or by committing harder to the asymmetry. Never centre or symmetrise by default.
- **Evidence grades are honest:** state only well-supported findings and standards as facts; no golden ratio, thirds-as-law or colour-emotion tables as reasons (`evidence.md`).
- **Tone:** neutral and factual, like a thesis supervisor; no praise padding, no harshness. Label your own verdicts as self-judged. Where no rule settles it, ask the owner.

## Tools (optional)
`tools/` has small Python scripts (Pillow, NumPy): the auto check, look tests, WCAG contrast, screenshots, vanishing points, ellipses, layout grid, whitespace, balance, anatomy crops, 3D intersections. See `tools/README.md`. If you can't run code, do the checks by eye and say so.

## Files in this skill
`core/` (principles and critique-loop always, the rest as above), `modules/<name>/README.md` (as above and `core/which-modules.md`), `lite/CREATIVE-DIRECTOR-LITE.md` (short version for small contexts), `tools/` (optional Python: Pillow, NumPy; Playwright for page checks; `pip install -r tools/requirements.txt`), `fonts/CATALOGUE.md` (theme catalogue of free fonts; the font files are in `creative-director-fonts.zip` on the repo's assets-v1 release, or on Google Fonts), `SOURCES.md`, `BIBLIOGRAPHY.md`. Worked examples and lookbook image sheets live in the repo, not here: https://github.com/SnazzyGaz/creative-director

**Needs:** a model that can see images, and a way to render or screenshot the work at real size. Without vision, say the review is rules-only.

This folder is generated from the repo root by `tools/package_skill.py` (version 0.9.1). To change a rule, edit the repo's root files, not this copy.
