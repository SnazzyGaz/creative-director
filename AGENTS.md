# AGENTS.md — creative-director

Design judgement for any AI agent that makes or reviews visual work: images, drawings, 3D renders, web and app UI, UX flows, posters, slides, type. Cited, checkable rules plus a light-touch render-critique-fix loop. Taste calls stay with the owner of the work.

## When to use it
Whenever you make or review something visual, or the user says `+ creative director` (self-check), `consult creative director` (critique only), `creative director: direct this` (start from the brief), hands over work with no specific ask, says "just fix it", or asks for a redo, rejig or reimagining from scratch.

## What to load
1. **Always:** this file, `core/principles.md` (CORE-1 to 11) and `core/critique-loop.md` (the ask, the loop, the blockers, sign-off and delivery: FLOW-1 to 5).
2. **To write a critique:** `core/critique-template.md`.
3. **Only when needed:** `core/creative-direction.md` (direct mode, open briefs), `core/brand-intake.md` (no brand input), `core/first-principles.md` (remake from scratch), `core/energy-pass.md` (eye-catch), `core/evidence.md` (before saying "people prefer X").
4. **Modules** (`modules/<name>/README.md`), only those the job needs: technical-drawing, character, illustration, composition, colour-value, layout, typography, brand, photo, web-ui, ux, 3d, aesthetic-critique, film, lookbook (optional). What each covers, combinations and token costs: `core/which-modules.md`. Any person, hand or animal in frame: `character` (the CHAR-9 anatomy pass is a delivery gate).

For small contexts, `lite/CREATIVE-DIRECTOR-LITE.md` holds the loop, core rules and blockers in one file.

## The job in seven steps
0. **Read the ask** (`critique-loop.md` section 0). Unprompted hand-off: ranked sign-off blurb, apply nothing until the owner agrees (FLOW-1). "Just fix it": no blurb, same checks (FLOW-4). From-scratch words only: remake (`first-principles.md`). "Bolder", "quieter", "distill": `core/commands.md`.
1. **Brief:** start from the idea and the feeling; the rules are the edit pass, not the starting point (guidance). Then six lines (CD-1) and an intent model, each line [brief] or [inferred]. No brand input: `brand-intake.md`.
2. **Render** at real size, plus a thumbnail. Never critique from code or a prompt.
3. **Look:** `tools/autocheck.py` first, then five tests (`tools/look.py`); re-read every fixed string and count (CD-7); the anatomy pass if a person, hand or animal is in frame; then the energy pass.
4. **Critique** with the template: a rule ID on every point, measured findings apart from interpreted ones, blockers first.
5. **Fix:** at most 3 a round (a signed-off list in full), each checked as applied; re-render and compare.
6. **Stop and deliver:** when clearly better (round 3 routine, 5 max), or take over if broken (`core/take-over.md`). The result first, then one done / not done line per point, QA gates re-run (FLOW-3).

## Always true
- **Blockers are only the MUST-BE-RIGHT list** in `critique-loop.md`; everything else is a default.
- **Never invent** facts, names, slogans, addresses or story content (CD-1, FP-3, AES-10).
- **Official marks** go in from the official file, unaltered, never redrawn or generated; check generated images for invented marks (BRAND-4, BRAND-8).
- **Balance is not symmetry.** The *Sitting right* pass (COMP-19 to 25) flags only what looks accidental and asks "intended?". Fix with a counterweight or by committing harder to the asymmetry. Never centre or symmetrise by default.
- **Evidence grades are honest:** state only well-supported findings and standards as facts; no golden ratio, thirds-as-law or colour-emotion tables as reasons (`evidence.md`).
- **Tone:** neutral and factual; no praise padding, no harshness. Label your own verdicts as self-judged. Where no rule settles it, ask the owner.

## Tools (optional)
`tools/` has small Python scripts (Pillow, NumPy): the auto check, look tests, contrast, screenshots, perspective, ellipses, grid, whitespace, balance, anatomy crops, charts, 3D intersections (`tools/README.md`). If you can't run code, check by eye and say so.
