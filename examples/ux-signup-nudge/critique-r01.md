## Critique: library sign-up form, round 1

**Brief:** see `brief.md`. Main flow: card number, email, password, create account. Done when a typo can be found and fixed without retyping.
**Criteria judged against:** CD-1, UX-1, UX-2, UX-3, UX-6, UX-7, UI-5, UI-6, CORE-7.
**Evidence looked at:** round-01-empty-390.png, round-01-error-390.png (tools/shot.sh); contrast-r01.txt (tools/contrast.py). Test input: password "bookworm" (8 characters, no number; the form's hidden rule is 10+ with a number) and an email with a typo (gmial.com).

### Brief check (CD-1, CD-5)
- Answers the brief: partly. The account can be created, but only by guessing the password rule. Must-keeps present: three fields (plus a confirm field), teal, single page: yes.

### Test results (evidence)
- Walkthrough: submit with the test input. Result: one banner at the top, "Error 422: Validation failed. Invalid input." No field is marked. Both password fields are cleared. The email typo is not mentioned.
- Squint/blur: the button leads; field labels vanish once a field has text (placeholders only).
- Greyscale: placeholders and the small print are close to the white ground.

### Meets criteria
- UX-1: the flow can be finished (once the rule is guessed).
- UI-6: button 5.47:1; error banner 4.92:1.
- UI-5: one primary button, clearly the action.

### Needs improvement (ranked, max 5)
1. [BLOCKER] UI-6 not met. Placeholder text is the only label, at 1.92:1; small print 2.32:1; field underlines 1.36:1 (non-text needs 3:1). Fix: real labels above each field in body colour; 3:1 field borders; small print to 4.5:1.
2. [IMPROVEMENT] UX-3 not met. Error is vague, far from its cause, uses a status code, and clears the passwords. The rule is never shown before the error. Fix: show the password rule under the label; on error, mark the field and say what is wrong and how to fix it; keep what was typed.
3. [IMPROVEMENT] UX-7 not met. After typing, the placeholder disappears, so a filled form has no labels to check against. Fixed by item 1.
4. [IMPROVEMENT] UX-6 not met. "Register", "SUBMIT", "Card no.*" and "Error 422". Fix: "Create your library account", "Create account", "Library card number" with where to find it.
5. [IMPROVEMENT] UX-3 (prevention). The email typo (gmial.com) is accepted silently. Fix: suggest the likely domain.

### Take-over check (4b)
- One MUST-BE-RIGHT failure (UI-6); the flow can be completed; the structure is sound. **Nudge**: fixes 1, 2 and 4 this round (3 is covered by 1).

### Questions for the owner
- Keep the "password again" field? Many forms drop it in favour of a show-password toggle; that is a product choice, not a rule.
