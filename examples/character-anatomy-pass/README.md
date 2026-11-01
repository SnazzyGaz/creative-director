# Anatomy pass: a hand that belonged to no one

A book cover ("My Tuna Lover", a comic story about a sailor obsessed with a tuna) made with Grok Bot's built-in GenerateImage, with the title and author set in code. The first delivered version passed the checks that were run on it (one key light, clean edges, type hierarchy and contrast) and still had a broken hand. The owner of the work spotted it at once. This example is why CHAR-9 exists: the fault was small in the frame and a whole-image look passed it.

All art here is AI-generated (1 November 2026). The pass/fail calls are Grok Bot's own, made by eye on the crops; no outside judge.

## Round 1: what was delivered ([art-r01.jpg](art-r01.jpg), crops in [before-sheet.jpg](before-sheet.jpg))

| # | Check | Result |
|---|---|---|
| A1 | Hand count | One arm with no hand, one hand with no arm. **FAIL** |
| A3 | Trace | The yellow sleeve crossing the fish comes from the figure's **left** shoulder (image right, since he faces us) and ends in a cuff with no hand. A separate hand grips the fish's belly below it, with no wrist or sleeve leading to it. **FAIL** |
| A2 | Finger count | Orphan hand: 4 fingers and a thumb. The figure's right cuff (image left) ends in a brown, fingerless, sausage-like shape. **FAIL** |
| A5 | Grip | Orphan hand's fingers wrap the belly with the thumb opposing, but no arm is attached to it. Not judged further. |
| A8, A9 | Face, fish | Eyes closed alike; fish has one eye, highlight on the sun side. PASS |

Three blockers in the figure. Fix: edit the arm region only, with the anatomy spelled out.

## Round 2 ([art-r02.jpg](art-r02.jpg))

Edit prompt: the left arm's hand comes straight out of the yellow cuff, wrist visible, four fingers curled round the fish, thumb opposing; remove the orphan hand and paint fish belly and coat there. Re-running the **whole** pass found that A3 and A1 now passed for that arm, but the right cuff's fingerless shape (A2) was still there. The fault had been in round 1 too; a region-only re-check would have missed it.

## Round 3 ([art-r03.jpg](art-r03.jpg), final cover [cover-v3.jpg](cover-v3.jpg), crops in [after-sheet.jpg](after-sheet.jpg))

Edit prompt: replace the brown shape with the right hand coming out of its cuff, fingers hooked over the fish's back edge, the rest hidden behind the fish. The fixed region was blended into the round 1 art with a soft mask, so everything outside the arms stays as it was, and the cover's type was re-composited unchanged.

| # | Check | Result |
|---|---|---|
| A1 | Hand count | Two, one per arm. PASS |
| A2 | Finger count | Figure's left hand: thumb plus 4 fingers. Right hand: 4 curled fingers, thumb hidden behind the fish (plausible occlusion). PASS |
| A3 | Trace | Left hand: wrist, dark inner cuff, yellow sleeve, to the left shoulder at image right. Right hand: out of the right cuff at image left. PASS |
| A4 | Thumb side | Left hand seen from the back, palm on the fish, fingers pointing to image left: thumb on top. Correct. PASS |
| A5 | Grip | Both are power grips: fingers curl round the fish's edge; the left thumb presses from the other side. PASS |
| A6 | Joints | Fingers bend towards the palm at the knuckles only. PASS |
| A7 | Merges and extras | None; the orphan hand is gone and its area reads as fish and coat. PASS |
| A8 | Face | Unchanged; lids closed alike, smile even. PASS |
| A9 | Fish | One eye, round pupil, highlight on the sun side; pectoral, first dorsal and anal fins each join the body, finlets along both edges. Note: the pectoral is long for a bluefin; the brief doesn't name the species, so left as is. PASS |
| A10, A11 | Cuffs; ground | Both cuffs dark-lined yellow oilskin; no feet in frame. PASS / n/a |

Two edits; the second came back clean. Crops were made with `tools/anatomy_crops.py`.
