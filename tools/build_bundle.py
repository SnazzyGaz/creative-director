#!/usr/bin/env python3
"""Build single-file prompt bundles for chat-only LLMs that can't read the repo's files.

    python3 tools/build_bundle.py            # writes dist/creative-director-prompt.md and dist/creative-director-prompt-full.md
    python3 tools/build_bundle.py --check    # rebuild in memory and check both build cleanly (for CI)

creative-director-prompt.md       AGENTS.md + the always-on core (principles, critique loop) + critique template + commands
creative-director-prompt-full.md  the above + the rest of core/ + every module README (no lookbook data, images or tools)

Paste or upload one as a system prompt, custom instructions or project knowledge. Each file keeps the repo's paths as
section headings, so "load core/critique-loop.md" means "use the section headed core/critique-loop.md". The output is
deterministic (no dates), so a rebuild with unchanged sources gives the same bytes. The rules live in the repo root;
these bundles are generated copies, published as release assets."""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = "https://github.com/SnazzyGaz/creative-director"
CORE = ["AGENTS.md", "core/principles.md", "core/critique-loop.md", "core/critique-template.md", "core/commands.md"]
REST = ["core/interaction-flow.md", "core/creative-direction.md", "core/first-principles.md", "core/brand-intake.md",
        "core/evidence.md", "core/which-modules.md"]
MODULES = ["technical-drawing", "character", "illustration", "composition", "colour-value", "layout", "typography",
           "brand", "web-ui", "ux", "3d", "aesthetic-critique", "lookbook"]


def version():
    m = re.search(r"^## (v[\d.]+)", (ROOT / "CHANGELOG.md").read_text(), re.M)
    return m.group(1) if m else "unversioned"


def preface(full: bool, files: list[str]):
    scope = ("the full rule set: core and every module" if full else
             "the always-on core, the critique template and the commands; modules are in the full bundle or the repo")
    return (f"# creative-director: single-file prompt bundle ({'full' if full else 'core'}, {version()})\n\n"
            f"This is a generated copy of the creative-director rules ({REPO}, MIT licence, Garyck Arntzen), for chat "
            f"assistants that can't open files. It holds {scope}.\n\n"
            "How to use it:\n"
            "- Follow the AGENTS.md section first. When it says to load a file, use the section below headed with that path. "
            "If a file it names isn't in this bundle, say so and work from what is here.\n"
            "- The Python tools (tools/autocheck.py and the others) can't run in a chat without code execution. Do those "
            "checks by eye, give estimates as estimates, and say the checks were done by eye.\n"
            "- You still need to see the actual work (an image, a screenshot at real size, or renders), not a description.\n"
            "- Taste calls go to the owner of the work.\n\n"
            "Files in this bundle: " + ", ".join(f"`{f}`" for f in files) + "\n")


def bundle(full: bool):
    files = CORE + (REST + [f"modules/{m}/README.md" for m in MODULES] if full else [])
    parts = [preface(full, files)]
    for f in files:
        text = (ROOT / f).read_text().strip()
        parts.append(f"\n\n---\n\n<!-- FILE: {f} -->\n## FILE: {f}\n\n{text}\n")
    return "".join(parts)


def main(argv):
    out = {"dist/creative-director-prompt.md": bundle(False), "dist/creative-director-prompt-full.md": bundle(True)}
    for path, text in out.items():
        assert "Fraunces" not in text
        tokens = round(len(text) / 4 / 100) * 100
        if "--check" not in argv:
            p = ROOT / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
        print(f"{path}  {len(text)/1024:.0f} KB  about {tokens:,} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
