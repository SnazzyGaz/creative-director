#!/usr/bin/env python3
"""Build single-file prompt bundles for chat-only LLMs that cannot read repo files.

    python3 tools/build_bundle.py            # writes dist/creative-director-prompt.md and dist/creative-director-prompt-full.md
    python3 tools/build_bundle.py --check    # rebuild in memory and verify all manifest files exist

Driven directly from manifest.json so new modules (e.g. photo, writing, brand subfiles) are never omitted.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
REPO = MANIFEST.get("repository", "https://github.com/SnazzyGaz/creative-director")

CORE_BUNDLE = [
    "AGENTS.md",
    "core/kernel.md",
    "core/principles.md",
    "core/critique-loop.md",
    "core/critique-template.md",
    "core/commands.md",
    "core/taste-profile.md",
]


def version():
    return "v" + str(MANIFEST.get("version", "2.0.0"))


def full_files():
    files = list(CORE_BUNDLE)
    for cf in MANIFEST.get("core_files", []):
        if cf["path"] not in files:
            files.append(cf["path"])
    for mod in MANIFEST.get("modules", {}).values():
        if mod["entry"] not in files:
            files.append(mod["entry"])
        for extra in mod.get("extra_files", []):
            if extra not in files:
                files.append(extra)
    return files


def preface(full: bool, files: list[str]):
    scope = (
        "the full rule set: v2 kernel, core files, and every registered module (core-visual + optional-domain)"
        if full else
        "the v2 always-on kernel, core principles, proportional loop, critique template, commands, and taste-profile guide"
    )
    return (
        f"# creative-director: single-file prompt bundle ({'full' if full else 'core'}, {version()})\n\n"
        f"Generated copy of the creative-director rules ({REPO}, MIT licence) for chat assistants that cannot open files. "
        f"It holds {scope}.\n\n"
        "How to use it:\n"
        "- Start with the `AGENTS.md` and `core/kernel.md` sections. When they point to another file, use the matching heading below.\n"
        "- Python tools (`tools/cd.py`, `tools/autocheck.py`, `tools/compose.py`) cannot run in a chat without code execution. "
        "When tools are unavailable, run checks by eye and label estimates explicitly.\n"
        "- Always inspect the actual render or screenshot at real size, never a text description.\n"
        "- Taste calls belong to the owner of the work (`AES-12`).\n\n"
        "Files in this bundle: " + ", ".join(f"`{f}`" for f in files) + "\n"
    )


def bundle(full: bool):
    files = full_files() if full else CORE_BUNDLE
    parts = [preface(full, files)]
    for f in files:
        p = ROOT / f
        if not p.is_file():
            raise FileNotFoundError(f"manifest file missing: {f}")
        text = p.read_text(encoding="utf-8").strip()
        parts.append(f"\n\n---\n\n<!-- FILE: {f} -->\n## FILE: {f}\n\n{text}\n")
    return "".join(parts)


def main(argv):
    out = {
        "dist/creative-director-prompt.md": bundle(False),
        "dist/creative-director-prompt-full.md": bundle(True),
    }
    for path, text in out.items():
        assert "Fraunces" not in text, f"Fraunces leaked into {path}"
        tokens = round(len(text) / 4 / 100) * 100
        if "--check" not in argv:
            p = ROOT / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8", newline="\n")
        print(f"{path}  {len(text)/1024:.0f} KB  about {tokens:,} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
