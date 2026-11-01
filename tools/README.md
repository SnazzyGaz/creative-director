# Tools

Small scripts that back the **Auto: yes/partly** notes in the modules. Python 3 with Pillow and numpy; `vp.py detect` and `ellipse.py` also need OpenCV (`pip install opencv-python-headless`). `shot.sh` needs google-chrome.

| Script | What it does | Rules |
|---|---|---|
| `look.py IMG SHEET.png` | One contact sheet with the five look tests (blur, thumbnail, flip, greyscale, edges), plus L* value stats and a "what leads" grid | critique loop step 2, CORE-2, CORE-3 |
| `contrast.py < pairs.txt` | WCAG contrast ratios, with alpha compositing | UI-6 |
| `shot.sh FILE.html PREFIX` | Headless screenshots at 390 px, 1280 px and 200% zoom | UI-10, critique loop step 1 |
| `beforeafter.py A B OUT.png` | Labelled side-by-side of two rounds | critique loop step 4 |
| `vp.py fit SEGS.csv` / `vp.py detect IMG OUT.png` | Least-squares vanishing points per edge family, horizon tilt, VP height mismatch, tilt of verticals. `detect` finds long straight segments to sort into groups | TD-PER-1, TD-PER-3 |
| `ellipse.py IMG ROI [--axis ...]` | Fits an ellipse in a box. Reports degree, minor-axis angle against the form's axis, fit residual, and a pointed/flat end check | TD-ELL-1, -2, -3 |

**Limits:**
- `vp.py` does not group edges into families: a bot or person does. Its result depends on the endpoints, so take them at zoom. Far vanishing points are unstable (see the `spread` figure).
- `ellipse.py` needs a tight box around one ellipse. Half-visible ellipses, such as a cylinder base, give an approximate degree. Its end check passed a synthetic test (a clean ellipse reads OK; a lemon shape is flagged) but has not been tested on real bad drawings. In `examples/technical-drawing-takeover/` it missed a planted lemon-shaped ellipse because the cylinder's side lines were inside the box; the minor-axis check (TD-ELL-1) still worked.
- Confirm overlays by eye. Tested on `examples/technical-drawing-still-life/` (see `measurements.md` there).
