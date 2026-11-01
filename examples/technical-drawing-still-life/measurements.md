# Measurements with tools/vp.py and tools/ellipse.py (added after the run)

| | r01 | r02 |
|---|---|---|
| Horizon tilt (vp.py fit) | -13.6 deg, VPs 1132 px apart in height: TD-PER-1 fails | -0.3 deg, 20 px apart: consistent |
| Verticals (vp.py, group v) | -1.8 to -5.3 deg | within +-1 deg |
| Can top degree (ellipse.py) | 0.32 | 0.24 |
| Can base degree (front arc only, approximate) | 0.47 | 0.37 |
| Minor axis vs can centre line | 1.0 / 1.7 deg | 0.1 / 0.4 deg |
| End check | OK | OK |

- r01 segments were picked by eye (`segments-r01.csv`). r02 segments came from `vp.py detect`, sorted into groups by eye (`segments-r02.csv`). On r01, detection missed parts of the right face, so picking by eye was needed.
- The tools agree with the round critiques. TD-ELL-2 is met in both rounds; the base is more open than the top.
- Overlays: `vp-r02.png`, `ellipse-fits.png` (r02 base, r01 top, r01 base).
