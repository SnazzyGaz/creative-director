"""Before: the kind of exploded view a bot makes with matplotlib's 3D axes (defaults kept)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from geometry import PARTS, FACES, HOLE
fig = plt.figure(figsize=(11.69, 8.27), dpi=150)
ax = fig.add_subplot(111, projection="3d")
cols = plt.cm.tab10.colors
for i, (name, v, d, dist, n, desc, q, size) in enumerate(PARTS):
    v = v + np.array(d) * dist
    polys = [[v[j] for j in f] for f in FACES]
    ax.add_collection3d(Poly3DCollection(polys, facecolor=cols[i], alpha=0.5, edgecolor="k", linewidth=1, label=f"{n}. {desc}"))
    c = v.mean(0)
    ax.text(c[0], c[1], c[2], f"Part {n}: {desc}", fontsize=9)
# hole as a circle on the front
t = np.linspace(0, 2 * np.pi, 60); cx, cy, cz = HOLE["centre"]; r = HOLE["r"]
ax.plot(cx + r * np.cos(t), np.full_like(t, cy - 110), cz + r * np.sin(t), "k", lw=1)
# screws as scattered points
sx = np.array([20, 130, 20, 130, 20, 130, 20, 130]); sy = np.array([-60, -60, -60, -60, 75, 75, 75, 75]); sz = np.array([60, 60, 160, 160, -30, -30, -30, -30])
ax.scatter(sx, sy, sz, c="r", s=20, label="7. Screws x8")
ax.set_xlim(-150, 300); ax.set_ylim(-150, 300); ax.set_zlim(-100, 400)
ax.set_xlabel("X (mm)"); ax.set_ylabel("Y (mm)"); ax.set_zlabel("Z (mm)")
ax.set_title("Bird Box Exploded View Diagram", fontsize=16)
ax.legend(loc="upper left")
plt.savefig("../before.png")
