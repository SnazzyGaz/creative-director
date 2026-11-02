#!/usr/bin/env python3
"""Fold a lookbook batch from a breeder folder into modules/lookbook/. Copy, filter, name check, in one step.

    python3 tools/lookbook_sync.py BREEDER_ROOT [--scan FILE ...] [--dry-run]
    python3 tools/lookbook_sync.py BREEDER_ROOT --check-only [--scan FILE ...]

BREEDER_ROOT holds SHARE_MANIFEST.txt and lookbook/ (looks.json, public_terms.py, index.png, sheets/).
What it does:
  1. Copies only files listed in SHARE_MANIFEST.txt: each sheet's 1200 px `_small.jpg` (saved as sheets/<name>.jpg)
     and index.png. Never anything under research/ or named PRIVATE_*.
  2. Filters looks.json to rows with share_safe = yes and status = live; drops internal fields (render, share_safe);
     points `sheet` at the copied file. Writes looks.json and looks.csv.
  3. Keeps a cumulative `retired` list (ID, date, short note): IDs already retired here stay retired even if the export
     drops them, and a live ID that matches a retired one stops the sync. A live ID that vanishes without being retired
     also stops it.
  4. Name check: every text in modules/lookbook/ (plus any --scan files) against the breeder's banned list
     (lookbook/public_terms.py BANNED). The list itself is read at run time and never copied into this repo.
Exit 1 on any name hit or ID problem; nothing is written in that case."""
import argparse, csv, io, json, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MOD = ROOT / "modules/lookbook"
DROP = {"render", "share_safe"}
TEXT_EXT = {".md", ".json", ".csv", ".txt", ".py"}

def banned_patterns(breeder):
    src = (breeder / "lookbook/public_terms.py").read_text()
    ns = {}
    exec(compile(src, "public_terms.py", "exec"), ns)          # read-only: no bytecode written to the breeder folder
    return [re.compile(p) for p in ns["BANNED"]]

def hits(text, pats):
    return sorted({m.group(0) for p in pats for m in p.finditer(text)})

def load_manifest(breeder):
    rows = [l.strip() for l in (breeder / "SHARE_MANIFEST.txt").read_text().splitlines() if l.strip() and not l.startswith("#")]
    bad = [r for r in rows if "research/" in r or "PRIVATE" in r]
    if bad: sys.exit(f"manifest lists private files, refusing: {bad}")
    return set(rows)

def retired_note(status):
    m = re.match(r"retired \(([\d-]+)\);?\s*(.*)", status)
    date, note = (m.group(1), m.group(2)) if m else ("", status)
    note = re.sub(r"\s*\([^)]*\)", "", note).strip()          # drop internal parentheticals
    note = re.sub(r"(LB-[\w]+) [A-Z][\w-]*(?: [A-Z][\w-]*)*", r"\1", note)   # keep IDs, not names
    return date, note

def build(breeder, scan_extra, dry):
    pats = banned_patterns(breeder)
    manifest = load_manifest(breeder)
    src = json.loads((breeder / "lookbook/looks.json").read_text())

    # images: only manifest entries
    sheets = {}   # breeder sheet path (png, as cited in looks.json) -> repo name
    for p in sorted(manifest):
        m = re.fullmatch(r"lookbook/sheets/(.+)_small\.jpg", p)
        if m: sheets[f"lookbook/sheets/{m.group(1)}.png"] = f"sheets/{m.group(1)}.jpg"
    if "lookbook/index.png" not in manifest: sys.exit("index.png not in SHARE_MANIFEST.txt")

    old = json.loads((MOD / "looks.json").read_text()) if (MOD / "looks.json").exists() else {"looks": [], "retired": []}
    retired = {r["id"]: r for r in old.get("retired", [])}
    live, problems = [], []
    for l in src["looks"]:
        if l.get("status") != "live":
            if l["id"] not in retired:
                d, n = retired_note(str(l.get("status", "")))
                retired[l["id"]] = {"id": l["id"], "retired": d, "note": n}
            continue
        if l.get("share_safe") != "yes": continue
        row = {k: v for k, v in l.items() if k not in DROP}
        if l["sheet"] not in sheets: problems.append(f"{l['id']}: sheet {l['sheet']} not shareable")
        row["sheet"] = sheets.get(l["sheet"], "")
        live.append(row)
    ids = [r["id"] for r in live]
    if len(ids) != len(set(ids)): problems.append("duplicate live IDs")
    clash = set(ids) & set(retired)
    if clash: problems.append(f"live IDs reuse retired IDs: {sorted(clash)}")
    vanished = {r["id"] for r in old["looks"]} - set(ids) - set(retired)
    if vanished: problems.append(f"IDs dropped without retirement: {sorted(vanished)}")

    out = {
        "about": "Lookbook tag file: one row per live look. Filter here (tools/lookbook_find.py), then open only the listed sheet. "
                 "Every example image is our own render from that look's rules. Optional reference, never a rule source.",
        "batch": src.get("batch"),
        "generated_by": "tools/lookbook_sync.py from the breeder export (see modules/lookbook/UPDATING.md)",
        "paths_relative_to": "modules/lookbook/",
        "counts": {"live": len(live), "established": sum(r["kind"] == "established" for r in live),
                   "keepers": sum(r["kind"] == "keeper" for r in live),
                   "partial": [r["id"] for r in live if r.get("read_status") == "partial"], "retired": len(retired)},
        "scales": src.get("scales", {}),
        "fields": [f for f in src.get("fields", []) if f not in DROP],
        "looks": live,
        "retired": sorted(retired.values(), key=lambda r: r["id"]),
    }
    js = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    cols = [c for c in live[0] if c != "hallmarks"]
    hl = list(live[0]["hallmarks"])
    buf = io.StringIO(); w = csv.writer(buf)
    w.writerow(cols[:cols.index("hint")] + [f"hl_{h}" for h in hl] + cols[cols.index("hint"):])
    flat = lambda v: "; ".join(map(str, v)) if isinstance(v, list) else v
    for r in live:
        vals = [flat(r[c]) for c in cols]
        i = cols.index("hint")
        w.writerow(vals[:i] + [r["hallmarks"].get(h, "") for h in hl] + vals[i:])
    cs = buf.getvalue()

    # name check over everything text that will sit in the module, plus extra files
    texts = {"looks.json": js, "looks.csv": cs}
    for p in MOD.glob("*"):
        if p.suffix in TEXT_EXT and p.name not in texts: texts[p.name] = p.read_text()
    for f in scan_extra: texts[f] = pathlib.Path(f).read_text()
    bad = {k: h for k, t in texts.items() for h in [hits(t, pats)] if h}
    for k, h in bad.items(): print("NAME HIT", k, h)
    for p in problems: print("ID PROBLEM", p)
    print(f"name check: {len(texts)} texts, {sum(len(h) for h in bad.values())} hits")
    if bad or problems: sys.exit(1)
    if dry:
        print(f"dry run: {len(live)} live looks, {len(sheets)} sheets, {len(retired)} retired IDs"); return

    (MOD / "sheets").mkdir(parents=True, exist_ok=True)
    keep = set()
    for png, name in sheets.items():
        small = breeder / png.replace(".png", "_small.jpg")
        shutil.copyfile(small, MOD / name); keep.add(MOD / name)
    for p in (MOD / "sheets").glob("*"):
        if p not in keep: p.unlink()                       # sheets that left the manifest leave the repo too
    shutil.copyfile(breeder / "lookbook/index.png", MOD / "index.png")
    (MOD / "looks.json").write_text(js)
    (MOD / "looks.csv").write_text(cs)
    size = sum(p.stat().st_size for p in MOD.rglob("*") if p.is_file())
    print(f"synced: {len(live)} live looks, {len(sheets)} sheets, {len(retired)} retired IDs, module {size/1e6:.1f} MB")

def check_only(breeder, scan_extra):
    pats = banned_patterns(breeder)
    files = [p for p in MOD.rglob("*") if p.suffix in TEXT_EXT] + [pathlib.Path(f) for f in scan_extra]
    bad = {str(p): h for p in files for h in [hits(p.read_text(), pats)] if h}
    for k, h in bad.items(): print("NAME HIT", k, h)
    print(f"name check: {len(files)} files, {sum(len(h) for h in bad.values())} hits")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("breeder", type=pathlib.Path)
    ap.add_argument("--scan", nargs="*", default=[], help="extra repo files to name-check (README, CHANGELOG, ...)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check-only", action="store_true", help="only run the name check on what is already here")
    a = ap.parse_args()
    check_only(a.breeder, a.scan) if a.check_only else build(a.breeder, a.scan, a.dry_run)
