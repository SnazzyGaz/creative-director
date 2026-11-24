#!/usr/bin/env python3
"""Build the portable Agent Skill: skills/creative-director/ (committed) and dist/creative-director-skill.zip.

    python3 tools/package_skill.py            # rebuild skills/creative-director/ and the zip
    python3 tools/package_skill.py --check    # exit 1 if the committed skill folder is out of date
    python3 tools/package_skill.py OUT.zip    # write the zip somewhere else

Reads version and metadata from manifest.json. Uses POSIX relative paths across Windows and Linux.
Never edit skills/creative-director/ by hand.
"""
import filecmp, json, pathlib, re, shutil, sys, tempfile, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
NAME = "creative-director"
SKILL_DIR = ROOT / "skills" / NAME
ZIP = ROOT / "dist/creative-director-skill.zip"
REPO = MANIFEST.get("repository", "https://github.com/SnazzyGaz/creative-director")
DESC = (
    "Tool-first design judgement and verification for AI agents: hard gates enforced in code "
    "(contrast, exact copy, charts, safe area, anatomy crops, deterministic compositing), "
    "a lean always-on kernel with manifest-driven module loading, proportional 3-tier workflows "
    "(fast QA, directed creation, deep remake), curated 415-look style bleed, and separate taste profiles. "
    "Use when making or reviewing visual work or UI, or when asked for \"+ creative director\", "
    "\"consult creative director\", \"direct this\", or a first-principles remake."
)
DIRS = ["core", "modules", "lite", "tools"]
FILES = [
    "manifest.json",
    "taste.default.json",
    "SOURCES.md",
    "BIBLIOGRAPHY.md",
    "LICENSE",
    "fonts/README.md",
    "fonts/CATALOGUE.md",
    "fonts/catalogue.json",
]
SKIP_FILES = {
    "modules/lookbook/looks.csv",
    "tools/lookbook_sync.py",
    "tools/package_skill.py",
    "tools/build_bundle.py",
    "modules/lookbook/UPDATING.md",
}
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".blend", ".pyc", ".zip"}
SKIP_PARTS = {"__pycache__", ".pytest_cache", "tests", "fixtures"}

assert len(NAME) <= 64 and re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", NAME) and "claude" not in NAME and "anthropic" not in NAME
assert 0 < len(DESC) <= 1024 and "<" not in DESC and "'" not in DESC


def version():
    if MANIFEST.get("version"):
        return str(MANIFEST["version"])
    m = re.search(r"^## (v[\d.]+[^\s]*)", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    return m.group(1).lstrip("v") if m else "0"


def skill_md():
    body = (ROOT / "AGENTS.md").read_text(encoding="utf-8").split("\n", 1)[1].lstrip()
    tail = (
        f"\n## Files in this skill\n"
        f"`manifest.json` (declarative module/tier/gate registry), `core/kernel.md` (always-on kernel ≤ 1,600 tokens), "
        f"`taste.default.json` (project taste profile starter), `core/` and `modules/` (loaded on demand via `tools/cd.py load`), "
        f"`tools/` (`cd.py`, `autocheck.py`, `compose.py`, `mcp_server.py`, `datagraphic.py`, `look.py`, `anatomy_crops.py`, `lookbook_find.py`, `font_find.py`), "
        f"`lite/CREATIVE-DIRECTOR-LITE.md`, `fonts/CATALOGUE.md`, `SOURCES.md`, `BIBLIOGRAPHY.md`. "
        f"Worked examples and lookbook image sheets live in the repo: {REPO}\n\n"
        f"**Needs:** a model that can see images and render/screenshot work at real size. Without vision, label the review rules-only.\n\n"
        f"This folder is generated from the repo root by `tools/package_skill.py` (version {version()}). Edit root files, not this copy.\n"
    )
    front = (
        f"---\nname: {NAME}\ndescription: '{DESC}'\nlicense: MIT (see LICENSE)\n"
        f"metadata:\n  author: Garyck Arntzen (https://x.com/_mintydoge)\n  version: \"{version()}\"\n  repository: {REPO}\n---\n"
    )
    return f"{front}\n# Creative director\n\n{body.rstrip()}\n{tail}"


def sources():
    files = [
        p for d in DIRS for p in sorted((ROOT / d).rglob("*"))
        if p.is_file()
        and p.suffix.lower() not in SKIP_EXT
        and not (SKIP_PARTS & set(p.relative_to(ROOT).parts))
        and p.relative_to(ROOT).as_posix() not in SKIP_FILES
    ]
    return files + [ROOT / f for f in FILES if (ROOT / f).is_file()]


def build(dest: pathlib.Path):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    md = skill_md()
    assert len(md.split()) * 1.4 < 5000 and md.count("\n") < 500, "SKILL.md body too long"
    (dest / "SKILL.md").write_text(md, encoding="utf-8", newline="\n")
    files = sources()
    for p in files:
        out = dest / p.relative_to(ROOT)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, out)
    return len(files) + 1


def tree(d: pathlib.Path):
    return sorted(p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file() and "__pycache__" not in p.parts)


def same_file(a: pathlib.Path, b: pathlib.Path) -> bool:
    if filecmp.cmp(a, b, shallow=False):
        return True
    # Tolerate git autocrlf line-ending differences on Windows runners.
    try:
        return a.read_bytes().replace(b"\r\n", b"\n") == b.read_bytes().replace(b"\r\n", b"\n")
    except OSError:
        return False


def check():
    with tempfile.TemporaryDirectory() as t:
        fresh = pathlib.Path(t) / NAME
        build(fresh)
        a, b = tree(fresh), tree(SKILL_DIR) if SKILL_DIR.exists() else []
        stale = sorted(set(a) ^ set(b)) + [f for f in a if f in b and not same_file(fresh / f, SKILL_DIR / f)]
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
