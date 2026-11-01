# Log: technical-drawing-takeover

Take-over case (section 4b). Synthetic line drawings made by code (`draw.py`), with errors planted in round 1 so the tools could be checked against known answers.

- r01: five MUST-BE-RIGHT failures. vp.py caught TD-PER-1 (VPs 200 px apart in height, horizon tilt 6.2 deg) and TD-PER-3 (verticals -7.6 to +2.3 deg). ellipse.py caught TD-ELL-1 (minor axes about 19 deg off). TD-ELL-2 (base flatter than top) from the construction values. Take over.
- r02: redrawn by construction: one horizon, both VPs on it, true verticals, tin on the lid's diagonals, base ellipse fuller than top. Every tool check passes. Stopped.
- **Tool miss:** ellipse.py did not flag the planted lemon-shaped top (TD-ELL-3). Its end check said "OK" in three box sizes, because the tin's side lines start at the ellipse ends and fall inside the box, pulling the fit (overlay: ell-r01-top.png). Caught by eye at 2x zoom. This confirms the limit already noted in tools/README.md: the end check needs a closed ellipse with nothing else in the box.
- The tool numbers on round 1 are exact for the vanishing points because the segment endpoints come from the drawing code. On a real drawing they would be picked by eye or by `vp.py detect`, with more error.
