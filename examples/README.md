# Examples: stress tests

Four runs of the critique loop (core/critique-loop.md) on generated work, done as a bot would. Every image here is generated or rendered from code; no third-party images. Each folder has the rounds, the look-test sheets (`look-rNN.png`), the critiques (`critique-rNN.md`) and a short `log.md`.

## Illustration: knight and castle (nudge, 2 rounds)
![before/after](illustration-knight/before-after.png)
Generic prompt gave a sky that out-shouted the knight (CORE-3, ILL-2) and a body lost in the forest (ILL-3, CORE-2). Three edits: simpler sky, mist behind the legs, rim light. The first two applied, the rim light didn't. Values went from murky to two clear groups. Clearly better.

## Web UI: typical "AI" landing page (nudge, 2 rounds)
![before/after](web-ui-landing/before-after.png)
Six text pairs failed WCAG contrast (UI-6 blocker, worst 1.84:1) and the page had 8 generic-AI tells (UI-7). Three code fixes: contrast tokens, less decoration, cards stack at zoom. Now every pair passes (min 5.17:1). It still looks generic, which needs a brand brief rather than another round. Phone view: `web-ui-landing/before-after-390.png`.

## Technical drawing: box and can (take-over, 3 rounds)
![before/after](technical-drawing-still-life/before-after.png)
Vanishing points at different heights and sheared verticals (TD-PER-1, TD-PER-3) triggered a rework (section 4b). The rework gets the construction right, but it dropped the open box from the brief and came out paler. Round 3 fixed a misread and didn't help. More correct, not clearly more appealing.

## README: this repo's own front page (nudge, 2 rounds)
The loop run on `README.md` itself, at 1280 and 390 px. One blocker (banner and diagram text unreadable on a phone, CORE-10) and two spacing and table fixes. Every problem was invisible at desktop width. See `readme-self-critique/`.

## Tools
Tools now live in the top-level `tools/` folder (see `tools/README.md`): `tools/look.py` (five look tests and value stats), `tools/contrast.py` (WCAG ratios), `tools/shot.sh` (headless Chrome at 390, 1280 and 200% zoom), `tools/beforeafter.py`.
