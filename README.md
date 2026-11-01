# creative-director

Design judgement for AI bots. This repo helps a bot improve its own visual output (3D models, drawings, generated images, web and app UI, UX flows) by nudging it toward what people measurably prefer.

It is a **light touch, not a rebuild**: keep the work's intent and what already works, make the smallest high-impact fixes (about three per round), and stop once it is clearly better. Only **MUST-BE-RIGHT** errors (perspective, anatomy, light, contrast and accessibility, broken flows, 3D build defects) are treated as blockers.

"Human-preferred" is grounded in evidence where possible: people judge visual appeal within about 50 ms [S36], lower visual complexity predicts better first impressions [S35], easy-to-perceive work (clear figure-ground, symmetry, grouping) is liked more [S37], and attractive interfaces are perceived as easier to use, though looks don't excuse serious problems [S34]. Popular claims that don't hold up, such as the golden ratio and the rule of thirds as a law, are listed in `core/evidence.md` so bots stop repeating them. Where no evidence or rule decides, the question goes to Gaz (Garyck Arntzen), whose taste is the final word.

It is written for bots, but a person should be able to read any page in two minutes.

## How a bot uses it

1. Read `core/principles.md` once per session, and `core/creative-direction.md` when taking a brief. These rules apply to everything.
2. Open `core/which-modules.md` and load only the modules the task needs.
3. Make the work, then run the loop in `core/critique-loop.md`: render, look, critique, fix (up to ~3 changes), re-render.
4. Write each critique with `core/critique-template.md`: neutral, factual, every point tied to a rule ID, ranked biggest first.
5. Stop when it is clearly better or the loop says so, and hand to Gaz. Never claim the work is "done" on taste alone.

## Usage: three ways to plug it in

Pick the lightest one that fits the job. All three use the same rules, so results stay consistent whoever does the checking.

### 1. Self-check (cheapest)
Add a line to a bot's instructions, or to a single request:

> `+ creative director` (or "use the creative-director skill")

The bot reads `core/`, loads the modules `core/which-modules.md` points to, and runs the loop on its own output: brief check, render, five look tests, critique against rule IDs, up to 3 fixes, re-render, stop when clearly better. Anything only a human can decide goes under "Questions for Gaz".

### 2. Consult (a second pair of eyes)
> `consult creative director`

Send the creative-director bot the brief plus the render, screenshot or file. It returns a neutral critique using `core/critique-template.md`: criteria judged, what meets them, ranked fixes, questions for Gaz. The maker applies the fixes and can send it back for one more look. Use this when the work matters.

### 3. Direct (for bigger jobs)
> `creative director: direct this`

The creative director joins at the start: writes the six-line brief (CD-1), sets the direction once (mood words, do/don't list, base colours and type, CD-2), asks for 2-3 rough options and picks one (CD-3), then reviews at checkpoints until the brief is met (CD-6).

### What to send
- The brief, or at least: what it is, who it's for, where and how big it's seen, what must stay.
- The actual output (image file, screenshot at real size, URL, or model renders). Never just a description.

## Using it with other AI tools

The repo works with any agent that can read files. Each tool finds its entry point automatically:

| Tool | Entry point |
|---|---|
| Cursor | `.cursor/rules/creative-director.mdc` and `AGENTS.md` |
| Claude Code / Claude Agent Skills | `CLAUDE.md`, `SKILL.md` (copy the repo into your skills folder) |
| OpenAI Codex, Gemini CLI, Jules, others | `AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| ChatGPT custom GPTs, Claude Projects, Gemini Gems | Upload `AGENTS.md`, `core/` and the modules you need as knowledge files, and paste the "How to use it" steps from `AGENTS.md` into the instructions |
| Anything that reads `llms.txt` | `llms.txt` |

All entry points point back to `AGENTS.md`, so there is one set of instructions to maintain.

## Rule format

Every rule has an ID (e.g. `CORE-2`, `TD-PER-1`, `UI-6`) that critiques cite, and the same five parts:

- **What**: the rule in one line.
- **Why**: what goes wrong without it.
- **Check**: a test you can actually run or look for.
- **Fix**: the usual remedy.
- **Source**: where the idea comes from (full list in `SOURCES.md`).

Technical-drawing rules are also tagged **MUST-BE-RIGHT** (an error here is a mistake, not a style choice) and say whether a tool could check them automatically.

## Folder map

```
creative-director/
  README.md              this file
  PROPOSED-REPO.md       what the GitHub repo should look like (draft, not created yet)
  SOURCES.md             every source cited, with links
  core/
    creative-direction.md brief, direction, options, feedback style, done-ness (CD-1..6)
    principles.md        shared rules: hierarchy, contrast, value, spacing, alignment, colour, type, restraint, balance
    evidence.md          what preference research supports, and the myths to stop citing
    critique-loop.md     render -> look -> critique -> fix -> re-render, and when to stop
    critique-template.md fill-in critique format
    which-modules.md     task type -> modules to load
  examples/              stress tests: before/after runs of the loop
  tools/                 look sheet, WCAG contrast, screenshots, before/after, VP line-fit, ellipse check (+ README.md)
  modules/
    technical-drawing/   perspective, cone of vision, proportion, light and shadow, ellipses
    illustration/        composition, focal point, shape, value, colour, edges, story, mood, gesture, generic AI image look (+ notes.md)
    web-ui/              type, spacing, grid, components, colour roles, contrast, resize, generic AI look (+ notes.md)
    ux/                  flows, feedback timing, errors, defaults, signifiers, target size, heuristics
    3d/                  model-qa and bot-creative-toolkit, silhouette, lighting ratios, PBR ranges, view transform

Each module README ends with **Myths and weak claims**. `notes.md` files hold optional depth.
```

## Ground rules for bots using this repo

- Paraphrase; never paste other people's text or images into the work or the critique.
- Be specific and neutral. Name the spot ("the left third", "the second button"), the evidence, the rule ID, and the fix.
- Preserve intent. Improve the work the bot made; don't replace it with a different idea.
- Rules are defaults, not laws. Breaking one on purpose is fine if you can say why. Breaking one by accident is the thing to catch.

## Licence

MIT, see [LICENSE](LICENSE). Cited works remain their authors' copyright; this repo paraphrases and links to them.
