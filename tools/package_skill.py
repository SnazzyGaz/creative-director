#!/usr/bin/env python3
"""Build the portable Agent Skill: skills/creative-director/ (committed) and dist/creative-director-skill.zip.

    python3 tools/package_skill.py            # rebuild skills/creative-director/ and the zip
    python3 tools/package_skill.py --check    # exit 1 if the committed skill folder is out of date
    python3 tools/package_skill.py OUT.zip    # write the zip somewhere else

The folder follows the open Agent Skills format (https://agentskills.io/specification), so the same copy works in
Hermes Agent, Claude (claude.ai upload, Claude Code, API), Codex, Gemini CLI, Cursor, GitHub Copilot, Devin/Windsurf
and other skills-compatible agents. It is generated: the rules live in the repo root (AGENTS.md, core/, modules/,
lite/, tools/), and this script copies them. Never edit skills/creative-director/ by hand.

Contents: SKILL.md (frontmatter + the AGENTS.md instructions), core/, modules/, lite/, the design tools in tools/,
the font catalogue (no font files), SOURCES.md, BIBLIOGRAPHY.md, LICENSE. No images, examples, caches, tests or
maintainer scripts (sync, packaging), so the folder stays small (about 1 MB) and passes skill installers' scans.
Frontmatter limits checked against agentskills.io and Anthropic's Agent Skills docs: name <= 64 chars, lowercase
letters, digits and single hyphens, matching the folder name, no reserved words; description 1-1024 chars, says
what and when; SKILL.md body well under 500 lines / 5k tokens."""
import filecmp, pathlib, re, shutil, sys, tempfile, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
NAME = "creative-director"
SKILL_DIR = ROOT / "skills" / NAME
ZIP = ROOT / "dist/creative-director-skill.zip"
REPO = "https://github.com/SnazzyGaz/creative-director"
DESC = ("Judge and improve visual work (generated images, illustrations, technical drawings, 3D renders, web and app UI, "
        "UX flows, typography, layout, brand, film and video: shots, edits, generated clips) against cited, checkable design rules, with a light-touch "
        "render-critique-fix loop and a comparative aesthetic layer (intent, side-by-side judgement, revision checks). Use when making or reviewing anything visual, or when the user says "
        "\"+ creative director\", \"consult creative director\" or \"creative director: direct this\", or asks to redo, rejig or reimagine "
        "a piece from scratch (step back, brief from first principles, 2-3 concepts, then build).")
DIRS = ["core", "modules", "lite", "tools"]
FILES = ["SOURCES.md", "BIBLIOGRAPHY.md", "LICENSE", "fonts/README.md", "fonts/CATALOGUE.md", "fonts/catalogue.json"]   # font catalogue only; font files stay in the repo
SKIP_FILES = {"modules/lookbook/looks.csv",            # the json carries the same rows
              "tools/lookbook_sync.py", "tools/package_skill.py", "tools/build_bundle.py",
              "modules/lookbook/UPDATING.md"}   # maintainer scripts, repo only
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".blend", ".pyc", ".zip"}
SKIP_PARTS = {"__pycache__", ".pytest_cache", "tests", "fixtures"}   # test suites stay in the repo

assert len(NAME) <= 64 and re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", NAME) and "claude" not in NAME and "anthropic" not in NAME
assert 0 < len(DESC) <= 1024 and "<" not in DESC and "'" not in DESC   # single-quoted in the YAML


def version():
    m = re.search(r"^## (v[\d.]+)", (ROOT / "CHANGELOG.md").read_text(), re.M)
    return m.group(1).lstrip("v") if m else "0"


def skill_md():
    body = (ROOT / "AGENTS.md").read_text().split("\n", 1)[1].lstrip()          # drop the "# AGENTS.md" title
    tail = (f"\n## Files in this skill\n`core/` (principles and critique-loop always, the rest as above), `modules/<name>/README.md` (as above and `core/which-modules.md`), "
            f"`lite/CREATIVE-DIRECTOR-LITE.md` (short version for small contexts), `tools/` (optional Python: Pillow, NumPy; Playwright for page checks; `pip install -r tools/requirements.txt`), "
            f"`fonts/CATALOGUE.md` (theme catalogue of free fonts; the font files are in the repo's `fonts/`), `SOURCES.md`, `BIBLIOGRAPHY.md`. "
            f"Worked examples, lookbook image sheets and font files live in the repo, not here: {REPO}\n\n"
            f"**Needs:** a model that can see images, and a way to render or screenshot the work at real size. Without vision, say the review is rules-only.\n\n"
            f"This folder is generated from the repo root by `tools/package_skill.py` (version {version()}). To change a rule, edit the repo's root files, not this copy.\n")
    front = (f"---\nname: {NAME}\ndescription: '{DESC}'\nlicense: MIT (see LICENSE)\n"
             f"metadata:\n  author: Garyck Arntzen\n  version: \"{version()}\"\n  repository: {REPO}\n---\n")
    return f"{front}\n# Creative director\n\n{body.rstrip()}\n{tail}"


def sources():
    files = [p for d in DIRS for p in sorted((ROOT / d).rglob("*"))
             if p.is_file() and p.suffix.lower() not in SKIP_EXT and not SKIP_PARTS & set(p.relative_to(ROOT).parts)
             and str(p.relative_to(ROOT)) not in SKIP_FILES]
    return files + [ROOT / f for f in FILES]


def build(dest: pathlib.Path):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    md = skill_md()
    assert len(md.split()) * 1.4 < 5000 and md.count("\n") < 500, "SKILL.md body too long"
    (dest / "SKILL.md").write_text(md)
    files = sources()
    for p in files:
        out = dest / p.relative_to(ROOT)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, out)
    return len(files) + 1


def tree(d: pathlib.Path):
    return sorted(str(p.relative_to(d)) for p in d.rglob("*") if p.is_file() and "__pycache__" not in p.parts)


def check():
    with tempfile.TemporaryDirectory() as t:
        fresh = pathlib.Path(t) / NAME
        build(fresh)
        a, b = tree(fresh), tree(SKILL_DIR) if SKILL_DIR.exists() else []
        stale = sorted(set(a) ^ set(b)) + [f for f in a if f in b and not filecmp.cmp(fresh / f, SKILL_DIR / f, shallow=False)]
    if stale:
        print("skills/creative-director/ is out of date; run python3 tools/package_skill.py\n  " + "\n  ".join(stale))
        return 1
    print(f"skills/{NAME}/ is up to date ({len(a)} files)")
    return 0


def main(argv):
    if "--check" in argv:
        return check()
    out = pathlib.Path(argv[0]) if argv else ZIP
    n = build(SKILL_DIR)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in tree(SKILL_DIR):
            z.write(SKILL_DIR / rel, f"{NAME}/{rel}")
    size = sum((SKILL_DIR / r).stat().st_size for r in tree(SKILL_DIR))
    print(f"skills/{NAME}/  {n} files, {size/1024:.0f} KB\n{out}  {out.stat().st_size/1024:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
