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
  4. Derived fields, computed here so every batch gets them (all read-only on the breeder folder):
     - nearest_looks: the 3 most similar live looks, by cosine similarity of the breeder's cached image embeddings of
       each look's render (lookbook/.dedup_cache/emb.npz, keyed by the render file's SHA-1). The breeding parents a
       keeper used to carry in that field move to bred_from.
     - colours: 3-5 dominant colours of the render as hex, largest share first (k-means in CIELAB, seeded).
     - getty_aat: for established looks listed in modules/lookbook/getty_aat.json (hand-verified Getty AAT Styles and
       Periods terms: id, label, url). Keepers never get one; unlisted looks stay blank.
  5. Name check: every text in modules/lookbook/ (plus any --scan files) against the breeder's banned list
     (lookbook/public_terms.py BANNED). The list itself is read at run time and never copied into this repo.

    python3 tools/lookbook_sync.py BREEDER_ROOT --enrich-only
re-derives the fields in 4 for the looks already here, without pulling a new batch.
Exit 1 on any name hit or ID problem; nothing is written in that case."""
import argparse, csv, hashlib, io, json, pathlib, re, shutil, sys

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

# ---------- derived fields (nearest_looks, colours, getty_aat) ----------
def _lab(rgb):
    import numpy as np
    c = rgb / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    xyz = c @ np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]]).T
    xyz = xyz / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[:, 1] - 16, 500 * (f[:, 0] - f[:, 1]), 200 * (f[:, 1] - f[:, 2])], 1)

def dominant_colours(path, k=6, keep=5, min_share=0.04):
    """3-5 dominant colours (hex, largest share first). Seeded k-means in CIELAB on a 160 px copy; clusters under
    4% of the pixels are dropped and clusters closer than dE 10 are merged."""
    import numpy as np
    from PIL import Image
    im = Image.open(path).convert("RGB"); im.thumbnail((160, 160))
    rgb = np.asarray(im).reshape(-1, 3).astype(float); lab = _lab(rgb)
    rng = np.random.default_rng(0)
    cen = lab[rng.choice(len(lab), 1)]
    for _ in range(k - 1):                                  # k-means++ seeding
        d = ((lab[:, None] - cen[None]) ** 2).sum(-1).min(1)
        cen = np.vstack([cen, lab[rng.choice(len(lab), 1, p=d / d.sum())]])
    for _ in range(25):
        lbl = ((lab[:, None] - cen[None]) ** 2).sum(-1).argmin(1)
        cen = np.array([lab[lbl == i].mean(0) if (lbl == i).any() else cen[i] for i in range(k)])
    share = np.array([(lbl == i).mean() for i in range(k)])
    kept = []                                               # [share, lab centre, summed rgb, n] largest first
    for i in np.argsort(-share):
        if share[i] == 0: continue
        m = lbl == i
        near = next((g for g in kept if np.linalg.norm(g[1] - cen[i]) < 10), None)   # merge near-identical clusters
        if near: near[0] += share[i]; near[2] += rgb[m].sum(0); near[3] += m.sum()
        else: kept.append([share[i], cen[i], rgb[m].sum(0), m.sum()])
    kept.sort(key=lambda g: -g[0])
    out = [(g[0], g[2] / g[3]) for g in kept if g[0] >= min_share]
    if len(out) < 3: out = [(g[0], g[2] / g[3]) for g in kept[:3]]   # flat images: top 3 anyway
    return ["#%02x%02x%02x" % tuple(int(round(v)) for v in c) for _, c in out[:keep]]

def enrich(live, breeder, src_looks):
    """Add nearest_looks (top 3 visual neighbours), bred_from, colours and getty_aat to the live rows, in place."""
    import numpy as np
    render = {l["id"]: l.get("render") for l in src_looks}
    cache = breeder / "lookbook/.dedup_cache/emb.npz"
    emb = np.load(cache) if cache.exists() else {}
    vec, missing = {}, []
    for r in live:
        rp = render.get(r["id"]); f = breeder / rp if rp else None
        key = "clip_" + hashlib.sha1(f.read_bytes()).hexdigest() if f and f.exists() else None
        if key and key in emb: vec[r["id"]] = emb[key] / np.linalg.norm(emb[key])
        else: missing.append(r["id"])
        if f and f.exists(): r["colours"] = dominant_colours(f)
    ids = sorted(vec); M = np.stack([vec[i] for i in ids]) if ids else None
    getty = {}
    gf = MOD / "getty_aat.json"
    if gf.exists(): getty = {k: v for k, v in json.loads(gf.read_text())["looks"].items()}
    for r in live:
        old = r.get("bred_from", r.get("nearest_looks", [])) if r["kind"] == "keeper" else []
        r["bred_from"] = old
        if r["id"] in vec:
            sim = M @ vec[r["id"]]
            r["nearest_looks"] = [ids[j] for j in np.argsort(-sim) if ids[j] != r["id"]][:3]
        else:
            r["nearest_looks"] = []
        r.setdefault("colours", [])
        g = getty.get(r["id"]) if r["kind"] == "established" else None
        r["getty_aat"] = {"id": g["id"], "label": g["label"], "url": f"http://vocab.getty.edu/page/aat/{g['id']}"} if g and g.get("id") else None
    if missing: print(f"no cached embedding for {len(missing)} look(s), nearest_looks left empty: {missing[:10]}")
    return live

NEW_FIELDS = ["nearest_looks", "bred_from", "colours", "getty_aat"]

def write_outputs(out, live):
    js = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    cols = [c for c in live[0] if c != "hallmarks"]
    hl = list(live[0]["hallmarks"])
    buf = io.StringIO(); w = csv.writer(buf)
    w.writerow(cols[:cols.index("hint")] + [f"hl_{h}" for h in hl] + cols[cols.index("hint"):])
    def flat(v):
        if isinstance(v, list): return "; ".join(map(str, v))
        if isinstance(v, dict): return f"{v.get('label')} (AAT {v.get('id')})"
        return "" if v is None else v
    for r in live:
        vals = [flat(r.get(c)) for c in cols]
        i = cols.index("hint")
        w.writerow(vals[:i] + [r["hallmarks"].get(h, "") for h in hl] + vals[i:])
    return js, buf.getvalue()

def fields_with_new(fields):
    f = [x for x in fields if x not in NEW_FIELDS and x not in DROP]
    i = f.index("status") if "status" in f else len(f)
    return f[:i] + NEW_FIELDS + f[i:]


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
        if row["kind"] == "keeper": row["bred_from"] = row.get("nearest_looks", [])
        if l["sheet"] not in sheets: problems.append(f"{l['id']}: sheet {l['sheet']} not shareable")
        row["sheet"] = sheets.get(l["sheet"], "")
        live.append(row)
    enrich(live, breeder, src["looks"])
    keys = list(dict.fromkeys(k for r in live for k in r))          # union: optional blocks like `interpreted` survive
    order = [k for k in keys if k not in NEW_FIELDS and k != "status"] + NEW_FIELDS + ["status"] if live else []
    live = [{k: r[k] for k in order if k in r} for r in live]
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
        "fields": fields_with_new(src.get("fields", [])),
        "looks": live,
        "retired": sorted(retired.values(), key=lambda r: r["id"]),
    }
    js, cs = write_outputs(out, live)

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

def enrich_only(breeder, scan_extra):
    """Re-derive nearest_looks, bred_from, colours and getty_aat for the looks already in the repo (no new batch)."""
    pats = banned_patterns(breeder)
    out = json.loads((MOD / "looks.json").read_text())
    src = json.loads((breeder / "lookbook/looks.json").read_text())
    live = enrich(out["looks"], breeder, src["looks"])
    order = [k for k in live[0] if k not in NEW_FIELDS and k != "status"] + NEW_FIELDS + ["status"]
    out["looks"] = live = [{k: r.get(k) for k in order} for r in live]
    out["fields"] = fields_with_new(out.get("fields", []))
    js, cs = write_outputs(out, live)
    texts = {"looks.json": js, "looks.csv": cs, **{f: pathlib.Path(f).read_text() for f in scan_extra}}
    bad = {k: h for k, t in texts.items() for h in [hits(t, pats)] if h}
    for k, h in bad.items(): print("NAME HIT", k, h)
    if bad: sys.exit(1)
    (MOD / "looks.json").write_text(js); (MOD / "looks.csv").write_text(cs)
    print(f"enriched {len(live)} looks: nearest_looks {sum(bool(r['nearest_looks']) for r in live)}, colours {sum(bool(r['colours']) for r in live)}, getty_aat {sum(bool(r['getty_aat']) for r in live)}")

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
    ap.add_argument("--enrich-only", action="store_true", help="re-derive nearest_looks, colours and getty_aat on the looks already here")
    a = ap.parse_args()
    if a.check_only: check_only(a.breeder, a.scan)
    elif a.enrich_only: enrich_only(a.breeder, a.scan)
    else: build(a.breeder, a.scan, a.dry_run)
