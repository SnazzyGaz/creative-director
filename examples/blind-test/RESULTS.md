# Blind test results: with and without the skill

Judged by the owner of the work, alone, on 3 Nov 2026: 100 briefs in eight batches, one image per arm per brief, sides and IDs hidden. One judge, so this says what the owner of the work prefers, not what people in general prefer. How the images were made and the known biases: [`README.md`](README.md).

## Result

One judgement per brief (batch 1 shows each pair twice; agreeing picks or the only one filled in count once). One-sided sign test over the briefs that were not ties (`score.py`).

| Batch | Briefs | With the skill | Without | Tie | Sign test (one-sided) | Reading |
|---|---|---|---|---|---|---|
| 1 (B1-B8) | 8 | 5 | 3 | 0 | 5 of 8, p = 0.36 | no clear result |
| 2 (B9-B20) | 12 | 5 | 7 | 0 | 7 of 12 for without, p = 0.39 | no clear result |
| 1 + 2, the skill before the energy pass | 20 | 10 | 10 | 0 | 10 of 20, p = 0.59 | a tie |
| 3 (B21-B30), after the energy pass | 10 | 8 | 1 | 1 | 8 of 9, p = 0.020 | for the skill, with the caveats below |
| 4 (B31-B40), v0.9.3 | 10 | 6 | 4 | 0 | 6 of 10, p = 0.38 | no clear result |
| 5 (B41-B50), v0.9.3 unchanged, a replication | 10 | 8 | 2 | 0 | 8 of 10, p = 0.055 | just short of clear |
| 3 to 5, with the energy pass | 30 | 22 | 7 | 1 | 22 of 29, p = 0.004 | for the skill, with the caveats below |
| All of batches 1 to 5 | 50 | 32 | 17 | 1 | 32 of 49, p = 0.022 | for the skill: met the 32-of-50 bar set in advance |
| 6 (B51-B60), infographics only, v0.9.4 | 10 | 4 | 6 | 0 | 6 of 10 for without, p = 0.38 | no clear result; a loss on the count |
| 3 to 6, with the energy pass | 40 | 26 | 13 | 1 | 26 of 39, p = 0.027 | for the skill, with the caveats below |
| All of batches 1 to 6 | 60 | 36 | 23 | 1 | 36 of 59, p = 0.059 | no clear result: one short of the 37-of-60 bar set before batch 6 |
| 7 (B61-B70), infographics only, v0.9.5 | 10 | 3 | 7 | 0 | 7 of 10 for without, p = 0.17 | no clear result; a loss on the count |
| 6 + 7, infographics | 20 | 7 | 13 | 0 | 13 of 20 for without, p = 0.13 | no clear result; behind on infographics |
| 3 to 7, with the energy pass | 50 | 29 | 20 | 1 | 29 of 49, p = 0.13 | no clear result |
| All of batches 1 to 7 | 70 | 39 | 30 | 1 | 39 of 69, p = 0.17 | no clear result: well short of the 43-of-70 bar set before batch 7 |
| 8 (B71-B100), six themes, v0.9.6 | 30 | 20 | 10 | 0 | 20 of 30, p = 0.049 | for the skill: met the 20-of-30 bar set before batch 8 |
| 3 to 8, with the energy pass | 80 | 49 | 30 | 1 | 49 of 79, p = 0.021 | for the skill, with the caveats below |
| **All** | **100** | **59** | **40** | **1** | **59 of 99, p = 0.035** | **for the skill: met the 59-of-100 bar set before batch 8** |

**The bar set in advance.** Before batch 4 was judged, the kit README said a clear overall result needs 32 of 50 for one side ([`README.md`](README.md), Known biases). The skill got exactly 32, with 17 against and 1 tie: one-sided p = 0.022. That overall count was the main test at 50 briefs. Before batch 6 was judged, the kit README raised the bar to 37 of 60. With batch 6 the skill stands at 36 to 23 with 1 tie (p = 0.059): **one win short, so the 60-brief result is not clear**, and it should be read that way. The 50-brief result still stands as what was tested then; it does not carry over to infographics. Before batch 7 was judged the bar became 43 of 70; batch 7 went 3 to 7, so all 70 stand at 39 to 30 with 1 tie (p = 0.17), **well short**. Before batch 8 was judged the kit README set the bar at 59 of 100 overall (p = 0.044; 58 would give 0.067) and 20 of 30 for batch 8 alone. Batch 8 went 20 to 10 (p = 0.049), so all 100 stand at 59 to 40 with 1 tie (p = 0.035): **the bar was met, so the 100-brief result is clear for the skill**, with the caveats below, and only just: one fewer win would have missed it. The per-batch and combined rows are extra looks at the same data (eighteen rows; a strict Bonferroni cut would be 0.05 / 18 ≈ 0.003); by that standard batch 3 alone (0.020) and batch 8 alone (0.049) are not clear, batches 3 to 5 together (0.004) just miss, and batches 3 to 6 (0.027), 3 to 7 (0.13) and 3 to 8 (0.021) are not. The pre-set overall count is the main test; the other rows show the trend, not separate proofs.

**What it means.** After the energy pass, the owner preferred the with-skill version in 22 of 29 decided briefs; before it, 10 of 20. The rise lines up with the rule change, but the briefs, the rules and the judge are not independent (see Caveats), so this is internal evidence for one judge's taste, not research. Batch 6, the first test confined to one category, went the other way (4 to 6 on infographics), which brings batches 3 to 6 to 26 of 39 (p = 0.027) and all 60 to just short of the bar. Batch 7, on v0.9.5's answer to batch 6, lost 3 to 7: **v0.9.5 made infographics worse, not better** (its notes below). On infographics the skill is now 7 to 13 behind; on pictures it still leads. Batch 8, on v0.9.6 and away from infographics, won 20 to 10 across six themes; screens were its weak spot (2 to 3).

**Strength** (1 slight, 2 clear, 3 strong; the owner left some blank):

| Winner | Picks | Slight | Clear | Strong | Not rated |
|---|---|---|---|---|---|
| With the skill | 59 | 15 | 31 | 6 | 7 |
| Without | 40 | 16 | 19 | 0 | 5 |

All six strong picks went to the skill (the sixth a batch 7 recycling process, S69), four of them in batches 4 and 5 (S41, S42, S49, S52). In batches 4 and 5 the skill's 14 wins were 3 slight, 6 clear, 4 strong and 1 not rated; the 6 losses were 3 slight and 3 clear. In batch 6 the skill's 4 wins were 2 slight and 2 clear, and its 6 losses 3 slight and 3 clear. In batch 7 its 3 wins were 1 slight, 1 clear and 1 strong, and its 7 losses 1 slight (a forced pick, S74) and 6 clear. Several picks across all batches were called forced, borderline, close, reluctant or a toss-up (S05, S07, S24, S26, S27, S29, S33, S39, S40, S54, S57, and a tough call and a judgement call in batch 6, S64 and S66). In batch 8 the skill's 20 wins were 3 slight and 17 clear, and its 10 losses 4 slight and 6 clear; nothing was rated strong or left unrated, and two wins were called forced (S89, S95).

**By medium** (all batches): illustration, picture books, characters and covers 26 with, 7 without, 1 tie; posters and flyers 6 with, 5 without; screens and web heroes 5 with, 7 without; packaging, labels, menus, infographics and notices 18 with, 20 without (batches 6 and 7, all infographics, 7 with, 13 without); logos (batch 8 only) 4 with, 1 without. The skill leads on pictures, logos and, in batch 8, packaging; on posters it is about even, and on screens and infographics it is behind.

**Position:** across the 101 judged sheets the owner picked the left image 50 times and the right 50 times, with one tie, so there is no side bias overall. In batch 7 the left image won 8 of 10 (two-sided p ≈ 0.11), with the with-skill image on the left in 5 of the 10, so that batch's split did not come from the sides. The with-skill image sat on the left in 5 of the 10 sheets in each of batches 5, 6 and 7. In batch 8 the left image won 15 of 30; the with-skill image was on the left in 15 sheets and won 10 of them, and on the right in 15 and won 10 of those.

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

**Batches 4 and 5.** The with-skill side won 14 of 20, with four strong wins (a night-run poster, a rainy picture-book spread, a paper-aeroplane spread and a web hero "by miles"). The notes on its wins named gesture over explanation (S48, S53), a picture that follows the words (S49), clean and dynamic art against a glowing, over-detailed chocolate-box look (S50), and quick reading at thumbnail size (S41). Even its wins came with fixes: an instruction left out of the text (S41), speech lettering lost on the soil (S42), a title too loud for a cold mood (S51), a cover's author name off-axis (S46).

Its six losses:
- **S39, web hero (slight):** the other side invented app screens, which the brief did not give; it looked better, and the owner said the with-skill side would win if the brief means finished work.
- **S40, novel cover (slight, reluctant):** the winner was warmer but read as pulpy young-adult fiction; the with-skill side was cold and distant but read as a classic.
- **S43, public infographic (clear):** one panel of the with-skill version failed badly, which sank an otherwise easier piece.
- **S47, jam label (clear):** the with-skill side was too contemporary for jam and had a stroke round its dark fruit; the winner looked like traditional jam, though it printed "small family farm" on the label word for word.
- **S55, menu board (clear):** the winner was balanced, high in contrast and easy to read at a distance: plain and effective for its job.
- **S57, park notice (slight, forced):** the with-skill side's solid centre block and lopsided bottom graphic looked amateur, like a printer's misalignment; the winner was basic text with an ugly yellow call to action.

**Sterile, again, in places.** The batch 1 and 2 complaint came back on two wins: a library infographic "perhaps a bit too sparse" next to a very busy one (S56), and a poster that was "academically tight but bland and sterile" next to a busy, fantastical, cosy one (S58). A picture-book cover won while called "too clean, refined and clinical" for children (S46). The energy pass narrowed the gap; it did not close it.

**Whites that weren't white.** Looking at the images afterwards, the owner noticed that many with-skill pieces had cream or yellowish whites where plain white was expected. Measured with [`whites.py`](whites.py) (luma of the lightest 0.5% of each image, 0 to 255, and the channel spread of those pixels):

| Arm | Median white luma | Median channel spread | Median blue minus red | Under 248 | Under 240 | Spread over 12 |
|---|---|---|---|---|---|---|
| With the skill | 248.3 | 12 | -10 | 25 | 12 | 24 |
| Without | 251.9 | 8 | -8 | 18 | 11 | 17 |

Brief by brief, the with-skill white was lower in 26, higher in 11 and within 1 in 13. The cause is in the prompts: 25 of the 50 with-skill prompts asked for cream, off-white or a warm white, and none of the plain briefs did. Those 25 images had a median white of 243.3 and a spread of 20; the other 25 had 250.2 and 4, about the same as the plain briefs. Some low whites are right (night scenes, dark covers, aged paper), so this is a tendency, not a fault in every image. v0.9.4 adds CV-11 (white means white) and an autocheck for it.

**Batch 6: infographics only, on v0.9.4.** Ten new infographic briefs, written before any image was made, to test the category batches 3 to 5 left "clear but plain". The skill lost 4 to 6, half the picks slight. The owner judged as a commissioner would: the information right first, then appeal.
- **Too plain.** A bar chart "accurate but sterile like a PowerPoint slide" against a dynamic, eye-catching one (S63); a sourdough timeline "too basic" against one with vibes, a stylish layout and a good amount of visual busyness, despite sloppy generated illustrations and an overused bakery name (S65); a nutrition sheet "matter of fact and sterile" against one with emotional direction, like real packaging (S66); a water-safety sheet practical but not eye-pleasing against one with better balance and density (S61).
- **Repetition.** A blood-pressure how-to repeated the same picture in every panel, "repetitive, wasteful"; the other side's specific diagrams served a reader who came for the information (S64).
- **Too busy, the other way.** The skill's voter-registration piece lost as "busy and visually chaotic" against a clean, direct one (S68). So the fix is not just "more": it is richer art direction with a checkable limit.
- **Wins.** A comic-strip how-to for cleanness, information economy, stable characters and clear warnings (S59); a fun-run map for punchier type and an unbroken trail (S60); a water cycle that better fitted the age range (S62); a bin guide with punchier illustrations (S67).
- **Charts and routes (found afterwards, not by the judge).** Neither generated bar chart was to scale. Measured with `tools/datagraphic.py check-bars`, the with-skill chart overstated the small bars by up to 12.5 points of the longest bar, and the other by up to about 10 (B53). The with-skill nutrition bars were up to 4.9 points off and about 17% short against their own 0-10% track (B60); the other side drew no bars. Neither fun-run map closed its loop at start = finish or showed a bridge where the route crossed the river (S60). An image model can't be trusted with numbers or geometry.
- **Whites.** All ten with-skill images had pure neutral whites (lightest 0.5%: luma 255, spread 0), so CV-11 held; three of the other side's had cream or warm grounds (B54, B58, B60).

**Batch 7: infographics again, on v0.9.5.** Ten new infographic briefs (B61-B70), written before any image was made. The with side followed v0.9.5: the full energy pass with drawn scenes, and charts and routes drawn in code and composited into a reserved area (wiped to white where the model drew in it; see the [kit README](README.md#how-the-images-were-made)). The skill lost 3 to 7, six of the losses clear. **v0.9.5 overcorrected**: the fix for "sterile" became decoration on top of the information.
- **Over-illustrated and unbalanced.** A red-kite fact sheet "way over-illustrated, unbalanced info presentation" against one with "simplified icons for sub-info" (S76); a library chart where "the graphic doesn't belong", very unbalanced (S74, a forced pick; the other side rendered the data twice).
- **Charts pasted on.** Even a win had charts that "cut into the graphic and look cheap and pasted on" (S73); the route win was accurate but basic, with place-name strokes cutting into the route and the map unbalanced against the family picture (S71).
- **Chart type.** A council-tax budget as bars in a white panel lost to a donut that was "compact, informational", "reads nicer here" (S72), though that donut was about 8 points off (below).
- **Flow and difference.** A sunflower cycle lost to one whose "transitional flow reads better", and its central hero title was "mildly amateurish" (S75); a market timeline read "samey" against framing that "differentiates times better" (S78).
- **Wrong style, missing text, a medical error.** A thin-ice sheet came out photoreal, "too demonstrative", dropped two required lines and showed people on the ice it warns against (S70); an inhaler comic lost as less coherent and showed the inhaler without its spacer in two panels (S77).
- **Wins.** A recycling process "clear, complex but accurate, eye-catching", strongly, against a magazine look with major errors (S69); the route map, against a side with wrong information (S71), and the reading chart despite its pasted-on look (S73).
- **Charts and routes (measured afterwards).** Every code-drawn chart on the with side was to scale (`check-bars`, worst error 0.7% of the longest bar), and its route closed with a bridge at both crossings. On the other side: the council-tax donut was off by up to about 8 points (social care 38% drawn as about 30%, parks 7% as about 12%), the reading chart used the same five book icons on every row whatever the number, the route map's arrows ran against its own "clockwise", and the library and kite sheets gave no chart. Accuracy alone did not win: the owner rewarded the inaccurate donut's layout.
- **Whites.** All ten with-skill images reached pure white; one of the other side's was dim and warm (B67). The owner added that the whites rule "could allow more warmth depending on context" (S78).
- **What the winners shared, across batches 6 and 7:** accurate information first; compact, balanced, information-dense layouts; one coherent style; simplified icons for secondary facts; a strong flow between steps; each step or period visibly different; punchy type; warmth; some richness, but neither sterile nor over-illustrated.

**Batch 8: six themes, on v0.9.6.** Thirty new briefs (B71-B100), five in each of six themes, written before any image was made and judged on sheets S79-S108. Every image on both sides is untouched model output. The skill won 20 to 10 (p = 0.049), meeting the 20-of-30 bar set in advance.

| Theme | Briefs | With the skill | Without | Its losses |
|---|---|---|---|---|
| Covers | 5 | 4 | 1 | S80 (slight) |
| Packaging | 5 | 4 | 1 | S91 |
| Logos | 5 | 4 | 1 | S93 (slight) |
| Characters and creatures | 5 | 3 | 2 | S97, S108 |
| Picture-book spreads | 5 | 3 | 2 | S92, S98 (slight) |
| Screens | 5 | 2 | 3 | S79 (slight), S88, S100 |

A single theme has five pairs, so a clear theme would need 5 of 5 (p = 0.031); none got there, so these rows are pointers, not results.

- **Screens are the weak spot.** The with side lost three of five. The Coldwater web hero lost because the other side "has soul" (S88). The Pacer run summary lost slightly: the with side dropped the "km" the brief asked for, though the owner liked its personality, perhaps too striking (S79). The Quillbox pricing section was "too bland and basic" (S100). The Harbourlight hero was a with-skill win (S107), though even there the other side had the better atmosphere; the with side won by showing the class filled. Sprout's app screen (S86) was the other win. The screens rules (grid, targets, exact text) kept the pieces tidy but not alive.
- **Too literal, or not suited.** A bear spread lost as too literal (S92); the Brightpath logo was "way literal, not creative" against one too abstract but visually preferred (S93); a kangaroo mascot lost to one better suited to the brief and its context (S97).
- **Craft slips.** The Snorgle was cute, but the other was better and the with side's sock was broken (S108). In the tortoise spread neither side had the right count; the with side was tighter and suited children, but the other's composition won (S98). A hot-sauce label had good brand type but lost on balance, eye pull and flow (S91). A fungi cover lost slightly to the other's central title (S80).
- **What the wins named.** A character that explains itself without a character sheet (S81); a picture book that tells the story across the pages, with composition on each page (S82); eye pull, composition and text that reads left to right (S84); a simple logo that sells it, against a busy one with mismatched type (S87); a wrapper theme the owner liked, though its florals read as ingredients rather than branding (S89, forced); a creature equal to the other but better as a stand-alone reference (S95, forced).
- **Wins with fixes.** A cover's author name lost in the grass, needing contrast (S101); a coffee bag that won though its branding was basic (S102).
- **Found afterwards by the maker, not the judge.** On the with side: the tortoise spread drew 11 guests and lost the full stop after "cups" (B95); the run summary dropped "km" (B84); the Brightpath wordmark used a capital B where lower case was asked (B100); the honey label had a stray comma (B79, a win); the Snorgle holds the sock rather than chewing it (B90). Exact strings and counts still slip.

## Caveats

- **Not independent.** The energy pass and the batch 3 briefs were written after reading the owner's notes on batches 1 and 2, by the same bot, for the same judge; the v0.9.3 rules and the batch 4 briefs followed the batch 3 notes. A win in batches 3 to 5 tests those rules on new briefs for this judge, not the skill as first written.
- **Batch 5 is a replication, not a test of v0.9.4.** It was made on the unchanged v0.9.3 skill, after batch 4 was built but before it was judged, so no rule changed between them. Batch 6 then tested v0.9.4, on infographics only.
- **The maker saw both arms** while making the images and sheets (the judge did not).
- **Batch 3 was mostly slight.** 5 of its 8 wins were rated slight, and 2 were not rated. Batches 4 and 5 had more clear and strong wins, but also the two picks the owner called forced (S57) or reluctant (S40).
- **One sample per arm**, first output kept, so the image model's luck counts: S43 was lost to one broken panel. Ten briefs is a small batch, five a small theme, and 100 is still a small test.
- **The briefs gave exact copy** from batch 3 on; that helps both arms but especially the with-skill prompt, which earlier had to use placeholders.
- **Batches 6 and 7 are one category.** They test infographics only, where the skill's lead was already thin, so their losses say the rules were weakest there, not that the skill got worse elsewhere.
- **Batch 7 changed the method.** Five with-side pieces had code-drawn charts composited in, so it tested the v0.9.5 workflow, and the pasted-on look may have helped the judge spot that side.
- **Batch 8 met its bars by one win.** 20 of 30 and 59 of 100 are the smallest counts that pass; one pick the other way and neither would.
- **One judge.** No other person or outside model has judged yet.

## Gaps found, and what changed

v0.9.3 adds rules for the first five gaps below, with these notes as internal evidence (one judge):
- **Issuer marks on official pieces** (BRAND-4, EN-2 item 6): use the real mark from its file with the name at the top; if there is none, ask, or leave a labelled slot and flag it. Never invent a crest, and don't fall back to a characterless text header.
- **Subject against ground, text on colour** (CV-10, EN-2 items 1 and 3): the subject must separate from its ground in value at a distance; on a saturated colour, test black and white text and use the higher-contrast one.
- **Concept fit and unwanted readings** (EN-2 item 8, CD-3): the idea suits the product's category and senses, not just its name; look for readings nobody meant.
- **Fun events show the fun** (EN-2 item 7): show the activity and the people, not an empty place.

Open after batch 3, and covered in v0.9.4: a title competing with the main image on a cover (S35, now LAY-16); a defining trait not shown (S36, now CHAR-6 through gesture). Official notices that are clear but bland (S37, S38) are still only partly covered (EN-1's light pass, LAY-17).

v0.9.4 adds rules for the batch 4 and 5 gaps, with the owner's notes as internal evidence (one judge):
- **Read the brief exactly** (CD-1, ILL-6, the loop's intent model): count what it fixes ("it" is one plane, S49); background facts set the mood and need not be drawn (a school, S42) or printed (a "small family farm", S47); no invented product screens in finished work (UI-11, S39); think about what it costs to print (S44).
- **Genre and tradition** (EN-2 item 8, AES-11, LAY-16): a label, cover or menu looks like its kind first (jam, S47; classic versus pulpy young-adult, S40); covers give the title a zone and put the author name on the axis (S46).
- **Mood and gesture** (EN-2 item 7, TYPE-10, CHAR-6, ILL-17): a title as loud as the mood (S51); traits through pose, not props or text (S48, S53); picture books need life, not clinical polish (S46, S50).
- **Instructions in the text** (EN-2 item 5): a call to action the art implies also goes in the words (S41).
- **Plain where plain works** (EN-1, LAY-17): menus, signage and timetables get a light pass at most (S55).
- **One broken panel fails the piece** (LAY-18, S43), and **blocks that look misprinted** (COMP-24 item 7, S57).
- **No outline strokes or text glows** to rescue a value clash (CV-10, S42, S47); fix the values. **Small text at a distance** is checked too (S42).
- **No chocolate-box over-render** and an honest sterile check (EN-3, S50, S56, S58).
- **White means white** (CV-11, `autocheck.py` whites check): neutral white unless the brief asks for cream.

Still open after v0.9.4: notices and infographics that are clear but plain (S37, S38, S57), and the sterile edge on sparse pieces (S56, S58). Batch 6 tested v0.9.4 on infographics and confirmed the first.

v0.9.5 adds rules for the batch 6 gaps, as internal evidence (one judge), untested until batch 7 is judged:
- **Infographics get the full energy pass** (EN-1, new EN-4): a one-sentence art direction with personality and an emotional register that fits the issuer; visual richness that carries information; "clean" is not a slide template. The busy-versus-chaotic line is checkable: one illustration style, one reading path, one hero and at most two secondary focal points, no filler pictures (S61, S63, S65, S66, S68).
- **Panels show something specific and different** (LAY-18): the detail each step is about, never one picture repeated, with people and objects kept the same (S64, S59).
- **Charts, maps and routes are drawn from the data in code** (new LAY-19, `tools/datagraphic.py`): bars composited into the art, or the art generated around a reserved area; bars checked within 2% of the data; a loop closes at start = finish and a crossing shows a bridge (B53, B60, S60). Graded well supported for honest scales (Pandey et al. 2015, S336) and internal evidence for the generator failures.

v0.9.6 answers the batch 7 gaps, as internal evidence (one judge), untested until another infographic batch is judged. New [`modules/layout/infographics.md`](../../modules/layout/infographics.md):
- **Layout first; the chart designed in** (INF-1): plan the hierarchy, grid and reading path first; the chart is the hero, in the piece's own colours, line weight, corners and type. Build it in code with spot art, or generate the full design with the chart area styled in and replace only the data marks. No white box behind it, no labels cut by strokes (`datagraphic.py check-panel`; `route` moves labels off the line) (S71, S73, S74).
- **An illustration budget** (INF-2): one spot illustration or one icon set, no bigger than the information; simplified icons for secondary facts; no photoreal unless asked (S70, S76).
- **Distinct steps, visible flow** (INF-3): each step or period its own frame, colour or icon, with connectors (S75, S78).
- **Chart type fits the data** (INF-4): part of a whole as a pie or donut of six slices at most, drawn from the data (`datagraphic.py donut`, `check-donut`); comparisons as bars (S72; Cleveland and McGill 1984, Spence and Lewandowsky 1991).
- **A hero title with hierarchy logic** (INF-5, S75), and **every required line with safety and medical steps checked** (INF-6, a blocker; S70, S77).
- **Energy from structure** (EN-4 rewritten): infographics get a structure pass (layout, type, colour and a focal chart), not more pictures.
- **Warmth as a named choice** (CV-11): neutral white stays the default for notices, UI, data and clinical pieces; a warm paper is allowed where context, brand, era or mood calls for it, named in the plan; `autocheck.py --warm "reason"` passes it (S78).

Open after batch 8, not yet answered by a rule: screens that are correct but lack soul or atmosphere (S88, S100, S107); exact units, strings, case and counts that slip (B84, B95, B100, B79); ideas that are too literal (S92, S93); and props drawn wrong (B90, S108). Any v0.9.7 change would be internal evidence (one judge) until tested.

## Files

- `blind-test-key.json` and `blind-test-key-2.json` to `-8.json`: the eight keys, each published after its batch was judged. `sha256sum -c KEY-SHA256.txt` passes for all eight; it also warns about the explanation lines in that file, which is expected.
- [`scoring-owner.csv`](scoring-owner.csv): the owner's picks and strengths. The reasons are paraphrased in plain language, and "left" and "right" are replaced with "this one" and "the other". Batch 1's repeat sheets (S10-S16) were left blank, as allowed.
- [`whites.py`](whites.py): the white measurement above (needs the images, which are not in git).
- Re-run: `python3 examples/blind-test/score.py --key examples/blind-test/blind-test-key.json --key examples/blind-test/blind-test-key-2.json --key examples/blind-test/blind-test-key-3.json --key examples/blind-test/blind-test-key-4.json --key examples/blind-test/blind-test-key-5.json --key examples/blind-test/blind-test-key-6.json --key examples/blind-test/blind-test-key-7.json --key examples/blind-test/blind-test-key-8.json examples/blind-test/scoring-owner.csv`

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
| S39 | B39 | web hero | without | 1 | Very close; both good, balanced and official. This one wins on looks but invents app screens; the other follows the brief and would win if the brief means finished work. |
| S40 | B31 | novel cover | without | 1 | Reluctant: warmer and better balanced, but reads as pulpy young-adult fiction; the other is cold and distant but reads as a classic. |
| S41 | B37 | poster | with | 3 | Reads instantly at thumbnail size, with great flow, and shows the event; the instruction to wear something bright should also be in the text. |
| S42 | B40 | picture-book spread | with | 3 | Dynamic, tight and warm; the speech text is too small and lost on the soil. The other has an amateurish glow round its text and forces the school into the scene. |
| S43 | B36 | public infographic | without | 2 | The other is easier and clearer, but one catastrophically failed panel forces a fail. |
| S44 | B35 | official notice | with | 2 | Cute, readable, eye-catching. Aside: full-colour 3D may be costly for a council to print, and one box feels slightly unbalanced. |
| S45 | B33 | character | with | - | No reason given. |
| S46 | B32 | picture-book cover | with | 1 | Too clean and clinical for children; the author name would be better centred and in white. |
| S47 | B38 | jam label | without | 2 | Looks like traditional jam at once, though printing "small family farm" is silly; the other is too contemporary, with a stroke round its dark fruit. |
| S48 | B34 | character | with | 2 | Shows the trait through gesture and is more charming; the other is hyper-literal. |
| S49 | B50 | picture-book spread | with | 3 | Tighter, cleaner, a cohesive story; the other shows two planes where the brief's "it" means one. |
| S50 | B46 | picture-book cover | with | 2 | Clean, concise yet dynamic; the other is a glowing, over-detailed chocolate-box painting, too busy. |
| S51 | B49 | crime cover | with | 2 | The winner, though its title is too loud for a cold mood; the other is cramped and hyper-literal. |
| S52 | B43 | web hero | with | 3 | Better by miles. |
| S53 | B47 | character | with | 2 | Sells the concept in gesture alone; the other explains it in text. |
| S54 | B42 | tea box | with | 1 | Close. |
| S55 | B48 | menu board | without | 2 | Balanced, high contrast, easy to read at a distance: effective for its job. |
| S56 | B44 | library infographic | with | 2 | The other is very busy; this one perhaps a bit too sparse. |
| S57 | B45 | park notice | without | 1 | Forced: basic text with an ugly yellow call to action; the other's centre block and lopsided graphic look like a printer's misalignment. |
| S58 | B41 | poster | with | 1 | Academically tight but bland and sterile; the other is busy but fantastical and cosy. |
| S59 | B59 | comic-strip how-to | with | 2 | Cleaner to the eye: information economy, stable characters, clear warnings, fit for purpose. |
| S60 | B58 | route map infographic | with | 2 | Punchier type and an unbroken, cohesive trail; more fun. Neither is true to the loop and the bridge (start = finish should read as a loop, and a river crossing should show a bridge). The other has a nice centred, official park-leaflet look. |
| S61 | B55 | safety infographic | without | 2 | Better balance, an appropriate amount of information, more pleasing. The other suits short, practical water-safety notes but is not pleasing to the eye. |
| S62 | B56 | children's infographic | with | 1 | Both decent; this one fits the age range better. The title is not lost, but not as punchy as it could be. |
| S63 | B53 | data infographic | without | 2 | Dynamic and eye-catching. The other is accurate but sterile, like a PowerPoint slide. |
| S64 | B52 | public how-to infographic | without | 1 | Tough call. Its specific diagrams are more useful to a reader who came for the information. The other is easier to read but repeats the same image in every panel: repetitive and wasteful. |
| S65 | B54 | process infographic | without | 1 | On vibes: stylish, a nice layout, a good amount of visual busyness, though it overuses the bakery's name and the illustrations look sloppy. The other is too basic. |
| S66 | B60 | nutrition fact sheet | without | 1 | A judgement call, for its emotional direction: it reads like real nutrition information on a bar's packaging, personal. The other is matter-of-fact and sterile, though a fact sheet may want that. |
| S67 | B57 | public infographic | with | 1 | Both good; this one is cleaner, with punchier illustrations. |
| S68 | B51 | public how-to infographic | without | 2 | Clean and direct. The other's art direction is busy and visually chaotic. |
| S69 | B64 | process infographic | with | 3 | Clear, complex but accurate, eye-catching. The other has an industrial-magazine look with major errors in the explainer. |
| S70 | B66 | safety infographic | without | 2 | Designed better. The other is too demonstrative. |
| S71 | B62 | route map infographic | with | 2 | Not amazing: accurate but a basic presentation, place-name strokes cut into the route, unbalanced against the family. The other has wrong information. |
| S72 | B69 | data infographic | without | 2 | Compact and informational; the pie chart reads nicer here. |
| S73 | B63 | data infographic | with | 1 | This one, but its charts cut into the graphic and look cheap and pasted on. |
| S74 | B61 | data infographic | without | 1 | Forced pick; both rejected. This one renders it twice; the other is very unbalanced, its graphic doesn't belong. |
| S75 | B68 | children's infographic | without | 2 | The transitional flow reads better. The other is tight and careful, but its central hero title is mildly amateurish. |
| S76 | B70 | wildlife fact sheet | without | 2 | Better design, simplified icons for the sub-information. The other is way over-illustrated, with an unbalanced information presentation. |
| S77 | B65 | comic-strip how-to | without | 2 | More coherent, though slightly more clinical. |
| S78 | B67 | timeline infographic | without | 2 | Its framing differentiates the times better; the other reads samey. Also: the whites rule is good but could allow more warmth depending on context. |
| S79 | B84 | mobile app screen | without | 1 | Informational, with the km as asked; the other has more personality, perhaps too striking. |
| S80 | B73 | book cover | without | 1 | Both good; a slight preference for its central title. |
| S81 | B89 | character design | with | 2 | Self-evident without needing a character sheet. |
| S82 | B94 | picture-book spread | with | 2 | Tells the story better: words across the pages, composition on each page. The other is words, half a wheel and children running off. |
| S83 | B86 | character design | with | 2 | No reason given. |
| S84 | B93 | picture-book spread | with | 2 | Better eye pull and composition, with the text reading left to right. |
| S85 | B99 | logo | with | 2 | No reason given. |
| S86 | B82 | mobile app screen | with | 2 | No reason given. |
| S87 | B98 | logo | with | 2 | Good and simple, sells it well; the other is too busy, with mismatched type. |
| S88 | B83 | web hero | without | 2 | Has soul. |
| S89 | B78 | chocolate bar wrapper | with | 1 | The other's florals read as branding, as they should; this one's read as ingredients, but its overall theme appeals. A forced pick. |
| S90 | B72 | album cover | with | 2 | No reason given. |
| S91 | B77 | hot sauce label | without | 2 | Better balanced, pulls the eye, better flow; the other has good brand type. |
| S92 | B91 | picture-book spread | without | 2 | The other is too literal. |
| S93 | B100 | logo | without | 1 | Too abstract, but preferred visually; the other is far too literal, not creative. |
| S94 | B75 | album cover | with | 2 | No reason given. |
| S95 | B87 | creature design | with | 1 | Both equal; this one works better as a stand-alone character reference, the other brings in the environment. A forced pick. |
| S96 | B74 | children's book cover | with | 2 | No reason given. |
| S97 | B88 | mascot design | without | 2 | Better suited to the brief and its context. |
| S98 | B95 | picture-book spread | without | 1 | Neither has the right count; the other is tighter and fits children, but this one's composition wins. |
| S99 | B79 | honey jar label | with | 2 | No reason given. |
| S100 | B85 | web pricing section | without | 2 | The other is too bland and basic. |
| S101 | B71 | book cover | with | 2 | The other's author name gets a bit lost in the grass; it needs contrast. |
| S102 | B76 | coffee bag | with | 1 | Preferred, but the branding is basic. |
| S103 | B97 | logo | with | 2 | No reason given. |
| S104 | B80 | shampoo bottle label | with | 2 | No reason given. |
| S105 | B96 | logo | with | 2 | No reason given. |
| S106 | B92 | picture-book spread | with | 2 | No reason given. |
| S107 | B81 | web hero | with | 2 | The other has better atmosphere; this one shows the class filled. |
| S108 | B90 | creature design | without | 2 | The other is cute, but this one is better; the other's sock is broken too. |
