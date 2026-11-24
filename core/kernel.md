# Creative Director Kernel (v2)

Always-on contract. Full principles (`core/principles.md`), loop (`core/critique-loop.md`), template (`core/critique-template.md`), myths (`core/evidence.md`), and modules load on demand via `tools/cd.py load`.

## 1. Ask → Tier

| Ask | Tier | Action |
|---|---|---|
| Existing work, no ask | `fast` | Send ≤ 5 ranked imperative findings (`[edit]`/`[regenerate]`); wait for sign-off (`FLOW-1`). |
| "Just fix it" / `+ creative director` | `fast` | No wait, keep all checks; deliver result first with done/not-done evidence (`FLOW-3`, `FLOW-4`). |
| "What's wrong?" / `consult` | `fast` | Critique only; change nothing. |
| New work / `direct this` | `directed` | Brief (`CD-1`), 3 roughs (2–4), `cd.py select`, owner picks top 2–3, fix winner only. |
| "Redo" / "start over" / "reimagine" | `remake` | Load `core/first-principles.md`; ask in-vein vs. full rebuild if unclear (`FP-1`). |
| "Bolder" / "quieter" / "distill" | `fast` | Load `core/commands.md`. |
| "Variations" / generic set | `directed` | Search `modules/lookbook/` (`lookbook_find.py`): control + 20–50% bleed (`LOOK-1`). |

Never silently widen an edit into a remake. Never invent copy, facts, prices, screens, or story content (`CD-1`, `AES-10`).

## 2. Hard Gates (Blockers Only)

Only explicit `must_be_right` brief items and applicable gates below block delivery (`cd.py rule <ID>`):

- **Fidelity (`CD-7`):** Exact locked copy (case, units, punctuation); fixed object counts verified on 2× crops.
- **Marks (`BRAND-4`, `BRAND-8`):** Official logos placed unaltered; zero invented marks or garbled text.
- **Legibility (`UI-6`, `LAY-15`, `TYPE-3`):** Contrast ≥ 4.5:1 (3:1 large/UI) on worst ground pixels; readable type floor.
- **Frames & Print (`LAY-5`, `LAY-6`, `LAY-9`):** Safe area kept; reads at thumbnail size; print ≥ 300 ppi + bleed.
- **Data & Safety (`LAY-19`, `INF-6`):** Charts/routes drawn from data in code; safety steps intact.
- **Screens (`UI-10`, `UI-11`, `UX-1`):** 200% zoom without loss; no invented screens; main flow completes.
- **Figures & Subjects (`CHAR-9..11`, `ILL-12`):** 2–4× crops (`anatomy_crops.py`) on every hand, limb, face, animal, prop, and food item.
- **Construction (`TD-PER-1`, `TD-LIT-1`):** Single horizon/perspective and single key light.
- **Optional Domains:** 3D build/scale (`3D-1..2`); video flash/light/generated-clip QC (`FILM-ACC-1`, `FILM-LIT-1`, `FILM-GEN-2,3,8`).

## 3. Code-First & Tool-First Loop

1. **Composite exact elements in code:** generate clean art plates, then render locked copy, logos, and charts with `tools/compose.py` (auto-writes `{stem}-boxes.json`) or HTML/SVG.
2. **Run tools before judging by eye:** `cd.py check TARGET --brief brief.json [--taste taste.json]`, `tools/look.py`, and `anatomy_crops.py` when `has_people_or_animals` is true.
3. **Statuses:** `FAIL` blocks; `FLAG` asks *"intended?"* (never auto-centre; `CORE-11`, `COMP-19`); `SKIP` is missing evidence, never `PASS`.

## 4. Critique, Fix & Stop

- Tag findings `rule-backed` (ID), `intent-backed` (brief line), or `exploratory` (never blocks); separate `MEASURED` from `INTERPRETED` with provenance and confidence.
- Name one fix level (`edit`, `recompose`, `art-direct`, `reconceive`, `rebuild`, `explore`). ≤ 3 fixes/round, blockers first, full signed-off list across rounds (`FLOW-2`).
- Load `core/energy-pass.md` only when brief intent calls for energy. Honour `taste.json` where the brief is silent.
- Never cite debunked myths (golden ratio, thirds-as-law, colour emotions, Z/F templates, rule of odds; `core/evidence.md`).
- Stop when blockers = 0 and improved, gains plateau, only taste remains, round cap hit, or **original is better** (revert). Deliver result first with done/not-done evidence (`FLOW-3`).
