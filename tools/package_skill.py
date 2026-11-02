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
        "\"+ creative director\", \"consult creative director\" or \"creative director: direct this\", or asks to redo, rejig or reimagine "
        "a piece from scratch (step back, brief from first principles, 2-3 concepts, then build).")
DIRS = ["core", "modules", "lite", "tools"]
FILES = ["SOURCES.md", "BIBLIOGRAPHY.md", "LICENSE", "fonts/README.md", "fonts/CATALOGUE.md", "fonts/catalogue.json"]   # font catalogue only; font files stay in the repo
SKIP_FILES = {"modules/lookbook/looks.csv"}   # the json carries the same rows
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".blend", ".pyc"}
SKIP_PARTS = {"__pycache__", ".pytest_cache"}

assert len(NAME) <= 64 and re.fullmatch(r"[a-z0-9-]+", NAME) and "claude" not in NAME and "anthropic" not in NAME
assert 0 < len(DESC) <= 1024 and "<" not in DESC and "'" not in DESC   # single-quoted in the YAML

def skill_md():
    body = (ROOT / "AGENTS.md").read_text().split("\n", 1)[1].lstrip()          # drop the "# AGENTS.md" title
    tail = (f"\n## Files in this skill\n`core/` (principles and critique-loop always, the rest as above), `modules/<name>/README.md` (as above and `core/which-modules.md`), "
            f"`lite/CREATIVE-DIRECTOR-LITE.md` (short version for small contexts), `tools/` (optional Python: Pillow, NumPy), "
            f"`fonts/CATALOGUE.md` (theme catalogue of free fonts; the font files are in the repo's `fonts/`), `SOURCES.md`, `BIBLIOGRAPHY.md`. Worked examples and images live in the repo, not here: {REPO}/tree/main/examples\n")
    return f"---\nname: {NAME}\ndescription: '{DESC}'\n---\n\n# Creative director\n\n{body.rstrip()}\n{tail}"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    md = skill_md()
    assert len(md.split()) * 1.4 < 5000, "SKILL.md body too long"
    files = [p for d in DIRS for p in sorted((ROOT / d).rglob("*"))
             if p.is_file() and p.suffix.lower() not in SKIP_EXT and not SKIP_PARTS & set(p.parts)
             and str(p.relative_to(ROOT)) not in SKIP_FILES]
    files += [ROOT / f for f in FILES]
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{NAME}/SKILL.md", md)
        for p in files:
            z.write(p, f"{NAME}/{p.relative_to(ROOT)}")
    print(f"{OUT}  {OUT.stat().st_size/1024:.0f} KB  {len(files)+1} files")

if __name__ == "__main__":
    main()
