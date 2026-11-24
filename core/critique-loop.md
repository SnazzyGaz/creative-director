# The critique loop: proportional tiers, verify, fix

**Purpose:** protect intent and what already works, applying rigor proportional to the job. Start from the idea and brief, construct exact elements in code where possible, verify fresh renders with tools, and stop when done.

> **v2 note:** Always-on guidance lives in `core/kernel.md` (≤ 1,600 tokens). Load this file when you need full loop procedure, take-over rules, or `FLOW-1..5` wording.

```
read ask -> pick tier (fast | directed | remake) -> brief + cd.py load
 -> [if directed/remake: roughs -> cd.py select -> owner pick]
 -> render / compose -> cd.py check + look.py + crops -> labelled critique
 -> pick fix level -> [sign-off] -> fix winner -> re-render -> compare -> stop
```

## Proportional Tiers

| Tier | When | Roughs | Round Cap |
|---|---|---|---|
| **Tier 1: `fast`** | Routine edits, self-checks, consults, quick fixes | 0 (preserve existing work) | 2 |
| **Tier 2: `directed`** | New visual pieces, open briefs, variations | 2–4 (3 recommended) | 3 |
| **Tier 3: `remake`** | Explicit "redo", "rejig", "start over", "reimagine" (`core/first-principles.md`) | 3–6 (4 recommended) | 5 |

## Blockers (MUST-BE-RIGHT)

Only explicit `must_be_right` brief conditions and the applicable hard gates in `manifest.json` (`core/kernel.md` §2) block delivery:

- Construction: one horizon, consistent perspective, ellipses, proportion and key light (`TD-PER`, `TD-ELL`, `TD-PRO`, `TD-LIT`).
- Copy and counts: every fixed string letter for letter, every fixed number counted on the render (`CD-7`).
- Bodies: `CHAR-9` anatomy pass, animal counts (`CHAR-10`), `MUST-BE-RIGHT` lines in `CHAR-2..7`, props as briefed (`CHAR-11`).
- Fixed frames: safe area (`LAY-5`), feed-size legibility (`LAY-6`), print bleed/resolution (`LAY-9`), text over images (`LAY-15`), type floor (`TYPE-3`), truthful data/routes (`LAY-19`), safe steps (`INF-6`).
- Screens: contrast (`UI-6`), text resize (`UI-10`), no invented screens (`UI-11`), main flow completes (`UX-1`).
- 3D: builds clean, right size and way up (`3D-1`, `3D-2`).
- Moving image: flash threshold (`FILM-ACC-1`), continuous key direction (`FILM-LIT-1`); generated video: identity, sampled anatomy, no invented text (`FILM-GEN-2`, `FILM-GEN-3`, `FILM-GEN-8`).
- Subjects and marks: official marks unaltered (`BRAND-4`), no invented marks (`BRAND-8`), food physically plausible (`ILL-12`).

Use `python3 tools/cd.py rule <ID>` for any full rule and sources.

## 0. Read the ask

| Ask | Tier / Mode | Action |
|---|---|---|
| Work handed over, no specific request | `fast` (Unprompted hand-off) | Analyse, send `FLOW-1` blurb, wait. |
| "Just fix it", "I want the result" | `fast` (Result wanted) | No wait; apply every imperative point, same checks (`FLOW-4`). |
| "What's wrong?", "consult creative director" | `fast` (Consult) | Critique only; change nothing. |
| Open brief, "direct this" | `directed` (Direct) | Idea and brief, 3 roughs then pick (`creative-direction.md`). |
| "Redo", "rejig", "start over", "reimagine" | `remake` (Remake) | `first-principles.md`: brief sign-off, 3–6 roughs then pick, full QA. |
| Own output, `+ creative director` | `fast` (Self-check) | Silent checks; ask only unresolved owner choices. |

Never infer a remake from an edit request. "Bolder", "quieter", "distill": `commands.md`. "Variations" or a generic set: `modules/lookbook/`.

## 1. Idea, brief, load, roughs

- Name **the one idea, feeling and tone first**, then create `brief.json` (`python3 tools/cd.py brief init "description"`). Fill `medium`, `has_people_or_animals`, `idea`, `feeling`, `audience`, `purpose`, `success`, `format`, fixed `copy`/`counts`, `constraints`, and `must_be_right`. Optionally set `tier` and `intent_tags`, and load a project `taste.json` (`core/taste-profile.md`).
- Run `python3 tools/cd.py load --brief brief.json` and read the returned files before making or fixing.
- Record intent (`AES-0`), each line `[brief]` or `[inferred]`. Protect must-keeps (`CD-1`, `CD-5`). Inference is not approval to add content.
- On `directed` (2–4 roughs, 3 recommended) or `remake` (3–6 roughs): make structurally different roughs, each with a one-line idea.
- Compare with `tools/cd.py select` (`pairwise` for 2–4 roughs, or `bracket`/`ranked` for 5–8 roughs so larger sets do not force 28 pairwise essays). Use an isolated fresh context (`isolated-subagent` or `separate-session`) when your runtime supports it; otherwise record `"context_mode": "same-session-self-review"` honestly rather than faking isolation.
- Show the top 2–3 to the owner with trade-offs (`AES-9`). Wait for a pick; **only the winner enters the fix loop**.
- On `fast` edits and consults, do not manufacture new directions.

## 2. Render or Compose

- Where exact copy, official logos, or data charts are required on a fixed frame, composite them deterministically over art plates using `tools/compose.py` (which emits `{stem}-boxes.json` automatically) or HTML/SVG + Playwright.
- Render at use size plus a 150–200 px thumbnail; keep each round. UI: 390 px, 1280 px, 200% zoom (`tools/shot.sh`). 3D: contact sheet. Film: watch in motion with sound, then sampled frames.

## 3. Check, then look

- Run `python3 tools/cd.py check FILE --brief brief.json [--taste taste.json]`. Quote measured numbers. When `{stem}-boxes.json` exists, `cd.py check` verifies exact copy (`CD-7`), safe area (`LAY-5`), AND worst-pixel text contrast (`UI-6`, `LAY-15`) automatically. `FAIL` must be fixed; `FLAG` asks "intended?" (never auto-centre); `SKIP` is missing evidence, never clearance.
- Run `tools/look.py` (blur/squint, thumbnail, mirror, luminance greyscale, edge strips), one factual line each.
- **Anatomy gate:** any person, hand or animal requires 2–4× crops (`tools/anatomy_crops.py`), one PASS/FAIL line per crop (`CHAR-9`). Repeat after figure edits.
- **Energy:** load `core/energy-pass.md` only when `cd.py load` or the agreed brief intent calls for energy. Never force quiet work louder.
- **Sitting right:** before delivery, check `modules/composition/sitting-right.md` (`COMP-19..25`): flag accidental misalignments or dead space without centring by default.

## 4. Critique (`critique-template.md`)

Judge composition, colour, lighting, readability, purpose and design rules together. Record what already works so it is preserved. Rank at most five findings by effect, structure before surface:

- **rule-backed:** cite an existing rule ID and threshold;
- **intent-backed:** cite the conflicting brief line;
- **exploratory:** an optional possibility (never blocks).

Every finding carries **provenance** and **confidence** (`high`/`medium`/`low`), separating `MEASURED` from `INTERPRETED`. No debunked myths (`core/evidence.md`).

### FLOW-1. An unprompted hand-off gets sign-off, not a redo

Send only imperative findings, ranked, five at most: label, rule ID or brief line, visible change, `[edit]` or `[regenerate]`. Optional ideas stay on one "also possible" line. Ask for sign-off and change nothing until it comes (`CD-4`).

## 5. Pick the fix level, then fix

Before any change, name **one intervention level and why**: `edit`, `recompose`, `art-direct`, `reconceive` (needs owner authority), `rebuild`, or `explore`.

Preserve subject, mood, palette and must-keeps (`CD-5`). If asked to change only one part, keep everything else intact. At most three changes per round, blockers first, smallest effective intervention. Verify each fix on a fresh render and re-run measurements (`AES-9`, `AES-10`).

### FLOW-2. Apply every signed-off point

The three-change cap spreads a signed-off list across rounds; it never truncates it. Signed-off points = attempted points.

### FLOW-4. "Just fix it" skips waiting, not checks

Apply every imperative point, run `FLOW-3`, deliver the result first with done/not-done lines.

### Take-over (FLOW-5)

Three blockers, one whole-piece failure, or unusable work: `core/take-over.md`. Name it up front as a rework; preserve the approved idea.

## 6. Compare and stop

Compare latest, previous and original for this brief, naming trade-offs. **"The original is better" is a valid verdict and stop**: revert, preserve it, explain why, and still list any unresolved blockers.

Stop when blockers = 0 and top improvements are done; the round is not clearly better; remaining points are taste; the next change alters the brief; or the tier's round cap is reached.

### FLOW-3. Re-check and deliver the result, not an unapplied critique

Verify every signed-off point on the final render. Result first, then one **done / not done + evidence/reason** line per point, plus a compact QA summary (gates, `cd.py check` status, anatomy/copy/contrast/whitespace/marks, taste profile applied) and any owner questions. Label self-judged verdicts clearly.
