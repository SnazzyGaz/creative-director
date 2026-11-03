# Blind test results: with and without the skill

Judged by the owner of the work, alone, on 3 Nov 2026: 30 briefs, one image per arm per brief, sides and IDs hidden. One judge, so this says what the owner of the work prefers, not what people in general prefer. How the images were made and the known biases: [`README.md`](README.md).

## Result

One judgement per brief (batch 1 shows each pair twice; agreeing picks or the only one filled in count once). One-sided sign test over the briefs that were not ties (`score.py`).

| Batch | Briefs | With the skill | Without | Tie | Sign test (one-sided) | Reading |
|---|---|---|---|---|---|---|
| 1 (B1-B8) | 8 | 5 | 3 | 0 | 5 of 8, p = 0.36 | no clear result |
| 2 (B9-B20) | 12 | 5 | 7 | 0 | 7 of 12 for without, p = 0.39 | no clear result |
| 1 + 2 | 20 | 10 | 10 | 0 | 10 of 20, p = 0.59 | a tie |
| 3 (B21-B30), after the energy pass | 10 | 8 | 1 | 1 | 8 of 9, p = 0.020 | for the skill, with the caveats below |
| **All** | **30** | **18** | **11** | **1** | **18 of 29, p = 0.13** | **no clear result** |

Batch 3's p = 0.020 is one of four tests run on these data (three batches and the total). Corrected for that (Bonferroni, 0.05 / 4 = 0.0125) it would not count as clear. Read it as a promising sign, not as proof.

**Strength** (1 slight, 2 clear, 3 strong; the owner left some blank):

| Winner | Picks | Slight | Clear | Strong | Not rated |
|---|---|---|---|---|---|
| With the skill | 18 | 6 | 5 | 1 | 6 |
| Without | 11 | 5 | 1 | 0 | 5 |

In batch 3 the skill's 8 wins were 5 slight, 1 clear and 2 not rated. Several picks across all batches were called forced, borderline, close, reluctant or a toss-up (S05, S07, S24, S26, S27, S29, S33).

**By medium** (all batches): illustration, picture books and characters 8 with, 1 without, 1 tie; posters and flyers 4 with, 5 without; screens and web heroes 2 with, 3 without; packaging, infographics and notices 4 with, 2 without.

**Position:** across the 31 judged sheets the owner picked the left image 14 times and the right 16 times, with one tie, so there is no sign of a side bias.

## What the notes said

**Batches 1 and 2: sterile versus slop.** The owner's notes described the two arms in almost opposite terms. The with-skill versions were called academic, sterile, clinical, basic or "too clean" in 10 of the 18 notes written on those sheets, and once "like word-processor clip art". The versions without the skill were called eye-catching, lively or dynamic, and in the same breath busy, generic or obviously machine-made, in 8 notes. Where the skill won, the notes mostly named clarity, a single idea, lean information, simplicity that suited the audience, or truth to the brief. Where it lost, they named the other side's energy, boldness, colour coding, official branding or obvious call to action. Neither end was what the owner wanted: several picks were the lesser of two failures.

**The change.** v0.9.2 added the [energy pass](../../core/energy-pass.md): once accuracy and clarity pass, and only where it applies, check for one focal hook at thumbnail size, confident display type, purposeful colour, movement, an obvious call to action, the issuer on official pieces and a mood that matches the brief. Energy comes from structure, not texture: no clutter, added copy or generated grain. Batch 3's with-skill prompts followed it.

**Batch 3.** "Sterile", "academic" and "clinical" do not appear in the batch 3 notes. The without-skill side was called too busy once. The criticisms moved to new places, often on the winning side:
- **Concept fit.** Both coffee bags read as fabric softener or soap, not coffee; the brand name pulled both toward the sea (S29).
- **Empty scenes.** The fête poster's empty street looked barren; selling fun needed a lively scene (S30).
- **Official identity.** An official header with no real logo looked characterless, like a children's project (S32); the issuer's real branding would have been better (S38); the issuer's name at the top read as official say-so rather than advertising (S37).
- **Text on colour.** Black text was lost on a red header; white would have read better (S32). Measured on that header, white is 4.74:1 and black 4.43:1.
- **Figure and ground.** A climber in dark clothes against a wall of the same tone disappeared at a distance (S34).
- **Unwanted readings.** A lone climbing shoe at a wall could read as an accident (S34).
- **Title against the focal image.** The losing cover's title fought the moon and unbalanced the layout (S35).
- **Still plain.** Both pool notices looked amateurish and bland (S37); the winning road notice was clear but "not nice to look at" (S38).

## Caveats for batch 3

- **Not independent.** The energy pass and the batch 3 briefs were written after reading the owner's notes on batches 1 and 2, by the same bot, for the same judge. A win here tests that rule on new briefs for this judge, not the skill as first written.
- **The maker saw both arms** while making the images and sheets (the judge did not).
- **Mostly slight.** 5 of the 8 wins were rated slight, and 2 were not rated.
- **One sample per arm**, first output kept, so the image model's luck counts. Ten briefs is a small batch.
- **The briefs gave exact copy** this time; that helps both arms but especially the with-skill prompt, which earlier had to use placeholders.

## Gaps found, and what changed

v0.9.3 adds rules for the first five gaps below, with these notes as internal evidence (one judge):
- **Issuer marks on official pieces** (BRAND-4, EN-2 item 6): use the real mark from its file with the name at the top; if there is none, ask, or leave a labelled slot and flag it. Never invent a crest, and don't fall back to a characterless text header.
- **Subject against ground, text on colour** (CV-10, EN-2 items 1 and 3): the subject must separate from its ground in value at a distance; on a saturated colour, test black and white text and use the higher-contrast one.
- **Concept fit and unwanted readings** (EN-2 item 8, CD-3): the idea suits the product's category and senses, not just its name; look for readings nobody meant.
- **Fun events show the fun** (EN-2 item 7): show the activity and the people, not an empty place.

Still open, with no new rule yet:
- a title competing with the main image on a cover (S35);
- a character's defining trait not shown: neither version of the lighthouse keeper looked scared of the dark (S36);
- official notices that are clear but bland (S37, S38).

## Files

- `blind-test-key.json`, `blind-test-key-2.json`, `blind-test-key-3.json`: the three keys, published after judging. `sha256sum -c KEY-SHA256.txt` passes for all three; it also warns about the explanation lines in that file, which is expected.
- [`scoring-owner.csv`](scoring-owner.csv): the owner's picks and strengths. The reasons are paraphrased in plain language, and "left" and "right" are replaced with "this one" and "the other". Batch 1's repeat sheets (S10-S16) were left blank, as allowed.
- Re-run: `python3 examples/blind-test/score.py --key examples/blind-test/blind-test-key.json --key examples/blind-test/blind-test-key-2.json --key examples/blind-test/blind-test-key-3.json examples/blind-test/scoring-owner.csv`

## Every judgement

Sheet, brief, medium, the arm the owner picked, strength, and the owner's reason (paraphrased).

| Sheet | Brief | Medium | Picked | Strength | Reason |
|---|---|---|---|---|---|
| S01 | B3 | poster | without | - | Gets who, what, when and why across fast and boldly; the other feels too academic. |
| S02 | B5 | illustration | with | - | More pleasant, and holds together around one idea. |
| S03 | B6 | illustration | with | - | Livelier in scope and colour, and cosy; the other feels bleak and run-down. |
| S04 | B8 | ui | with | - | Tight and lean with its information; the other is busy and overwhelming. |
| S05 | B7 | ui | without | 1 | Borderline: the other has nicer energy but looks obviously machine-made. |
| S06 | B4 | illustration | with | 2 | Its simplicity suits a children's book; the busier one might suit children who like lots to look at. |
| S07 | B1 | poster | without | 1 | Forced choice: one is over-academic and sterile, the other obvious generated slop. |
| S08 | B4 | illustration | with | 2 | Repeat of S06, same pick. |
| S09 | B2 | poster | with | 2 | Very sterile and academic, but shows night best. |
| S17 | B15 | illustration | with | 2 | More polished and truer to the brief, though the postwoman clue is missing; the other overdoes it to political-cartoon level and misses the detective. |
| S18 | B9 | poster | without | 1 | Lively and eye-catching, though busy and obviously generated; the other is over-clinical, like word-processor clip art. |
| S19 | B20 | infographic | without | 2 | Colour-coded, easier for a general audience, and carries official branding; the other is too basic and clinical. |
| S20 | B12 | poster | with | 2 | Clean, though the type is basic; the other catches the eye but is busy generated slop. |
| S21 | B17 | ui | without | - | - |
| S22 | B13 | illustration | with | - | - |
| S23 | B19 | packaging | without | - | - |
| S24 | B10 | poster | without | 1 | Picked reluctantly, as a client might prefer it; one is a generated eye-catcher, the other academic and basic. |
| S25 | B14 | illustration | with | 3 | Clearly this one. |
| S26 | B11 | poster | without | 1 | Forced: one is a generic generated layout, the other too clinical and minimal. |
| S27 | B16 | illustration | with | 1 | Close: the other is over-busy with generated texture; this one is clean, if a little sterile. |
| S28 | B18 | ui | without | - | One is too clean; the other a bit busy, but its call to action is more obvious. |
| S29 | B26 | packaging | with | 1 | Forced: neither idea works; coffee shouldn't read as sea or water, and both look like fabric softener or soap packaging. The brand name pushed the sea theme. |
| S30 | B21 | poster | with | 1 | More original, but the empty street looks barren; it needed a lively scene to sell the fun. |
| S31 | B27 | web hero | with | - | Grabs attention and gets the idea across at a glance. |
| S32 | B23 | infographic | with | - | Easier to take in, but its official header has no character: official pieces need the real logo or they look like a children's project. Black text gets lost on the red; white would be better. The other is too busy. |
| S33 | B25 | kids book | with | 1 | A toss-up; this one is composed better. |
| S34 | B22 | poster | with | 2 | More original idea, but the climber is lost in the scene: dark clothes on a wall of the same tone don't read from a distance. The other's lone shoe at the wall could read as an accident. |
| S35 | B24 | kids book | without | - | Its central title reads better; the spirit and gist win despite its problems. The other's illustration is tighter, but its title fights the moon and the layout is unbalanced. |
| S36 | B30 | character | tie | - | Both meet the brief and fall short equally; they read as the same character, one slightly older but still young. |
| S37 | B29 | official notice | with | 1 | Both look equally amateurish; this one gets the information across more strongly, and the name at the top reads as an official say-so for an on-site notice, not as advertising. Bland. |
| S38 | B28 | official notice | with | 1 | Clearer information, though not nice to look at; the issuer's real branding would have been better. |
