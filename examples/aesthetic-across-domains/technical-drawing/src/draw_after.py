"""After: true isometric exploded view drawn in 2D with hidden lines removed, a 2:1 line-weight hierarchy
(ISO 128-2 style), explode paths as thin chain lines, ISO 6433-style item balloons on aligned leaders,
a parts list, and type from the repo's font library (Public Sans + Martian Mono)."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Polygon, Circle
from scipy.spatial import ConvexHull
from geometry import PARTS, FACES, HOLE, T

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from common import static_font
PS = "grotesk-neutral/publicsans/PublicSans[wght].ttf"; MM = "monospace-code/martianmono/MartianMono[wdth,wght].ttf"
FP = {k: fm.FontProperties(fname=static_font(PS if k.startswith("s") else MM, w)) for k, w in
      (("s400", 400), ("s600", 600), ("s700", 700), ("m400", 400), ("m500", 500))}
INK, PAPER, MUTE, ACC = "#1b1d1f", "#fbfaf7", "#8a8d90", "#b4541b"
THICK, THIN, XTHIN = 1.8, 0.9, 0.45    # 4:2:1

# isometric view from front-right-above: the front (with the hole), the right side and the tops face the viewer
VIEWDIR = np.array([1.0, -1.0, 1.0]) / np.sqrt(3)        # from the object towards the viewer
_f = -VIEWDIR; _r = np.cross(_f, [0, 0, 1.0]); _r /= np.linalg.norm(_r); _u = np.cross(_r, _f)
def P(v):
    v = np.atleast_2d(np.asarray(v, float)); return np.c_[v @ _r, v @ _u]
def depth(v):  # larger = nearer the viewer
    v = np.atleast_2d(np.asarray(v, float)); return v @ VIEWDIR
NEAR = VIEWDIR
fig = plt.figure(figsize=(11.69, 8.27), dpi=200)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.02, 0.04, 0.60, 0.92]); ax.set_aspect("equal"); ax.axis("off")

def normal(v, f):
    a, b, c = v[f[0]], v[f[1]], v[f[2]]
    n = np.cross(b - a, c - a); return n / np.linalg.norm(n)

parts = []
for name, v, d, dist, n, desc, q, size in PARTS:
    off = np.array(d, float) * dist
    parts.append(dict(name=name, v=v + off, v0=v, off=off, n=n, desc=desc, q=q, size=size, d=np.array(d, float), dist=dist))
order = sorted(parts, key=lambda p: depth(p["v"].mean(0))[0])  # far first

# explode paths: thin chain lines from the assembled position to the exploded one, drawn under everything
for p in parts:
    c0 = p["v0"].mean(0); c1 = p["v"].mean(0)
    a, b = P(c0)[0], P(c1)[0]
    ax.plot([a[0], b[0]], [a[1], b[1]], color=MUTE, lw=XTHIN, ls=(0, (10, 3, 2, 3)), zorder=1)

z = 2
for p in order:
    v = p["v"]
    vis = [f for f in FACES if normal(v, f) @ NEAR > 1e-6]
    for f in vis:
        nz = normal(v, f)
        shade = "#ffffff" if nz[2] > 0.5 else ("#f2f0ea" if nz[1] < -0.5 else "#dedad1")  # tops lightest, fronts light, right sides darker: light from upper left
        ax.add_patch(Polygon(P(v[list(f)]), closed=True, fc=shade, ec=INK, lw=THIN, joinstyle="round", zorder=z))
    if p["name"] == "front":   # entrance hole on the front face (y = min)
        cx, cy, cz = HOLE["centre"]; r = HOLE["r"]; t = np.linspace(0, 2 * np.pi, 120)
        ring = np.c_[cx + r * np.cos(t), np.full_like(t, cy) + p["off"][1], cz + r * np.sin(t)]
        ax.add_patch(Polygon(P(ring), closed=True, fc="#3a3c3e", ec=INK, lw=THIN, zorder=z + 0.5))
    hull = P(v)[ConvexHull(P(v)).vertices]
    ax.add_patch(Polygon(hull, closed=True, fill=False, ec=INK, lw=THICK, joinstyle="round", zorder=z + 0.6))
    p["hull"] = hull; p["z"] = z; z += 1

# screws: 4 on the front's explode line (into the sides), 4 under the base (into the walls), in the accent colour
def screw(at, axis, zo, target=None, length=30):
    a = np.array(at, float); b = a + np.array(axis, float) * length
    pa, pb = P(a)[0], P(b)[0]
    if target is not None:   # thin dotted line from the screw tip to where it enters the part
        pt = P(target)[0]
        ax.plot([pb[0], pt[0]], [pb[1], pt[1]], color=ACC, lw=0.7, ls=(0, (1.5, 2)), zorder=zo)
    ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=ACC, lw=2.2, solid_capstyle="butt", zorder=zo)
    ax.add_patch(Circle(pa, 3.2, fc=PAPER, ec=ACC, lw=1.1, zorder=zo + 0.01))
    return pa
fr = [p for p in parts if p["name"] == "front"][0]; ba = [p for p in parts if p["name"] == "base"][0]
screw_pts = []
for x, zz in ((T / 2, 40), (150 - T / 2, 40), (T / 2, 170), (150 - T / 2, 170)):   # through the front into the sides' front edges
    screw_pts.append(screw((x, fr["off"][1] - 55, zz), (0, 1, 0), 100, target=(x, fr["off"][1], zz)))
for x, y in ((T / 2, 35), (150 - T / 2, 115), (T / 2, 115), (150 - T / 2, 35)):        # up through the base into the sides
    screw_pts.append(screw((x, y, ba["off"][2] - 125), (0, 0, 1), ba["z"] - 0.2, target=(x, y, ba["off"][2])))

# item balloons: two aligned columns, leaders at one angle family, dot on the part
items = [(p["n"], p) for p in parts] + [(7, None)]
xs = np.concatenate([p["hull"][:, 0] for p in parts]); ys = np.concatenate([p["hull"][:, 1] for p in parts])
L, R = xs.min() - 70, xs.max() + 70
def anchor(p):
    h = p["hull"]; c = h.mean(0); return c
side = {1: L, 2: L, 4: L, 3: R, 5: R, 6: R, 7: L}
targets = {n: (anchor(p) if p is not None else screw_pts[0]) for n, p in items}
GAP = 44  # minimum balloon spacing in drawing units
for col in (L, R):
    ns = sorted([n for n in side if side[n] == col], key=lambda n: -targets[n][1])
    ys_b = [targets[n][1] for n in ns]
    for i in range(1, len(ys_b)):            # push down to keep spacing
        ys_b[i] = min(ys_b[i], ys_b[i - 1] - GAP)
    for n, by in zip(ns, ys_b):
        tx_, ty = targets[n]
        bx = col
        ax.plot([bx + (16 if col == L else -16), tx_], [by, ty], color=INK, lw=XTHIN * 1.4, zorder=60)
        ax.add_patch(Circle((tx_, ty), 2.6, color=INK if n != 7 else ACC, zorder=61))
        ax.add_patch(Circle((bx, by), 16, fc=PAPER, ec=(ACC if n == 7 else INK), lw=THIN * 1.2, zorder=62))
        ax.text(bx, by - 0.5, str(n), ha="center", va="center", fontsize=10.5, fontproperties=FP["m500"], color=(ACC if n == 7 else INK), zorder=63)
sp = np.array(screw_pts); ax.set_xlim(L - 30, R + 30); ax.set_ylim(min(ys.min(), sp[:, 1].min()) - 30, ys.max() + 40)

# title block and parts list (right column)
tx = 0.645
fig.text(tx, 0.885, "Nest box, 32 mm entrance", fontproperties=FP["s700"], fontsize=19, color=INK)
fig.text(tx, 0.85, "Exploded view · isometric · all sizes in mm · 15 mm board", fontproperties=FP["s400"], fontsize=10, color="#4a4d50")
rows = [(p["n"], p["desc"], p["q"], p["size"]) for p in parts] + [(7, "Screw, 4 x 30 mm", 8, "")]
y = 0.77
fig.text(tx, y, "No.", fontproperties=FP["s600"], fontsize=9, color="#4a4d50")
fig.text(tx + 0.04, y, "Part", fontproperties=FP["s600"], fontsize=9, color="#4a4d50")
fig.text(tx + 0.19, y, "Qty", fontproperties=FP["s600"], fontsize=9, color="#4a4d50")
fig.text(tx + 0.225, y, "Size", fontproperties=FP["s600"], fontsize=9, color="#4a4d50")
fig.add_artist(plt.Line2D([tx, 0.965], [y - 0.012, y - 0.012], color=INK, lw=THIN, transform=fig.transFigure))
for i, (n, desc, q, size) in enumerate(rows):
    yy = y - 0.05 - i * 0.042
    col = ACC if n == 7 else INK
    fig.text(tx, yy, f"{n}", fontproperties=FP["m400"], fontsize=10, color=col)
    fig.text(tx + 0.04, yy, desc, fontproperties=FP["s400"], fontsize=10.5, color=INK)
    fig.text(tx + 0.19, yy, f"{q}", fontproperties=FP["m400"], fontsize=10, color=INK)
    fig.text(tx + 0.225, yy, size, fontproperties=FP["m400"], fontsize=8.5, color="#4a4d50")
    fig.add_artist(plt.Line2D([tx, 0.965], [yy - 0.016, yy - 0.016], color="#d8d5ce", lw=XTHIN, transform=fig.transFigure))
fig.text(tx, 0.32, "Assembly order", fontproperties=FP["s700"], fontsize=11, color=INK)
steps = ["Screw the sides (4, 5) to the base (1).", "Fix the front (2) and back (3) to the sides.", "Lay the roof (6) on the sloped tops and screw down."]
for i, s in enumerate(steps):
    fig.text(tx, 0.285 - i * 0.034, f"{i + 1}", fontproperties=FP["m400"], fontsize=10, color=INK)
    fig.text(tx + 0.025, 0.285 - i * 0.034, s, fontproperties=FP["s400"], fontsize=10.5, color=INK)
fig.text(tx, 0.075, "Chain lines show where each part moves to. Screws in orange.", fontproperties=FP["s400"], fontsize=9, color="#4a4d50")
plt.savefig(os.path.join(os.path.dirname(__file__), "..", "after.png"), facecolor=PAPER)
