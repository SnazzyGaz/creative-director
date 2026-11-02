# Creative director, lite

A short version of this repo for tools with a small context window. It keeps the loop, the core rules and the blockers. The full rules, checks and sources are in `core/` and `modules/`. Use the full version when you can.

## The loop

Always judge a fresh render or screenshot, never your own code or prompt.

**Read the ask first.** Work handed over with no specific request: analyse it, reply with a short ranked list of only the imperative changes (rule ID, what will change, [edit] or [regenerate]) and wait for sign-off; change nothing yet. After sign-off apply every signed-off point (regenerate if an edit can't do it), re-check each one and the light, anatomy and type blockers, and deliver the result with one done / not done line per point. "Just fix it" skips the sign-off, not the checks. Never hand over an unapplied critique as the result.

0. **Brief.** Before making anything, write down: purpose, audience, where it will be seen, must-keeps, and what "done" means. Don't invent facts the brief doesn't give (names, prices, addresses, slogans), and don't add story content (characters, creatures, objects) to make a piece prettier unless the brief leaves room or the owner agrees. No brand input? Ask the owner for name, audience, colours, type, three voice words, likes and dislikes; if no answer, label your choices as assumed. Add the intended mood, style and degree of polish, marked [brief] or [inferred]. Before calling a choice a flaw, ask whether it looks deliberate and whether it works.
1. **Render** at the real viewing size plus a thumbnail. UI: phone (390 px), desktop (1280 px) and 200% zoom. Keep every round (`round-01.png`, ...).
2. **Look** with five tests, one factual line each: blur (what leads?), thumbnail (does the idea survive?), flip (lopsided or tilted?), greyscale (is the value structure there?), edges and corners (tangents, stray spots).
3. **Critique.** List the rule IDs in scope first. Every point names a rule, the evidence and one fix. No rule, no point: it becomes a question for the owner. Record what already meets the criteria, so it is kept. Rank by effect, structure before surface, five points at most. Neutral and factual: no praise, no harshness. Measure at 2x zoom or with a tool before calling a failure. Keep measured findings (tool-checked; only these can block) apart from interpreted ones (aesthetic: name the visible feature, its effect and the trade-off, and label it as interpretation).
4. **Fix** at most 3 things per round, blockers first. Smallest change that works; keep the subject, style, mood and layout idea. Re-render, compare side by side, and **check each fix actually applied**. Revert anything that made it worse. For mood or energy, change one or two things, then judge old and new side by side for the brief (which is stronger, why, at what cost, strong or marginal; "neither" is allowed), not by score.
5. **Stop** when no blockers remain and the top points are done, when a round is not clearly better, when what is left is taste, or at round 3 (5 at most). Hand off: latest and previous render, what changed with rule IDs, what was left and why, and questions for the owner. The owner decides when it is finished.

**Remake from scratch** (only when asked: "from scratch", "redo", "rejig", "start over", "reimagine"): step back first. Write what it is and where it is seen, who it is for, its one job, the feeling, the given facts word for word (check them against each other; never invent), what must survive and what was incidental, and how done is judged. Send that as a 5-8 line brief for sign-off. Then make 2-3 concepts that differ in structure (what leads, how the space is divided), not just in font or colour, recommend one against the brief, build it, run every blocker check below, and compare it side by side with the original (FP-1..9). Design for the piece's real medium and use (printed poster, feed post, pavement board), not for how a reference happened to be photographed or cropped. Transcribe the original's facts first, including disclaimers; flag contradictory or unsourced claims as questions. New imagery is built from what the subject really is (its parts, real references, art direction), never by re-describing the old picture; crop food and real subjects at 2-4x for plausibility: separate strands or grains, no tiling or mesh, each component right (FP-9, ILL-12).

**Take over** (rework, no 3-fix cap) when: 3+ blockers at once, or one that breaks the whole piece; it fails blur and thumbnail outright; it would need more than 3 rounds; or it is unusable for its purpose. Say it is a rework and why. Re-read the brief first, keep its idea and must-keeps, then run the normal loop on the new version.

## Blockers (MUST-BE-RIGHT)

Only these block. Everything else is an improvement.

- **Perspective:** one horizon per picture; objects on one ground plane share it; verticals vertical unless 3-point is intended; foreshortening matches distance (TD-PER-1..5).
- **Ellipses:** the minor axis follows the cylinder's axis; ellipses get fuller further from eye level; smooth and symmetrical, no lemons or footballs (TD-ELL-1..3).
- **Proportion and anatomy:** measured, not guessed; left and right agree (TD-PRO-1..2).
- **Light:** one key light direction; lit and shadow sides stay separate; cast shadows sit on the ground (TD-LIT-1..3).
- **Figures, hands, animals (delivery gate):** crop each hand, limb join, face and animal head at 2x-4x and check one by one: hand count and five digits per hand; each hand traced along its forearm to the shoulder on the correct side (a figure facing you has its right arm on the image's left); thumb opposes the fingers on anything held; joints bend the right way; nothing merged or extra; eyes match; animal eyes, legs or fins match the species. Any fail blocks delivery; re-check everything after each edit (CHAR-3, CHAR-4, CHAR-7, CHAR-9, CHAR-10).
- **Fixed frames (social, thumbnails, print):** key content inside the platform's safe area; main message readable at feed size (about 400 px wide); print has 3 mm bleed and 300 ppi at final size (LAY-5, LAY-6, LAY-9). Signage: key lines' cap height about distance ÷ 250 (LAY-7).
- **Whitespace (LAY-10):** every empty area is a margin, a gap between groups, or named focal space. Squint: no empty band or block (including inside a row, between a small left item and a small right item) larger than about 1.5x the largest intended gap between groups. After any image swap or re-crop, re-review the whole layout. A series also gets a set pass: same logo size and position, margins, palette and type logic (BRAND-6).
- **Type size:** no reading text under 14 px, nothing meaningful under 12 px (TYPE-3).
- **Logos and marks:** include the official mark (own, team, sponsor, crest) from the official file (owner, brand site, or Wikimedia Commons checked against the brand), at good quality, unaltered, with its clear space and minimum size; never redrawn, restyled or AI-generated; the only cleaning allowed is a background knockout, a faithful trace or a one-colour silhouette, with the shapes unchanged and checked by overlaying the source; with no file, set the name in plain text (or a labelled placeholder for a nameless symbol). Generated images: no invented logos or garbled lettering on jerseys, bottles, packaging or signs (BRAND-4, BRAND-8).
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
- **Composition:** place things clearly on or clearly off the centre and axes, never just off (COMP-1); weigh it, then mirror-flip (COMP-2); faces and words are heavy (COMP-3); room in front of anything that looks or moves (COMP-5); one dominant per attribute (COMP-8); repeat families, vary members (COMP-9); 3-5 big shapes at thumbnail (COMP-13); full symmetry or clear asymmetry (COMP-17).
- **Colour and value:** check every important edge in greyscale (CV-3); judge colour in place (CV-4); hold one of hue, lightness or chroma steady (CV-5); strongest colour in the smallest area at the focus (CV-6); survives colour-vision deficiency (CV-9).
- **Pages:** one axis (LAY-11); text over images checked on the worst pixels (LAY-15); paragraphs marked one way (TYPE-12).
- **3D:** physically plausible materials (3D-6); a view transform that doesn't clip (AgX in current Blender, not Standard; 3D-7).

## Myths: don't use as reasons

The golden ratio (as a source of beauty), the rule of thirds as a law, fixed colour-emotion claims, leading lines that "force" the eye, Z/F layout templates, colour-wheel schemes as proof of harmony, and the rule of odds. Cite a rule, not a myth. Taste in art and design is far less shared than taste in faces or landscapes: taste calls go to the owner of the work (AES-12).
