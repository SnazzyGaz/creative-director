# Prompts (GenerateImage, Grok Bot's built-in image tool)

**Before (one call, the kind of prompt a bot writes from the brief):**
> A cute children's picture book illustration of a little girl about seven years old in a yellow raincoat walking her small scruffy brown dog along a stone harbour wall in the evening, boats in the harbour, vibrant colours, highly detailed, beautiful sunset, magical atmosphere, wide two-page spread. (16:9)

**After, round 1 (regenerate, before art as reference for the two characters):** gouache picture-book spread; same girl and dog, new composition, palette and light; the wall curves from bottom left to five low cottages on the far right; girl and dog on the right half at about 70% of the width, walking right towards the cottages; nothing important in the middle 12% (the fold); upper-left sky plain for text; two or three small moored boats on the left page; one light only, the afterglow behind low hills on the right, warm edge on right-facing edges, near sides in cool shade; no lamps, glowing objects, sun disc, sparkles or god rays; muted blue-grey palette with the raincoat as the one strong colour; no lighthouse, birds, flowers, lamps, spires, drawn fold line or text. *Result: they walked left, away from home. Rejected.*

**Round 2 (edit of round 1):** turn girl and dog to walk right towards the cottages, lost profile, mid-stride; both arms complete; remove the sun disc; same light and palette. *Result: direction right; the lead split into a line in one hand and a closed loop in the other (anatomy pass A7 fail).*

**Round 3 (edit of round 2):** make the lead one continuous strap from one hand to the collar; the other hand empty and relaxed. *Result: anatomy pass clean; dog straddled the fold.*

**Round 4 (edit of round 3, delivered):** move the dog right, close to the girl, wholly in the right half; lead one continuous slack line; everything else unchanged. *Result: dog trots just ahead of her, lead from her far hand; fold clear.*

All text is set in code (`compose_before.py`, `compose_after.py`); no lettering was generated.
