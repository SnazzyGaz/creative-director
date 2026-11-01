# Anatomy sweep and hero lighting fixes (1 November 2026)

After CHAR-9 and CHAR-10 (the anatomy pass) became a delivery gate in v0.4.1, every image in `examples/` and the README hero was swept with it, and two lighting faults in the hero (TD-LIT-1, one key light) that had been left captioned were fixed.

How: every image was looked at whole; every person, hand, limb join, face and animal head was cropped at 2x-4x with [`tools/anatomy_crops.py`](../../tools/anatomy_crops.py) and checked against A1-A11 (hand count, finger count, trace to the shoulder, thumb side, grip, joints, merges and extras, face, animal counts, clothing, ground). All calls are Grok Bot's own, made by eye on the crops; no outside judge. Images with no person or animal are listed as n/a.

## The two fixes

| Image | Fault | Fix | Re-check |
|---|---|---|---|
| Middle fox cover, with the skill ([before r2](../baseline-comparison/fox-with-r2.jpg), [after r3](../baseline-comparison/fox-with.jpg)) | The open book glowed and lit the fox's face from below while the low sun lit it from the left: two key lights. The art prompt itself asked for a glowing book | One GenerateImage edit of the art ([prompt](../baseline-comparison/src/PROMPTS.md)): plain paper, sun as the only key light, everything else kept; type re-set unchanged | Light: no glow or halo; the pages catch sun on their left edge only. Contrast: title 9.71:1, author 7.48:1 (mean ground). Anatomy: pass. [Before and after](fox-with-book-before-after.jpg) · [crops](fox-with-r3-anatomy-sheet.jpg) |
| Aesthetic poster ([before r2](../aesthetic-benchmark/poster-aes-r2.jpg), [after r3](../aesthetic-benchmark/poster-aes.jpg)) | The bass stood outside the lamp's cone yet was brightly lit, and had a violin's outline | Two more edits (three in all since the first review; [prompts](../aesthetic-benchmark/src/PROMPTS.md)). The first of today's two kept the violin shape and flat light (rejected); the second moved the bass beside the lamp, lit its lamp side and redrew it with sloped shoulders | Light: lamp side cream and amber, far side navy (mean grey 131 vs 40), shadow falls away from the lamp. Contrast: all pass (title 14.57:1). Shape: double bass. Minor: far edge just past the drawn cone (in shadow), hard light/shadow line, a stray line by the bridge. [Before and after](poster-aes-bass-before-after.jpg) · [crops](poster-aes-r3-bass-sheet.jpg) |

The README hero ([light](../../docs/assets/baseline-light.jpg), [dark](../../docs/assets/baseline-dark.jpg)) was rebuilt from the fixed images with `python3 docs/assets/src/build.py baseline`.

## Sweep: delivered, with-skill and aesthetic-layer images

| Image | What's in it | Result |
|---|---|---|
| Hero (`docs/assets/baseline-*.jpg`) | The six images below | PASS (after the two fixes) |
| `baseline-comparison/fox-with.jpg` (r3) | Fox: head, both forepaws on the book, hind leg, tail | PASS. A8/A9: two eyes, two ears, one nose. A2: mitten paws, no separate digits drawn, same on both. A3: each forepaw traces to its shoulder. A7: none. A11: sits on the grass with a contact shadow |
| `baseline-comparison/poster-with.jpg` | Flat navy bass, small lamp | n/a (no character). Light: flat silhouette with a glow behind the lamp, no modelled form to contradict it |
| `aesthetic-benchmark/fox-aes.jpg` | Fox, as above, golden hour | PASS (head, paws on book, hind leg, tail) |
| `aesthetic-benchmark/poster-aes.jpg` (r3) | Bass, lamp, houses | n/a for anatomy; lighting fixed, see above |
| Reference set 01, moth poster (rules; rules + aesthetic) | Moth on a flower | PASS: four wings, two feathered antennae, one body; legs hidden by the wings in both. The second, tiny moth in the aesthetic version is too small to judge even at 4x |
| Reference set 03, lighthouse (rules) | No figure | n/a |
| Reference set 03, lighthouse (rules + aesthetic) | Keeper seen from behind, with a staff | PASS: one head, two legs and feet on the path; the left hand closes on the staff; the right arm hangs at his side inside the coat, hand hidden (plausible occlusion, not a merge) |
| Reference set 04, badger mascot (rules; rules + aesthetic) | Cartoon badger holding a book; walking version with satchel | PASS. A2: three digits show on each hand round the book edge and four toes on each foot, the same on both sides of each pair (a cartoon convention, consistent). A3: both arms trace to their shoulders. The walking version's lifted front foot shows its sole and pads, which fits the step; the satchel strap runs continuously from shoulder to bag. [Crops](bramble-aes-anatomy-sheet.jpg) |
| Reference set 11, night-shift spread (rules; rules + aesthetic) | Photo-real fox on a wet street | PASS: four legs (two fore, two hind) each ending in a paw on the ground, two eyes, two ears, one tail |
| Reference set 02, 05, 06, 07, 08, 09, 10, 12 | Posters, UI, renders, drawing, logo, landscape | n/a (no person or animal) |
| `character-anatomy-pass/cover-v3.jpg` | Sailor hugging a tuna | PASS (that example's own full pass, re-viewed: two hands each traced to a sleeve, five digits on the visible hand, fish one eye, fins joined) |
| `character-hands/generated.jpg` | Barista waving, holding a cup | PASS (that example's audit, re-viewed on its crops: five digits on the waving hand, four plus hidden thumb on the cup hand, eyes match) |
| `illustration-knight/round-02.png` (delivered) | Knight from behind, sword | PASS: two legs and sabatons on the ground; the right gauntlet closes round the grip above the crossguard; the left arm is under the cape (occluded) |
| `illustration-takeover/round-02.png` (delivered) and `round-03.png` | Cat in a lit window | PASS: silhouette with two ears, front legs to the sill, tail |
| Everything else (UI screenshots, technical drawings, 3D renders, common-failures, social cards, banners, look sheets, before/after strips) | No person or animal | n/a |

No delivered, with-skill or aesthetic-layer image failed the anatomy pass, so none was regenerated for anatomy.

## Without, before and input images (noted, not fixed)

These are meant to show faults, so they are left as generated.

| Image | Anatomy note |
|---|---|
| `baseline-comparison/fox-without.jpg` | Fox paws on the book and face pass; its faults are invented text and clutter |
| `baseline-comparison/poster-without.jpg` | No character |
| `baseline-comparison/fox-with-r1.jpg`, `fox-with-r2.jpg` | Earlier rounds: anatomy passes, but the glowing book breaks TD-LIT-1 (fixed in r3) |
| `aesthetic-benchmark/fox-aes-r1.jpg` | Withdrawn round: added robin and fireflies (AES-10) and the glowing book (TD-LIT-1) |
| `aesthetic-benchmark/poster-aes-r1.jpg`, `poster-aes-r2.jpg` | Earlier rounds: the bass lit from nowhere (TD-LIT-1, fixed in r3) |
| Reference set 11, no skill | Fox: four legs, head and tail pass |
| `illustration-knight/round-01.png` | Before: same knight pose; gauntlet and legs pass at 2x |
| `illustration-takeover/round-01.png`, `cross-model/inputs/illustration-keepers-cat.jpg` | Before/input: cat from behind, looked at full size only; its faults are light from several directions |
| `character-anatomy-pass/art-r01.jpg`, `art-r02.jpg` | That example's failing rounds (orphan hand, fingerless cuff), kept as evidence |
