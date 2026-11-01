# Outside runs

| Run | Model and route | Status | What it shows |
|---|---|---|---|
| [claude-opus-5.5-2026-11-01](claude-opus-5.5-2026-11-01/) | Claude Opus 5.5, claude.ai with code execution, full skill (repo checkout) | **Contaminated: smoke test only, not a score** | The kit and tools work outside Grok Bot. See below. |

## claude-opus-5.5-2026-11-01 (smoke test)

Run by the repo owner on 1 November 2026. The model labelled the run itself as **contaminated**: it had read `RUBRIC.md` (the answer keys) and the examples earlier in the same chat, and no baseline was run. Its self-score (all faults found, no false alarms) is therefore inflated and **is not a result**. Nothing here says whether the skill helps Claude, or by how much.

What it does show:
- A model other than Grok Bot loaded the repo and followed the loop from the files alone.
- It ran `tools/vp.py` and `tools/ellipse.py` on the drawing by itself and reported measured values (horizon tilt, vertical lean, ellipse axis and end checks), with overlays saved here.
- It cited rule IDs that exist and fit the faults (TD-PER-1/3, TD-ELL-1/2/3, UX-1, UI-6, UI-10, ILL-2, ILL-11, CD-5 and others).
- Task A became a take-over rework ([`crumb-and-co.html`](claude-opus-5.5-2026-11-01/crumb-and-co.html)): one column and one action, every text pair passes (lowest 6.11:1, re-checked here with `tools/contrast.py`), no horizontal scroll at 390 px or at 200% text. The brand orange #E8743B is kept only for rules and borders (2.79:1 on the paper, decorative, so not used for text).
- It ended with questions for the owner (the pre-order route is a phone link because no online order link was given; allergen wording; navigation removed because no pages were given).

Still wanted: a **clean, blind run** per model, in a fresh chat, without the rubric, with a baseline. See [the kit](../README.md).

## gpt-6-2026-11-01-pilot (pilot)

ChatGPT GPT-6, run by the repo owner on 1 November 2026. GPT labelled it itself as **contaminated**: it had read the rubric, and the with and without outputs were written in one chat, not in fresh sessions. Its scorecard is indicative only and **is not a result**. Files as delivered, plus [`VERIFY.md`](gpt-6-2026-11-01-pilot/VERIFY.md).

What it shows:
- The baseline (without) critiques already found most faults: 5/5 on task A, 4/5 on B and C, by its own count.
- The with-skill critiques differed mainly in **structure**: blockers first, rule IDs on each point, the brief's must-keeps stated and kept, and confidence and measurement limits stated.
- GPT ran no tools, so it gave **no measurements** (no vanishing points, ellipse checks or contrast ratios); its drawing critique is a visual judgement.
- Task A's rewritten page was not rendered by GPT. Checked here: it passes contrast (all text pairs, lowest 3.00:1 for large text, 5.89:1 for normal text), reflows at 390 px and at 200% text, and keeps the brief's facts. See [`VERIFY.md`](gpt-6-2026-11-01-pilot/VERIFY.md).

## What the two pilots suggest (not proof)

- **Baselines are already good at finding faults.** In both pilots the strong models found most planted faults without the skill (GPT's baseline: 4 or 5 of 5). The skill is not mainly a fault-finder for these models.
- **The added value showed as structure:** blockers ranked first, rule IDs, the brief kept intact, confidence stated, and owner questions at the end.
- **Measurements came from the tools, not the skill text.** Where the tools were run (Claude), the critique gave measured numbers (horizon tilt in degrees, ellipse axis error, contrast ratios); where they weren't (GPT), it gave visual estimates.
- Both runs are contaminated pilots (rubric read; no fresh sessions or blind scoring). A clean, blind run per model is still wanted.
