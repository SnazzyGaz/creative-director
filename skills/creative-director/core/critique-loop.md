# The critique loop: idea, roughs, pick, check, fix

**Purpose:** protect intent and what already works. Start from an idea, not a checklist. Judge fresh renders, never code or a prompt. Parallel roughs help explore [SRC-95, SRC-96]; the 4–8 range and fresh-context procedure are practice defaults, not a proven optimum.

```
read the ask -> idea + brief -> 4–8 roughs -> fresh-context head-to-head
 -> show top 2–3 -> owner picks -> render -> check -> look -> critique
 -> choose fix level -> [sign-off] -> fix winner -> re-render -> compare -> stop
```

## Blockers (MUST-BE-RIGHT)

Only these and explicit must-be-right brief conditions block delivery. Scope gates to the medium; conditional gates remain mandatory, looked up by ID. The 40-rule selection is in `principles.md`.

- Construction: one horizon, consistent perspective, ellipses, proportion and key light (TD-PER, TD-ELL, TD-PRO, TD-LIT).
- Copy and counts: every fixed string letter for letter, every fixed number counted on the render (CD-7).
- Bodies: CHAR-9 anatomy pass, animal counts (CHAR-10), MUST-BE-RIGHT lines in CHAR-2 to CHAR-7, props as briefed (CHAR-11).
- Fixed frames: safe area (LAY-5), feed-size legibility (LAY-6), print bleed/resolution (LAY-9), text over images (LAY-15), type floor (TYPE-3), truthful data/routes (LAY-19), safe steps (INF-6).
- Screens: contrast (UI-6), text resize (UI-10), main flow completes (UX-1).
- 3D: builds clean, right size and way up (3D-1, 3D-2).
- Moving image: flash threshold (FILM-ACC-1), continuous key direction (FILM-LIT-1); generated video: identity, sampled anatomy, no invented text (FILM-GEN-2, FILM-GEN-3, FILM-GEN-8).
- Subjects and marks: official marks unaltered (BRAND-4), no invented marks (BRAND-8), food physically plausible (ILL-12).

Use `python3 tools/cd.py rule <ID>` for the full rule and sources; load the relevant module when a group of rules is needed. Outside the 40 does not mean optional.

## 0. Read the ask

| Ask | Mode | Action |
|---|---|---|
| Work handed over, no specific request | Unprompted hand-off | Analyse, send FLOW-1 blurb, wait. |
| “Just fix it”, “I want the result” | Result wanted | No wait; apply every imperative point, same checks (FLOW-4). |
| “What's wrong?”, “consult creative director” | Consult | Critique only; change nothing. |
| Open brief, “direct this” | Direct | Idea and brief, roughs then pick (`creative-direction.md`). |
| “Redo”, “rejig”, “start over”, “reimagine” | Remake | `first-principles.md`: brief sign-off, roughs then pick, full QA. |
| Own output, `+ creative director` | Self-check | Silent checks; ask only unresolved owner choices. |

Never infer a remake from an edit request. Unclear ask: unprompted hand-off. “Bolder”, “quieter”, “distill”: `commands.md`. “Variations” or a generic set: `modules/lookbook/`.

## 1. Idea, brief, roughs, pick

- Say **the one idea, feeling and tone first** (what kind of piece it is). Let that shape type, colour, energy and adornment; no single tidy default. Create `brief.json` with `python3 tools/cd.py brief init 'description'`, then fill purpose, audience, format/size, fixed copy/counts, constraints, success and must-be-right (`tools/brief.md`). Do not mistake an empty template for an agreed brief. No brand input: `brand-intake.md`. Run `python3 tools/cd.py load --brief brief.json` and read every listed file before the first rough and each fix; quote the matched media and rule IDs.
- Record intent (AES-0), each part [brief] or [inferred]. Protect must-keeps (CD-1, CD-5). Inference is not approval to add content.
- On new work or an authorised reconception, make **4–8 structurally different roughs**, each with a one-line idea.
- Compare head-to-head in a **fresh context of the same model**, given the brief and roughs, not the maker's rationale. Compare idea, feeling, tone, hierarchy and must-keeps; state the visible difference and trade-off (AES-9). `cd.py select` prepares the packet; no second-model checker.
- Show the **top 2–3 to the owner of the work**, explaining what each gains and loses. Wait for a pick; **only the winner enters the fix loop**.
- Edits and consults do not trigger new directions; mark selection not applicable and get approval before widening the task.

## 2. Render

Render the winner at use size plus a 150–200 px thumbnail; keep each round. UI: phone, desktop, 200% zoom (`tools/shot.sh`). 3D: a contact sheet. Film: review in motion and on sampled frames.

## 3. Check, then look

`python3 tools/cd.py check FILE --brief brief.json` emits JSON and delegates to `autocheck.py` (contrast, type, spacing, edges, space, balance, whites). Quote numbers. FAILs need fixing; FLAG means “intended?”, not a reason to centre. SKIP is missing evidence, never clearance. Images need OCR/transcription, text regions for contrast, and manual type-size review; fixed object counts need labelled crop/count evidence. Without tools, check by eye and say so.

Do the five tests (`tools/look.py`), one factual line each: blur/squint (what leads), thumbnail (what survives), mirror (drawing/weight), luminance greyscale (value groups), crop/edges (contacts and stray brights).

**Anatomy gate:** any person, hand or animal: crop hands, joins, faces and animal heads at 2–4x; trace and count, one PASS/FAIL line per crop (CHAR-9, `tools/anatomy_crops.py`). Whole-image viewing is not enough. Any fail blocks; repeat after figure edits.

**Energy follows the named tone:** load `energy-pass.md` when feeling, purpose or kind calls for life. Name the genre and scope. A quiet brief may skip the push; EN-5 still applies. Never turn a quiet brief louder to complete a ritual.

Before delivery, the *Sitting right* pass (COMP-19 to COMP-25, `modules/composition/sitting-right.md`): rotate 180°, cover each half, gap measure, balance, edge/alignment sweep. Flag accidents, ask “intended?”. Use counterweight or firmer asymmetry; never centre by default.

## 4. Critique (`critique-template.md`)

Judge composition, colour, lighting, readability, purpose and the design rules together; a passed measurement is not the whole job. Keep must-keeps. Record what works. Rank at most five findings by effect, structure before surface. Each finding has:

- **rule-backed**: cite a broken existing rule ID and threshold;
- **intent-backed**: cite the conflicting brief line, without inventing a rule;
- **exploratory**: a visible possibility, not an obligation. No rule ID required.

All three carry **provenance** (tool/version and measurement, rule lookup/path, or visual read/crop) and **confidence** (high/medium/low with why). Also distinguish MEASURED from INTERPRETED: taste is not a measured failure. Only verified mandatory failures block; a verified conflict with an explicit must-be-right brief condition can block too. An exploratory finding never blocks. No myths as reasons (`evidence.md`).

### FLOW-1. An unprompted hand-off gets sign-off, not a redo

Send only imperative findings, ranked, five at most: label, rule ID or brief line, visible change, **[edit]** or **[regenerate]**. Optional ideas stay on one “also possible” line. Ask for sign-off and change nothing until it comes. Notes are suggestions until accepted (CD-4).

## 5. Pick the fix level, then fix

Before any change, name **one intervention level and why**:

- **edit**: local copy, value, spacing or detail; keep the structure.
- **recompose**: move or resize existing parts; keep the idea.
- **art-direct**: change staging, light, pose or treatment; keep the idea.
- **reconceive**: change the idea; needs authority to revisit it and roughs-then-pick.
- **rebuild**: remake production to realise the approved idea reliably.
- **explore**: a reversible test, not a required correction.

This level is separate from execution ([edit] or [regenerate]); neither silently grants permission to change the brief. Preserve subject, mood, palette and must-keeps (CD-5). If the owner of the work asked to change only one part, change only that, keeping type, colour and arrangement; do not regenerate the whole piece. At most three changes per round; blockers first, smallest effective intervention. Check each change applied on a fresh render. After image swaps, review the whole layout (LAY-10); after figure changes, repeat anatomy. Make aesthetic changes one or two at a time; compare and re-run measurements (AES-9, AES-10).

### FLOW-2. Apply every signed-off point

The three-change cap spreads a signed-off list over rounds; it never truncates it. If an edit cannot achieve a point, regenerate rather than omit it, preserving intent and saying why. Signed-off points = attempted points.

### FLOW-4. “Just fix it” skips waiting, not checks

Apply every imperative point, run FLOW-3, deliver the result first with done/not-done lines.

### Take-over (FLOW-5)

Three blockers, one whole-piece failure, or unusable work: `take-over.md`. Say it is a redo; preserve its approved idea. A take-over does not authorise reconception.

## 6. Compare and stop

Compare latest, previous and original for this brief, including the cost of a change. Swap left/right when preference is marginal. **“The original is better” is a valid verdict and stop**, including an earlier rough: revert, preserve it, explain why. If that original still has blockers, name them; preference does not clear delivery gates.

Stop when no blockers remain and top improvements are done; the round is not clearly better; the remainder is taste; the next change alters an approved brief; or round 3 for routine work (5 maximum). Label verdicts self-judged; the owner decides taste.

### FLOW-3. Re-check and deliver the result, not an unapplied critique

On the final render verify every signed-off point. QA: construction/light; anatomy; type/contrast; whitespace and Sitting right; official/invented marks; real-subject crops; exact copy/counts/facts; no additions; neutral whites; intent-gated energy or “skipped: brief reason”; the `cd.py load` list quoted and those files read. Signage adds viewing distance (LAY-7); a series adds BRAND-6. See the blocker list above for medium-specific gates.

Result first, then one **done / not done + evidence/reason** line per point. Include latest and previous render, what changed, what remains and why, and owner questions. A favourable comparison is not evidence that an unapplied fix was done.
