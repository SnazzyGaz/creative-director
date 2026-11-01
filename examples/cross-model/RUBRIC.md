# Scoring rubric

Score each run against the answer key for its task. A fault counts as **found** when the output names the problem clearly enough that a person could act on it, even without the rule ID. Baseline runs are scored the same way; they aren't expected to cite IDs.

## Answer keys

### Task A: web UI (5 faults, 3 blockers)
| # | Fault | Rule | Blocker |
|---|---|---|---|
| A1 | Pre-order can't be completed: the "Submit"/"Go" controls go nowhere; the pre-order box is clipped off-screen on a phone | UX-1 | yes |
| A2 | Text contrast fails everywhere (all 11 measured pairs below WCAG AA; worst 1.13:1) | UI-6 | yes |
| A3 | Fixed-width, absolutely positioned layout overflows at 390 px and at 200% text | UI-10, CORE-10 | yes |
| A4 | Too many typefaces (six) | UI-1, CORE-7 | no |
| A5 | No reading order or hierarchy; button colours with no roles; nine nav items; filler copy | CORE-1, UI-4, CORE-6, UX-6 | no |

**Task A fix check** (on the model's new HTML, screenshot at 390 px and 1280 px): pre-order is a real link or button, visible at 390 px; every text pair passes 4.5:1 (3:1 for large text; `tools/contrast.py`); no horizontal scroll at 390 px or at 200% text (`tools/shot.sh`); all must-keeps present. Count passes out of 4.

### Task B: illustration (5 faults, 1 blocker)
| # | Fault | Rule | Blocker |
|---|---|---|---|
| B1 | Several light sources that disagree (lamp, burst behind the tower, lightning both sides, sparkles) | TD-LIT-1 | yes |
| B2 | The cat is not the point of highest contrast; the lamp and sky are | ILL-2, CORE-3 | no |
| B3 | Generic AI look: rainbow sky, sparkles, god rays, glow, all equally sharp, centred symmetric subject | ILL-11, CORE-8, ILL-5, ILL-1 | no |
| B4 | No readable moment: the cat faces away; no boat reads as the keeper's | ILL-6 | no |
| B5 | Full spectrum of saturated colour with no roles | ILL-4, CORE-6 | no |

### Task C: technical drawing (5 faults, all blockers)
| # | Fault | Rule | Blocker |
|---|---|---|---|
| C1 | Left and right vanishing points at different heights (no single horizon) | TD-PER-1 | yes |
| C2 | Verticals lean, in different directions | TD-PER-3 | yes |
| C3 | Ellipses tilted: minor axes ~19 deg off the tin's axis | TD-ELL-1 | yes |
| C4 | Base ellipse flatter than the top; it should be fuller (further from eye level) | TD-ELL-2 | yes |
| C5 | Top ellipse has pointed ends (a "lemon") | TD-ELL-3 | yes |

## Scores per run

| Measure | How |
|---|---|
| **Found** | faults found / 5 |
| **Blockers found** | blockers found / blockers in the key |
| **Ranked** | 1 if the blockers are listed before the improvements, else 0 |
| **False alarms** | claims that are wrong when checked (e.g. "the verticals are fine", a contrast pass that measures as a fail, a fault that isn't there). Taste opinions stated as opinions are not false alarms. |
| **Fix quality** | per found fault: 2 = fix would solve it, 1 = right direction but vague, 0 = wrong or none. Report the total / 10 |
| **Brief kept** | must-keeps the output keeps or protects (CD-5) / total; for B and C, 1 if no fix would drop a must-keep |
| **Rule IDs correct** | with-skill runs only: IDs that match the fault / IDs cited |
| **Task A fix check** | passes / 4 (above) |

Extra faults beyond the key are fine; list them in the notes, and say whether they're real.
