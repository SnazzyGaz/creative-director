# Installing creative-director in any agent

The rules are plain Markdown. Any agent or LLM that can read text can use them. There are three ways in, from most capable to most basic:

1. **As a skill.** [`skills/creative-director/`](../skills/creative-director/) is a self-contained skill in the open [Agent Skills format](https://agentskills.io/specification) (`SKILL.md` with `name` and `description`, plus `core/`, `modules/`, `lite/`, the design tools and the font catalogue; about 0.8 MB, no images). The agent sees only the name and description until a visual task comes up, then loads the rest. Most current agents read this format.
2. **As project instructions.** Open this repo, or a project that includes it, and the agent reads [`AGENTS.md`](../AGENTS.md) (or its own pointer file: `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/creative-director.mdc`). Every pointer file leads to `AGENTS.md`, which is the single source of instructions.
3. **As one pasted file.** For chat assistants with no file access: a single-file bundle from the [latest release](https://github.com/SnazzyGaz/creative-director/releases/latest) (see [Any other LLM](#any-other-llm-or-chat-assistant)).

The skill folder and the bundles are generated from the root files by [`tools/package_skill.py`](../tools/package_skill.py) and [`tools/build_bundle.py`](../tools/build_bundle.py). Edit the root files, never the generated copies; `python3 tools/package_skill.py --check` fails if the skill folder is out of date, and a GitHub Action runs it on every push.

**What every setup needs:** a model that can see images, and a way to render or screenshot the work at real size. The Python tools are optional (see [Tools](#optional-python-tools)).

## Quick reference

| Agent | Skill location it reads | Instruction file it reads | Fastest install |
|---|---|---|---|
| Hermes Agent | `~/.hermes/skills/`, `.hermes/skills/`, `.agents/skills/` | `.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules` | `hermes skills install SnazzyGaz/creative-director/skills/creative-director` |
| Claude Code | `~/.claude/skills/`, `.claude/skills/` | `CLAUDE.md` (imports `AGENTS.md`), or `AGENTS.md` | `gh skill install SnazzyGaz/creative-director creative-director --agent claude-code --scope user` |
| claude.ai, Claude desktop | uploaded zip | — | Upload [the skill zip](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-skill.zip) |
| OpenAI Codex | `~/.agents/skills/`, `.agents/skills/` | `AGENTS.md` | `gh skill install SnazzyGaz/creative-director creative-director --agent codex --scope user` |
| Cursor | `~/.cursor/skills/`, `~/.agents/skills/`, `.cursor/skills/`, `.agents/skills/` | `AGENTS.md`, `.cursor/rules/*.mdc` | `gh skill install SnazzyGaz/creative-director creative-director --agent cursor --scope user` |
| Gemini CLI | `~/.gemini/skills/`, `~/.agents/skills/`, `.gemini/skills/`, `.agents/skills/` | `GEMINI.md` (imports `AGENTS.md`) | `gemini skills install https://github.com/SnazzyGaz/creative-director.git --path skills/creative-director` |
| GitHub Copilot | `~/.copilot/skills/`, `~/.agents/skills/`, `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `.github/copilot-instructions.md`, `AGENTS.md` | `gh skill install SnazzyGaz/creative-director creative-director` |
| Devin Local, Windsurf | `~/.config/devin/skills/`, `~/.agents/skills/`, `.devin/skills/`, `.windsurf/skills/`, `.agents/skills/` | `AGENTS.md` | `gh skill install SnazzyGaz/creative-director creative-director --agent devin --scope user` |
| Cline | `.cline/skills/` | `AGENTS.md`, `.clinerules/` | `gh skill install SnazzyGaz/creative-director creative-director --agent cline` |
| Aider | — | files passed with `--read` | `aider --read AGENTS.md` |
| Grok Bot | built in | — | [One-click bot](https://x.ai/bot/XWBKgRnDOw7uR5SpKx3Af) |
| Anything else | `~/.agents/skills/` if it reads skills | `AGENTS.md` if it reads it | `npx skills add SnazzyGaz/creative-director` or a [prompt bundle](#any-other-llm-or-chat-assistant) |

`~/.agents/skills/` is the shared folder that Codex, Cursor, Gemini CLI, GitHub Copilot and Devin all read, so one copy there serves all of them. Hermes reads it too once you add it as an external directory (below).

## Hermes Agent (Nous Research)

Hermes uses the Agent Skills format and keeps skills in `~/.hermes/skills/` [H1].

**Install the skill from GitHub** (runs Hermes's security scan, then installs):

```bash
hermes skills install SnazzyGaz/creative-director/skills/creative-director
```

Or add the repo as a tap, then search and install from it (taps read `skills/` by default) [H1]:

```bash
hermes skills tap add SnazzyGaz/creative-director
hermes skills install SnazzyGaz/creative-director/skills/creative-director
```

Hermes downloads the whole skill folder from GitHub [H3]. The skill has no high-severity findings in Hermes's scanner, so community-trust installs aren't blocked. Update later with `hermes skills check` and `hermes skills update`.

**Use it:** Hermes lists it by name and description and loads it when a task matches. To load it on purpose, type `/creative-director` followed by the request, for example `/creative-director consult on this poster` with the image attached [H1].

**Share one copy with other agents:** if you keep skills in `~/.agents/skills/` (for example, after a `gh skill` or `npx skills` install for Codex or Cursor), point Hermes at it in `~/.hermes/config.yaml` [H1]:

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
```

**Working inside this repo:** Hermes loads `AGENTS.md` from the working directory as project context [H2], so a Hermes session started in a clone of this repo follows the rules with no install.

## Claude

**Claude Code.** Personal skills live in `~/.claude/skills/<name>/SKILL.md`, project skills in `.claude/skills/<name>/SKILL.md` [C1]. Either:

```bash
gh skill install SnazzyGaz/creative-director creative-director --agent claude-code --scope user
# or, without gh:
curl -L -o /tmp/cd.zip https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-skill.zip
unzip /tmp/cd.zip -d ~/.claude/skills/
```

Inside this repo, Claude Code reads `CLAUDE.md`, which imports `AGENTS.md` with `@AGENTS.md`, the pattern Anthropic recommends for sharing one file with other tools [C2].

**claude.ai and the Claude desktop app.** Turn on *Code execution and file creation* in Settings > Capabilities. Then go to Customize > Skills, click **+**, choose **+ Create skill**, then **Upload a skill**, and upload [`creative-director-skill.zip`](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-skill.zip). Toggle it on. On Team and Enterprise plans an owner may need to allow skills first [C3].

**Claude Projects.** Upload `dist/creative-director-prompt.md` from the latest release as project knowledge (or the full bundle for every module).

## OpenAI Codex

Codex reads skills from `~/.agents/skills/` (personal) and `.agents/skills/` (repo), and instructions from `AGENTS.md` [O1, O2]. Install with `gh skill` (above), or copy the folder:

```bash
git clone --depth 1 https://github.com/SnazzyGaz/creative-director /tmp/cd
mkdir -p ~/.agents/skills && cp -r /tmp/cd/skills/creative-director ~/.agents/skills/
```

Use it with `$creative-director` or `/skills`, or let Codex pick it when a task matches [O1]. Inside this repo Codex reads `AGENTS.md` directly. Codex's default cap on combined instruction files is 32 KiB [O2]. `AGENTS.md` alone is about 5 KB, and the core files are loaded on demand, so it fits.

## Cursor

Cursor loads skills from `.agents/skills/`, `.cursor/skills/`, `~/.agents/skills/` and `~/.cursor/skills/`, and also from the Claude and Codex skill folders [U1]. Use the `gh skill` line above or the copy step from Codex. Inside this repo, Cursor reads `AGENTS.md` and the rule `.cursor/rules/creative-director.mdc`, which points to it [U2].

## Gemini CLI

Gemini CLI reads skills from `~/.gemini/skills/`, `~/.agents/skills/`, `.gemini/skills/` and `.agents/skills/`, and can install them from a Git repository [G1]:

```bash
gemini skills install https://github.com/SnazzyGaz/creative-director.git --path skills/creative-director
```

`--path` points at the skill inside the repo; add `--consent` to skip the confirmation prompt [G1]. Check it with `/skills list`. Inside this repo, Gemini CLI reads `GEMINI.md`, which imports `AGENTS.md` [G2]. To have Gemini read `AGENTS.md` in your own projects, set `"context": {"fileName": ["AGENTS.md", "GEMINI.md"]}` in `.gemini/settings.json` [G2].

## GitHub Copilot

Copilot (CLI, cloud agent, and agent mode in VS Code, Visual Studio and JetBrains) reads skills from `.github/skills/`, `.claude/skills/` or `.agents/skills/` in a repo, and from `~/.copilot/skills/` or `~/.agents/skills/` [P1]:

```bash
gh skill install SnazzyGaz/creative-director creative-director                       # this project, for Copilot
gh skill install SnazzyGaz/creative-director creative-director --scope user --agent github-copilot
```

`gh skill` installs the latest tagged release by default. Pin one with `--pin v0.8.2`. For repository instructions, Copilot reads `.github/copilot-instructions.md`, and its cloud agent also reads `AGENTS.md` [P2].

## Devin Local and Windsurf

Devin Local, in Devin Desktop (Windsurf's docs now lead here), reads `AGENTS.md` as always-on rules. It reads skills from `.devin/skills/`, `.agents/skills/`, the legacy `.windsurf/skills/`, `~/.config/devin/skills/` and `~/.agents/skills/` [W1]. Use `gh skill install ... --agent devin`, or copy the folder into one of those.

## Cline, Aider and others

- **Cline:** project skills in `.cline/skills/`; it also reads `AGENTS.md` as rules [L1]. `gh skill install SnazzyGaz/creative-director creative-director --agent cline`.
- **Aider:** no skill system. Load the rules read-only with `aider --read AGENTS.md --read core/principles.md --read core/critique-loop.md`, or add a `read:` list to `.aider.conf.yml` [A1].
- **Everything else that reads skills** (OpenCode, Goose, Amp, Kiro, Qwen Code, Roo Code, Junie, OpenHands and many more): `npx skills add SnazzyGaz/creative-director` asks which agents to install to [V1], and `gh skill install` lists its supported agents with `gh skill install --help`.

## Grok Bot

One click: [Creative Director bot](https://x.ai/bot/XWBKgRnDOw7uR5SpKx3Af). It installs a bot with the creative-director skill that reads the current rules from this repo.

## Any other LLM or chat assistant

For ChatGPT custom GPTs or projects, Gemini Gems, Claude Projects, Le Chat, local models in a chat UI, or anything with no file access:

| File | What it holds | Size |
|---|---|---|
| [`creative-director-prompt.md`](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-prompt.md) | `AGENTS.md`, principles, critique loop, critique template, commands | about 9,000 tokens |
| [`creative-director-prompt-full.md`](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-prompt-full.md) | the above, the rest of `core/`, and every module | about 81,000 tokens |
| [`lite/CREATIVE-DIRECTOR-LITE.md`](../lite/CREATIVE-DIRECTOR-LITE.md) | the loop, core rules and blockers, hand-written short version | about 3,100 tokens |

Paste one into the system prompt or custom instructions, or upload it as knowledge. Each bundle keeps the repo's file paths as section headings, so "load `core/critique-loop.md`" points at a section in the same file. The bundle tells the model that the Python checks can't run in a plain chat, so it does them by eye and says so. Rebuild the bundles yourself with `python3 tools/build_bundle.py`; the output has no dates, so unchanged sources give identical files.

For a model that can browse but not hold files, give it the raw URL of `AGENTS.md` (`https://raw.githubusercontent.com/SnazzyGaz/creative-director/main/AGENTS.md`) and ask it to follow it. That is how the Grok Bot skill works. [`llms.txt`](../llms.txt) lists every file for tools that read it.

## Optional Python tools

The skill carries the measuring scripts in `tools/`. They need Python 3:

```bash
pip install -r tools/requirements.txt     # Pillow, NumPy, OpenCV; trimesh, rtree, manifold3d for 3D; Playwright
playwright install chromium               # only for page checks (autocheck.py on a URL or HTML file, shot.sh)
python3 tools/autocheck.py poster.png     # run from the skill or repo folder
```

`autocheck.py` checks images with Pillow and NumPy alone. It needs Playwright only for pages. If an agent can't run code, it does the checks by eye and says so. The maintainer scripts (lookbook sync, packaging) and the test suites stay in the repo and aren't in the skill.

## Updating

- **Skill installs:** `hermes skills update`, `gh skill update`, `npx skills update`, or re-copy the folder from a fresh clone.
- **Zip and bundles:** download again from the [latest release](https://github.com/SnazzyGaz/creative-director/releases/latest).
- **Maintainers:** after changing a rule, run `python3 tools/package_skill.py` and `python3 tools/build_bundle.py`, commit `skills/creative-director/`, and attach the zip and both bundles to the release.

## Sources

Checked 3 November 2026.

- [H1] Hermes Agent, *Skills System*: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- [H2] Hermes Agent, *Context Files*: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
- [H3] Hermes Agent source, `tools/skills_hub_github.py` (GitHub installs download the full skill directory) and `tools/skills_guard.py` (install policy): https://github.com/NousResearch/hermes-agent
- [S1] Agent Skills specification: https://agentskills.io/specification
- [C1] Claude Code, *Extend Claude with skills*: https://code.claude.com/docs/en/skills
- [C2] Claude Code, *How Claude remembers your project* (CLAUDE.md, AGENTS.md, `@` imports): https://code.claude.com/docs/en/memory
- [C3] Anthropic, *Use skills in Claude*: https://support.claude.com/en/articles/12512180-use-skills-in-claude
- [O1] OpenAI, *Build skills* (Codex skill locations): https://learn.chatgpt.com/docs/build-skills
- [O2] OpenAI, *Custom instructions with AGENTS.md*: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- [U1] Cursor, *Agent Skills*: https://cursor.com/docs/skills
- [U2] Cursor, *Rules*: https://cursor.com/docs/rules
- [G1] Gemini CLI, *Agent Skills*: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- [G2] Gemini CLI, *Provide context with GEMINI.md files*: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- [P1] GitHub Docs, *About agent skills*: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- [P2] GitHub Docs, *Support for different types of custom instructions*: https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/custom-instructions-support
- [W1] Devin, *Devin Local Customizations*: https://docs.devin.ai/desktop/devin-local/customizations
- [L1] Cline, *Skills*: https://docs.cline.bot/customization/skills
- [A1] Aider, *Specifying coding conventions*: https://aider.chat/docs/usage/conventions.html
- [V1] vercel-labs/skills, *Creating skills* (discovery paths, supported agents): https://github.com/vercel-labs/skills
