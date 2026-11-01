#!/usr/bin/env python3
"""Build creative-director-skill.zip: a Claude Agent Skill (claude.ai upload, Claude Code, Claude API) and a
Claude Project knowledge pack. Run from anywhere: python3 tools/package_skill.py [OUT.zip]

Contents: creative-director/ with SKILL.md (frontmatter + the full AGENTS.md instructions), core/, modules/, lite/,
tools/ (scripts only), the font catalogue (fonts/*.md, catalogue.json; no font files) and SOURCES.md, LICENSE. No examples, images or caches.
Checked against Anthropic's Agent Skills docs (1 Nov 2026): name <= 64 chars, lowercase letters, digits and hyphens,
no reserved words; description non-empty, <= 1024 chars, says what and when; SKILL.md body kept short (< 5k tokens)."""
import pathlib, re, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist/creative-director-skill.zip"
NAME = "creative-director"
REPO = "https://github.com/SnazzyGaz/creative-director"
DESC = ("Judge and improve visual work (generated images, illustrations, technical drawings, 3D renders, web and app UI, "
        "UX flows, typography, layout, brand) against cited, checkable design rules, with a light-touch "
        "render-critique-fix loop and a comparative aesthetic layer (intent, side-by-side judgement, revision checks). Use when making or reviewing anything visual, or when the user says "
        "\"+ creative director\", \"consult creative director\" or \"creative director: direct this\".")
DIRS = ["core", "modules", "lite", "tools"]
FILES = ["SOURCES.md", "LICENSE", "fonts/README.md", "fonts/CATALOGUE.md", "fonts/catalogue.json"]   # font catalogue only; font files stay in the repo
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".blend", ".pyc"}
SKIP_PARTS = {"__pycache__", ".pytest_cache"}

assert len(NAME) <= 64 and re.fullmatch(r"[a-z0-9-]+", NAME) and "claude" not in NAME and "anthropic" not in NAME
assert 0 < len(DESC) <= 1024 and "<" not in DESC and "'" not in DESC   # single-quoted in the YAML

def skill_md():
    body = (ROOT / "AGENTS.md").read_text().split("\n", 1)[1].lstrip()          # drop the "# AGENTS.md" title
    body = body.replace('(see README "Usage")', "(the three modes are below)").replace("using this repo", "using this skill")
    modes = ("\n## Modes\n"
             "- **Self-check** (`+ creative director`): run the loop on your own output.\n"
             "- **Consult** (`consult creative director`): the user sends the brief and the real output; return a neutral "
             "critique with ranked fixes (`core/critique-template.md`).\n"
             "- **Direct** (`creative director: direct this`): join at the start, write the brief, set direction, pick from "
             "rough options, review at checkpoints (`core/creative-direction.md`, CD-1..6).\n"
             "- **Hand-off with no specific ask:** analyse, send a ranked sign-off blurb of the imperative changes, and apply "
             "nothing until the owner signs off; \"just fix it\" gets the finished result with a done / not done list "
             "(`core/interaction-flow.md`).\n"
             "\nAlways work from the actual output (image, screenshot at real size, URL or renders), never a description.\n")
    tail = (f"\n## Files in this skill\n`core/` (always), `modules/<name>/README.md` (as `core/which-modules.md` says), "
            f"`lite/CREATIVE-DIRECTOR-LITE.md` (short version for small contexts), `tools/` (optional Python: Pillow, NumPy), "
            f"`fonts/CATALOGUE.md` (theme catalogue of free fonts; the font files are in the repo's `fonts/`), `SOURCES.md`. Worked examples and images live in the repo, not here: {REPO}/tree/main/examples\n")
    return f"---\nname: {NAME}\ndescription: '{DESC}'\n---\n\n# Creative director\n\n{body.rstrip()}\n{modes}{tail}"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    md = skill_md()
    assert len(md.split()) * 1.4 < 5000, "SKILL.md body too long"
    files = [p for d in DIRS for p in sorted((ROOT / d).rglob("*"))
             if p.is_file() and p.suffix.lower() not in SKIP_EXT and not SKIP_PARTS & set(p.parts)]
    files += [ROOT / f for f in FILES]
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{NAME}/SKILL.md", md)
        for p in files:
            z.write(p, f"{NAME}/{p.relative_to(ROOT)}")
    print(f"{OUT}  {OUT.stat().st_size/1024:.0f} KB  {len(files)+1} files")

if __name__ == "__main__":
    main()
