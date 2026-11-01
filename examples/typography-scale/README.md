# Type check: the plan card

The [common-failures type-scale case](../common-failures/README.md) re-judged against `modules/typography/`, with the numbers read from the HTML. Images: [before and after](../common-failures/type-scale-before-after.png).

| Check | Before | After | Rule |
|---|---|---|---|
| Families | 5 (Lobster, Oswald, Courier Prime, Source Sans 3, Georgia) | 2 (Fraunces display, Source Sans 3 text) | TYPE-1 |
| Sizes, px | 31, 29, 17, 15, 13.5 | 36, 24, 17, 14 | TYPE-2 |
| Neighbouring ratios | 1.07, 1.71, 1.13, 1.11 | 1.50, 1.41, 1.21 | TYPE-2 (≥ 1.1) |
| Body size | 15 px (main line, monospace) | 17 px | TYPE-3 (default 16) |
| Smallest text | 13.5 px bold | 14 px, muted colour | TYPE-3 (floor 12) |
| Signals per level | size, family, weight and style all change at once | size and weight; colour only for the fine print | TYPE-7 |

Findings on the before version, ranked: TYPE-1 (five families, three with strong voices that contradict each other); TYPE-2 (31 and 29 px headings only 7% apart, so neither leads); TYPE-7 (every line uses a different signal, so nothing groups). No blocker: all text is above the 12 px floor.

The after version meets all three. Remaining taste call for the owner: Fraunces gives the heading an editorial voice; a plain bold of the text face would also pass the rules.
