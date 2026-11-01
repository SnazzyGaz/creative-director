# Layout check: the X launch card

The repo's own launch card ([card-1600x900.png](../../docs/assets/social/card-1600x900.png)), judged against `modules/layout/` and `modules/typography/` after it shipped. Measured with Python on the exported PNG; no changes made, so this is a critique only. Small versions: [feed-400.png](feed-400.png) (phone feed width) and [thumb-200.png](thumb-200.png).

Brief: an X post image announcing the repo; seen in a phone feed; one idea: "design judgement for AI agents".

## Meets the criteria

| Rule | Measurement |
|---|---|
| LAY-4 size and ratio | 1600 × 900, 16:9: X's single-image ratio, shown uncropped [S124, S130]. |
| LAY-3 one focal point | Blur and thumbnail: title first, sketch second, footer last. Three text levels. |
| LAY-6 main message | Title x-height about 78 px, so about 19 px at 400 px wide. Subtitle x-height about 30 px, so 7.5 px at 400 wide (floor about 6). Both read at feed size. |
| UI-6 contrast | Ink #EEE9DF 15.1:1, muted #A39C91 6.7:1, accent #D9825F 6.4:1 on #161514. All pass 4.5:1. |
| LAY-1 grid | Title, subtitle and footer share the left edge (x = 112); the sketch's labels end at x ≈ 1486, mirroring it on the right (114 px). |
| TYPE-1, TYPE-2 | One display family (Fraunces) plus a functional mono; title to subtitle ratio about 2.6, well separated. |

## Findings

1. **LAY-6 / TYPE-3, the proof point is unreadable at feed size.** The orange `TD-ELL-1` caption, the card's one proof point, has an x-height of about 8-10 px at full size, so about 2-2.5 px at 400 px wide. It reads only when the image is opened. *Fix:* double the caption size, or drop the second caption line and keep the rule ID. Default, not blocker: the main message still reads.
2. **LAY-2, uneven margins.** Left and right margins are 112 px (12.4% of the short side) but the footer sits 61 px (6.8%) from the bottom. *Fix:* raise the footer to 112 px from the bottom; the gap to the subtitle stays over 150 px. Owner's call whether the tighter footer is deliberate.
3. **LAY-5, reuse crops.** As a GitHub social preview (2:1, centre crop) the footer would sit 13 px from the bottom edge; as a 1:1 crop the title is cut. *Fix:* use separate exports (the repo already has a 1200 × 675; a 1280 × 640 is still needed for GitHub) rather than reusing this file.
4. **Footer at feed size.** The URL's x-height is about 3 px at 400 wide. Acceptable because the URL is in the post text too; mention only.

Verdict: passes all blockers; three default findings, one (the proof point caption) worth fixing in the next version. Taste questions for the owner: whether the sketch should carry more weight than the title in the thumbnail.
