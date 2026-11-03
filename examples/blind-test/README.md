# Blind test kit: with and without the skill

**Status: ready to judge, not yet judged. No results exist.** Nothing here has been shown to outside models, and nothing in this repo should claim the skill wins or loses until the sheets are scored.

This tests one narrow question: given the same brief and the same image model, does a prompt written by following this skill give a piece that people would rather hand to a client than the plain brief does? It does **not** test the critique loop, type set in code, or any of the Python checks.

## How the images were made

- **Briefs.** 8 briefs reused from earlier examples, written before this test: 3 posters, 3 illustrations, 2 UI screens. All 8, with both prompts word for word, are in [`briefs.json`](briefs.json).
  - B1 jazz night poster and B4 fox book cover come from [`../baseline-comparison/`](../baseline-comparison/).
  - B2, B3, B5, B6, B7 and B8 come from the frozen briefs in [`../aesthetic-benchmark/reference-set/sources/briefs.md`](../aesthetic-benchmark/reference-set/sources/briefs.md) (01, 02, 03, 12, 05, 06).
- **Without the skill:** the brief text, sent as is.
- **With the skill:** a prompt written by Grok Bot following the skill at Step 0: only the brief's facts as text, a hierarchy, two typefaces at most, one light, a value plan, a small palette and a list of things not to add. When the brief left copy open (B4's title, B7's pitch), the with-skill prompt used the brief's own words or a marked placeholder.
- **Same model, same effort.** Both arms used GenerateImage (Grok Bot's built-in image tool) on 3 Nov 2026, at the same aspect ratio, **one call each, first output kept**, with no edits, rerolls, retouching or type set afterwards. That is one round per arm, so the extra-round bias noted in the reference set doesn't apply here.
- B7's brief said "Photo supplied"; no photo can be given to the image model, so that phrase was dropped from both arms.

## Known biases (read before scoring)

- The with-skill prompts were written by the same bot that maintains the skill, and it saw every image while making the sheets. It must not judge.
- The judging sheets show the brief, so a judge can see that one piece sticks to the brief's words and the other adds slogans, signs or extra facts. That's part of what the skill is for, but it makes the with-skill piece easier to spot.
- Image models follow long prompts unevenly; one sample per arm per brief is noisy. 8 briefs is a small test: only 7 or 8 of 8 for one side counts as a clear result (`score.py` does the sign test).

## Files

| File | What it is |
|---|---|
| [`briefs.json`](briefs.json) | The 8 briefs and both prompts, word for word |
| [`blind.py`](blind.py) | Shuffles the 16 images into 16 judging sheets (each pair twice, sides swapped, random 4-letter IDs) and writes the hidden key |
| [`KEY-SHA256.txt`](KEY-SHA256.txt) | Hash of the hidden key, committed before judging |
| [`SCORING.md`](SCORING.md), [`scoring.csv`](scoring.csv) | The scoring form, for the owner of the work and any other judge |
| [`OUTSIDE-MODEL-PROMPT.md`](OUTSIDE-MODEL-PROMPT.md) | The prompt for outside models, to use only after the owner has scored |
| [`score.py`](score.py) | Tallies filled-in forms against the key once judging is over |

**Not in git:** the 16 generated images and the 16 sheets (kept out to keep the repo small and the test blind), and the key. Whoever runs the test gets the sheets directly.

## Running it

1. The owner of the work scores all 16 sheets alone, first, in `scoring.csv` (or the table in `SCORING.md`). **The owner's picks weigh most**: the skill exists to make work its owner would sign off.
2. Optional: other people, then outside models with [`OUTSIDE-MODEL-PROMPT.md`](OUTSIDE-MODEL-PROMPT.md). Every judge is reported separately; model picks never outweigh the owner's.
3. Publish the key next to `KEY-SHA256.txt`, check its hash, run `python3 examples/blind-test/score.py --key blind-test-key.json scoring-*.csv`, and write up the result here, whatever it is, with the sheets.
