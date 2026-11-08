# Creative direction: brief first, then craft

**Purpose:** the critique loop checks craft. This file adds the step a creative director takes before that: does the work answer the brief, for its audience? A bot acts as its own first-pass director. The yardstick is the brief, not taste. Where the brief is silent, the question goes to the owner of the work (the person who commissioned it).

**Guidance, not a rule:** start from the idea: what the piece says and how it should feel. Use the rules afterwards to edit and sharpen it, not to generate it. Work built outward from the rules tends to come out correct but lifeless.

Keep it light. These are defaults, not blockers, except CD-7, which is on the MUST-BE-RIGHT list in `critique-loop.md`. Grade: every CD rule is a Procedure, built on the practice and studies cited (`evidence.md`).

## CD-1. Have a brief before making anything
- **What:** Six short lines: the problem or purpose; the audience; the one idea (a single sentence); where and how big it is seen; must-keeps and constraints (brand, subject, format); how you'll judge it done.
- **Why:** Weak briefs waste work. In a 2022 survey most agency staff called client briefs inadequate, and few marketers had agreed criteria for judging the work [SRC-88]. A good brief is a platform that opens up ideas, not a box that closes them [SRC-89, SRC-90, SRC-107].
- **Check:** Can you fill all six lines? If not, see *When the world is not locked*: ask the owner, or if they asked you to invent, write the brief and show it before generating.
- **Read it exactly:** count what the brief fixes ("it" means one; a named number is that number; CD-7 checks it on the render), and keep background facts as mood rather than forcing each into the picture or the copy (ILL-6).
- **Production cost:** note how it will be made and paid for. Full-colour print, 3D renders or special finishes may be wasteful on a council or charity budget; ask, or offer a cheaper version that keeps the idea (owner's note on a batch 4 council notice, S44).


## When the world is not locked

A locked brief from the owner of the work (purpose, audience, the facts that must appear, tone or genre) is enough: do not re-ask; note any leftover CD-1 lines as [inferred] and work.

If the ask has no world and they did not say to invent one, ask them, all at once. Short answers and "don't know" are fine. Ask: what it is for; who it is for; the facts that must appear (who, what, when, where); and the tone or genre. Propose theme, mood and colour from those answers, unless they already named them. Do not collect a long form.

If they said to invent (from your mind, surprise me, make some up), write a complete brief first: purpose, audience, the facts, tone or genre, and a proposed theme, mood and colour. Show that world, or those worlds if there are several, before generating. Do not generate from an invented brief they have not seen.

When inventing worlds, vary them. Do not default to salt, marshes, lighthouses, harbours or coastal weather; that cluster is a habit, not a standing direction.

## CD-2. Set the direction once, then hold it
- **What:** Before styling, write 3-5 mood words or "pillars", a do/don't list, and the tokens that follow from them (palette roles, type, shape, light). Use your own or generated references; describe, don't copy.
- **Why:** Mood boards and art guides frame the task, align people and steer later work [SRC-97, SRC-98]. Game art directors turn pillars into a guide with do/don't examples and review against it [SRC-99, SRC-100]. Film production designers do the same for a whole production [SRC-106]. Without this, defaults decide (UI-7).
- **Check:** Does each colour, type and layout choice trace back to the direction? If it traces to a default, flag it.

## CD-3. Try a few options, choose, and drop the rest early
- **What:** For an open brief, make 4–8 structurally different roughs (thumbnails, quick renders). Compare head-to-head in a fresh context of the same model, not a second model. Show the top 2–3 to the owner of the work; only their winner goes through the fix loop. Pick against the brief and give a one-line reason for each dropped option. `tools/cd.py select` supports the packet and review; `critique-loop.md` is the procedure.
- **Why:** In a controlled study, making designs in parallel gave better results and more variety than refining one at a time [SRC-95]. Diverge, then converge [SRC-96]. Rough work keeps attention on the idea, not the finish [SRC-91]. Being wrong early is cheap [SRC-94]. Go for one strong idea [SRC-92].
- **Check:** Were options compared before polishing? Is the chosen one the best answer to CD-1, not just the first one made?
- **Concept fit:** test each option against the product's category and senses, not only its name: a coffee named after a harbour still has to look like something to drink, not a cleaning product. Look for readings nobody meant (a lone object can suggest an accident). An event sold on fun shows the activity and the people. Details: EN-2 items 7 and 8 (`energy-pass.md`).

## CD-4. Feedback says what and why, not how
- **What:** Name the problem, where it is, and why it matters for the brief or audience. A fix is offered as an example; the maker decides how to solve it. Talk about the work, never the maker.
- **Why:** Pixar's Braintrust gives notes without authority to mandate fixes, because the cause of a problem often lies elsewhere [SRC-94]. Feedback that pulls attention to the person rather than the task often lowers performance [SRC-102]. Specific, actionable, justified critique is rated more helpful [SRC-103]. Annotated, precise notes suit later stages, once the concept is locked [SRC-104].
- **Check:** This is how the template's Fix lines are already written. Label findings rule-backed (ID), intent-backed (brief line) or exploratory, each with provenance and confidence. Choose the intervention level before changing work (`critique-loop.md`).

## CD-5. Protect the idea through every round
- **What:** Each fix, and especially a take-over rework, keeps the one idea and the must-keeps from CD-1. After each round, re-read the brief. If the owner of the work asks to change only one part (the photograph, a stroke weight), treat everything they did not name as a must-keep. Do not regenerate the whole piece and rewrite type, colour or arrangement along the way.
- **Why:** Directors guard the core idea against compromise [SRC-87, SRC-89, SRC-93]. In the stress tests, a rework fixed the perspective but quietly dropped part of the subject (`examples/technical-drawing-still-life/`).
- **Check:** Is anything in the brief's must-keeps missing or changed? If so, flag it as CD-5, ranked first. Did a revision change something that was not asked for, such as type arrangement, palette or lockup proportions?

## CD-6. Done means the brief is met
- **What:** Stop when the work meets the CD-1 criteria with no blockers. If the next change serves taste rather than the brief or audience, it's done. “The original is better” is a valid verdict: revert and stop, reporting any remaining blockers.
- **Why:** A key art-direction skill is telling real improvement from personal preference [SRC-101]. Agreed criteria make "done" checkable [SRC-88]. The loop's stop rules apply (`critique-loop.md` section 7).

## CD-7. Exact copy and counts survive generation (MUST-BE-RIGHT)
- **What:** After every render, edit or regeneration, re-read each string the brief fixes, on the image, letter for letter: words, units ("km"), case (a lower-case wordmark stays lower case), punctuation and spacing. Nothing missing, nothing added. Then count every number the brief fixes (ten cups, ten guests, three steps, one plane) on the image itself.
- **Why:** Image generators drop, add and change characters and miscount objects, and a glance reads what it expects. In batch 8 the with-skill side dropped a unit (B84), a full stop (B95), the asked-for case (B100), added a stray comma (B79) and drew 11 guests for ten (B95); the maker found all five afterwards, not the judge (`examples/blind-test/RESULTS.md`).
- **Check:** Two columns: each string as briefed, and as it reads on the render; mark match or slip. For each fixed count, count on a 2× crop, one tick per item. Any slip is a blocker.
- **Fix:** Set text in code over the art where possible (set type can't slip); otherwise edit the wrong characters or regenerate and re-read. For counts, add or remove the item, or regenerate with the number stated and count again. Never deliver a slip with a note.
- **Grade:** Procedure. Internal evidence (five slips in one batch, one judge); untested as a rule.

## When the ask is "from scratch"
CD-1 to CD-7 assume the brief is given. When the owner asks for a redo, rejig or reimagining, write the brief yourself from first principles, get it signed off, and compare 4–8 roughs in a fresh context of the same model, show the top 2–3, and build only the chosen winner: `core/first-principles.md` (FP-1..9).

## Presenting the result
Lead with the brief and the idea. Show the chosen option, a one-line reason, and what was dropped and why. Answer the concerns people raise rather than selling harder [SRC-105]. Report open questions plainly.
