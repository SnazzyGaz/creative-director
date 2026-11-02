# What people measurably prefer (and what they don't)

Use this page when a critique wants to say "people prefer X". Cite it only for what the studies show. Where the evidence is weak, say so, and treat the rule as a craft default, not a fact about viewers.

**Evidence grades used across the repo** (introduced in v0.5.0 for `composition/`, `colour-value/` and the new rules elsewhere):
- **Well supported:** replicated experiments or a meta-analysis back the core claim.
- **Partly supported:** some experimental support, but narrow stimuli, small effects or mixed results.
- **Craft wisdom:** long agreement among teachers and practitioners, untested or untestable in the lab. A default, not a fact about viewers.
- **Contested / myth:** tested and not supported, or the popular version goes well beyond the evidence. Don't cite it as a reason.

## Findings strong enough to lean on

| Finding | What it means for a fix | Source |
|---|---|---|
| **First impressions are fast and stable.** Visual appeal is judged in about 50 ms. | The thumbnail and blur tests are not optional; they show what that first glance gets. | [S36] |
| **Visual complexity predicts first impressions.** On websites, high perceived complexity gets the lowest appeal ratings. | When in doubt, remove rather than add (CORE-8). | [S35] |
| **Fluency feels good.** Things that are easy to perceive are liked more: clear figure-ground contrast, symmetry, repetition, typical (prototypical) forms. | Clear grouping, strong figure-ground and consistency (CORE-2, CORE-4, CORE-9) are about pleasure as well as function. | [S37] |
| **Looks buy goodwill, not forgiveness.** Attractive interfaces are perceived as more usable and earn tolerance for minor problems only. | Never trade a working flow for looks (UX-1). | [S34] |
| **Colour preference follows associations.** Across many colours, people like those linked to things they like (clear blues, cyans) and dislike those linked to things they don't (dark yellows, browns). The model explains about 80% of the variance in average preference. | A muddy dark yellow-brown needs a reason. Context changes associations, so the brief wins. | [S40] |
| **Colour pairs: harmony comes from similar hue, preference from lightness contrast.** Pairs of very different hues are rarely rated harmonious. Lightness contrast between figure and ground raises preference. | Use analogous hues for unity. Get separation from value, not from clashing hues. | [S41] |
| **Curves are liked a little more than sharp angles.** Curved versions of neutral objects were liked more often than sharp-angled ones. | Sharp, pointed shapes read as tense. Use them on purpose (ILL-8), not by default. | [S42] |
| **Curvature preference is real but modest and not universal.** A meta-analysis of 61 studies found a medium effect (g = 0.39), moderated by presentation time, stimulus type, expertise and task. | Rounded forms are a gentle default for friendly pieces, not a rule (ILL-8). | [S225, S226] |
| **Faces and text pull the eye far beyond their size**, whatever the viewer's task; depicted gaze shifts attention automatically. | Weigh every face, figure and word in the balance and eye path (COMP-3, COMP-4). | [S239, S240, S243] |
| **Objects facing into the frame are preferred (inward bias).** | Give looking and moving things room in front (COMP-5). | [S218, S219] |
| **Balance is judged mostly from position and the whole picture**, and a centre-of-mass offset predicts balance ratings of simple pictures. Balance and liking are only loosely linked, and first-glance balance in complex work depends on grouping and recognition. | Use `tools/balance.py` as a prompt, then judge by eye (COMP-2). | [S235, S237, S238] |
| **Symmetry is the strongest predictor of "beautiful" for abstract patterns.** | Choose full symmetry or clear asymmetry; avoid near-symmetry (COMP-17). | [S234] |
| **Order and complexity are separate dimensions.** | Add order when adding elements (COMP-9, COMP-15). | [S231, S230] |
| **Typicality and novelty jointly raise appeal ("most advanced, yet acceptable").** Prototypes are easier to process and liked more; repeated exposure raises liking. | Be fresh in one or two dimensions, typical in the rest (AES-11). | [S232, S233, S257] |
| **Shared taste is high for faces (about 66%) and landscapes (29%), low for architecture (11-12%) and art (8%).** | Taste calls about style go to the owner of the work (AES-12). | [S251] |
| **Mid-complexity fractal patterns (D about 1.3-1.5) are liked on average, with clear individual differences.** | Offer detail at several scales (COMP-14). | [S228, S229] |
| **Gist comes from coarse structure first; lower contrast and blur read as distance.** | Big shapes before detail (COMP-13); lower contrast with depth (CV-8). | [S244, S247, S248] |
| **The F-shaped scan is a symptom of unformatted text, and formatting prevents it.** | Design for scanning; don't lay out to a template (LAY-14). | [S259] |
| **Red-green colour-vision deficiency affects about 8% of men of Northern European descent.** | Back colour distinctions with lightness or a second cue (CV-9). | [S252] |

## Myths and weak claims

Don't cite these as rules. If a bot's critique leans on one, correct it.

- **"The golden ratio is what people find beautiful."** Early support did not survive re-testing. A large later study found at most a weak population preference, with large differences between individuals [S38]. Other tests found no special pull of the golden rectangle, including no automatic preference for it in art pictures [S39]. A golden-ratio type scale is just one ratio among many (UI-1).
- **"Put the subject on a thirds line."** In one study, photos that follow the rule of thirds scored only slightly higher, and the link to aesthetic ratings was weak [S43]. For single-object images, a centred placement was preferred in about two thirds of judgements, at every object size [S44]. Unequal divisions still help in busy scenes (ILL-1). For a single subject, neither off-centre nor centred is the default: judge by intent (maintainer decision, 2026-11-01).
- **"People like medium complexity" (Berlyne's inverted U) as a universal law.** The evidence is mixed. Many visual studies find a straight-line or no relation. It fits some music data better [S45]. Use S35's narrower finding instead: lower *perceived* complexity helps first impressions of interfaces.
- **"Red makes people anxious/hungry; blue builds trust."** Colour-psychology effects are context-dependent and were mostly shown in small studies. A 2020 meta-analysis found little robust evidence that red impairs performance [S46]. Don't justify a palette with colour-emotion claims. Justify it with roles, contrast and the brief.
- **"Seven plus or minus two menu items."** Miller's paper is about holding items in memory, not choosing from options that stay visible on screen [S64]. See the UX module.
- **"Three clicks or users leave."** No published evidence supports this. Click count alone doesn't predict success [S66].

- **"Serifs read better in print, sans on screen."** Controlled tests find no reliable legibility difference between serif and sans at normal sizes [S111]. Size, measure and spacing matter more [S113, S114]. See `modules/typography/`.
- **"The ideal line is exactly 66 characters."** 45-90 is a comfort range; some studies find faster reading on longer lines while people prefer medium ones [S112].
- **"We read words by their outline shape."** The word-shape account is not supported; we recognise words from their letters [S118].
- **"Beautiful faces follow the golden ratio."** No good evidence (see the golden-ratio point above). Averageness and symmetry have modest, supported effects [S139]; perfect mirror symmetry can look artificial.
- **"The uncanny valley is one universal curve."** Evidence for a single curve is mixed. Mismatched realism cues, such as realistic skin with abnormal eyes, are the best-supported trigger [S136, S138]. See CHAR-5.
- **"72 dpi for screen, 300 for print" as a screen rule.** On screen only pixel dimensions matter; ppi matters only at print size (LAY-9).

**Added in v0.5.0 (composition, colour, layout):**
- **"Balance means symmetry or centring."** Balance is equilibrium of visual weights. Asymmetric and off-centre work balances by the lever (weight times distance), and fulcrum and centre-of-mass studies measure exactly that [S235, S237]. Balance only loosely predicts liking, and for art first-glance balance follows grouping and recognition more than a weight sum [S238]. Never centre or symmetrise by default (COMP-19).
- **The golden ratio, again, in depth.** Reviews of a century of tests find no robust preference for the golden rectangle [S220]; replications of Fechner's original method found none [S221]. Famous "golden" buildings and paintings rely on choosing what to measure [S222, S224]; the nautilus shell's spiral is not golden [S223]. Book canons called "golden" are built on simple ratios such as 2:3 [S211]. Hambidge's dynamic symmetry is a usable design system, but not proof of what the Greeks did [S194]. Use any ratio for consistency (COMP-16), never as a reason for beauty.
- **"Leading lines force the eye along a path."** Eye-tracking shows paths depend on content (people and faces first), task and viewer [S241, S242, S243]; lines help connect places but there is little evidence they steer on their own (COMP-4).
- **"Viewers read every layout in a Z, an F or the Gutenberg diagram."** The F is a symptom of poor formatting [S259]; the others are teaching sketches, not tested laws (LAY-14).
- **"Always use an odd number of objects" (rule of odds).** No direct test found. Pairs can split attention; triads can feel complete; but the count is not a rule.
- **"The right side of a picture is heavier" or "the eye always enters at the top left".** Lateral effects exist but are small and depend on reading direction and task [S254, S255, S261]. Contested.
- **Colour-wheel harmony schemes guarantee harmony.** Rated harmony follows shared hue, shared chroma and lightness difference more than wheel geometry [S41, S245]. Craft starting points only (CV-5).
- **Fixed colour-area ratios ("Goethe's" numbers, via Itten).** Tradition; not tested, and not found in the 1840 English Goethe [S192, S48] (CV-6).
- **"Complementary colours are the most harmonious pair."** Pairs of very different hue are rarely rated harmonious [S41].
- **Birkhoff's aesthetic measure (M = order / complexity, 1933).** Historical; its predictions did not hold up in later tests, although order and complexity remain useful separate dimensions [S231].
- **Fractal analysis can authenticate paintings.** The original Pollock analysis [S227] was challenged on method; treat it as disputed.
- **"Margins should follow the golden ratio" / "the optical centre is exactly X% above centre".** Margin canons are traditional and built on simple ratios [S211]; the optical centre is craft wisdom with a small perceptual basis [S264], and printers placed it anywhere from slightly above centre to a third down [S205].

## How to use this in a critique

- Write "evidence: [S41]" only when the study matches the case (similar task, similar viewers). Otherwise cite the craft rule and its source.
- If a fix rests only on a myth above, drop it.
- Taste questions with no rule and no evidence go to the owner of the work.
