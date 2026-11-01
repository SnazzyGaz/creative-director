# Log: readme-self-critique

The repo's own loop, run on its README. Rendered with GitHub's markdown API plus github-markdown-css in headless Chrome (`render.sh`), at 1280 and 390 px. Images are built in code: `docs/assets/src/build.py`.

- r01: first design. One blocker: banner subtitle and loop labels unreadable on a phone (CORE-10, UI-10). Images flush against text, caption collides with the strip (CORE-5, UI-3). Usage table wraps badly at 390 (UI-2).
- r02: 3 fixes, all applied. Found a second cause for the caption collision (`<sub>` has line-height 0 on GitHub). Fixed a wrong label in the banner. Clearly better on phones. Stopped.
- Lesson: check at phone width. Every problem in this run was invisible at 1280.
