# Consult: parcel box with tin (technical-drawing check)

**Verdict:** The idea reads and both must-keeps hold. Five construction blockers fail, though, and they share one cause: the verticals and ellipses were drawn by eye rather than to a single horizon. With 3+ blockers the guide says to rework rather than patch. Redraw the construction layer (TD-CON-1), then re-ink. This is a consult, so nothing below has been applied.

## Brief
- Purpose: product sketch of a parcel box with a round tin on its lid [brief]
- View: two-point perspective, eye level above the box [brief]
- Must-keeps: the box corner faces the viewer, the tin is centred on the lid, line only [brief]
- Polish: a clean construction sketch, with no shading or light to judge, so TD-LIT-1..3 do not apply [inferred]
- "Done" means every TD-PER and TD-ELL check passes with the must-keeps unchanged [inferred]

## Look
- **Blur:** the box mass leads and the tin comes second. This is the right order.
- **Thumbnail:** it reads as "box with a can on top". The flared box sides make it read more like a tray or plinth than a parcel.
- **Flip:** mirrored, the tin's lean to the right and the pointed top stand out more.
- **Greyscale:** not relevant here (it is line only and has one line weight).
- **Edges:** there are no accidental tangents. The back lid edges stop cleanly at the tin's sides.

## What already works (keep)
- **Corner toward the viewer:** the near corner faces the viewer, and the top face angle is 143.5°. With the vanishing points (VPs) 1,880 px apart on a 1,200 px frame, TD-PER-5 passes.
- **Seen from above:** both VPs sit above the box (y = 56 and y = 255, with the lid at y ≈ 320–470), so we do look down onto the lid.
- **Edges agree with their VPs:** each set of receding edges, including both back lid edges, meets its own VP within 1.6 px. Only the two VPs disagree with each other (see point 2).
- **Tin centred on lid (TD-PER-4):** the perspective diagonals put the lid centre at (564, 372). The tin's base centre is about (572, 365), which is off by about 10 px, or 5% of the tin's width. That is centred. Keep this point as the tin's anchor.

## Critique (ranked, all measured, all blockers)

1. **TD-PER-3: the verticals are not vertical, and the tin leans the other way from the box.** The box edges measure −7.6° (left), −3.6° (front corner) and +2.4° (right). The box sides spread apart toward the bottom and roughly converge to a point above the picture, near (750, −2900). That is a worm's-eye three-point view, the opposite of "seen from above". The tin sides lean +3.0° and +3.4° the other way. **Fix:** make every vertical plumb (0°): the three box corners and both tin sides. [edit: redraw verticals]
   *Question:* is a tapered box intended? The taper is too consistent to be accidental. If it is not intended, it fails the two-point brief.

2. **TD-PER-1: two eye levels.** The left VP is at (−363, 56) and the right VP at (1515, 255). They are 199 px apart in height, which tilts the horizon by 6.1° (the tool's limit is 1.5°). **Fix:** draw one horizontal horizon first, for example around y ≈ 150 or anywhere above the lid, with both VPs on it about as far apart as now. Then redraw the receding edges to them. [edit: redraw box edges]

3. **TD-ELL-3: the tin top is a lemon.** The two arcs meet in points where the tin sides join them, at (470, 205) and (657, 242). The ellipse.py end check measures 0.83 and 0.82 against a true ellipse (below 0.93 counts as pointed). **Fix:** draw the top as a full, smooth ellipse. Draw the side lines tangent to its ends, not into corners. [edit]

4. **TD-ELL-1: the tin ellipses are rotated.** The top ellipse's major axis tilts 12°. Its minor axis is 15.6° off the tin's centre line, which itself leans 3.6°. The base arc tilts about 8°, and its lowest point sits about 50 px right of the tin's axis. For an upright tin in two-point perspective, the axis is vertical, both major axes are horizontal and the minor axes lie on the axis. **Fix:** draw a vertical centre line through the lid centre (564, 372). Draw both ellipses square to it, with the base ellipse centred on that point. [edit]

5. **TD-ELL-2: the base is flatter than the top, which is backwards.** Seen from above, the base is further below eye level than the top, so it must be the fuller ellipse. Measured by hand from pixel samples, the front of the base dips about 20 px below its chord. The top dips about 33 px at about the same width, giving a degree of roughly 0.25 for the base and 0.37 for the top. (ellipse.py's fit of the half-visible base ran past the tin and is not reliable, so treat these figures as approximate.) **Fix:** open the base ellipse so it is a little fuller than the top, then re-measure both ellipses with ellipse.py. [edit]

## Suggested order (max 3 fixes per round)
Round 1:
- Set the horizon and VPs (2).
- Plumb all the verticals (1).
- Set the tin axis and the anchor at the lid centre (4).

Round 2:
- Redraw both ellipses smooth (3), with the base fuller than the top (5).

Then re-run both tools.

## How this was measured
- I used the attached `vp.py` and `ellipse.py` on the full-size PNG. The line segments came from `vp.py detect` and I sorted them into families by eye:
  - Left family: the bottom-left edge, the top-left front edge and the back-right lid edge.
  - Right family: the bottom-right edge, the top-right front edge and the back-left lid edge.
  - Verticals: the three box corners and the two tin sides.
- For the tin top, ellipse.py fitted a degree of 0.433 (161 × 70 px) with a mean residual of 0.018. Its fit cuts off the pointed ends. The span as drawn (about 187 × 69 px) gives about 0.37.
- The near-corner angle, the hidden back corner and the lid centre were worked out from the fitted VPs and the perspective diagonals.
