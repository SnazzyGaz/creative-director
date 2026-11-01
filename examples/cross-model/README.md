# Cross-model test kit

**Status: two outside pilot runs, no clean runs yet.** Besides Grok Bot, there is one Claude Opus 5.5 run and one ChatGPT GPT-6 run in [`runs/`](runs/). Both are **contaminated** (each model had read the rubric first; GPT also wrote its with and without answers in one chat), so they are smoke tests, not scores. What they suggest: the baselines already found most faults (4 or 5 of 5); the skill's added value showed as structure (blockers first, rule IDs, the brief kept intact, confidence stated) and, where the tools were run (Claude), measured numbers instead of visual guesses. Details in [`runs/README.md`](runs/README.md). This kit lets anyone check whether the skill helps in Claude, ChatGPT, Gemini or another model, with the same inputs, the same prompts and the same scoring. Results are welcome as a pull request or an issue (see [Contribute](#contribute)).

## What you run

Three tasks, each run twice per model: **without** the skill (baseline) and **with** it. Use a fresh chat for every run, so nothing carries over.

| Task | Input (in `inputs/`) | Answer key from |
|---|---|---|
| A. Web UI critique and fix | `ui-bakery.html`, `ui-bakery-1280.png`, `ui-bakery-390.png` | [`web-ui-takeover/critique-r01.md`](../web-ui-takeover/critique-r01.md) |
| B. Illustration critique | `illustration-keepers-cat.jpg` | [`illustration-takeover/critique-r01.md`](../illustration-takeover/critique-r01.md) |
| C. Technical drawing critique | `drawing-box-tin.png` | [`technical-drawing-takeover/critique-r01.md`](../technical-drawing-takeover/critique-r01.md) |

All three inputs are deliberately bad, with known faults (planted or measured), so a critique can be scored against a fixed list. **Don't show the model the answer key**, and don't let it read `RUBRIC.md` or `examples/` in the same chat (both outside runs so far did, see [`runs/`](runs/)).

## How to give the model the skill

- **Claude (claude.ai Projects or Claude Code):** add `SKILL.md`, `AGENTS.md`, `core/` and the module named in the task as project knowledge, or run in a checkout of this repo (Claude Code reads `CLAUDE.md`).
- **ChatGPT:** attach `lite/CREATIVE-DIRECTOR-LITE.md` and the module file named in the task (or paste them at the top of the chat).
- **Gemini:** same as ChatGPT: attach or paste the lite file and the module.
- **Any agent with file access (Cursor, Codex, Jules, Copilot):** run in a checkout of the repo; the entry points lead to `AGENTS.md`.

Write down which route you used: the full skill and the lite file are different conditions.

## Prompts (copy exactly)

### Task A: web UI, baseline
> Attached are the HTML and two screenshots (1280 px and 390 px wide) of a landing page for a small bakery, "Crumb & Co". Brief: get local customers to pre-order weekend bread; audience is neighbours, mostly on phones, often outdoors; the one idea is "order by Thursday, collect on Saturday"; it must keep the name, the pre-order action, opening hours, the address, the brand orange #E8743B, and the three loaves (sourdough, rye, seeded). Critique the page, list what is good and what must change in order of importance, then write an improved HTML file.

### Task A: web UI, with the skill
> Use the creative-director skill in direct mode. Attached are the HTML and two screenshots (1280 px and 390 px wide) of a landing page for a small bakery, "Crumb & Co". Brief: get local customers to pre-order weekend bread; audience is neighbours, mostly on phones, often outdoors; the one idea is "order by Thursday, collect on Saturday"; it must keep the name, the pre-order action, opening hours, the address, the brand orange #E8743B, and the three loaves (sourdough, rye, seeded). Critique the page against the rules, citing rule IDs, then write an improved HTML file.

### Task B: illustration, baseline
> Attached is a draft of one spread for a children's picture book (ages 4-7). Brief: the lighthouse keeper is out at sea in a storm and the cat waits for the boat. The cat is the focal point; it must keep the cat, the lighthouse, a stormy sea at night and the keeper's small boat coming home, and leave a quiet area for two lines of text. Done when, at thumbnail size, a reader finds the cat first and can tell it is waiting for the boat. Critique this image: what works, what must change, in order of importance, and how you would fix each point.

### Task B: illustration, with the skill
> Use the creative-director skill in consult mode. Attached is a draft of one spread for a children's picture book (ages 4-7). Brief: the lighthouse keeper is out at sea in a storm and the cat waits for the boat. The cat is the focal point; it must keep the cat, the lighthouse, a stormy sea at night and the keeper's small boat coming home, and leave a quiet area for two lines of text. Done when, at thumbnail size, a reader finds the cat first and can tell it is waiting for the boat. Critique this image against the rules, citing rule IDs.

### Task C: technical drawing, baseline
> Attached is a line drawing of a parcel box with a round tin standing on its lid, meant as a product sketch in two-point perspective seen from above eye level. Must keep: box corner toward the viewer, tin centred on the lid, line only. Check the drawing's perspective and ellipses. List every error you find, in order of importance, with how to fix it.

### Task C: technical drawing, with the skill
> Use the creative-director skill in consult mode. Attached is a line drawing of a parcel box with a round tin standing on its lid, meant as a product sketch in two-point perspective seen from above eye level. Must keep: box corner toward the viewer, tin centred on the lid, line only. Check the drawing against the technical-drawing rules, citing rule IDs. If you can run code, use the repo's `tools/vp.py` and `tools/ellipse.py`.

## Scoring

Score each run with [`RUBRIC.md`](RUBRIC.md): faults found from the answer key (recall), wrong claims (false alarms), whether the fixes are right, and, for task A, whether the new page passes the blockers. Fill in [`RESULTS-TEMPLATE.md`](RESULTS-TEMPLATE.md), one file per model, saved as `results/<model>-<date>.md`.

Score blind if you can: have someone who didn't run the model score the outputs with the labels removed.

## Contribute

- **Pull request:** add `results/<model>-<YYYY-MM-DD>.md` (from the template) plus the raw outputs (text, and task A's HTML and a screenshot) in `results/<model>-<YYYY-MM-DD>/`.
- **Issue:** open a [cross-model run](https://github.com/SnazzyGaz/creative-director/issues/new?template=cross-model-run.md) issue and paste the filled-in template; attach the outputs.

Report bad results as readily as good ones: a run where the skill made things worse is the most useful kind.
