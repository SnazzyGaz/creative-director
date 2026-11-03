# Film: reviewing moving work

How to review a clip, sequence, edit, animatic or storyboard, and the template to report it. The general loop (`core/critique-loop.md`) still applies: evidence first, blockers first, at most a few fixes a round, owner's taste decides taste.

### FILM-REV-1. Watch it in motion, hands-on, before judging from frames (Procedure)
- **What:** Review in this order: (1) watch the whole piece at full speed, at the delivered size and device (phone for vertical social, a large screen for long-form), with sound, without stopping; (2) watch again, noting timecodes; (3) scrub cuts, moves and suspect moments frame by frame; (4) only then sample frames and run still-image checks on them.
- **Why:** Rhythm, performance, movement, sound and the feel of a cut exist only in motion; a contact sheet finds faults but can't judge them. Frame-only review over-rates composition and misses timing.
- **Check:** The critique says what was watched, how (size, device, sound on), how many times, and which timecodes were scrubbed. A critique made from stills alone says so and is marked partial.
- **Fix:** If you can't play the file, ask for it; don't judge motion from stills. For storyboards and animatics, play the animatic at its timing or read the board with the shot durations in hand.
- **Grade:** Procedure.
- **Source:** [S269, S280]; critique loop.

### FILM-REV-2. Make a shot list as you watch (Procedure)
- **What:** One line per shot: number, in and out timecode, duration, size, angle, movement, the beat it serves, and anything flagged. This is the evidence for FILM-EDIT-3, FILM-STORY-0 and FILM-STORY-5.
- **Why:** Pacing and coverage claims need numbers, not impressions.
- **Check:** Every shot has a line. Durations add up to the running time.
- **Fix:** Use shot-boundary detection to start the list (for example the ffmpeg scene filter in `generated.md`), then correct by eye.
- **Grade:** Procedure.
- **Source:** [S283, S285].

### FILM-REV-3. Storyboards and shot lists are reviewed as plans (Procedure)
- **What:** For a board or shot list, check what can be checked before anything is shot or generated: the beat per panel, coverage and the 180° plan (an overhead sketch), screen direction across panels, shot sizes against the beats, intended movement and durations, and where the cuts fall. Panel transitions follow ILL-7 and the illustration notes.
- **Why:** Fixing a crossed line or a missing reaction shot on paper is free.
- **Check:** Each panel has a beat, a size, a duration and a camera position on the overhead plan.
- **Fix:** Add, remove or re-order panels; re-plan coverage.
- **Grade:** Procedure.
- **Source:** [S271, S272].

---

## Film critique template

Copy, fill in, keep it short; drop sections that don't apply. It extends `core/critique-template.md`.

```markdown
## Film critique: <piece name>, round <n>

**Brief:** <purpose, audience, the one idea, delivery (platform, ratio, length, device), must-keeps>
**Beats (FILM-STORY-0):** <one line per scene or shot group: what changes, what the viewer should feel or know> [brief|inferred]
**How reviewed (FILM-REV-1):** <watched n× at size/device, sound on/off; timecodes scrubbed; frames sampled every x s; contact sheets made>
**Criteria judged against:** <rule IDs>

### Blockers (must be clean before delivery)
- Flashing (FILM-ACC-1): <pass / fail at timecode, measured how>
- Light within each continuous scene (FILM-LIT-1): <pass / fail, shots>
- Identity (FILM-GEN-2) · anatomy on sampled frames (FILM-GEN-3, CHAR-9) · invented text (FILM-GEN-8): <pass / fail / n.a., with frame and region>
- Text size and contrast on the worst frame (FILM-TXT-1, TYPE-3, UI-6): <pass / fail>

### The beat check (FILM-STORY-0)
| Beat / shot | Choice | Serves / neutral / fights | Note |
|---|---|---|---|

### Shot list (FILM-REV-2), short form
| # | In-out | Dur | Size / angle / move | Beat | Flags |
|---|---|---|---|---|---|

### Continuity and cutting
- 180° and 30° (FILM-CON-1, FILM-CON-2): <cuts that cross or jump; intended?>
- Eyelines, screen direction, match on action (FILM-CON-3 to FILM-CON-5)
- Eye-trace across cuts (FILM-EDIT-2): <cuts where focus jumps with no cue>
- Pace (FILM-EDIT-3): <average shot length per section; does it follow intensity?>

### Light, colour, sound
- Key side and ratio per scene (FILM-LIT-1, FILM-LIT-3) · motivation (FILM-LIT-2)
- Shot matching and skin (FILM-COL-1, FILM-COL-2) · colour script strip read (FILM-STORY-3)
- Dialogue, loudness, sync (FILM-SND-1, FILM-SND-2) · music and silence against the beat (FILM-STORY-7, FILM-STORY-8)

### Key frames (still-image checks; sampled, not the whole review)
- <frame timecode>: look tests and Sitting right flags (COMP-19 to COMP-25: FLAG only, nothing centred to clear a flag)

### Needs improvement (ranked, biggest first, max 5)
1. [BLOCKER|IMPROVEMENT] <RULE-ID> at <timecode>: <evidence>. Fix: <smallest effective change>.

### Deliberate exceptions
- <RULE-ID>: broken on purpose because <beat or brief>.

### Questions for the owner of the work
- <taste or story choices no rule settles>
```
