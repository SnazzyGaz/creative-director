# Before and after across domains

These are illustrations, not test evidence. Each pair comes from one sample on each side, made and critiqued by the agent that ran the loop. The owner of the work saw ten pairs and picked six for the README. The other four were left out, so these six are a chosen set, not a fair sample. For the evidence, see the [blind test](../blind-test/RESULTS.md).

**How each pair was made** (v0.9.7, one image model for both sides):
- **Baseline:** the brief pasted in as is, with the first output kept.
- **Creative Director v0.9.7:** the full loop. This means routing with [`which-modules`](../../core/which-modules.md), a plan (mood line, hierarchy, value plan, exact copy with "no other words"), a render, `tools/autocheck.py` and the look tests, a critique with rule IDs, and at most two fix rounds. The best render was kept.

Every brief uses an invented name and exact copy.

| Pair | Brief (exact copy) | Rules that fired on the baseline | Rounds and notes on the rules version |
|---|---|---|---|
| [01 Book cover](01-book-cover.jpg) | A literary novel about a family keeping an apple orchard alive on a flooding coast. "The Salt Orchard", "Mara Quell". | CD-7, AES-10: "A LITERARY NOVEL" and a tagline were invented. LAY-16, LAY-15: the title sits over a busy tree and the author name over grass. EN-2: a figure seen from behind, a cliché. | 1 round. Autocheck failed LAY-10 on the empty sky and water. This was judged to be named space that holds the type. The symmetry is intended (COMP-17). |
| [02 Packaging label](02-packaging-label.jpg) | A 340 g jar of raw wildflower honey. "Hollow Pine", "Raw Wildflower Honey", "340 g". | BRAND-10: no brand mark. COMP: a scene, a hive and mixed scripts all compete. | 2 rounds. The first was too sterile (EN-3), and its honeycomb cell looked like a sticker. The fix adds a honey drip to the hollow (BRAND-9) and a hand-cut wordmark arched with the label. |
| [04 Character design](04-character-design.jpg) | Pip, a nine-year-old inventor, mascot for a children's science club. Goggles up, screwdriver in her right hand, a tool belt. | BRAND-8, AES-10: an invented "SCIENCE CLUB" text and a gear logo. | 1 round. The anatomy pass (CHAR-9) found no faults on hands, feet or face. The pose shows her traits (CHAR-6). The props are as briefed (CHAR-11). |
| [06 Logo](06-logo.jpg) | A café with a pottery studio where people paint mugs. "Kettle & Kiln". | CD-7: an invented tagline. BRAND-9: three literal icons side by side. | 2 rounds. The first had thin brick lines that broke up at 16 px and a cramped "&". The fix is a stacked lockup in bold shapes. |
| [08 Event poster](08-event-poster.jpg) | "Northlight Jazz Night", "Friday 14 March, 8 pm", "The Ferry Room, Quay Street", "Tickets £12". | BRAND-9 and EN-2 item 8: a stock saxophone, with the name's idea unused. | 2 rounds. In the first, the title touched the top edge (LAY-5). The baseline was already strong; this version is more distinctive, not a rescue. |
| [09 Exploded view](09-product-illustration.jpg) | The Brightwell desk lamp. Five labels: "Base", "Arm", "Hinge", "Shade", "LED module". | CD-7: an invented title, part descriptions and materials. Construction: parts were off one axis, and the LED module was square in a round shade. | 1 round. One assembly axis and one light (TD-PER, TD-LIT). Only the five labels. |

Every word in these images was rendered by the image model, not set in code. Every string was checked letter for letter against the brief (CD-7).
