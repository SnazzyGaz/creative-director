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
