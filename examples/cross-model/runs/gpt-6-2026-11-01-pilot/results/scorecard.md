# Results and scoring — GPT-specific tester

Date: 2026-11-01
Evaluator: ChatGPT GPT-6
Status: **pilot / reconstructed paired responses, not a clean independent A/B experiment**

## Why this is not a clean benchmark result
I inspected the repository's rubric before producing the skill-conditioned analyses. That creates rubric contamination. Also, the paired outputs were written in this conversation rather than generated in six separate fresh sessions. They are useful for a qualitative side-by-side check, but should not be treated as statistically independent model runs or as proof that the skill causes improvement.

## Scorecard

Scoring key: faults found / 5; blockers found; blocker-first ordering (yes/no); false alarms; fix quality /10. The repository's rubric should remain the authoritative final scoring guide. Since some values require judging wording and the run setup was not blind, the scores below are indicative and should not be merged into official cross-model results.

| Task | Condition | Faults found | Blockers found | Blockers prioritised | False alarms | Fix quality /10 | Output check |
|---|---|---:|---:|---|---|---:|---|
| A | Baseline-style | 5/5 | 3/3 | Yes | 0 obvious | 8 | Not rendered/tested |
| A | Skill-style | 5/5 | 3/3 | Yes | 0 obvious | 9 | Source improved; viewport/contrast tests not run |
| B | Baseline-style | 4/5 | 1/1 | Yes | 0 obvious | 7 | No revised image generated |
| B | Skill-style | 5/5 | 1/1 | Yes | 0 obvious | 9 | No revised image generated |
| C | Baseline-style | 4/5 | 4/5 | Mostly | 0 obvious | 7 | No geometric measurements |
| C | Skill-style | 5/5 | 5/5 | Yes | 0 obvious | 9 | No geometric measurements |

## Interpretation

The skill-style answers are more systematic: they explicitly separate blockers, use rule IDs, order fixes, state preservation constraints and flag confidence/measurement limits. This is partly expected because the skill prompt directly requests those behaviours, so these observations alone do not prove better underlying judgement.

The clearest practical artifact is Task A's rewritten HTML. It uses a responsive layout, real semantic controls and an honest mailto draft instead of fake submit controls. But it has not been rendered in a browser at 390/1280 px or tested at 200% text zoom, and the example email address is a placeholder. Do not deploy it unchanged.

## Suggested next clean run
1. Create six fresh sessions; attach only the task input and prompt appropriate to that condition.
2. Do not include the answer key or rubric in the model context.
3. Save raw output exactly as returned.
4. Score anonymized outputs with a separate evaluator.
5. Render and test Task A's HTML, and generate revised images for B/C if assessing correction ability.
6. Keep the current scorecard labeled “pilot” and do not submit it as clean cross-model results.
