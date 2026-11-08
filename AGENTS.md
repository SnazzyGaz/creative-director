# AGENTS.md — creative-director v0.11.2

Design judgement for visual work: idea first, roughs then pick, evidence-labelled critique, then the smallest effective fix. Taste stays with the owner of the work.

## Load

1. **Always:** this file, `core/principles.md` (40 existing rules: CORE-1..11, FLOW-1..5 and 24 gate/intent reminders) and `core/critique-loop.md`.
2. **Critique:** `core/critique-template.md`.
3. **On demand:** `python3 tools/cd.py rule <ID>` for full wording and sources; task routing in `core/which-modules.md`. Load only relevant modules or rules, not the whole library. People/animals require character and its anatomy gate.
4. **Intent only:** `core/energy-pass.md` when the feeling, purpose or kind of piece calls for life, never by medium alone. Calm or official work can skip.

`lite/CREATIVE-DIRECTOR-LITE.md` is a separate small-context bundle, not the 40-rule selection.

## Work

0. **Read the ask.** Unprompted hand-off: analyse, sign-off blurb, wait (FLOW-1). “Just fix it”: no wait, same checks (FLOW-4). Consult: critique only. From-scratch words: `core/first-principles.md`; no silent remake. “Bolder”, “quieter”, “distill”: `core/commands.md`.
1. **Idea, feeling and tone first**, then structured `brief.json` (`tools/cd.py brief init`). Medium, people/animals, purpose, audience, size, copy/counts, constraints, must-be-right; distinguish [brief] from [inferred]. No brand input: `core/brand-intake.md`; open direction: `core/creative-direction.md`. Then `python3 tools/cd.py load --brief brief.json`. Read every listed file before work; quote the match list.
2. **Roughs then pick.** New work: 4–8 roughs; head-to-head in a fresh context of the SAME model, not a second model. Show top 2–3 to the owner; only their winner enters the fix loop. `tools/cd.py select` supports this. Existing edits/consults preserve intent; no forced new directions.
3. **Render and look.** Actual size and thumbnail. `tools/cd.py check` delegates to `autocheck.py`; SKIP is not clearance. Five tests (`tools/look.py`); exact copy/counts (CD-7); cropped anatomy gate (CHAR-9) if applicable. Energy from the named tone. Sitting right before delivery: never centre to clear a flag.
4. **Critique.** Label findings **rule-backed** (ID), **intent-backed** (brief line), **exploratory** (option). Every finding: provenance and confidence. Separate measured from interpreted. Exploratory findings never block.
5. **Choose the fix level first:** edit, recompose, art-direct, reconceive, rebuild or explore; state why and authority. At most 3 changes per round, the signed-off list in full. Check each applied, re-render, compare.
6. **Stop.** No blockers and clearly better, not improving, or **the original is better**: revert and stop. Preference never clears remaining blockers. Round 3 routine / 5 max. Result first, done/not-done evidence per point and final QA (FLOW-3). Take-over: name it up front (FLOW-5, `core/take-over.md`).

## Guardrails

Blockers: explicit must-be-right brief conditions and the loop's conditional gates. Never invent facts, copy or story content. Official marks use the unaltered file; no generated marks. Neutral whites. Balance is not symmetry: counterweight or firmer asymmetry, not automatic centring. Evidence grades stay honest; no golden-ratio or thirds-as-law reasons (`core/evidence.md`). Plain, factual notes; self-judged verdicts labelled, owner choices left open.

Tools and JSON contracts: `tools/README.md`, `tools/brief.md`. Without code, check by eye and say so; without vision, call the review rules-only.
