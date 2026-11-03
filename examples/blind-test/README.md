# Blind test kit: with and without the skill

**Status: batch 1 (S01-S16) being judged by the owner of the work; batch 2 (S17-S28) ready, not yet judged. No results exist.** Nothing here has been shown to outside models, and nothing in this repo should claim the skill wins or loses until the sheets are scored.

This tests one narrow question: given the same brief and the same image model, does a prompt written by following this skill give a piece that people would rather hand to a client than the plain brief does? It does **not** test the critique loop, type set in code, or any of the Python checks.

## How the images were made

- **Briefs.** 20 briefs in two batches. All 20, with both prompts word for word, are in [`briefs.json`](briefs.json).
  - **Batch 1 (B1-B8):** reused from earlier examples, written before this test: 3 posters, 3 illustrations, 2 UI screens.
  - B1 jazz night poster and B4 fox book cover come from [`../baseline-comparison/`](../baseline-comparison/).
  - B2, B3, B5, B6, B7 and B8 come from the frozen briefs in [`../aesthetic-benchmark/reference-set/sources/briefs.md`](../aesthetic-benchmark/reference-set/sources/briefs.md) (01, 02, 03, 12, 05, 06).
  - **Batch 2 (B9-B20):** written for this test on 3 Nov 2026, after the owner asked for more pairs to judge, and before any of their images were made: 4 posters and flyers (B9-B12), 4 illustrations (book cover, editorial, character, picture-book scene: B13-B16), 2 UI screens (B17, B18), a packaging label (B19) and an infographic (B20). Plain, realistic briefs with invented names; some give the exact copy, some leave it open (B10's headline, B19's label copy). Made the same way as batch 1.
- **Without the skill:** the brief text, sent as is.
- **With the skill:** a prompt written by Grok Bot following the skill at Step 0: only the brief's facts as text, a hierarchy, two typefaces at most, one light, a value plan, a small palette and a list of things not to add. When the brief left copy open (B4's title, B7's pitch, B10's headline, B19's label), the with-skill prompt used the brief's own words or a marked placeholder.
- **Same model, same effort.** Both arms used GenerateImage (Grok Bot's built-in image tool) on 3 Nov 2026, at the same aspect ratio, **one call each, first output kept**, with no edits, rerolls, retouching or type set afterwards. That is one round per arm, so the extra-round bias noted in the reference set doesn't apply here.
- B7's brief said "Photo supplied"; no photo can be given to the image model, so that phrase was dropped from both arms.

## Known biases (read before scoring)

- The with-skill prompts were written by the same bot that maintains the skill, and it saw every image while making the sheets. It must not judge.
- The judging sheets show the brief, so a judge can see that one piece sticks to the brief's words and the other adds slogans, signs or extra facts. That's part of what the skill is for, but it makes the with-skill piece easier to spot.
- Image models follow long prompts unevenly; one sample per arm per brief is noisy. `score.py` runs a one-sided sign test over the briefs that weren't ties, for all 20 together and for each batch. With no ties, a clear result (p < 0.05) needs **15 of 20** for one side overall, 7 of 8 in batch 1 alone, or 10 of 12 in batch 2 alone; ties lower the count needed but also the briefs counted. Anything less is no clear result.
- **Repeats.** Batch 1 shows each pair twice with the sides swapped, to catch position bias. A human judge recognises the repeat, so it adds nothing for them: batch 2 has **one sheet per brief**, with the side picked at random per sheet, and batch 1's two sheets are scored as one judgement per pair (agreeing picks, or the only one filled in; disagreeing picks are a tie). Swapped repeats still make sense for outside-model judges, so `blind.py --repeat` can still build them.

## Files

| File | What it is |
|---|---|
| [`briefs.json`](briefs.json) | The 20 briefs (batch 1 and 2) and both prompts, word for word |
| [`blind.py`](blind.py) | Shuffles a batch's images into judging sheets (random sides, random 4-letter IDs; `--repeat` for each pair twice with sides swapped, as in batch 1) and writes that batch's hidden key |
| [`KEY-SHA256.txt`](KEY-SHA256.txt) | Hashes of the two hidden keys (one per batch), each committed before its batch was judged |
| [`SCORING.md`](SCORING.md), [`scoring.csv`](scoring.csv) | The scoring form, for the owner of the work and any other judge |
| [`OUTSIDE-MODEL-PROMPT.md`](OUTSIDE-MODEL-PROMPT.md) | The prompt for outside models, to use only after the owner has scored |
| [`score.py`](score.py) | Tallies filled-in forms against the key once judging is over |

**Not in git:** the 40 generated images and the 28 sheets (16 in batch 1, 12 in batch 2; kept out to keep the repo small and the test blind), and the two keys. Whoever runs the test gets the sheets directly.

## Running it

1. The owner of the work scores all 28 sheets alone, first, in `scoring.csv` (or the table in `SCORING.md`). **The owner's picks weigh most**: the skill exists to make work its owner would sign off.
2. Optional: other people, then outside models with [`OUTSIDE-MODEL-PROMPT.md`](OUTSIDE-MODEL-PROMPT.md). Every judge is reported separately; model picks never outweigh the owner's.
3. Publish both keys next to `KEY-SHA256.txt`, check their hashes (`sha256sum -c`), run `python3 examples/blind-test/score.py --key blind-test-key.json --key blind-test-key-2.json scoring-*.csv`, and write up the result here, whatever it is, with the sheets.
