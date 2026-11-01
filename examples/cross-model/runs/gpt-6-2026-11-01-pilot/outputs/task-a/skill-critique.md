# Task A — skill-condition response (reconstructed)

## Direct-mode critique
- **UX-1 / CORE-10 — blocker:** the pre-order controls are inert spans, and the fixed-width absolutely positioned wrapper breaks on mobile. Evidence: `.wrap{width:1250px}` and `.btn` spans labelled Submit/Go.
- **UI-6 — blocker:** several text/background pairs have insufficient contrast. Examples include `#5b00c9` on `#7a00ff`, `#ff9900` on `#ffe600`, and `#c0c0c0` on white.
- **UI-10 — blocker:** absolute positioning and fixed width cause overflow at narrow viewports and enlarged text.
- **UI-1 / CORE-7:** too many unrelated typefaces and decorative treatments fragment the system.
- **CORE-1 / UI-4 / UX-6:** hierarchy and reading order are weak; nine navigation items and a marquee compete with the pre-order proposition.
- **Brief preservation:** the bakery name, three loaf types, hours, address and brand orange must remain.

## Targeted fix plan
1. Replace fixed/absolute layout with responsive semantic sections and mobile-first stacking.
2. Make the order action real and honest about its behavior. With no order backend available, use a validated form that prepares an email draft, and label it as such rather than implying it submits an order online.
3. Establish readable contrast and a single type system; use the brand orange as an accent.
4. Re-render at 390px and 1280px and at 200% text zoom; verify no horizontal overflow, working action, and WCAG AA text contrast.

## Revised output
See `improved-bakery.html`. It retains the required content and #E8743B. The form uses a mailto draft rather than pretending a server-side order system exists.

## Verification status
Source inspection supports responsive structure and semantic controls. A browser-rendered screenshot, automated contrast audit and 200% zoom check were not run, so those outcomes are not claimed as verified.
