# Creative director, lite

Short version for small context windows; full rules and sources in `core/` and `modules/`.

## The loop

Judge a fresh render or screenshot, never your own code or prompt.

**Read the ask first.** Work handed over with no specific request: reply with a short ranked list of only the imperative changes (rule ID, the change, [edit] or [regenerate]) and wait for sign-off. Then apply every signed-off point, re-check each one and the light, anatomy and type blockers, and deliver with one done / not done line per point. "Just fix it" skips the sign-off, not the checks. Never hand over an unapplied critique as the result.

0. **Brief.** Purpose, audience, where it is seen, must-keeps, what "done" means, and the intended mood, style and polish, each marked [brief] or [inferred]. Count what the brief fixes ("it" is one). Never invent facts (names, prices, addresses, slogans) or add story content (characters, objects) unless the brief leaves room or the owner agrees. No brand input: ask for name, audience, colours, type, three voice words, likes and dislikes; otherwise label choices as assumed. Before calling a choice a flaw, ask whether it looks deliberate and works.
1. **Render** at real viewing size plus a thumbnail; UI at 390 px, 1280 px and 200% zoom. Keep every round.
2. **Look:** blur (what leads?), thumbnail (does the idea survive?), flip (lopsided?), greyscale (value structure?), edges and corners (tangents, stray spots). One factual line each.
3. **Critique.** Every point names a rule, the evidence and one fix; no rule, no point (ask the owner instead). Note what already works, so it is kept. Rank by effect, structure before surface, five points at most. Neutral, no praise. Measure at 2x or with a tool before calling a failure. Keep measured findings (only these block) apart from interpreted ones (name the feature, its effect and the trade-off; label it).
4. **Fix** at most 3 per round, blockers first, smallest change that works; keep subject, style, mood and layout idea. Re-render, compare side by side, check each fix applied, revert what got worse. For mood or energy, change one or two things and judge old against new for the brief (which is stronger, why, at what cost; "neither" is allowed), not by score.
**Energy pass**, once the checks pass (skip for forms, dense data, accessibility-critical UI; light for notices, menus, dashboards; full for heroes, pricing and app home screens, with a named mood): one focal hook that leads at thumbnail, off its ground in value, display type with a big size step, one accent or a colour code (text on strong colour: the better of black or white), some movement, an obvious call to action, the issuer's real mark on official pieces, an idea one step past the literal that fits the category and genre, a title as loud as the mood, traits shown by pose, life in picture books. Energy from structure, not texture: no clutter, grain or added content (EN-1..3).
5. **Stop** when no blockers remain and the top points are done, a round is not clearly better, what is left is taste, or at round 3 (5 at most). Hand off both renders, changes with rule IDs, what was left and why, and questions. The owner decides when it is finished.

**Remake from scratch** (only on "redo", "start over" or similar): write a 5-8 line brief for sign-off (what and where, who for, one job, feeling, the given facts word for word, what must survive). Make 2-3 concepts that differ in structure, not just font or colour; recommend one, build it, run every blocker, compare with the original (FP-1..9). Design for the real medium. Build new imagery from what the subject really is, never by re-describing the old picture; crop food and real subjects at 2-4x for plausibility (FP-9, ILL-12).

**Take over** (rework, no 3-fix cap) when 3+ blockers, one that breaks the piece, a failed blur and thumbnail, more than 3 rounds needed, or unusable. Say so and why, keep the brief's idea and must-keeps, then run the loop.

## Blockers (MUST-BE-RIGHT)

Only these block; everything else is an improvement.

- **Perspective:** one horizon; objects on one ground share it; verticals vertical unless 3-point is meant; foreshortening matches distance (TD-PER-1..5).
- **Ellipses:** minor axis on the cylinder's axis; fuller away from eye level; smooth, no lemons (TD-ELL-1..3).
- **Proportion and anatomy:** measured, left and right agree (TD-PRO-1..2).
- **Light:** one key direction; lit and shadow sides separate; cast shadows on the ground (TD-LIT-1..3).
- **Figures, hands, animals (delivery gate):** crop each hand, limb join, face and animal head at 2-4x: five digits per hand, each hand traced to the shoulder on the correct side, thumb opposing on anything held, joints bend right, nothing merged or extra, eyes match, animals true to species. Props whole and used as briefed (chewed, not held). Re-check after every edit (CHAR-3, -4, -7, -9, -10, -11).
- **Fixed frames:** key content in the safe area; main message readable at about 400 px wide; print 3 mm bleed, 300 ppi (LAY-5, LAY-6, LAY-9). Signage cap height about distance ÷ 250 (LAY-7).
- **Whitespace (LAY-10):** every empty area is a margin, a gap between groups or named focal space; no empty band or block over about 1.5x the largest intended gap. Re-review after any image swap. A series keeps logo, margins, palette and type logic (BRAND-6).
- **Copy and counts:** re-read every fixed string letter for letter (units, case, punctuation) and count every fixed number on the render (CD-7).
- **Type size:** reading text 14 px or more, nothing meaningful under 12 px (TYPE-3).
- **Text over images:** a quiet zone; contrast on the worst pixels (LAY-15).
- **Food and real subjects:** plausible at 2-4x crops (ILL-12).
- **Logos and marks:** the official file, unaltered, with clear space and minimum size; never redrawn or generated (only a knockout, faithful trace or one-colour silhouette, checked by overlay); no file, set the name in plain text. No invented logos or garbled lettering in generated images (BRAND-4, BRAND-8).
- **Contrast:** text 4.5:1; 3:1 for large text (about 24 px) and UI boundaries; never colour alone (UI-6).
- **Zoom:** text grows to 200% without clipping (UI-10). **Flow:** the main task completes (UX-1).
- **3D:** no high or medium model-qa issues unless intended; right size and way up (3D-1, 3D-2).
- **Video:** at most three large flashes a second (FILM-ACC-1); one light side in a continuous scene (FILM-LIT-1); generated clips keep identity, pass anatomy on frames every 0.5-1 s, no invented text (FILM-GEN-2, -3, -8).

## Core rules (all work)

- **CORE-1** One hierarchy: one lead, a clear second and third (blur). **CORE-2** Value before colour: greyscale still reads. **CORE-3** Strongest contrast at the focal point only.
- **CORE-4** Spacing groups things, gaps from one scale (4/8/16/24/32). **CORE-5** Align to shared edges and a grid. **CORE-6** Every colour has a role; few accents.
- **CORE-7** Three to five type sizes on one scale; 45-90 characters a line; leading 1.3-1.5. **CORE-8** Remove before adding. **CORE-9** Same thing, same look.
- **CORE-10** Check at the real viewing size. **CORE-11** Balance by visual weight; fix with a counterweight or firmer asymmetry, never by centring by default.

## Common module checks

- **Illustration:** one focal point (ILL-2); clear silhouettes (ILL-3); values, then palette (CV-1, CV-2); hard edges only where attention goes (ILL-5); no generic AI look (ILL-11).
- **Web UI:** one type scale (TYPE-2); a grid and one obvious primary action (UI-4); consistent components with states (UI-5); no gradient blobs, emoji icons or three identical cards (UI-7).
- **UX:** prevent errors, then explain in place with input kept (UX-3); plain language (UX-6); visible labels (UX-7).
- **Composition:** clearly on or off centre and axes (COMP-1); weigh, then mirror (COMP-2); faces and words are heavy (COMP-3); room in front (COMP-5); one dominant per attribute (COMP-8); 3-5 big shapes (COMP-13); full symmetry or clear asymmetry (COMP-17).
- **Sitting right (before delivery):** squint, thumbnail, mirror, rotate 180°, cover each half, sweep edges. Flag only the accidental (lopsided weight, near-misses, crammed or floating elements, tangents, near-alignments, uneven gutters) and ask "intended?". Never centre or symmetrise by default (COMP-19 to COMP-25).
- **Colour and value:** neutral white unless warmth is a named choice (CV-11); important edges in greyscale (CV-3); judge in place (CV-4); hold one of hue, lightness or chroma (CV-5); strongest colour smallest, at the focus (CV-6); survives colour-vision deficiency (CV-9).
- **Pages:** one axis per group (LAY-11); paragraphs marked one way (TYPE-12). **3D:** plausible materials (3D-6); AgX (3D-7).
- **Film:** name the beat and check each choice against it (FILM-STORY-0); watch in motion with sound first (FILM-REV-1); one side of the 180° line, cuts with a real change (FILM-CON-1, -2); motivated moves (FILM-CAM-1); one look, skin first (FILM-COL-1, -2); subtitles in safe areas, slow enough to read (FILM-TXT-1, -2).

## Myths: don't use as reasons

Golden ratio as beauty, thirds as law, fixed colour emotions, lines that "force" the eye, Z/F templates, colour-wheel schemes as proof, the rule of odds. Taste in design is far less shared than in faces or landscapes: taste calls go to the owner (AES-12).
