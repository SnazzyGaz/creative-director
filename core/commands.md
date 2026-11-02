# One-word commands: bolder, quieter, distill

**Purpose:** what to do when the owner of the work says just "bolder", "quieter" or "distill" (or "louder", "calmer", "simplify", "strip it back"). Each is one round of the critique loop with a fixed direction: keep the brief, the idea and the must-keeps (CD-5), change only what the word asks for, then run the auto check and the five tests again. Every rule here is a Procedure (`evidence.md`): it sets how to act on the word, not a finding about what people prefer.

Format: **What / Check**. The checks are written so a second reader can confirm them on the before and after renders side by side (`tools/beforeafter.py`).

### CMD-1. Bolder: more contrast, more scale difference, more commitment
- **What:** Widen the gap between the main thing and the rest (CORE-1, CORE-3): a bigger step in size between the hero and the next level, a deeper value range at the focus (CV-1), one accent pushed further while the rest stays put (CV-6), and any hedged placement pushed to read as chosen (COMP-20). With a lookbook look applied, raise its strength one notch on the dial (hint -> leaning -> strong; full only on request; `modules/lookbook/README.md`). Turn the rest down rather than adding new loud elements (CORE-8).
- **Check:**
  1. The size ratio between the largest and the next type or shape level is larger than before (TYPE-2).
  2. The focus holds the highest contrast, and the gap to the next-highest is larger than before (CORE-3; squint test).
  3. Still at most about three levels of emphasis, and no new element was added only to be loud (CORE-3, CORE-8).
  4. The auto check has no new FAIL: contrast, text size and safe margin still hold (UI-6, TYPE-3, LAY-5).
  5. **Sitting right is kept:** an off-centre layout stays off-centre or commits further (COMP-19, COMP-20). Bolder never means centring, symmetrising or filling the empty space (COMP-23).

### CMD-2. Quieter: less noise, less saturation, less ornament
- **What:** Lower everything that competes with the main thing (CORE-3): fewer saturated colours and a smaller area for the strongest one (CORE-6, CV-6), less ornament, texture and decoration that has no job (CORE-8), fewer type sizes and weights (TYPE-1, TYPE-2), and a smaller value range away from the focus (CV-1). With a lookbook look applied, lower its strength one notch (strong -> leaning -> hint; at hint, drop the look). Keep the hierarchy: quieter is not flatter.
- **Check:**
  1. Fewer saturated colours, or the same colours over a smaller area, than before (CV-6).
  2. Fewer ornaments, textures or decorative elements, and none of the remaining ones lacks a job (CORE-8).
  3. Type sizes counted by the auto check are the same or fewer (TYPE-2).
  4. The main thing still leads in the blur and thumbnail tests (CORE-1, LAY-6), and the auto check has no new FAIL (contrast must not fall below UI-6).
  5. **Sitting right is kept:** the composition and its asymmetry stay as they were (COMP-19); space freed by removal is kept as space with a job (COMP-23), not re-filled or re-centred.

### CMD-3. Distill: remove until the one job still works, and no further
- **What:** Name the piece's one job in a sentence from the brief (CD-1), for example "say what, where and when from across the street". Then remove elements one at a time, in order of least use to that job, and stop at the last removal that still leaves the job working (CORE-8: "hide it: is the piece worse?"). Merge before deleting where two elements do the same work. Never remove a must-keep, an official mark or required text (CD-5, BRAND-4).
- **Check:**
  1. The one-job sentence is written down, and every remaining element can be tied to it.
  2. Each removal is listed with the test result after it; the last listed removal still passes the job, and the next candidate would break it.
  3. The job still passes at its real size (thumbnail or feed size, CORE-10, LAY-6) and the auto check has no new FAIL.
  4. **Sitting right is kept:** removing elements can shift the visual weight; re-run `tools/balance.py` and the Sitting right pass and fix with a counterweight or a firmer asymmetry, never by centring what is left (COMP-19, COMP-20).

**Reporting:** one line per command: what changed, the rule IDs, the auto check numbers before and after (for example "type sizes 7 -> 4, worst contrast 5.1 -> 6.3:1"), and the lookbook strength if one is applied (`LB-014 Suprematism: hint -> leaning`).
