# Creative director, lite

A short version of this repo for tools with a small context window. It keeps the loop, the core rules and the blockers. The full rules, checks and sources are in `core/` and `modules/`. Use the full version when you can.

## The loop

Always judge a fresh render or screenshot, never your own code or prompt.

0. **Brief.** Before making anything, write down: purpose, audience, where it will be seen, must-keeps, and what "done" means. Don't invent facts the brief doesn't give (names, prices, addresses, slogans). No brand input? Ask the owner for name, audience, colours, type, three voice words, likes and dislikes; if no answer, label your choices as assumed. Add the intended mood, style and degree of polish, marked [brief] or [inferred]. Before calling a choice a flaw, ask whether it looks deliberate and whether it works.
1. **Render** at the real viewing size plus a thumbnail. UI: phone (390 px), desktop (1280 px) and 200% zoom. Keep every round (`round-01.png`, ...).
2. **Look** with five tests, one factual line each: blur (what leads?), thumbnail (does the idea survive?), flip (lopsided or tilted?), greyscale (is the value structure there?), edges and corners (tangents, stray spots).
3. **Critique.** List the rule IDs in scope first. Every point names a rule, the evidence and one fix. No rule, no point: it becomes a question for the owner. Record what already meets the criteria, so it is kept. Rank by effect, structure before surface, five points at most. Neutral and factual: no praise, no harshness. Measure at 2x zoom or with a tool before calling a failure. Keep measured findings (tool-checked; only these can block) apart from interpreted ones (aesthetic: name the visible feature, its effect and the trade-off, and label it as interpretation).
4. **Fix** at most 3 things per round, blockers first. Smallest change that works; keep the subject, style, mood and layout idea. Re-render, compare side by side, and **check each fix actually applied**. Revert anything that made it worse. For mood or energy, change one or two things, then judge old and new side by side for the brief (which is stronger, why, at what cost, strong or marginal; "neither" is allowed), not by score.
5. **Stop** when no blockers remain and the top points are done, when a round is not clearly better, when what is left is taste, or at round 3 (5 at most). Hand off: latest and previous render, what changed with rule IDs, what was left and why, and questions for the owner. The owner decides when it is finished.

**Take over** (rework, no 3-fix cap) when: 3+ blockers at once, or one that breaks the whole piece; it fails blur and thumbnail outright; it would need more than 3 rounds; or it is unusable for its purpose. Say it is a rework and why. Re-read the brief first, keep its idea and must-keeps, then run the normal loop on the new version.

## Blockers (MUST-BE-RIGHT)

Only these block. Everything else is an improvement.

- **Perspective:** one horizon per picture; objects on one ground plane share it; verticals vertical unless 3-point is intended; foreshortening matches distance (TD-PER-1..5).
- **Ellipses:** the minor axis follows the cylinder's axis; ellipses get fuller further from eye level; smooth and symmetrical, no lemons or footballs (TD-ELL-1..3).
- **Proportion and anatomy:** measured, not guessed; left and right agree (TD-PRO-1..2).
- **Light:** one key light direction; lit and shadow sides stay separate; cast shadows sit on the ground (TD-LIT-1..3).
- **Figures:** right digit count per hand, thumbs on the correct side; eyes match and look at one point; every limb traceable, none fused or extra (CHAR-3, CHAR-4, CHAR-7).
- **Fixed frames (social, thumbnails, print):** key content inside the platform's safe area; main message readable at feed size (about 400 px wide); print has 3 mm bleed and 300 ppi at final size (LAY-5, LAY-6, LAY-9).
- **Type size:** no reading text under 14 px, nothing meaningful under 12 px (TYPE-3).
- **Logo:** the supplied file, unaltered, with its clear space and minimum size (BRAND-4).
- **Contrast:** text at least 4.5:1; 3:1 for large text (about 24 px) and for UI boundaries; never colour as the only signal (UI-6).
- **Zoom:** text can grow to 200% without clipping or overlap (UI-10).
- **Flow:** the main task can be completed, with every step reachable (UX-1).
- **3D:** built correctly: no high or medium model-qa issues unless intended (floating, intersecting, flipped or duplicate parts) and the right size and way up (3D-1, 3D-2).

## Core rules (all work)

- **CORE-1 One hierarchy.** One thing leads, then a clear second and third. Check with blur.
- **CORE-2 Value before colour.** The greyscale version must still read.
- **CORE-3 Contrast where it matters.** Strongest contrast at the focal point, nowhere else.
- **CORE-4 Spacing groups things.** Related items closer; spacing from one scale.
- **CORE-5 Align to something.** Shared edges and a grid.
- **CORE-6 Colour with a job.** Each colour has a role; few accents.
- **CORE-7 Type that reads.** One or two families, a few clear size steps.
- **CORE-8 Restraint.** Remove before adding; every element has a reason.
- **CORE-9 Consistency.** Same thing, same look (icons, buttons, radii, strokes).
- **CORE-10 Reads at its real size.** Check at the size people will see it.
- **CORE-11 Balance by visual weight.**

## Common module checks

- **Illustration:** one focal point (ILL-2); clear silhouettes (ILL-3); plan values, then palette (ILL-4); hard edges only where you want attention (ILL-5); avoid the generic AI look: rainbow glow, sparkles, light from everywhere (ILL-11).
- **Web UI:** one type scale (UI-1); spacing from a scale (UI-3); a grid and one obvious primary action (UI-4); consistent components with visible states (UI-5); avoid generic AI tells such as gradient blobs, emoji icons and three identical cards (UI-7).
- **UX:** errors prevented, then explained in place with the input kept (UX-3); plain language (UX-6); labels stay visible (UX-7).
- **3D:** physically plausible materials (3D-6); a view transform that doesn't clip (AgX in current Blender, not Standard; 3D-7).

## Myths: don't use as reasons

The golden ratio, the rule of thirds as a law, and fixed colour-emotion claims. Cite a rule, not a myth.
