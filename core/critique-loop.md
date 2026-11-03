# The critique loop: read the ask, render, look, critique, fix, deliver

**Purpose:** a light touch. The loop nudges output (a drawing, generated image, 3D model, UI or flow) toward what people measurably prefer while keeping its intent and what already works. Smallest changes with the biggest effect; stop once it is clearly better. Always look at a fresh render, never at your own code or prompt.

```
read the ask -> brief -> render -> AUTO CHECK -> LOOK (5 tests, energy) -> CRITIQUE (ranked, rule IDs) -> [sign-off] -> FIX -> re-render -> compare -> deliver
                           ^                                                                       |
                           +---------------------- repeat only while clearly improving ------------+
```

Why bother: appeal is judged in about 50 ms [S36]; high visual complexity is liked least [S35]; attractive work earns tolerance for minor problems, not serious ones [S34]. So fix blockers first, simplify, then polish lightly. Grades: `evidence.md`. Every rule in this file is a Procedure.

## Blockers (MUST-BE-RIGHT)

Only these block delivery; everything else is a default.
- **Construction:** one horizon and consistent perspective, ellipses, proportion, one key light (TD-PER, TD-ELL, TD-PRO, TD-LIT).
- **Bodies:** a clean anatomy pass (CHAR-9) when a person, hand or animal is in frame; animal counts (CHAR-10); the MUST-BE-RIGHT lines in CHAR-2 to CHAR-7.
- **Fixed frames:** safe area (LAY-5), legible at feed size (LAY-6), print bleed and resolution (LAY-9), text over images (LAY-15), type under the size floor (TYPE-3), data and routes drawn true (LAY-19), every required line and safe steps (INF-6).
- **Screens and flows:** contrast (UI-6), text resize (UI-10), the main flow completes (UX-1).
- **3D:** builds clean, right size and way up (3D-1, 3D-2).
- **Moving image:** no flashing above the threshold (FILM-ACC-1); one key direction within a continuous scene (FILM-LIT-1); for generated video, identity, anatomy on sampled frames and no invented text (FILM-GEN-2, -3, -8).
- **Marks and subjects:** official marks unaltered (BRAND-4), no invented marks (BRAND-8), food physically plausible (ILL-12).

## 0. Read the ask

| What the person said | Call it | What happens |
|---|---|---|
| Work handed over, no specific ask ("here's a cover", "put this through the CD") | **Unprompted hand-off** | Analyse, send a sign-off blurb, wait (FLOW-1). |
| "Just fix it", "I want the result" | **Result wanted** | No blurb. Fix every imperative point, check, deliver (FLOW-4). |
| "What's wrong with this?", "consult creative director" | **Consult** | Critique only (`critique-template.md`); change nothing. "Do it" afterwards is the sign-off. |
| "creative director: direct this", or a brief with no work | **Direct** | Brief, direction, rough options (`creative-direction.md`, CD-1 to CD-3), then the loop; sign-off at those checkpoints. |
| "Redo / rejig / start over / reimagine / from scratch" | **Remake** | `first-principles.md` (FP-1 to FP-9): brief signed off, 2-3 concepts, build, full QA. |
| The agent's own output (`+ creative director`) | **Self-check** | Run the loop silently; ask only taste calls; deliver with the FLOW-3 checklist. |

Never assume a remake without a from-scratch word. Unclear ask: treat it as an unprompted hand-off; a blurb costs one message, a wrong redo the piece. Flow diagram: `interaction-flow.md`.

## 1. Brief

- Have the brief (CD-1) and direction (CD-2). No brand input (colours, type, voice, logo)? Run `brand-intake.md` first. Open brief: 2-3 rough options first (CD-3).
- **Intent model (AES-0):** purpose, audience, mood, style, focal experience, polish, must-keeps, each marked [brief] or [inferred]. Count what the brief fixes ("it" is one). Before calling a choice a flaw, ask if it is deliberate and works.
- The first critique point every round: does it answer the brief, are the must-keeps intact (CD-1, CD-5)?

## 2. Render

At the size people see it, plus a thumbnail. UI: phone and desktop widths and 200% zoom (`tools/shot.sh`). 3D: the measured checks first (`modules/3d/`), then a contact sheet. Keep every round.

## 3. Look: auto check, then five tests

**Auto check first** (if you can run code): `python3 tools/autocheck.py FILE|URL --out DIR` measures contrast, type, spacing, edges, space, balance and whites against each rule's own number. Fix every FAIL (* = blocker), then judge by eye, quoting its numbers. FLAG asks "intended?"; balance is never a FAIL or a reason to centre. Image text checks are SKIP without `--text-box`: check by eye.

| Test | How | Reveals |
|---|---|---|
| **Squint / blur** | Blur ~5-10 px at screen size | What leads when detail goes [S1] |
| **Thumbnail** | ~150-200 px wide | Whether the idea survives at feed size |
| **Mirror** | Flip horizontally (and upside down for pictures) | Drawing errors, lopsided weight, tilts [S7] |
| **Greyscale** | By luminance or OKLCH L, not HSL L | Value structure [S5] |
| **Crop / edges** | Each edge and corner; a tighter crop | Tangents, frame contacts, dead space, stray brights |

`tools/look.py` makes all five as one sheet. Write one factual line per test ("Blur: the badge leads; the headline is second").

**Anatomy pass (delivery gate):** with any person, hand or animal in frame, crop each hand, limb join, face and animal head at 2-4x and write one pass/fail line per crop (CHAR-9, `tools/anatomy_crops.py`). A whole-image look doesn't count; any fail blocks.

**Energy pass** (after the checks, where it applies; `energy-pass.md`): a focal hook at thumbnail that stands off its ground in value, display type with real hierarchy, purposeful colour, movement, an obvious call to action, an idea that fits the category; on official pieces the issuer's real mark or a flagged slot. From structure, not texture: no clutter, grain or additions.

**Before delivery, the Sitting right pass** (COMP-19 to COMP-25, `modules/composition/sitting-right.md`): rotate 180°, cover each half, gap measure (LAY-10), `tools/balance.py`, edge and alignment sweep. Flag only what looks accidental and ask "intended?". Asymmetric and off-centre work is valid: fix broken balance with a counterweight or by committing harder to the asymmetry. Never centre or symmetrise by default.

## 4. Critique (`critique-template.md`)

- **Criteria first:** list the rule IDs in scope. **Every point cites a rule ID**; no rule, no point: it becomes a question for the owner.
- **No myths as reasons** (golden ratio, thirds as law, colour-emotion tables; `evidence.md`).
- **Meets criteria:** record what to preserve.
- **Needs improvement:** ranked by effect on the whole, structure before surface, five at most. Blockers marked.
- **Measure at zoom** (2x+, or `tools/vp.py`, `ellipse.py`, `contrast.py`) before calling a failure.
- **MEASURED vs INTERPRETED:** measured findings (tool or count) can block; interpreted ones (AES-1 to AES-8) name a visible feature, its effect and the trade-off, labelled as interpretation. When they conflict, state the trade-off; don't settle it toward the neater option.
- **Register:** factual. Not "the face feels weak", but "CORE-3 not met: highest contrast is the top-right sky, not the face. Fix: lower the sky one value step."

### FLOW-1. An unprompted hand-off gets a sign-off blurb, not a redo
- **What:** After the full analysis, reply with only the **imperative** changes (blockers, and what the piece fails its brief without): ranked, five at most, each with its rule ID, what visibly changes, and **[edit]** (keep the art) or **[regenerate]** (new art or redo). Optional ideas go on one "also possible" line or nowhere. Ask for sign-off; apply nothing before it.
- **Why:** Notes are suggestions until the owner accepts them (CD-4). Asking costs one message; a wrong guess costs a redo.
- **Check:** Ranked, cited, concrete, tagged, five lines at most, nothing changed yet?
- **Format:**
  ```
  Imperative changes (sign off and I'll apply all of them):
  1. [regenerate] CHAR-9: the hand at bottom right has no arm. New art with both hands traced to the shoulders.
  2. [edit] TYPE-3, UI-6: author name is 3.1:1 on the sky. Set in code on a darker band, at least 4.5:1.
  Also possible (not needed): a warmer palette. OK to go ahead?
  ```

## 5. Fix and re-render

- **Preserve intent:** subject, style, mood, palette and layout concepts belong to the brief and the owner.
- **At most ~3 changes a round**, blockers first; smallest effective change; prefer removing to adding.
- **Check each fix applied** against the fix as written (generators skip and drift); a fix that didn't apply is not done.
- **Re-run the anatomy pass in full** after any edit touching a figure, and the LAY-10 whole-layout review after any image swap or re-crop.
- **Aesthetic changes one or two at a time**: compare side by side, keep, refine or revert, and re-run the measured checks (AES-9, AES-10).
- Re-run the five tests; revert anything that made it worse. One log line per round: change, rule, result.

### FLOW-2. After sign-off, apply every signed-off point
- **What:** Apply all signed-off points; the three-fix cap doesn't cut the list short (spread it over rounds). If an edit can't achieve a point, regenerate rather than drop it, and say so. Keep the idea and must-keeps (CD-5).
- **Check:** Points signed off = points attempted.

### FLOW-4. "Just fix it" skips the sign-off, not the checks
- **What:** Apply every imperative point, run FLOW-3, and deliver the result first, with the change list after it.
- **Check:** Is the first thing delivered the result, with done / not done lines?

## 6. Take over or nudge

Take over (full rework) when any is true: three or more blockers at once, or one that breaks the whole piece (no consistent horizon, broken anatomy, a main flow that can't complete, a failed 3D build); it fails the thumbnail and blur tests outright; three-change rounds would need more than three rounds; it is unusable for its purpose. Keep the brief's idea and must-keeps (CD-5) and re-read the brief before regenerating; regeneration is where the subject drifts.

A take-over repairs a broken piece and keeps its idea. A **remake** ("from scratch") rebuilds from a new brief: `first-principles.md`.

### FLOW-5. Egregious work: take over, but say so first
- **What:** Put "this needs a redo, not an edit, because ..." in the first line. In an unprompted hand-off the redo is point 1 [regenerate] and still waits for sign-off; under "just fix it", do it and say so up front.

## 7. Stop and deliver

Stop when: no blockers remain (including a clean anatomy pass on the latest render) and the top improvements are done; or the latest round isn't clearly better; or what is left are questions no rule settles; or the next fix would change the brief or something the owner approved; or round 3 for routine work (5 at most). Report rather than polish.

### FLOW-3. Re-check before delivery; never pass off an unapplied critique as the result
- **What:** On the final render, check each signed-off point, then the QA gates: light (TD-LIT-1), anatomy (CHAR-9), type size and contrast (TYPE-3, UI-6), whitespace (LAY-10), Sitting right (COMP-25), marks (BRAND-4 overlay check, BRAND-8), real-subject crops (ILL-12), transcribed facts (FP-3), no additions (AES-10), whites (CV-11), energy (EN-2, where it applies); signage adds viewing distance (LAY-7), a series adds the set pass (BRAND-6). Deliver the result first, then one line per point, **done** or **not done** with the reason. A critique alone is never the deliverable.
- **Why:** Edits silently skip instructions; an anatomy fault once passed every other check because nobody cropped the hands (`examples/character-anatomy-pass/`).
- **Check:** A line for every point? Does each "done" match the render?
- **Format:**
  ```
  1. Hand traced to the arm (CHAR-9): done, anatomy pass clean.
  2. Author contrast (UI-6): done, 7.2:1.
  QA: light pass · anatomy pass · type pass · whitespace pass · sitting right: 1 flag, intended. Left for you: palette (taste call).
  ```

After the checklist: latest and previous render, what changed (rule IDs), what was left and why, questions for the owner. Never call work finished on taste; label your own verdicts as self-judged.
