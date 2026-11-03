# Prompt for outside models

Use this only after the owner of the work has filled in their own sheet, so model answers can't colour theirs. Give each model the 38 sheet images (`S01.jpg` to `S38.jpg`) one at a time, in a fresh chat each, with the text below. Don't tell it which tool, skill or rules made the images, and don't show it the key, `briefs.json` or this repo. Record the model name and version in the `judge` column and `model` in `judge_type`.

---

You are judging design work for a client. The image shows one brief and two finished pieces made for it, each labelled with a four-letter ID under it.

Pick the one you would hand to the client for this brief. Judge the piece as a whole: does it do what the brief asks, is all the information correct and readable, is it well made, and would the intended audience respond to it? Don't reward length of text or number of details for their own sake.

Answer in exactly this format and nothing else:

```
preferred_id: <the four-letter ID, or SAME if you truly can't choose>
strength: <1 slight, 2 clear, 3 strong>
reason: <one sentence, at most 25 words>
```

---

**Notes for whoever runs it**

- One answer per sheet. Don't re-ask or regenerate to get a different answer; if the model refuses or answers in the wrong format, record `SAME` with the reason `no valid answer`.
- Models share blind spots with each other and with the image model, so their picks are reported separately and never outweigh the owner's.
- Nothing in this kit has been run on outside models yet.
