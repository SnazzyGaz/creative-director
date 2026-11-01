# Cross-model run: Claude Opus 5.5, 1 Nov 2026

**Condition:** with the skill, full route (repo checkout + `lite/`, `core/`, modules, `tools/`), claude.ai with code execution.
**CONTAMINATED:** the model had read `RUBRIC.md` (answer keys) and the examples README earlier in the same chat. No baseline was run (impossible after reading the skill). Do not merge as a clean result; use only as a smoke test of the kit and tools.

## Task C: technical drawing (consult)
Tools: `vp.py detect` then `vp.py fit` on my own grouping; `ellipse.py` with a vertical axis.

1. **TD-PER-1 (blocker):** L VP (-363, 56), R VP (1515, 253): horizon tilted 6.0 deg, VPs 197 px apart in height. Fix: pick one horizon and re-aim both edge families at it.
2. **TD-PER-3 (blocker):** box verticals lean -7.6 (left), -3.9 (front), +2.2 deg (right); tin sides +2.9/+3.4. Fix: true verticals (two-point, above eye level as briefed).
3. **TD-ELL-1 (blocker):** top and base ellipses' minor axes 12.8 and 11.9 deg off vertical (the tin axis). Fix: minor axis on the tin's centre line.
4. **TD-ELL-2 (blocker):** base degree 0.25, top 0.40. Seen from above, the base is further from eye level and must be fuller than the top. Fix: open the base ellipse past the top's degree.
5. **TD-ELL-3 (blocker):** top ellipse end check 0.82/0.74 (pointed, a lemon). Fix: round the ends; draw it through the box diagonals.
- Check, not a fault yet: base ellipse centre (571,357) sits ~15 px behind the lid's diagonal centre (564,372); in perspective it should sit slightly in front. Confirm once C1/C2 are fixed.

## Task A: web UI (direct, take-over)
Blockers 3, so rework.
1. **UX-1 (blocker):** "Submit"/"Go" are spans with no target; at 390 px the pre-order box is clipped off the right edge. Pre-order cannot be done.
2. **UI-6 (blocker):** 10/10 measured text pairs fail; worst 1.25:1 ("Go"), body pre-order text 1.43:1.
3. **UI-10 / CORE-10 (blocker):** fixed 1250 px absolute layout; tagline and pre-order box run off-screen at 390 px.
4. **UI-1 / CORE-7:** seven declared families (none load, so fallback mix).
5. **CORE-1 / UI-4 / CORE-8 / UX-6:** no reading order; "click"/"here" buttons; nine nav items for pages that don't exist; filler copy ("Allergens: may contain everything", "Follow us on 9 platforms"); marquee renders as an empty band.

Rework: `crumb-and-co.html`. One column, the idea as the headline, one action. Fix check: action visible at 390 px (yes), all text pairs pass (min 6.11:1), no horizontal scroll at 390 px or 200% text (yes), must-keeps present (yes; #E8743B kept as accent rule/borders, 2.79:1 on cream so not used for text, darker #9E4012 carries text).
**Owner questions:** the only real pre-order route on the page was the phone number, so the button is `tel:`; swap in an online order link if one exists. Allergen info removed as unusable; needs real wording. Nav removed (no pages given).

## Task B: illustration (consult)
Look tests: blur leads with the lamp and rainbow sky; cat dark on dark rocks in greyscale.
1. **TD-LIT-1 (blocker):** light from the lamp, a burst behind the tower, lightning both sides, glowing sparkles on the rocks. Fix: one key (the lamp), storm light as a dim secondary.
2. **ILL-2 / CORE-3:** the cat is not where contrast peaks; lamp and sky are. Fix: rim-light the cat from the beam, push sky values down.
3. **CD-5 / ILL-6:** no keeper's small boat: a tall ship and a wreck instead; the cat looks out to sea, but at nothing. Fix: one small rowing/fishing boat in the beam, cat's head turned toward it.
4. **ILL-11 / CORE-8:** generic AI look: rainbow nebula, sparkles everywhere incl. rocks, god rays, even detail. Fix: remove sparkles and nebula, soften background edges (ILL-5).
5. **ILL-4 / CORE-6:** full saturated spectrum, no colour roles. Fix: storm blues/greys, warm lamp and cat as the only warm notes.
- Extra (CD-5): no quiet area for two lines of text; the sky is the busiest region.

## Self-score (inflated: key was known)
| | C | A | B |
|---|---|---|---|
| Found | 5/5 | 5/5 | 5/5 |
| Blockers found | 5/5 | 3/3 | 1/1 |
| Ranked | 1 | 1 | 1 |
| False alarms | 0 | 0 | 0 |
| Fix check | n/a | 4/4 | n/a |
