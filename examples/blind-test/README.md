# Blind test kit: with and without the skill

**Status: all three batches judged by the owner of the work: 18 to 11 for the skill with 1 tie over 30 briefs (sign test p = 0.13, no clear result).** Batches 1 and 2 tied 10 to 10. Where the version without the skill won, the owner's notes mostly named its eye-catch, energy or obvious call to action, so v0.9.2 added the energy pass ([`core/energy-pass.md`](../../core/energy-pass.md)). Batch 3, made after it, went 8 to 1 with 1 tie (p = 0.020), but it is not independent of the first two batches, its maker saw both arms, and most picks were slight. Full write-up, the owner's reasons and the gaps found: [`RESULTS.md`](RESULTS.md). The three keys are now published here. Nothing has been shown to outside models yet.

This tests one narrow question: given the same brief and the same image model, does a prompt written by following this skill give a piece that people would rather hand to a client than the plain brief does? It does **not** test the critique loop, type set in code, or any of the Python checks.

## How the images were made

- **Briefs.** 30 briefs in three batches. All 30, with both prompts word for word, are in [`briefs.json`](briefs.json).
  - **Batch 1 (B1-B8):** reused from earlier examples, written before this test: 3 posters, 3 illustrations, 2 UI screens.
  - B1 jazz night poster and B4 fox book cover come from [`../baseline-comparison/`](../baseline-comparison/).
  - B2, B3, B5, B6, B7 and B8 come from the frozen briefs in [`../aesthetic-benchmark/reference-set/sources/briefs.md`](../aesthetic-benchmark/reference-set/sources/briefs.md) (01, 02, 03, 12, 05, 06).
  - **Batch 2 (B9-B20):** written for this test on 3 Nov 2026, after the owner asked for more pairs to judge, and before any of their images were made: 4 posters and flyers (B9-B12), 4 illustrations (book cover, editorial, character, picture-book scene: B13-B16), 2 UI screens (B17, B18), a packaging label (B19) and an infographic (B20). Plain, realistic briefs with invented names; some give the exact copy, some leave it open (B10's headline, B19's label copy). Made the same way as batch 1.
  - **Batch 3 (B21-B30):** written for this test on 3 Nov 2026, after the batch 1 and 2 result and after the energy pass was added, and before any of their images were made: 2 posters (B21, B22), an infographic (B23), 2 picture-book pieces (cover B24, spread B25), a coffee bag (B26), a web hero (B27), 2 official notices (B28, B29) and a character concept (B30). Each brief gives its exact copy, since open copy pushed earlier with-skill prompts into placeholders. Made the same way, one sheet per brief.
- **Without the skill:** the brief text, sent as is.
- **With the skill:** a prompt written by Grok Bot following the skill at Step 0: only the brief's facts as text, a hierarchy, two typefaces at most, one light, a value plan, a small palette and a list of things not to add. Batch 3's with-skill prompts also follow the energy pass (EN-2): a focal hook, confident display type, purposeful colour, movement or scale contrast, an obvious call to action and the issuer's name on official pieces, with no added grain or texture. When the brief left copy open (B4's title, B7's pitch, B10's headline, B19's label), the with-skill prompt used the brief's own words or a marked placeholder.
- **Same model, same effort.** Both arms used GenerateImage (Grok Bot's built-in image tool) on 3 Nov 2026, at the same aspect ratio, **one call each, first output kept**, with no edits, rerolls, retouching or type set afterwards. That is one round per arm, so the extra-round bias noted in the reference set doesn't apply here.
- B7's brief said "Photo supplied"; no photo can be given to the image model, so that phrase was dropped from both arms.

## Known biases (read before scoring)

- The with-skill prompts were written by the same bot that maintains the skill, and it saw every image while making the sheets. It must not judge.
- Batch 3 is not independent of batches 1 and 2: the energy pass was written after reading the owner's notes on them, so a batch 3 win tests that rule on new briefs, judged by the same person, not the skill as first written.
- The judging sheets show the brief, so a judge can see that one piece sticks to the brief's words and the other adds slogans, signs or extra facts. That's part of what the skill is for, but it makes the with-skill piece easier to spot.
- Image models follow long prompts unevenly; one sample per arm per brief is noisy. `score.py` runs a one-sided sign test over the briefs that weren't ties, for all briefs together and for each batch. With no ties, a clear result (p < 0.05) needs **20 of 30** for one side overall (15 of 20 for batches 1 and 2), 7 of 8 in batch 1 alone, 10 of 12 in batch 2 alone, or 9 of 10 in batch 3 alone; ties lower the count needed but also the briefs counted. Anything less is no clear result.
- **Repeats.** Batch 1 shows each pair twice with the sides swapped, to catch position bias. A human judge recognises the repeat, so it adds nothing for them: batches 2 and 3 have **one sheet per brief**, with the side picked at random per sheet, and batch 1's two sheets are scored as one judgement per pair (agreeing picks, or the only one filled in; disagreeing picks are a tie). Swapped repeats still make sense for outside-model judges, so `blind.py --repeat` can still build them.

## Files

| File | What it is |
|---|---|
| [`briefs.json`](briefs.json) | The 30 briefs (batches 1 to 3) and both prompts, word for word |
| [`blind.py`](blind.py) | Shuffles a batch's images into judging sheets (random sides, random 4-letter IDs; `--repeat` for each pair twice with sides swapped, as in batch 1) and writes that batch's hidden key |
| [`KEY-SHA256.txt`](KEY-SHA256.txt) | Hashes of the three keys (one per batch), each committed before its batch was judged |
| `blind-test-key.json`, `-2`, `-3` | The keys, published after judging; `sha256sum -c KEY-SHA256.txt` passes for all three |
| [`RESULTS.md`](RESULTS.md) | The result, per batch and overall, with the owner's reasons and the gaps found |
| [`scoring-owner.csv`](scoring-owner.csv) | The owner's picks and strengths, with the reasons paraphrased |
| [`SCORING.md`](SCORING.md), [`scoring.csv`](scoring.csv) | The scoring form, for the owner of the work and any other judge |
| [`OUTSIDE-MODEL-PROMPT.md`](OUTSIDE-MODEL-PROMPT.md) | The prompt for outside models, to use only after the owner has scored |
| [`score.py`](score.py) | Tallies filled-in forms against the key once judging is over |

**Not in git:** the 60 generated images and the 38 sheets (16 in batch 1, 12 in batch 2, 10 in batch 3; kept out to keep the repo small). Whoever runs the test gets the sheets directly.

## Running it

1. The owner of the work scores the sheets alone, first (done for all three batches), in `scoring.csv` (or the table in `SCORING.md`). **The owner's picks weigh most**: the skill exists to make work its owner would sign off.
2. Optional: other people, then outside models with [`OUTSIDE-MODEL-PROMPT.md`](OUTSIDE-MODEL-PROMPT.md). Every judge is reported separately; model picks never outweigh the owner's.
3. Publish the keys next to `KEY-SHA256.txt`, check their hashes (`sha256sum -c`), run `python3 examples/blind-test/score.py --key blind-test-key.json --key blind-test-key-2.json --key blind-test-key-3.json scoring-*.csv`, and write up the result, whatever it is (done: [`RESULTS.md`](RESULTS.md)).
