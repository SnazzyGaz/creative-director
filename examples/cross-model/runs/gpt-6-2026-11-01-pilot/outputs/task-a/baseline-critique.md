# Task A — baseline-condition response (reconstructed)

## Main issues, ranked
1. The pre-order action is not functional: “Submit” and “Go” are spans, not controls with behavior. A customer cannot place an order.
2. The fixed 1250px wrapper and absolute positioning will overflow a 390px phone viewport and at enlarged text sizes.
3. Contrast is severely inadequate in several areas, including orange text on yellow, purple on purple, and pale text on white.
4. Visual hierarchy is noisy: marquee, gradient, rotated boxes, oversized heading and nine navigation labels compete for attention.
5. Typography is inconsistent and hard to scan; long filler copy hides the deadline and collection instruction.
6. The three loaves, opening hours and address are present, but the information is buried.

## Fix
Use a semantic, responsive single-page layout. Put “Order by Thursday, collect Saturday” near the top; make a clear order CTA; group the three breads; show hours/address in a compact details section; use orange as an accent; and test at phone and desktop widths. Preserve name, loaves, hours, address and #E8743B.

## Limitations
This baseline response is a separately written baseline-condition answer for this evaluation, not a logged output from an independently reset model session. It must not be presented as a blinded run.
