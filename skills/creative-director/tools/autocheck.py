#!/usr/bin/env python3
"""autocheck.py: one command for the measurable checks, before any judgement by eye (critique loop step 3).

    python3 tools/autocheck.py TARGET [TARGET ...] [--out DIR] [--json FILE] [--width 1280] [--height 800]
                               [--text-box x0,y0,x1,y1[:large] ...] [--print 420x594mm] [--intended Y0-Y1,...] [--axis left|right]

TARGET is an image (PNG/JPG), an HTML file or an http(s) URL. Pages are opened in headless Chromium (playwright)
and measured from the DOM (computed styles, text boxes) plus screenshots; images are measured from pixels only.
Every check cites the rule it comes from and uses that rule's own threshold. No AI judgement is involved.

Statuses: FAIL = outside the rule's stated number (fix first; a blocker if the rule is MUST-BE-RIGHT);
FLAG = measured, but the rule asks for a decision ("intended?"); PASS; SKIP = can't be measured here (said why).
Balance and placement results are never FAIL and never suggest centring (COMP-19, COMP-20).
Exit 1 if any check FAILs. --out DIR writes report.txt, report.json and the screenshots and sheets.

Reuses: contrast.py (WCAG ratio), whitespace.py (LAY-10), balance.py (COMP-19). Needs Pillow and numpy;
page mode needs playwright (`pip install playwright && playwright install chromium`)."""
import argparse, contextlib, io, json, math, os, pathlib, re, sys, tempfile
from collections import Counter
import numpy as np
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import contrast, whitespace, balance  # noqa: E402

def chk(cid, name, rule, status, measured, threshold, detail="", blocker=False):
    return dict(id=cid, name=name, rule=rule, status=status, measured=measured, threshold=threshold, detail=detail, blocker=blocker)

def rel_lum(rgb):  # rgb 0-255
    return contrast.L([c / 255 for c in rgb])

def ratio_lum(a, b):
    hi, lo = max(a, b), min(a, b); return (hi + 0.05) / (lo + 0.05)

# ---------------------------------------------------------------- pixel checks (images and page screenshots)

def quiet(fn, *a, **k):
    with contextlib.redirect_stdout(io.StringIO()): return fn(*a, **k)

def check_whitespace(path, intended=(), axis=None, sheet=None):
    o = quiet(whitespace.analyse, path, None, intended, 1.5, sheet=sheet, axis=axis)
    worst = max(o["bands"], key=lambda b: b["ratio"] if b["ratio"] != float("inf") else 0, default=None)
    dz = o.get("dead_zone") or {}
    sparse = [r for r in o["sparse"] if r[3] > 0.01]          # mostly-empty rows that hold some content (empty bands are counted above)
    fails = [b for b in o["bands"] if b["fail"] and b["ratio"] != float("inf")] + ([dz] if dz.get("fail") else [])
    lone = [b for b in o["bands"] if b["fail"] and b["ratio"] == float("inf")]   # the only interior gap: nothing to compare with
    meas = []
    if worst: meas.append(f"largest band {worst['h']} px = " + (f"{worst['ratio']}x the largest other gap" if worst['ratio'] != float('inf') else f"{worst['pct']}% of the height, the only interior gap"))
    if dz: meas.append(f"largest empty region {dz.get('ratio')}x the largest gap ({dz.get('pct_area')}% of area)")
    det = "Name the job of each flagged space or regroup (COMP-23); declare deliberate space with --intended. Never fix by centring."
    if fails:
        return chk("dead-space", "Dead space / empty bands", "LAY-10", "FAIL", "; ".join(meas), "band or empty block > 1.5x the largest intended gap (LAY-10, self-chosen craft number)", det)
    st = "FLAG" if sparse or lone or (dz and (dz.get("ratio") or 0) > 1.5 and dz.get("pct_area", 0) > 3 and (dz.get("symmetric_flank") or dz.get("open_side"))) else "PASS"
    extra = (f"; {len(sparse)} sparse row band(s) to review by eye" if sparse else "") + ("; one interior gap only, so no other gap to compare it with: judge it against the margins by eye" if lone else "")
    return chk("dead-space", "Dead space / empty bands", "LAY-10", st, "; ".join(meas) + extra or "no interior bands", "1.5x the largest intended gap (LAY-10)", "PASS means review by eye, not approval." if st == "PASS" else det)

def check_balance(path, sheet=None):
    o = quiet(balance.analyse, path, None, sheet)
    if not o: return chk("balance", "Visual-weight balance", "COMP-19", "SKIP", "no content found", "", "")
    m = f"DCM {o['dcm']:.0f} (dx {o['dx']:+.0f}%, dy {o['dy']:+.0f}%), right/left {o['lr']:.2f}, bottom/top {o['tb']:.2f}"
    det = ("If unintended: a counterweight on the light side or a firmer asymmetry (COMP-19, COMP-20). "
           "Off-centre work is valid; never centre or symmetrise by default.")
    st = "FLAG" if o["dcm"] > 25 else "PASS"
    return chk("balance", "Visual-weight balance", "COMP-19, COMP-2", st, m,
               "reading bands from balance.py (self-chosen): >25 strongly off-centre = FLAG: intended?; never FAIL",
               ("FLAG: intended? " + det) if st == "FLAG" else "Weights near equilibrium or mildly off-centre. Finish by eye: faces, words and gaze add weight pixels can't see (COMP-3).")

def content_mask(im):
    a = np.asarray(im.convert("RGB")).astype(float); H, W = a.shape[:2]
    e = max(2, int(0.02 * min(H, W)))
    border = np.concatenate([a[:e].reshape(-1, 3), a[-e:].reshape(-1, 3), a[:, :e].reshape(-1, 3), a[:, -e:].reshape(-1, 3)])
    q = (border // 16).astype(int); keys, cnt = np.unique(q, axis=0, return_counts=True)
    bg = keys[cnt.argmax()] * 16 + 8
    return np.sqrt(((a - bg) ** 2).sum(2)) > 38

def components(mask, min_px):
    """Connected components (4-neighbour) of a boolean mask: list of (x0, y0, x1, y1, n). Pure numpy/py union-find on runs."""
    H, W = mask.shape; lab = np.zeros((H, W), int); parent = [0]
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    nxt = 1
    for y in range(H):
        row = mask[y]; x = 0
        while x < W:
            if not row[x]: x += 1; continue
            x0 = x
            while x < W and row[x]: x += 1
            ids = set(lab[y - 1, x0:x][lab[y - 1, x0:x] > 0]) if y else set()
            if ids:
                r = min(find(i) for i in ids)
                for i in ids: parent[find(i)] = r
            else:
                parent.append(nxt); r = nxt; nxt += 1
            lab[y, x0:x] = r
    roots = np.array([find(i) for i in range(len(parent))]); lab = roots[lab]
    out = []
    for r in np.unique(lab[lab > 0]):
        ys, xs = np.nonzero(lab == r)
        if len(xs) >= min_px: out.append((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1, len(xs)))
    return out

def check_edges_image(path):
    im = Image.open(path); W0, H0 = im.size; s = 300 / max(W0, H0)
    small = im.convert("RGB").resize((max(1, round(W0 * s)), max(1, round(H0 * s))))
    m = content_mask(small); H, W = m.shape
    comps = components(m, max(4, int(0.0004 * H * W)))
    band = 0.06 * min(H, W)   # LAY-5: keep at least 6-8% of the short side free of text
    near, bleed = [], []
    for x0, y0, x1, y1, n in comps:
        d = min(x0, y0, W - x1, H - y1)
        box = tuple(round(v / s) for v in (x0, y0, x1, y1))
        if d <= 0: bleed.append(box)
        elif d < band: near.append((round(d / s), box))
    m_txt = f"{len(near)} element(s) inside the 6% edge band" + (f" (closest {min(n[0] for n in near)} px)" if near else "") + f"; {len(bleed)} run off the edge"
    det = ("Each one: if it is text or a key element, pull it to the margin (LAY-5); if it is a crop, make it decisive. "
           "Bleeds: check none just kisses the edge (tangent, COMP-24 item 3). Boxes in report.json.")
    st = "FLAG" if near else "PASS"
    return chk("edges", "Crowded edges / safe margin", "COMP-24, LAY-5", st, m_txt,
               "LAY-5: keep at least 6-8% of the short side free of text (6% used); COMP-24: nothing closer to the frame than the margin system allows",
               det if near else "Nothing sits in the edge band. Bleeds are listed for a look at the crop.") | {"near": near[:20], "bleed": bleed[:20]}

def check_text_boxes(path, boxes):
    """LAY-15 / UI-6 for text in an image: worst-pixel contrast inside each given text box (text = minority tone)."""
    a = np.asarray(Image.open(path).convert("RGB")).astype(float); res = []; worst = None
    for spec in boxes:
        big = spec.endswith(":large"); x0, y0, x1, y1 = [int(v) for v in spec.split(":")[0].split(",")]
        px = a[y0:y1, x0:x1].reshape(-1, 3)
        if len(px) < 4: continue
        lum = np.array([rel_lum(p) for p in px[:: max(1, len(px) // 4000)]])
        t = (lum.min() + lum.max()) / 2
        for _ in range(10):   # two-tone split on luminance
            lo, hi = lum[lum <= t], lum[lum > t]
            if not len(lo) or not len(hi): break
            t = (lo.mean() + hi.mean()) / 2
        lo, hi = lum[lum <= t], lum[lum > t]
        if not len(lo) or not len(hi): continue   # one flat tone: no text found in the box
        text_is_light = len(hi) < len(lo)
        txt = np.median(hi if text_is_light else lo)
        ground = hi if not text_is_light else lo
        worst_g = np.percentile(ground, 5 if not text_is_light else 95)   # dark text: darkest ground; light text: lightest
        r = ratio_lum(txt, worst_g); need = 3.0 if big else 4.5
        res.append(dict(box=spec, ratio=round(float(r), 2), need=need, ok=bool(r >= need)))
        worst = r if worst is None else min(worst, r)
    if not res: return None
    bad = [r for r in res if not r["ok"]]
    return chk("contrast", "Text contrast (worst pixels, given text boxes)", "UI-6, LAY-15", "FAIL" if bad else "PASS",
               f"{len(bad)}/{len(res)} boxes below; worst {worst:.2f}:1", "4.5:1 (3:1 large text) against the worst ground pixels (UI-6, LAY-15)",
               "Move the text to a calm area, add a scrim or a panel (LAY-15)." if bad else "", blocker=True) | {"boxes": res}

def check_print(path, spec):
    m = re.fullmatch(r"([\d.]+)x([\d.]+)(mm|in)", spec)
    if not m: return chk("print-ppi", "Print resolution", "LAY-9", "SKIP", f"bad --print {spec}", "", "")
    w, h, u = float(m.group(1)), float(m.group(2)), m.group(3)
    if u == "mm": w, h = w / 25.4, h / 25.4
    W, H = Image.open(path).size; ppi = min(W / w, H / h)
    return chk("print-ppi", "Print resolution", "LAY-9", "PASS" if ppi >= 300 else "FAIL", f"{ppi:.0f} ppi at {spec}",
               "at least 300 ppi at final printed size (LAY-9)", "Re-render at size; don't upsample." if ppi < 300 else "", blocker=True)

IMAGE_SKIPS = [
    ("text-size", "TYPE-3, LAY-6", "no DOM: x-height can't be read from pixels reliably. Scale to 400 px wide (thumb-400.png) and measure the main message's x-height by eye (about 6 px or more)."),
    ("type-sizes", "TYPE-2", "no DOM: list the sizes by eye."),
    ("measure", "TYPE-4", "no DOM: count characters on three lines by eye."),
    ("leading", "TYPE-5", "no DOM."),
    ("spacing-scale", "CORE-4, COMP-24", "no DOM: use grid.py on a screenshot, or measure gaps at zoom."),
]

def run_image(path, a, out):
    checks = [check_whitespace(path, a.intended, a.axis, out and str(out / "whitespace.png")),
              check_balance(path, out and str(out / "balance.png")), check_edges_image(path)]
    tb = check_text_boxes(path, a.text_box) if a.text_box else None
    if tb: checks.insert(0, tb)
    else: checks.insert(0, chk("contrast", "Text contrast", "UI-6, LAY-15", "SKIP", "", "",
                               "no DOM: text can't be found in pixels honestly. Pass --text-box x0,y0,x1,y1[:large] per line of text to measure worst-pixel contrast."))
    if a.print: checks.append(check_print(path, a.print))
    for cid, rule, why in IMAGE_SKIPS: checks.append(chk(cid, cid, rule, "SKIP", "", "", why))
    if out:
        im = Image.open(path).convert("RGB"); im.resize((400, max(1, round(im.height * 400 / im.width))), Image.LANCZOS).save(out / "thumb-400.png")
    W, H = Image.open(path).size
    return dict(target=str(path), mode="image", size=[W, H], checks=checks)

# ---------------------------------------------------------------- page checks (DOM)

JS = r"""
() => {
  const cv = document.createElement('canvas'); cv.width = cv.height = 1; const cx = cv.getContext('2d', {willReadFrequently: true});
  const rgba = c => { cx.clearRect(0,0,1,1); cx.fillStyle = '#000'; cx.fillStyle = c; cx.fillRect(0,0,1,1); const d = cx.getImageData(0,0,1,1).data; return [d[0],d[1],d[2],d[3]/255]; };
  const opac = el => { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; };
  const shown = el => { for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const s = getComputedStyle(e); if (s.display === 'none' || s.visibility === 'hidden') return false; } return true; };
  const blockish = s => !['inline', 'contents'].includes(s.display);
  const tiny = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width < 2 || r.height < 2 || s.clip === 'rect(0px, 0px, 0px, 0px)' || s.clipPath === 'inset(50%)'; };
  const texts = [], blocks = new Map();
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
  while ((n = tw.nextNode())) {
    const t = n.textContent.replace(/\s+/g, ' ').trim(); if (!t) continue;
    const el = n.parentElement; if (!el || ['SCRIPT','STYLE','NOSCRIPT','TEMPLATE','OPTION','TITLE'].includes(el.tagName)) continue;
    if (el.closest('svg')) continue;
    if (!shown(el) || tiny(el)) continue;
    const op = opac(el); if (op < 0.05) continue;
    const r = document.createRange(); r.selectNodeContents(n);
    const rects = [...r.getClientRects()].filter(q => q.width > 0.5 && q.height > 0.5).map(q => [q.left, q.top, q.right, q.bottom]);
    if (!rects.length) continue;
    const s = getComputedStyle(el); const fs = parseFloat(s.fontSize);
    let b = el; while (b !== document.body && !blockish(getComputedStyle(b))) b = b.parentElement;
    texts.push({t: t.slice(0, 60), len: t.length, tag: el.tagName.toLowerCase(), fs, fw: parseInt(s.fontWeight) || 400, color: rgba(s.color), op, rects,
                link: !!el.closest('a'), btn: !!el.closest('button,[role=button],label,select,input,summary')});
    if (!blocks.has(b)) { const bs = getComputedStyle(b); const bb = b.getBoundingClientRect();
      blocks.set(b, {tag: b.tagName.toLowerCase(), lh: bs.lineHeight, fsb: parseFloat(bs.fontSize), box: [bb.left, bb.top, bb.right, bb.bottom], rects: [], chars: 0, fsc: {}}); }
    const B = blocks.get(b); B.rects.push(...rects); B.chars += t.length; B.fsc[fs] = (B.fsc[fs] || 0) + t.length;
  }
  // gaps between in-flow siblings, padding of framed boxes
  const gaps = [], rows = [], pads = [];
  for (const p of document.body.querySelectorAll('*')) {
    if (!shown(p)) continue;
    const ps = getComputedStyle(p);
    const kids = [...p.children].filter(c => { const s = getComputedStyle(c); const r = c.getBoundingClientRect();
      return shown(c) && r.width > 0 && r.height > 0 && !['absolute','fixed'].includes(s.position) && !['SCRIPT','STYLE','BR'].includes(c.tagName); });
    const framed = (ps.backgroundColor !== 'rgba(0, 0, 0, 0)' && ps.backgroundColor !== 'transparent') || parseFloat(ps.borderTopWidth) > 0 || parseFloat(ps.borderLeftWidth) > 0;
    if (framed && kids.length) for (const k of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) { const v = parseFloat(ps[k]); if (v > 0) pads.push(v); }
    if (kids.length < 2) continue;
    const R = kids.map(c => c.getBoundingClientRect());
    const row = R.every((r, i) => i === 0 || Math.abs(r.top - R[0].top) < 2) && R.every((r, i) => i === 0 || r.left >= R[i-1].right - 1);
    if (row) { const g = R.slice(1).map((r, i) => r.left - R[i].right); g.forEach(v => v > 0 && gaps.push(v));
      const w = R.map(r => r.width); if (R.length >= 3 && Math.max(...w) <= 1.1 * Math.min(...w)) rows.push({gaps: g, sel: p.tagName.toLowerCase() + (p.className && typeof p.className === 'string' ? '.' + p.className.split(' ')[0] : '')});
    } else {
      const S = R.slice().sort((a, b) => a.top - b.top);
      for (let i = 1; i < S.length; i++) { const g = S[i].top - S[i-1].bottom; if (g > 0 && S[i].left < S[i-1].right && S[i].right > S[i-1].left) gaps.push(g); }
    }
  }
  const targets = [];
  for (const el of document.querySelectorAll('a[href],button,input:not([type=hidden]),select,textarea,summary,[role=button],[role=link],[role=tab],[role=checkbox],[role=switch]')) {
    if (!shown(el)) continue; const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    let b = el.parentElement; while (b && b !== document.body && !blockish(getComputedStyle(b))) b = b.parentElement;
    const inline = el.tagName === 'A' && getComputedStyle(el).display === 'inline' && b && (b.innerText || '').replace(/\s+/g, ' ').trim().length > (el.innerText || '').trim().length + 20;
    if (el.type === 'checkbox' || el.type === 'radio') { const lab = el.closest('label'); if (lab) { const lr = lab.getBoundingClientRect(); targets.push({w: lr.width, h: lr.height, inline: false, what: 'label>' + el.type}); continue; } }
    targets.push({w: r.width, h: r.height, inline, what: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + ((el.innerText || el.value || el.getAttribute('aria-label') || '') + '').trim().slice(0, 24)});
  }
  const clipped = [];
  for (const el of document.body.querySelectorAll('*')) {
    const s = getComputedStyle(el); if (!shown(el)) continue;
    const hid = ['hidden','clip'].includes(s.overflowX) || ['hidden','clip'].includes(s.overflowY) || s.textOverflow === 'ellipsis';
    if (hid && (el.innerText || '').trim() && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) && el.clientWidth > 0) clipped.push(el.tagName.toLowerCase() + ': ' + el.innerText.trim().slice(0, 30));
  }
  return {vw: innerWidth, vh: innerHeight, docW: document.documentElement.scrollWidth, docH: document.documentElement.scrollHeight,
          texts, blocks: [...blocks.values()], gaps, rows, pads, targets, clipped: clipped.slice(0, 20)};
}
"""

HIDE_TEXT = "*,*::before,*::after,*::placeholder{color:transparent!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important;caret-color:transparent!important;text-decoration-color:transparent!important;border-color:transparent!important;outline-color:transparent!important}*::marker{color:transparent!important}"

def lines_of(rects, fs):
    tops = sorted(r[1] for r in rects); n = 0; last = None
    for t in tops:
        if last is None or t > last + 0.5 * fs: n += 1; last = t
    return n

def page_checks(d, shot, bgshot):
    checks = []
    a = np.asarray(Image.open(shot).convert("RGB")); b = np.asarray(Image.open(bgshot).convert("RGB")).astype(float)
    H, W = b.shape[:2]
    # --- contrast (UI-6): text colour against the worst pixels of its own ground (text hidden in bgshot)
    res = []
    for t in d["texts"]:
        xs = [r for r in t["rects"] if r[2] > 0 and r[3] > 0 and r[0] < W and r[1] < H]
        if not xs: continue
        px = np.concatenate([b[max(0, int(r[1])):min(H, int(math.ceil(r[3]))), max(0, int(r[0])):min(W, int(math.ceil(r[2])))].reshape(-1, 3) for r in xs])
        if len(px) < 4: continue
        px = px[:: max(1, len(px) // 3000)]
        lum = np.array([rel_lum(p) for p in px])
        col, al = t["color"][:3], t["color"][3] * t["op"]
        med = np.median(px, 0)
        tl = rel_lum([c * al + g * (1 - al) for c, g in zip(col, med)])
        gmed = np.median(lum)
        worst = np.percentile(lum, 95 if tl > gmed else 5)
        r_w, r_m = ratio_lum(tl, worst), ratio_lum(tl, gmed)
        big = t["fs"] >= 24 or (t["fs"] >= 18.5 and t["fw"] >= 700)
        need = 3.0 if big else 4.5
        res.append(dict(text=t["t"], fs=t["fs"], ratio=round(float(r_w), 2), median_ratio=round(float(r_m), 2), need=need, ok=bool(r_w >= need),
                        busy=bool(np.ptp(lum) > 0.2)))
    # busy ground (photo, gradient, border) where the median ground passes: a flag to check by eye, not a fail
    mixed = sorted([r for r in res if not r["ok"] and r["busy"] and r["median_ratio"] >= r["need"]], key=lambda r: r["ratio"])
    bad = sorted([r for r in res if not r["ok"] and r not in mixed], key=lambda r: r["ratio"])
    st = "FAIL" if bad else ("FLAG" if mixed else ("PASS" if res else "SKIP"))
    allw = bad + mixed
    det = "; ".join(f"\"{r['text'][:30]}\" {r['ratio']}:1 (need {r['need']})" for r in bad[:6])
    if mixed:
        det += ("; " if det else "") + f"{len(mixed)} on a busy ground that passes at its median (check by eye): " + "; ".join(f"\"{r['text'][:24]}\" worst {r['ratio']}, median {r['median_ratio']}" for r in mixed[:3])
    checks.append(chk("contrast", "Text contrast (WCAG)", "UI-6, LAY-15", st,
                      f"{len(bad)}/{len(res)} text runs below" + (f" (+{len(mixed)} mixed-ground)" if mixed else "") + f"; worst {min((r['ratio'] for r in (bad or res)), default=0)}:1",
                      "4.5:1, 3:1 for large text (about 24 px, or 18.5 px bold), against the worst 5% of ground pixels behind the text (UI-6, LAY-15)",
                      det, blocker=True) | {"items": allw[:30]})
    # --- text size (TYPE-3)
    blocks = d["blocks"]
    def running(B):
        fs = max(B["fsc"], key=B["fsc"].get) if B["fsc"] else B["fsb"]
        return B["chars"] >= 80 or (lines_of(B["rects"], float(fs)) >= 2 and B["chars"] >= 50)
    run_sizes = sorted({float(max(B["fsc"], key=B["fsc"].get)) for B in blocks if B["fsc"] and running(B)})
    small = [t for t in d["texts"] if t["fs"] < 12]
    run_small = [B for B in blocks if B["fsc"] and running(B) and float(max(B["fsc"], key=B["fsc"].get)) < 14]
    run_soft = [B for B in blocks if B["fsc"] and running(B) and 14 <= float(max(B["fsc"], key=B["fsc"].get)) < 16]
    st = "FAIL" if small or run_small else ("FLAG" if run_soft else "PASS")
    sizes = Counter(); [sizes.update({round(t["fs"] * 2) / 2: t["len"]}) for t in d["texts"]]
    checks.append(chk("text-size", "Minimum text size", "TYPE-3", st,
                      f"smallest {min(sizes) if sizes else '-'} px; {len(small)} text runs under 12 px; running text at {', '.join(f'{s:g}' for s in run_sizes) or '-'} px",
                      "blocker: any meaningful text < 12 px, reading text < 14 px; default: reading text >= 16 px, labels >= 12 px (TYPE-3)",
                      "; ".join(f"\"{t['t'][:24]}\" {t['fs']:g}px" for t in small[:6]) + (f"; {len(run_soft)} reading block(s) at 14-15 px (below the 16 px default)" if run_soft else ""),
                      blocker=bool(small or run_small)))
    # --- distinct type sizes (TYPE-2)
    ss = sorted(sizes); near = [(x, y) for x, y in zip(ss, ss[1:]) if y / x < 1.1]
    n = len(ss); st = "FAIL" if n > 6 else ("FLAG" if n == 6 or near else "PASS")
    checks.append(chk("type-sizes", "Distinct type sizes", "TYPE-2", st, f"{n} sizes: " + ", ".join(f"{s:g}" for s in ss),
                      "about 5-6 sizes per page at most; neighbouring sizes at least 1.1x apart unless the same role (TYPE-2)",
                      ("near-duplicate pairs: " + ", ".join(f"{x:g}/{y:g}" for x, y in near) + " (merge unless same role)") if near else ""))
    # --- measure (TYPE-4) and leading (TYPE-5) on blocks of 3+ lines
    long, short, tight, loose, seen = [], [], [], [], 0
    for B in blocks:
        if not B["fsc"]: continue
        fs = float(max(B["fsc"], key=B["fsc"].get)); nl = lines_of(B["rects"], fs)
        if nl < 3: continue
        seen += 1
        tops = {}
        for r in B["rects"]: k = round(r[1] / (0.5 * fs)); tops.setdefault(k, []).append(r)
        widths = [max(r[2] for r in v) - min(r[0] for r in v) for v in tops.values()]
        cw = sum(r[2] - r[0] for r in B["rects"]) / max(1, B["chars"])
        cpl = round(max(widths) / cw) if cw else 0
        lh = float(B["lh"][:-2]) / fs if B["lh"].endswith("px") else (1.2 if B["lh"] == "normal" else None)
        if cpl > 90: long.append((cpl, B["tag"]))
        elif cpl < 45: short.append((cpl, B["tag"]))
        if lh and lh < 1.3 and B["tag"] not in ("h1", "h2", "h3"): tight.append((round(lh, 2), B["tag"]))
        if lh and lh > 1.3 and B["tag"] in ("h1", "h2", "h3"): loose.append((round(lh, 2), B["tag"]))
    if not seen:
        checks.append(chk("measure", "Body line length", "TYPE-4", "SKIP", "no text block of 3+ lines", "45-90 characters (TYPE-4)", ""))
        checks.append(chk("leading", "Line spacing", "TYPE-5", "SKIP", "no text block of 3+ lines", "body 1.3-1.5 (TYPE-5)", ""))
    else:
        checks.append(chk("measure", "Body line length", "TYPE-4", "FAIL" if long else ("FLAG" if short else "PASS"),
                          f"{seen} blocks of 3+ lines; {len(long)} over 90 chars" + (f" (longest {max(long)[0]})" if long else "") + f"; {len(short)} under 45",
                          "45-90 characters per line, about 65 ideal; narrow columns can go to 30-40 (TYPE-4)",
                          ("Fix: max-inline-size: 65ch. " if long else "") + (f"{len(short)} narrow block(s): fine for captions and sidebars, check the rest." if short else "")))
        checks.append(chk("leading", "Line spacing", "TYPE-5", "FAIL" if tight else ("FLAG" if loose else "PASS"),
                          f"{len(tight)} body block(s) below 1.3" + (f" (tightest {min(tight)[0]})" if tight else "") + f"; {len(loose)} multi-line headline(s) above 1.3",
                          "body line height 1.3-1.5 (up to 1.6 on long measures); headlines about 1.0-1.2 (TYPE-5)", "line-height 'normal' counted as 1.2"))
    # --- spacing scale and near misses (CORE-4, COMP-24)
    vals = [round(v * 2) / 2 for v in d["gaps"] + d["pads"] if 0.5 <= v <= 160]
    c = Counter(vals); off = {v: k for v, k in c.items() if abs(v / 4 - round(v / 4)) > 0.13}
    used = sorted(c); nm = [(x, y) for i, x in enumerate(used) for y in used[i + 1:] if y >= 8 and 1 <= y - x <= max(2, 0.1 * y)]
    share = 100 * (1 - sum(off.values()) / max(1, len(vals)))
    checks.append(chk("spacing-scale", "Spacing on one scale", "CORE-4", "PASS" if not off else "FLAG",
                      f"{len(vals)} gaps and paddings, {share:.0f}% on a 4 px step; off-scale: " + (", ".join(f"{v:g}px x{k}" for v, k in sorted(off.items(), key=lambda kv: -kv[1])[:8]) or "none"),
                      "gaps from one small scale (e.g. 4/8/16/24/32/48: steps of 4, CORE-4); the rule sets no pass rate, so off-scale values are flags", "Snap each gap to the scale and give it a role (CORE-4)." if off else ""))
    rows_bad = [r for r in d["rows"] if len(r["gaps"]) >= 2 and max(r["gaps"]) - min(r["gaps"]) > max(1, 0.1 * max(r["gaps"]))]
    st = "FLAG" if nm or rows_bad else "PASS"
    checks.append(chk("near-miss", "Near-miss gaps and uneven gutters", "COMP-24, CORE-4", st,
                      f"{len(nm)} near-duplicate gap pair(s)" + (": " + ", ".join(f"{x:g}/{y:g}" for x, y in nm[:8]) if nm else "") + f"; {len(rows_bad)} row(s) of equal items with uneven gutters",
                      "gutters that should be equal differ by more than about 10% (COMP-24, self-chosen); near-duplicate values within 10% (or 2 px) of each other",
                      ("Snap to one value or make the difference clear (COMP-24)." if st == "FLAG" else "") + (" Rows: " + "; ".join(f"{r['sel']} gaps {[round(g) for g in r['gaps']]}" for r in rows_bad[:4]) if rows_bad else "")))
    # --- edges (COMP-24 crammed): text outside the page's own margin line, or touching the viewport edge
    vw = d["vw"]; L = []
    for B in blocks:
        rs = [r for r in B["rects"] if r[1] < H]
        if rs: L.append((min(r[0] for r in rs), vw - max(r[2] for r in rs), B))
    lefts = Counter(round(l) for l, _, _ in L if l >= 0)
    margin = min([v for v, k in lefts.items() if k >= 3], default=None)
    crowd = [(round(l), round(rr)) for l, rr, _ in L if (l <= 1 or rr <= 1) or (margin is not None and (l < margin - 1 or rr < margin - 1))]
    checks.append(chk("edges", "Text crowding the frame", "COMP-24", "FLAG" if crowd else "PASS",
                      f"page margin line {margin if margin is not None else '-'} px (smallest left inset shared by 3+ text blocks); {len(crowd)} text block(s) closer to the edge",
                      "nothing closer to the frame than the margin system allows; no contour just touching the edge (COMP-24)",
                      ("Insets (left, right) px: " + ", ".join(map(str, crowd[:8])) + ". Pull to the margin or bleed decisively; intended?") if crowd else ""))
    return checks

def run_page(target, a, out):
    from playwright.sync_api import sync_playwright
    url = target if re.match(r"https?://", target) else pathlib.Path(target).resolve().as_uri()
    tmp = pathlib.Path(out) if out else pathlib.Path(tempfile.mkdtemp(prefix="autocheck-"))
    shot, bgshot = tmp / f"page-{a.width}.png", tmp / f"page-{a.width}-notext.png"
    checks = []
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox"])
        def open_(w, h, dpr=1):
            pg = br.new_page(viewport={"width": w, "height": h}, device_scale_factor=dpr)
            pg.goto(url, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(a.settle)
            return pg
        pg = open_(a.width, a.height)
        docH = pg.evaluate("document.documentElement.scrollHeight")
        if docH > a.height:   # measure the whole page in one state (viewport stretched; vh units may stretch too)
            pg.set_viewport_size({"width": a.width, "height": min(docH, 6000)}); pg.wait_for_timeout(400)
        d = pg.evaluate(JS); pg.screenshot(path=str(shot))
        pg.add_style_tag(content=HIDE_TEXT); pg.wait_for_timeout(300); pg.screenshot(path=str(bgshot))
        fold = tmp / f"page-{a.width}-fold.png"
        Image.open(shot).crop((0, 0, a.width, min(a.height, Image.open(shot).height))).save(fold)
        checks += page_checks(d, str(shot), str(bgshot))
        ws = check_whitespace(str(shot), a.intended, a.axis, str(tmp / "whitespace.png"))
        if ws["status"] == "FAIL":   # on a page, pixels can't tell space from a dark canvas, video or photo
            ws["status"] = "FLAG"; ws["detail"] += " Page mode reads pixels only: a canvas, video or flat image counts as space, so this is a flag; see whitespace.png."
        checks.append(ws)
        checks.append(check_balance(str(fold), str(tmp / "balance.png")))
        pg.close()
        # phone width: text size again, touch targets, sideways scroll
        pm = open_(390, 844); dm = pm.evaluate(JS); pm.screenshot(path=str(tmp / "page-390.png")); pm.close()
        tg = [t for t in dm["targets"] if not t["inline"]]
        small_t = [t for t in tg if t["w"] < 44 or t["h"] < 44]
        checks.append(chk("targets", "Touch targets at 390 px", "UI-5", "FAIL" if small_t else ("PASS" if tg else "SKIP"),
                          f"{len(small_t)}/{len(tg)} controls under 44 x 44" + (f" (smallest {min(min(t['w'], t['h']) for t in small_t):.0f} px)" if small_t else ""),
                          "at least 44 x 44 pt (Apple) / 48 dp (Material); inline links in running text skipped (UI-5)",
                          "; ".join(f"{t['what']} {t['w']:.0f}x{t['h']:.0f}" for t in sorted(small_t, key=lambda t: min(t['w'], t['h']))[:6])))
        small_m = [t for t in dm["texts"] if t["fs"] < 12]
        checks.append(chk("text-size-390", "Minimum text size at 390 px", "TYPE-3", "FAIL" if small_m else "PASS",
                          f"{len(small_m)} text runs under 12 px; smallest {min((t['fs'] for t in dm['texts']), default=0):g} px", "any meaningful text >= 12 px (TYPE-3)",
                          "; ".join(f"\"{t['t'][:24]}\" {t['fs']:g}px" for t in small_m[:5]), blocker=bool(small_m)))
        side = dm["docW"] > dm["vw"] + 1
        # 200% zoom: half-width viewport at device scale 2, as tools/shot.sh does
        pz = open_(a.width // 2, a.height // 2, 2); dz = pz.evaluate(JS); pz.screenshot(path=str(tmp / "page-zoom200.png")); pz.close()
        zside = dz["docW"] > dz["vw"] + 1
        st = "FLAG" if side or zside or dz["clipped"] else "PASS"
        checks.append(chk("reflow", "Sideways scroll and clipped text (phone, 200% zoom)", "UI-10", st,
                          f"sideways scroll: phone {'yes' if side else 'no'}, 200% zoom {'yes' if zside else 'no'}; {len(dz['clipped'])} box(es) clipping their text at 200%",
                          "text scales to 200% without being clipped, overlapping or hiding content (UI-10)",
                          ("Clipped: " + "; ".join(dz["clipped"][:5]) + ". " if dz["clipped"] else "") + "Look at page-zoom200.png: a FLAG is a blocker if content is lost.", blocker=False))
        br.close()
    return dict(target=target, mode="page", size=[a.width, d["docH"]], checks=checks)

def jsonable(o):
    return o.item() if hasattr(o, "item") else str(o)

ORDER = {"FAIL": 0, "FLAG": 1, "PASS": 2, "SKIP": 3}

def report(r):
    lines = [f"autocheck: {r['target']}  ({r['mode']}, {r['size'][0]} x {r['size'][1]})"]
    for c in sorted(r["checks"], key=lambda c: ORDER[c["status"]]):
        tag = c["status"] + ("*" if c["status"] == "FAIL" and c["blocker"] else "")
        lines.append(f"{tag:5s} {c['rule']:16s} {c['name']}: {c['measured'] or '-'}")
        if c["threshold"] and c["status"] != "SKIP": lines.append(f"{'':22s}rule: {c['threshold']}")
        if c["detail"]: lines.append(f"{'':22s}{c['detail']}")
    n = Counter(c["status"] for c in r["checks"])
    lines.append(f"{n['FAIL']} FAIL ({sum(c['blocker'] and c['status'] == 'FAIL' for c in r['checks'])} blocker*), {n['FLAG']} FLAG, {n['PASS']} PASS, {n['SKIP']} SKIP. "
                 "Fix the FAILs first, then judge by eye (critique loop step 3). Quote these numbers; don't estimate them.")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="+"); ap.add_argument("--out", type=pathlib.Path); ap.add_argument("--json", type=pathlib.Path)
    ap.add_argument("--width", type=int, default=1280); ap.add_argument("--height", type=int, default=800)
    ap.add_argument("--settle", type=int, default=1500, help="ms to wait after load (apps that draw after load)")
    ap.add_argument("--text-box", action="append", default=[], help="image mode: x0,y0,x1,y1[:large] around one text line")
    ap.add_argument("--print", help="image mode: printed size, e.g. 420x594mm, for the LAY-9 ppi check")
    ap.add_argument("--intended", default="", help="y ranges of deliberate space for LAY-10, e.g. 300-520")
    ap.add_argument("--axis", choices=["left", "right"], help="declared flush-left/right layout (LAY-10)")
    a = ap.parse_args()
    a.intended = [tuple(int(v) for v in s.split("-")) for s in a.intended.split(",") if s]
    results = []
    for i, t in enumerate(a.targets):
        out = None
        if a.out:
            out = a.out / (re.sub(r"[^\w.-]+", "_", t)[-60:] if len(a.targets) > 1 else ""); out.mkdir(parents=True, exist_ok=True)
        is_img = pathlib.Path(t).suffix.lower() in (".png", ".jpg", ".jpeg", ".webp") and not re.match(r"https?://", t)
        r = run_image(t, a, out) if is_img else run_page(t, a, out)
        txt = report(r); print(txt + ("\n" if i < len(a.targets) - 1 else ""))
        r["summary"] = dict(Counter(c["status"] for c in r["checks"])); results.append(r)
        if out:
            (out / "report.txt").write_text(txt + "\n"); (out / "report.json").write_text(json.dumps(r, indent=1, default=jsonable) + "\n")
    if a.json: a.json.write_text(json.dumps(results if len(results) > 1 else results[0], indent=1, default=jsonable) + "\n")
    sys.exit(1 if any(c["status"] == "FAIL" for r in results for c in r["checks"]) else 0)

if __name__ == "__main__":
    main()
