#!/usr/bin/env python3
"""check_budgets.py: token budgets for the rule files, so the load an agent carries can't creep up unnoticed.

    python3 tools/check_budgets.py           # table of every budgeted file or set; exit 1 if any is over
    python3 tools/check_budgets.py --loads   # also print the typical loads from core/which-modules.md (not enforced)

Counts use tiktoken's cl100k_base encoding when it is installed (`pip install tiktoken`; the CI installs it), otherwise
characters / 4, which runs within a few percent on these files. Other models tokenise differently (roughly +-15%).
A file over budget is split (an entry file plus on-demand detail files) or tightened; rules and IDs are not dropped.
Raising a budget is a deliberate change: edit BUDGETS below and say why in CHANGELOG.md."""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
try:
    import tiktoken
    _enc = tiktoken.get_encoding("cl100k_base")
    count, METHOD = (lambda s: len(_enc.encode(s))), "tiktoken cl100k_base"
except Exception:                                   # no tiktoken, or no network to fetch its encoding
    count, METHOD = (lambda s: round(len(s) / 4)), "characters / 4"

ALWAYS = ["AGENTS.md", "core/principles.md", "core/critique-loop.md"]
# (label, files, budget). Sets are summed. Per-file rules for everything else follow below.
BUDGETS = [
    ("always-on set (AGENTS + principles + loop)", ALWAYS, 6500),
    ("always-on set + critique template", ALWAYS + ["core/critique-template.md"], 8000),
    ("AGENTS.md", ["AGENTS.md"], 1500),
    ("core/principles.md", ["core/principles.md"], 2100),
    ("core/critique-loop.md", ["core/critique-loop.md"], 3300),
    ("core/critique-template.md", ["core/critique-template.md"], 1500),
    ("lite/CREATIVE-DIRECTOR-LITE.md", ["lite/CREATIVE-DIRECTOR-LITE.md"], 2500),
]
MODULE_ENTRY = 6000      # each modules/<name>/README.md
ON_DEMAND = 4500         # each other .md in core/ and modules/ (detail files loaded only when needed)
SKIP = {"modules/lookbook/UPDATING.md"}   # maintainer notes, never loaded for a critique

LOADS = {  # typical loads, as listed in core/which-modules.md
    "screen (web-ui + ux + energy-pass)": ["modules/web-ui/README.md", "modules/ux/README.md", "core/energy-pass.md"],
    "social card (layout + typography)": ["modules/layout/README.md", "modules/typography/README.md"],
    "social card + composition (with Sitting right)": ["modules/layout/README.md", "modules/typography/README.md",
        "modules/composition/README.md", "modules/composition/sitting-right.md"],
    "figure (character + technical-drawing + illustration)": ["modules/character/README.md",
        "modules/technical-drawing/README.md", "modules/illustration/README.md"],
    "poster remake (first-principles + layout + typography + aesthetic)": ["core/first-principles.md",
        "modules/layout/README.md", "modules/typography/README.md", "modules/aesthetic-critique/README.md"],
    "infographic (layout + infographics + typography + illustration)": ["modules/layout/README.md", "modules/layout/infographics.md",
        "modules/typography/README.md", "modules/illustration/README.md"],
    "photo (photo + character + illustration)": ["modules/photo/README.md", "modules/character/README.md",
        "modules/illustration/README.md"],
    "video review (film README + story + review)": ["modules/film/README.md", "modules/film/story.md", "modules/film/review.md"],
    "full video review (+ edit.md + generated.md)": ["modules/film/README.md", "modules/film/story.md",
        "modules/film/review.md", "modules/film/edit.md", "modules/film/generated.md"],
}


def tokens(files):
    return sum(count((ROOT / f).read_text()) for f in files)


def rows():
    out = [(label, tokens(files), cap) for label, files, cap in BUDGETS]
    budgeted = {f for _, files, _ in BUDGETS if len(files) == 1 for f in files}
    for p in sorted((ROOT / "modules").glob("*/README.md")):
        out.append((str(p.relative_to(ROOT)), count(p.read_text()), MODULE_ENTRY))
    for p in sorted([*(ROOT / "core").glob("*.md"), *(ROOT / "modules").glob("*/*.md")]):
        rel = str(p.relative_to(ROOT))
        if rel in budgeted or rel in SKIP or p.name == "README.md":
            continue
        out.append((rel, count(p.read_text()), ON_DEMAND))
    return out


def main(argv):
    over = 0
    print(f"token budgets ({METHOD})")
    for label, n, cap in rows():
        bad = n > cap
        over += bad
        print(f"{'OVER' if bad else 'ok  '}  {n:6,} / {cap:6,}  {label}")
    if "--loads" in argv:
        base = tokens(ALWAYS + ["core/critique-template.md"])
        print(f"\ntypical loads (always-on + template = {base:,}; not enforced)")
        for label, files in LOADS.items():
            print(f"        {base + tokens(files):6,}  {label}")
    print(f"\n{over} over budget" if over else "\nall within budget")
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
