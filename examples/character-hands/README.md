# Character check: hands and face on a generated portrait

A zoom audit (`modules/character/`) on one image from an AI image generator, generated for this example on 1 November 2026. The prompt asked for a waist-up barista holding a cup in one hand and waving with the other, the kind of pose that used to break hands. Image: [generated.jpg](generated.jpg); 2x crops: [wave hand](zoom-wave-hand.jpg), [cup hand](zoom-cup-hand.jpg), [face](zoom-face.jpg). Measurements are in pixels on the 768-wide view, by eye on the crops.

## Zoom audit

| Check | Result | Rule |
|---|---|---|
| Waving hand: digits | 5. Thumb on the midline side, correct for a left hand shown palm-out. Middle finger longest; little finger ends near the ring finger's last joint. | CHAR-3 pass |
| Cup hand: digits | 4 visible, thumb implied behind the cup. Fingers bend only at joints and rest on the cup's surface; none pass through it. | CHAR-3 pass |
| Hand size | Waving hand, wrist crease to middle fingertip, about 250 px; face, chin to hairline, about 220 px: about 1.15×. Slightly large; plausible if the hand is nearer the camera. | CHAR-3 note |
| Eyes | Same size and shape; gaze converges on the camera; the right eye (image right) is a little more closed, consistent with the smile. Eye line about halfway between skull top and chin; gap between the eyes about one eye width. | CHAR-4 pass |
| Limbs | 2 arms traced shoulder to hand; the raised left forearm meets an elbow at the right edge; no fused or extra parts. Apron straps continuous on both sides. | CHAR-7 pass |
| Realism level | Skin, eyes, hair and hands all photographic; no mismatch. | CHAR-5 pass |
| Weight and landmarks | Not judged: waist-up crop, no feet or full height. | CHAR-2, CHAR-6 n/a |

## Verdict

No blockers. One note (the waving hand reads a little large); a fix would be to scale that hand about 10% smaller or accept it as perspective, which is the owner's call. Nothing to rework.

The honest finding: this generator passed a pose that the module's checklist was written for. The audit still earned its place: it took about a minute, and it is the only way to say "the hands are fine" with evidence rather than a glance.
