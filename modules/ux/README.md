# Module: UX (how it works)

Flows, feedback, errors, defaults, and the usability heuristics. Load with `core/` and usually `web-ui/`. A bot can't run a real user test, so these rules are for a heuristic review: walk the flow yourself, screen by screen, and check each rule.

Format: **What / Why / Check / Fix / Grade / Source**. **MUST-BE-RIGHT** marks blockers.

---

### UX-1. The main flow can be completed (MUST-BE-RIGHT)
- **What:** A first-time user can finish the main task (sign up, buy, save, export) without dead ends.
- **Why:** Good looks earn tolerance for minor problems, not for a broken task [S34].
- **Check:** Write the task as steps. Walk it in the build. Note every point where the next step isn't visible, or where you had to guess.
- **Fix:** Remove or merge steps; make the next action the primary button on each screen.
- **Grade:** Partly supported (usability research).
- **Source:** NN/g heuristics #6, #8 [S4]; NN/g aesthetic-usability effect [S34].

### UX-2. Visible system status
- **What:** Every action gets feedback quickly: pressed state, progress for anything over about a second, a clear success state.
- **Why:** Without feedback people repeat actions or abandon.
- **Check:** Trigger every action and time the response against three limits: under 0.1 s feels instant; under 1 s keeps the user's train of thought, with no indicator needed; over 1 s needs a busy indicator; over about 10 s needs a progress bar and a way to cancel. Throttle the network: are loading states shown?
- **Fix:** Add pressed/loading/success states; disable double-submit; show progress for long tasks.
- **Grade:** Partly supported (usability heuristics, from testing practice).
- **Source:** NN/g heuristic #1 [S4]; Nielsen, *Response Time Limits* [S65].

### UX-3. Errors: prevent, then explain and recover
- **What:** Prevent likely errors (constraints, good defaults, confirmations for destructive actions). When an error happens: show it next to the cause, in plain language, say how to fix it, keep the user's input, don't blame them, and don't show it before they've had a chance to finish.
- **Why:** Errors are where most frustration and abandonment happen.
- **Check:** Submit empty, wrong and edge-case inputs. Is each message near the field, specific, constructive, and is input preserved? Does any error appear just from tabbing through an empty field?
- **Fix:** Rewrite messages (what happened + how to fix); move them inline; preserve input; validate on submit or after input, not on focus loss of an untouched field.
- **Grade:** Partly supported (usability heuristics, from testing practice).
- **Source:** NN/g, *Error-Message Guidelines* [S14]; heuristics #5, #9 [S4].

### UX-4. Good defaults
- **What:** Pre-fill the most common or safest value; never default to the first alphabetical option or the most expensive one.
- **Why:** Most users keep defaults, so the default *is* the experience for most people.
- **Check:** List every pre-set value (selects, toggles, plans). Is each the most common or safest choice?
- **Fix:** Change defaults to the common case; use the context you have (location, previous choice).
- **Grade:** Partly supported (defaults research summarised by NN/g).
- **Source:** NN/g, *The Power of Defaults* [S15].

### UX-5. Control and a way out
- **What:** Every step has an obvious back/cancel; destructive actions can be undone or ask for confirmation.
- **Why:** People make slips; being trapped erodes trust.
- **Check:** On each screen, find the exit in under two seconds. Delete something: can you undo it?
- **Fix:** Add cancel/back; add undo (preferred) or confirm.
- **Grade:** Partly supported (usability heuristics).
- **Source:** NN/g heuristic #3 [S4].

### UX-6. Speak the user's language, follow conventions
- **What:** Labels use the user's words, not internal jargon or error codes; common patterns (logo goes home, cart top right, settings icon) work as expected.
- **Why:** People spend most of their time on other products and expect yours to work the same way (Jakob's law). They scan, take the first reasonable option, and muddle through. They don't read instructions.
- **Check:** Read every label aloud: would a newcomer know what it does? Compare key patterns with two well-known products in the same category.
- **Fix:** Rename; revert novel patterns unless there's a measured reason.
- **Grade:** Partly supported (usability heuristics).
- **Source:** NN/g heuristics #2, #4 [S4]; *Laws of UX*, Jakob's law [S61]; Krug, *Don't Make Me Think* (pages should be self-evident) [S63].

### UX-7. Recognition over recall
- **What:** Options, labels and needed information stay visible; users don't have to remember things between screens.
- **Why:** Short-term memory is small.
- **Check:** Is there any step where you need information from a previous screen that is no longer shown? Do form fields keep visible labels (not placeholder-only)?
- **Fix:** Show summaries; use persistent labels.
- **Grade:** Well supported (recognition is easier than recall).
- **Source:** NN/g heuristic #6 [S4].

### UX-8. Show what can be done, and map controls to results
- **What:** Every interactive element has a visible signifier (it looks clickable, draggable or editable). Controls sit near and are arranged like the things they affect (natural mapping). Constraints rule out invalid actions.
- **Why:** An affordance nobody can see doesn't help. Norman's revised account says signifiers are what designers control.
- **Check:** Screenshot a screen, without hover. Mark everything you think is clickable, then check against the code. Look for false signifiers (styled text that isn't a link) and hidden ones (hover-only actions on touch screens). Do controls match the layout of what they change?
- **Fix:** Give interactive elements a consistent, visible style. Move controls next to their target; disable or hide impossible options; use input types that constrain (date pickers, steppers).
- **Grade:** Partly supported (Norman's framework; widely tested in practice).
- **Source:** Norman, *The Design of Everyday Things*, revised edition (affordances, signifiers, mapping, constraints, feedback) [S62]; Krug [S63].

### UX-9. Frequent actions are big and close
- **What:** The most frequent or important targets are large and near where the pointer or thumb already is. Dangerous actions are kept away from common ones.
- **Why:** Fitts's law: the time to hit a target grows with distance and shrinks with size.
- **Check:** For the main task, measure the size of each target and its distance from the previous one. Is the primary button small or far away? Is "Delete" next to "Save"?
- **Fix:** Enlarge and move primary targets (UI-5 minimums). Make whole rows or cards clickable where it is safe. Separate destructive actions.
- **Grade:** Well supported (Fitts's law).
- **Source:** NN/g, *Fitts's Law* and *Touch Targets* [S67]; *Laws of UX* [S61].

## Myths and weak claims
- **"Max 7 ± 2 menu items" (Miller):** Miller studied memory, not choosing from visible options. Menus are recognition tasks. Broad, well-grouped menus are usually fine [S64]. Use chunking and clear labels instead.
- **"Three clicks or they leave":** no supporting evidence. Clear next steps (information scent) matter more than click count [S66].
- **"Hick's law means fewer options is always better":** it models simple choice-reaction tasks. Scanning a familiar or ordered menu doesn't follow it well [S68]. Cut options only when they are truly unneeded (CORE-8).
- **"Under 400 ms (Doherty) is the UX standard":** that comes from a 1982 IBM productivity study. Use NN/g's 0.1 / 1 / 10 s limits for feedback design [S65].
- **"Users read the page":** they mostly scan [S63]. Write for scanning: front-load labels and keep chunks short.
