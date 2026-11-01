# Prompt for an outside model judge

Use a **fresh chat** with no memory, project files or web browsing. Do not give the model this repository or its link. Attach the 12 images from [`pairs/`](pairs/) (pair-01.jpg to pair-12.jpg), then paste the prompt below. For the second pass, open another fresh chat, attach the 12 images from [`pairs-swapped/`](pairs-swapped/) and paste the same prompt.

Record the model name and version, the date, and which pass it was. Report model judges separately from people.

---

```text
You are judging 12 pairs of design images. Each attached image shows one pair: a one-line brief at the top and two versions, labelled A and B under each image. All images were made by an AI system. Judge only what you can see in the attached images. Do not search the web, do not look anything up, and do not guess how or by whom they were made.

For each pair, decide which version is stronger for its brief, taking into account what the piece is for, its audience, legibility, accuracy to the brief, and how good it looks. You may answer N if neither is good enough. A version's position (left or right) is not relevant.

Answer with exactly one line per pair, in this format, and nothing else:
pair | choice (A, B or N) | strength (strong or marginal) | reason (max 20 words)

Example:
01 | B | marginal | Clearer title at small size; the other has more atmosphere but weaker hierarchy.
```

---

The full briefs (longer than the one-line versions on the images) are in [`JUDGING.md`](JUDGING.md); human judges can use them, but give model judges the images only, so every model sees the same input.
