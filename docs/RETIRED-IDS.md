# Retired and moved IDs

Rule IDs are never reused. When a rule moves or merges, its old ID is retired here and stays reserved, so older critiques, examples and test notes that cite it can still be followed. Until v0.9.7 each retired ID also kept a one-line "Moved to" stub in its module; those stubs now live only in this table.

| Old ID | Now | Since |
|---|---|---|
| UI-1 (one type scale) | TYPE-2 | v0.6.0 |
| UI-2 (size, measure, leading, ragged right) | TYPE-3, TYPE-4, TYPE-5, TYPE-13 | v0.6.0 |
| UI-3 (spacing scale) | CORE-4 | v0.6.0 |
| ILL-4 (value plan, notan, palette) | CV-1, CV-2, CV-5 | v0.6.0 |
| ILL-9 (colour in place, one colour of light) | CV-4, CV-7 | v0.6.0 |
| COMP-7 (empty space) | COMP-23 | v0.6.0 |
| COMP-21 (what makes weight) | COMP-2 | v0.6.0 |
| TD-CON-2 (gesture before structure) | ILL-10 | 1 Nov 2026 |
| INF-3 (each step looks different, and the steps flow) | LAY-18 | v0.9.7 |

**Other reserved numbers.** Source IDs: SRC-33 is retired, and before v0.9.7 sources were cited as `[Sn]` (now `[SRC-n]`, same numbers; bare S-numbers such as S88 are blind-test sheets). Lookbook IDs: retired looks are in the `retired` list of `modules/lookbook/looks.json` and are never reused (`modules/lookbook/UPDATING.md`); unused numbers such as LB-139 are draft rejects that never went live.
