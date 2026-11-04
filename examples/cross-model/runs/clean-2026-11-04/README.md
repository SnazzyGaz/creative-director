# Clean runs, 4 November 2026

The first clean outside runs of the kit. Claude has all six runs (3 tasks, baseline and with skill). GPT has two runs, and they are on different tasks, so there is no GPT pair yet.

## Method
- Each run had its own folder with only its inputs and `prompt.txt`. The with-skill runs also had `lite/CREATIVE-DIRECTOR-LITE.md` and the module the task names. No run saw the repo, `RUBRIC.md` or `examples/`.
- **Claude:** run through the Cowork app, with a fresh task per run that read only its own folder.
- **GPT:** ChatGPT Free on its default model, a new Temporary Chat per run, with memory off. The text files were pasted into the message and the images were attached.
- Runs were shuffled (run-01 to run-06) and scored against the answer keys in [`RUBRIC.md`](../../RUBRIC.md) before the key that maps runs to task and condition was opened. Scores are in [`scores.csv`](scores.csv).

## Results (found / blockers found / fix quality)

| Task | Claude baseline | Claude with skill | GPT |
|---|---|---|---|
| A, web UI | 5/5, 3/3, 9/10 | 5/5, 3/3, 10/10 | with skill: 5/5, 3/3, 6/10 |
| B, illustration | 4/5, 0/1, 8/10 | 5/5, 1/1 (implied), 8/10 | pending |
| C, technical drawing | 5/5, 5/5, 10/10 | 5/5, 5/5, 10/10 | baseline: 2/5, 2/5, 3/10, 2 false alarms |

Claude had no false alarms in either condition and ranked blockers first every time. Every rule ID cited in the with-skill runs matched its fault.

## What the skill added
- **Claude:** fault-finding barely changed, since the baseline already found 14 of 15. The one gain was task B's blocker, the light sources that disagree, which the baseline missed (the with-skill run only implies it). The main difference was in structure: rule IDs, the brief stated, measurements from the kit's tools, a rework-or-regenerate verdict, and fixes capped per round.
- **GPT:** no pair yet, so nothing can be concluded. Its task C baseline missed the horizon, the ellipse tilt and the pointed top ellipse. It also made two wrong claims: that the ellipse tilt is "not inherently wrong" and that both ellipses should match. That hints the skill may help GPT more on drawing, but the task C with-skill run is needed to test it.

## Caveats
- **Not fully blind.** The with-skill prompts name the skill, so the scorer could tell the condition from the prompt.
- **One scorer, one run per cell.** These results are indicative, not statistical.
- **Task A fix check skipped.** The rewritten pages were not rendered or measured for contrast and reflow.
- **GPT is incomplete.** Task B (both conditions), task A baseline and task C with skill are still pending because of the Free plan's upload limits.
- **Fraunces.** Claude's with-skill task A page loads the Fraunces typeface. The skill doesn't currently rule out that typeface, so this is a note for the owner's house style, not a scoring fault.
