"""Mauna Loa annual mean CO2, 1959-2025. python3 chart.py before|after OUT.png
Data: NOAA Global Monitoring Laboratory, co2_annmean_mlo.csv (public domain), retrieved 1 Nov 2026."""
import os, sys
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [l.strip().split(",") for l in open(os.path.join(HERE, "co2_annmean_mlo.csv")) if l[0].isdigit()]
yr = [int(r[0]) for r in rows]; ppm = [float(r[1]) for r in rows]
MODE, OUT = sys.argv[1], sys.argv[2]

if MODE == "before":
    # a typical first try: defaults, a bar per year in a rainbow, a legend for one series, every year as a tick
    fig, ax = plt.subplots(figsize=(8, 5), dpi=200)
    ax.bar(yr, ppm, color=plt.cm.rainbow([i / len(yr) for i in range(len(yr))]), label="CO2 (ppm)")
    ax.set_title("CO2 Levels Over The Years", fontsize=16, fontweight="bold")
    ax.set_xlabel("Year"); ax.set_ylabel("CO2")
    ax.set_xticks(yr); ax.tick_params(axis="x", labelrotation=90, labelsize=5)
    ax.grid(True); ax.legend()
    ax.annotate("Alarming increase!", xy=(2015, 400), xytext=(1975, 430), arrowprops=dict(arrowstyle="->"), fontsize=11, color="red")
    fig.tight_layout(); fig.savefig(OUT); sys.exit(0)

S = "/tmp/aad-static-fonts/"
for f in ("Newsreader-36-560.ttf", "SourceSans3-400.ttf", "SourceSans3-600.ttf"):
    fm.fontManager.addfont(S + f)
serif = fm.FontProperties(fname=S + "Newsreader-36-560.ttf")
sans = fm.FontProperties(fname=S + "SourceSans3-400.ttf"); sansb = fm.FontProperties(fname=S + "SourceSans3-600.ttf")
INK, SOFT, GRID, PAPER, ACC = "#1f1d1a", "#5c5852", "#e3ded4", "#faf7f1", "#b23a1e"
plt.rcParams.update({"font.family": "Source Sans 3", "font.size": 11, "text.color": INK,
                     "axes.labelcolor": SOFT, "xtick.color": SOFT, "ytick.color": SOFT})
fig = plt.figure(figsize=(8, 5), dpi=200, facecolor=PAPER)
ax = fig.add_axes([0.075, 0.12, 0.80, 0.60], facecolor=PAPER)
ax.plot(yr, ppm, color=ACC, lw=2.2, solid_capstyle="round")
ax.plot([yr[0], yr[-1]], [ppm[0], ppm[-1]], "o", color=ACC, ms=4.5)
ax.text(yr[0] + 1, ppm[0] - 2.5, f"{ppm[0]:.0f} ppm in {yr[0]}", fontproperties=sansb, fontsize=11, color=INK, va="top")
ax.text(yr[-1] + 1.2, ppm[-1], f"{ppm[-1]:.0f} ppm\nin {yr[-1]}", fontproperties=sansb, fontsize=11, color=INK, va="center", linespacing=1.15)
ax.set_xlim(1957, 2026); ax.set_ylim(300, 440)
ax.set_yticks(range(300, 441, 20)); ax.set_xticks(range(1960, 2021, 10))
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(SOFT); ax.spines["bottom"].set_linewidth(0.8)
ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0, labelsize=10.5, pad=6); ax.tick_params(axis="x", length=3, color=SOFT, labelsize=10.5)
for t in ax.get_xticklabels() + ax.get_yticklabels():
    t.set_fontproperties(sans); t.set_fontsize(10.5)
fig.text(0.075, 0.905, "Carbon dioxide at Mauna Loa has risen every year since 1959",
         fontproperties=serif, fontsize=17.5, color=INK)
fig.text(0.075, 0.855, "Annual mean CO\u2082 in parts per million. The yearly rise has roughly tripled: 0.86 ppm a year\nin the 1960s, 2.63 ppm a year in 2016\u20132025.",
         fontproperties=sans, fontsize=11, color=SOFT, va="top", linespacing=1.12)
fig.text(0.075, 0.035, "Source: NOAA Global Monitoring Laboratory, Mauna Loa Observatory annual means (file of 9 Oct 2026).",
         fontproperties=sans, fontsize=9, color=SOFT)
fig.savefig(OUT, facecolor=PAPER)
