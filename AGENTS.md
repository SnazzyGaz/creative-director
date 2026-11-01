# AGENTS.md — creative-director

Instructions for any AI agent (Cursor, Claude Code, Codex, Copilot, Gemini, ChatGPT, Grok Bot, etc.) using this repo to judge and improve visual work: images, drawings, 3D renders, web and app UI, UX flows.

## When to use it
Use it when you make or review something visual, or when the user says `+ creative director`, `consult creative director`, or `creative director: direct this` (see README "Usage").

## How to use it
1. Read `core/principles.md`, `core/critique-loop.md` and `core/creative-direction.md`.
2. Use `core/which-modules.md` to load only the modules the job needs (`modules/<name>/README.md`).
3. Check the brief first (CD-1). If there is no brief, write the six-line brief and state your assumptions. If it has no brand input, run `core/brand-intake.md` (ask the owner; if no answers, label assumptions). Write the intent model too (purpose, audience, mood, style, focal experience, polish, must-keeps), marking each line from the brief or inferred.
4. Render or screenshot the real output at its real size. Never critique from code or a prompt alone.
5. Run the five look tests (`tools/look.py` if you can run Python), critique with `core/critique-template.md`, citing a rule ID on every point. Keep MEASURED findings (checked with a tool) apart from INTERPRETED ones (aesthetic readings tied to a visible feature, labelled as interpretation). If a person, hand or animal is in frame, run the anatomy pass (`modules/character/`, CHAR-9): crop and check every hand, limb join, face and animal head; any fail blocks delivery. For mood, energy or distinctiveness, load `modules/aesthetic-critique/` and judge versions side by side, not by score.
6. Make at most 3 fixes per round, blockers first, and check each one actually applied. Aesthetic changes: one or two at a time, then keep, refine or revert, and re-run the measured checks. Re-render and compare. Stop when clearly better (round 3 routine, 5 max), or take over per section 4b if the work is fundamentally broken.
7. Hand off: before/after, rules judged, what changed, what was left, and questions for the human. Taste calls belong to the owner of the work.

## Tone
Neutral and factual, like a doctoral supervisor. Every point is tied to a named criterion. No praise padding, no harshness. Light touch: preserve the intent and what already works.

## Tools (optional)
`tools/` has small Python scripts: look tests, WCAG contrast, screenshots, vanishing points, ellipses, before/after sheets. See `tools/README.md`. If you can't run code, do the same checks by eye and say so.
