#!/usr/bin/env python3
"""creative-director v2 CLI front door.

Commands:
  cd.py brief init "Description" --out brief.json
  cd.py taste init --out taste.json
  cd.py load --brief brief.json [--taste taste.json]
  cd.py rule <ID>
  cd.py check TARGET --brief brief.json [--taste taste.json] [--boxes ...] [--observations ...]
  cd.py select r1.png r2.png r3.png --brief brief.json [--review review.json] [--owner-choice R2]
  cd.py compose spec.json --out final.png [--html final.html]
  cd.py generate-docs

See manifest.json and tools/brief.md for schemas. Zero dependencies beyond stdlib + Pillow/NumPy.
"""
import argparse
from collections import Counter
import csv
import difflib
import hashlib
import io
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'manifest.json'
BRIEF = ROOT / 'tools' / 'brief-template.json'
TASTE_DEFAULT = ROOT / 'taste.default.json'
RULE_HEADING = re.compile(r'^#{2,6}\s+(?:\*\*)?([A-Z0-9][A-Z0-9]*(?:-[A-Z0-9]+)*-\d+)\b.*$', re.M)
VALID_TIERS = ('', 'fast', 'directed', 'remake')
VALID_CONTEXT_MODES = ('isolated-subagent', 'separate-session', 'same-session-self-review')
REMAKE_WORDS = ('from scratch', 'redo', 'rejig', 'start over', 'reimagine', 'rethink')
OCR_MIN_CONFIDENCE = 50


def emit(value):
    print(json.dumps(value, indent=2, ensure_ascii=False))


def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


# Backward-compatible alias used by older tests/callers
load = load_json


def load_manifest():
    return load_json(MANIFEST_PATH)


def rel_posix(path):
    return Path(path).resolve().relative_to(ROOT.resolve()).as_posix()


def approx_tokens(paths):
    total = 0
    for rel in paths:
        p = ROOT / rel
        if p.is_file():
            total += round(len(p.read_text(encoding='utf-8')) / 4)
    return total


def read_brief(path, require_medium=True):
    b = load_json(path)
    if not isinstance(b, dict) or type(b.get('schema_version')) is not int or b.get('schema_version') not in (1, 2):
        raise ValueError('brief schema_version must be 1 or 2')
    for field in ('description', 'idea', 'feeling', 'audience', 'purpose', 'success'):
        if not isinstance(b.get(field), str):
            raise ValueError(f'brief {field} must be a string')
    tier = b.get('tier', '')
    if not isinstance(tier, str) or tier not in VALID_TIERS:
        raise ValueError(f'brief tier must be one of {VALID_TIERS}')
    b.setdefault('tier', '')
    intent_tags = b.get('intent_tags', [])
    if not isinstance(intent_tags, list) or not all(isinstance(x, str) for x in intent_tags):
        raise ValueError('brief intent_tags must be a list of strings')
    b.setdefault('intent_tags', [])
    if not isinstance(b.get('medium'), str) or (require_medium and not b['medium'].strip()):
        raise ValueError('brief medium must be a nonempty string (fill it after brief init)')
    if type(b.get('has_people_or_animals')) is not bool:
        raise ValueError('brief has_people_or_animals must be boolean')
    for field in ('constraints', 'must_be_right'):
        if not isinstance(b.get(field), list) or not all(isinstance(x, str) for x in b[field]):
            raise ValueError(f'brief {field} must be a list of strings')
    f = b.get('format', {})
    if not isinstance(f, dict):
        raise ValueError('format must be an object')
    for k in ('width', 'height'):
        if type(f.get(k)) is not int or f[k] < 1:
            raise ValueError(f'format.{k} must be a positive integer in pixels')
    if f.get('kind') not in ('fixed', 'screen'):
        raise ValueError('format.kind must be fixed or screen')
    if type(b.get('safe_area_px')) not in (int, float) or not math.isfinite(b['safe_area_px']) or b['safe_area_px'] < 0:
        raise ValueError('safe_area_px must be non-negative')
    if 2 * b['safe_area_px'] >= min(f['width'], f['height']):
        raise ValueError('safe area leaves no usable frame')
    for field, key in (('copy', 'text'), ('counts', 'item')):
        if not isinstance(b.get(field), list):
            raise ValueError(f'{field} must be a list')
        seen = set()
        for x in b[field]:
            if not isinstance(x, dict) or not isinstance(x.get(key), str) or not x[key] or '\n' in x[key] or '\r' in x[key] or x[key] in seen:
                raise ValueError(f'{field}: nonempty unique {key} required')
            if type(x.get('count')) is not int or x['count'] < 0:
                raise ValueError(f'{field}: count must be a non-negative integer')
            seen.add(x[key])
    if type(b.get('exact_copy')) is not bool:
        raise ValueError('exact_copy must be boolean')
    return b


def read_taste(taste_path=None, brief_path=None):
    """Load an explicit taste.json, a sibling taste.json beside brief.json, or taste.default.json."""
    chosen = None
    source = 'default'
    if taste_path:
        chosen = Path(taste_path)
        if not chosen.is_file():
            raise ValueError(f'taste profile not found: {taste_path}')
        source = str(chosen)
    elif brief_path:
        sibling = Path(brief_path).resolve().parent / 'taste.json'
        if sibling.is_file():
            chosen = sibling
            source = str(sibling)
    if chosen is None:
        if TASTE_DEFAULT.is_file():
            chosen = TASTE_DEFAULT
            source = 'taste.default.json'
        else:
            return None, 'none'
    if chosen.suffix.lower() in ('.yaml', '.yml'):
        try:
            import yaml
        except ImportError as exc:
            raise ValueError('YAML taste profiles require PyYAML; use JSON (.json) for zero-dependency support') from exc
        data = yaml.safe_load(chosen.read_text(encoding='utf-8'))
    else:
        data = load_json(chosen)
    if not isinstance(data, dict):
        raise ValueError('taste profile must be a JSON object')
    return data, source


def rules():
    """Canonical root files only; normalized to POSIX relative paths on all platforms."""
    found = {}
    for p in sorted([*(ROOT / 'core').glob('*.md'), *(ROOT / 'modules').glob('*/*.md')]):
        text = p.read_text(encoding='utf-8')
        rel = p.relative_to(ROOT).as_posix()
        for m in RULE_HEADING.finditer(text):
            level = len(m.group().split()[0])
            end = re.search(r'^#{1,' + str(level) + r'}\s', text[m.end():], re.M)
            block = text[m.start():m.end() + end.start() if end else len(text)].strip()
            rid = m.group(1)
            if rid in found:
                raise ValueError(f'ambiguous rule {rid}: {found[rid][0]} and {rel}')
            found[rid] = (rel, block)
    return found


def result(cid, status, provenance, **extra):
    return dict(id=cid, status=status, passed=status == 'PASS', provenance=provenance, **extra)


def copy_check(b, text, provenance, fallible_ocr=False):
    if text is None:
        return result('copy', 'SKIP', provenance, reason='No rendered text evidence; cannot certify CD-7.')
    observed = Counter(text.splitlines())
    expected = Counter({x['text']: x['count'] for x in b['copy']})
    missing = list((expected - observed).elements())
    extra = list((observed - expected).elements()) if b['exact_copy'] else [line for line, n in (observed - expected).items() if line in expected for _ in range(n)]
    return result('copy', ('FLAG' if fallible_ocr else 'FAIL') if missing or extra else 'PASS', provenance, rule='CD-7',
                  missing=missing, extra=extra, observed=dict(observed),
                  diff=list(difflib.ndiff(list(expected.elements()), text.splitlines())))


def ocr_image(target):
    if not shutil.which('tesseract'):
        return None, [], 'tesseract unavailable; install it or supply --ocr-text'
    p = subprocess.run(['tesseract', str(target), 'stdout', 'tsv'], capture_output=True, text=True, timeout=90)
    if p.returncode:
        raise ValueError('tesseract failed: ' + p.stderr.strip())
    groups = {}
    boxes = {}
    for row in csv.DictReader(io.StringIO(p.stdout), delimiter='\t', quoting=csv.QUOTE_NONE):
        if row['level'] != '5' or not row['text'].strip() or float(row['conf']) < OCR_MIN_CONFIDENCE:
            continue
        key = tuple(row[k] for k in ('page_num', 'block_num', 'par_num', 'line_num'))
        groups.setdefault(key, []).append(row['text'])
        x, y, w, h = (int(row[k]) for k in ('left', 'top', 'width', 'height'))
        old = boxes.get(key, [x, y, x + w, y + h])
        boxes[key] = [min(old[0], x), min(old[1], y), max(old[2], x + w), max(old[3], y + h)]
    return '\n'.join(' '.join(words) for words in groups.values()), list(boxes.values()), f'tesseract TSV on current render; confidence >= {OCR_MIN_CONFIDENCE} (fallible; verify visually)'


def text_manifest(path):
    """Code-set text: [text, [x0,y0,x1,y1], [r,g,b]] per rendered line."""
    rows = load_json(path)
    if not isinstance(rows, list):
        raise ValueError('boxes manifest must be a list')
    for row in rows:
        if not isinstance(row, list) or len(row) != 3 or not isinstance(row[0], str) or '\n' in row[0] or '\r' in row[0]:
            raise ValueError('boxes manifest rows need text, box and RGB')
        box, rgb = row[1:]
        if not isinstance(box, list) or len(box) != 4 or not all(type(v) in (int, float) and math.isfinite(v) for v in box) or min(box[:2]) < 0 or box[2] <= box[0] or box[3] <= box[1]:
            raise ValueError('invalid manifest text box')
        if not isinstance(rgb, list) or len(rgb) != 3 or not all(type(v) in (int, float) and math.isfinite(v) and 0 <= v <= 255 for v in rgb):
            raise ValueError('invalid manifest RGB')
    return '\n'.join(row[0] for row in rows), [row[1] for row in rows]


def manifest_to_text_boxes(boxes):
    """Convert manifest bounding boxes into autocheck --text-box specs (estimating :large for tall display lines)."""
    specs = []
    for box in boxes:
        x0, y0, x1, y1 = (int(round(v)) for v in box)
        if x1 <= x0 or y1 <= y0:
            continue
        suffix = ':large' if (y1 - y0) >= 28 else ''
        specs.append(f'{x0},{y0},{x1},{y1}{suffix}')
    return specs


def copy_crops(target, boxes, missing):
    """Candidate OCR regions, not proof: missing lines may be anywhere in the frame."""
    from PIL import Image
    target = Path(target)
    dest = target.with_name(target.stem + '-copy-crops')
    dest.mkdir(exist_ok=True)
    crops = []
    with Image.open(target) as im:
        regions = list(boxes)
        if missing or not regions:
            regions.append([0, 0, im.width, im.height])
        for i, box in enumerate(regions):
            x0, y0, x1, y1 = box
            bounds = [max(0, math.floor(x0) - 8), max(0, math.floor(y0) - 8),
                      min(im.width, math.ceil(x1) + 8), min(im.height, math.ceil(y1) + 8)]
            crop = im.crop(bounds)
            crop.thumbnail((640, 320))
            path = dest / f'region-{i + 1}.png'
            crop.save(path)
            crops.append(dict(box=bounds, path=str(path)))
    return crops


def check(a):
    b = read_brief(a.brief)
    taste, taste_source = read_taste(getattr(a, 'taste', None), a.brief)
    page = bool(re.match(r'https?://', a.target)) or Path(a.target).suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp')

    # Pre-discover text manifest on images so its geometry feeds autocheck contrast automatically.
    text, boxes, source = None, [], 'no OCR evidence'
    fallible_ocr = False
    auto_text_boxes = list(a.text_box)
    if not page:
        manifest = Path(a.boxes) if a.boxes else Path(a.target).with_name(Path(a.target).stem + '-boxes.json')
        if a.boxes or manifest.is_file():
            text, boxes = text_manifest(manifest)
            source = 'code-set text manifest: ' + str(manifest)
            if not auto_text_boxes:
                auto_text_boxes.extend(manifest_to_text_boxes(boxes))

    with tempfile.TemporaryDirectory(prefix='cd-check-') as tmp:
        report = Path(tmp) / 'autocheck.json'
        cmd = [sys.executable, str(ROOT / 'tools/autocheck.py'), a.target, '--json', str(report),
               '--width', str(b['format']['width']), '--height', str(b['format']['height'])]
        for box in auto_text_boxes:
            cmd += ['--text-box', box]
        if taste and isinstance(taste.get('whites'), dict) and taste['whites'].get('default') == 'warm':
            reason = taste['whites'].get('warm_reason') or f"taste profile ({taste.get('name', 'custom')})"
            cmd += ['--warm', reason]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
        if p.returncode not in (0, 1) or not report.exists():
            raise ValueError('autocheck failed: ' + p.stderr.strip()[-1200:])
        measured = load_json(report)

    if page:
        text, source = measured.get('text'), 'autocheck visible DOM text (not OCR; verify image/canvas text by eye)'
        boxes = [r for t in measured.get('text_runs', []) for r in t['rects']]
    elif not source.startswith('code-set text manifest:') and not a.no_ocr and not a.ocr_text:
        text, boxes, source = ocr_image(a.target)
        fallible_ocr = True

    if a.ocr_text and not source.startswith('code-set text manifest:'):
        text, source = Path(a.ocr_text).read_text(encoding='utf-8').rstrip('\n'), 'supplied render transcript: ' + str(a.ocr_text)
        fallible_ocr = False
    if a.text_box:
        for box in a.text_box:
            vals = [int(v) for v in box.split(':')[0].split(',')]
            if len(vals) != 4 or vals[0] < 0 or vals[1] < 0 or vals[2] <= vals[0] or vals[3] <= vals[1]:
                raise ValueError('text boxes require x0,y0,x1,y1 within the frame')
            boxes.append(vals)

    missing_intent = [k for k in ('idea', 'feeling', 'audience', 'purpose', 'success') if not b[k].strip()]
    copy_result = copy_check(b, text, source, fallible_ocr=fallible_ocr)
    if copy_result['status'] == 'FLAG':
        suspect = [box for line, box in zip(text.splitlines(), boxes) if line in copy_result['extra']]
        copy_result.update(crop_boxes=suspect, crops=copy_crops(a.target, suspect, copy_result['missing']),
                           reason='Fallible OCR mismatch: read candidate crops and whole-frame overview for missed lettering.')
    checks = [result('brief-intent', 'SKIP' if missing_intent else 'PASS', 'structured brief; not an aesthetic judgement', missing=missing_intent), copy_result]

    evidence = load_json(a.observations) if a.observations else {}
    if not isinstance(evidence, dict) or not isinstance(evidence.get('counts', {}), dict):
        raise ValueError('observations must be an object with a counts object')
    if evidence:
        if page or evidence.get('target_sha256') != hashlib.sha256(Path(a.target).read_bytes()).hexdigest():
            raise ValueError('count observations must name the SHA-256 of the current local image')
    for item in b['counts']:
        obs = evidence.get('counts', {}).get(item['item'])
        if obs is not None and (not isinstance(obs, dict) or type(obs.get('count')) is not int or obs['count'] < 0 or not obs.get('provenance')):
            raise ValueError('count observation needs non-negative integer count and provenance')
        checks.append(result('count:' + item['item'], 'SKIP' if obs is None else ('PASS' if obs['count'] == item['count'] else 'FAIL'),
                             obs['provenance'] if obs else 'no crop/count evidence supplied', rule='CD-7', expected=item['count'], observed=obs))
    if not b['counts']:
        checks.append(result('counts', 'PASS', 'brief has no fixed object counts', rule='CD-7'))

    for cid in ('contrast', 'text-size'):
        c = next((c for c in measured['checks'] if c['id'] == cid), None)
        checks.append(result(cid, c['status'] if c else 'SKIP', 'tools/autocheck.py (uses contrast.py)', measurement=c))

    width, height = measured['size']
    margin = b['safe_area_px']
    bad = [box for box in boxes if min(box[0], box[1], width - box[2], height - box[3]) < margin]
    checks.append(result('safe-area', 'FAIL' if bad else ('PASS' if boxes else 'SKIP'),
                         source + '; text geometry plus supplied boxes; non-text key elements still need visual review',
                         rule='LAY-5', margin_px=margin, outside=bad, measured_boxes=len(boxes)))
    checks.append(result('format', 'PASS' if [width, height] == [b['format']['width'], b['format']['height']] else 'FAIL',
                         'autocheck rendered size', expected=b['format'], observed=[width, height]))
    complete = all(c['status'] in ('PASS', 'FLAG') for c in checks) and not any(c['status'] == 'FAIL' for c in measured['checks'])
    flagged = any(c['status'] == 'FLAG' for c in checks)
    status = ('FLAG' if flagged else 'PASS') if complete else 'FAIL'
    emit(dict(schema_version=2, target=a.target, passed=complete and not flagged, status=status, checks=checks,
              taste_profile=taste_source, autocheck=measured, unverified_brief_conditions=b['must_be_right'],
              scope='Mechanical checks only. SKIP/FLAG is not a pass; review OCR, figures, marks and intent visually.'))
    return 0 if complete else 1


def select(a):
    b = read_brief(a.brief, require_medium=False)
    if not 2 <= len(a.roughs) <= 8 or len(set(a.roughs)) != len(a.roughs):
        raise ValueError('select needs 2–8 distinct rough files (3 recommended for Tier 2)')
    for path in a.roughs:
        if not Path(path).is_file():
            raise ValueError('rough not found: ' + path)
    ids = [f'R{i + 1}' for i in range(len(a.roughs))]
    mode = getattr(a, 'mode', None) or ('pairwise' if len(ids) <= 4 else 'bracket')
    if mode not in ('pairwise', 'bracket', 'ranked'):
        raise ValueError('mode must be pairwise, bracket, or ranked')

    review_template = dict(
        context_mode='isolated-subagent',
        mode=mode,
        comparisons=[dict(a='R1', b='R2', stronger='R1', reason='', trade_off='', confidence='medium')],
        shortlist=ids[:min(2, len(ids))],
    )
    packet = dict(
        schema_version=2,
        stage='review-needed',
        mode=mode,
        brief=b,
        roughs=dict(zip(ids, a.roughs)),
        instruction=(
            'Compare roughs against idea, feeling, and must_be_right. Use an isolated subagent or separate session '
            'without maker rationale when available; otherwise record context_mode="same-session-self-review" honestly. '
            'Name visible differences and trade-offs. Show the top 2–3 to the owner; only their winner enters the fix loop. '
            '"The original is better" is a valid stop.'
        ),
        review_template=review_template,
    )

    if a.review:
        review = load_json(a.review)
        if not isinstance(review, dict):
            raise ValueError('review must be a JSON object')
        # Honest context mode: support v2 context_mode or legacy same_model/fresh_context fields.
        if 'context_mode' in review:
            ctx = review['context_mode']
            if ctx not in VALID_CONTEXT_MODES:
                raise ValueError(f'context_mode must be one of {VALID_CONTEXT_MODES}')
        elif review.get('same_model') is True and review.get('fresh_context') is True:
            ctx = 'separate-session'
        else:
            raise ValueError(f'review must set context_mode ({", ".join(VALID_CONTEXT_MODES)})')

        review_mode = review.get('mode', mode)
        comps = review.get('comparisons')
        if review_mode in ('pairwise', 'bracket'):
            if not isinstance(comps, list) or not comps:
                raise ValueError('review needs a nonempty comparisons list')
            pairs = set()
            touched = set()
            for pair in comps:
                if not isinstance(pair, dict):
                    raise ValueError('comparison must be an object')
                x, y = pair.get('a'), pair.get('b')
                if x not in ids or y not in ids or x == y or pair.get('stronger') not in (x, y, None):
                    raise ValueError('invalid head-to-head comparison')
                key = tuple(sorted((x, y)))
                if key in pairs:
                    raise ValueError('duplicate pair')
                if not pair.get('reason') or not pair.get('trade_off') or pair.get('confidence') not in ('high', 'medium', 'low'):
                    raise ValueError('each pair needs reason, trade_off and confidence')
                pairs.add(key)
                touched.update((x, y))
            if review_mode == 'pairwise' and len(pairs) != len(ids) * (len(ids) - 1) // 2:
                raise ValueError('pairwise mode requires comparing every pair before shortlisting')
            if review_mode == 'bracket' and touched != set(ids):
                raise ValueError('bracket mode must evaluate every rough in at least one comparison')
        elif review_mode == 'ranked':
            ranking = review.get('ranking')
            if not isinstance(ranking, list) or len(ranking) != len(ids) or set(r.get('id') for r in ranking if isinstance(r, dict)) != set(ids):
                raise ValueError('ranked mode requires a ranking entry for every rough ID')
            for r in ranking:
                if not r.get('reason') or not r.get('trade_off'):
                    raise ValueError('each ranked entry needs reason and trade_off')
        else:
            raise ValueError('review mode must be pairwise, bracket, or ranked')

        shortlist = review.get('shortlist', [])
        max_short = min(3, len(ids))
        min_short = min(2, len(ids))
        if not isinstance(shortlist, list) or not all(isinstance(x, str) for x in shortlist) or not (min_short <= len(shortlist) <= max_short) or len(set(shortlist)) != len(shortlist) or not set(shortlist) <= set(ids):
            raise ValueError(f'shortlist must hold {min_short}–{max_short} distinct rough IDs')
        if a.owner_choice and a.owner_choice not in shortlist:
            raise ValueError('owner choice must be in the shortlist')
        packet.update(
            stage='winner-ready' if a.owner_choice else 'awaiting-owner',
            context_mode=ctx,
            mode=review_mode,
            review=review,
            winner=a.owner_choice,
            choice_provenance='caller-supplied owner choice; not inferred by this tool',
        )
    elif a.owner_choice:
        raise ValueError('--owner-choice needs a completed --review')
    emit(packet)
    return 0


def normalise(text):
    return text.lower().replace('’', "'").replace('“', '"').replace('”', '"')


def has_word(text, phrase):
    return re.search(r'(?<![a-z0-9])' + re.escape(normalise(phrase)) + r'(?![a-z0-9])', normalise(text)) is not None


def haystack(brief):
    parts = [brief.get(key, '') or '' for key in ('description', 'idea', 'feeling', 'audience', 'purpose', 'success')]
    parts.extend(brief.get('constraints') or [])
    parts.extend(brief.get('must_be_right') or [])
    parts.extend(brief.get('intent_tags') or [])
    return ' '.join(str(p) for p in parts)


def infer_tier(brief):
    if brief.get('tier'):
        return brief['tier']
    probe = normalise(' '.join((brief.get('description', ''), brief.get('medium', ''), brief.get('purpose', ''))))
    if any(has_word(probe, w) for w in REMAKE_WORDS):
        return 'remake'
    if any(has_word(probe, w) for w in ('consult', 'quick fix', 'self-check', 'edit only', 'tweak')):
        return 'fast'
    return 'directed'


def load_plan(brief, taste=None, taste_source='default'):
    manifest = load_manifest()
    index = rules()
    medium = normalise(brief['medium'].strip())
    full_text = normalise(haystack(brief))
    intent_text = normalise(' '.join([
        brief.get('feeling', ''),
        brief.get('purpose', ''),
        brief.get('idea', ''),
        ' '.join(brief.get('intent_tags') or []),
    ]))

    tier = infer_tier(brief)
    tier_info = manifest['tiers'][tier]
    energetic = any(has_word(intent_text, trig) for trig in manifest.get('energy_triggers', []))

    files = []
    optional_files = []
    matched = []
    groups = []
    reasons = []
    explicit_rule_ids = set()

    # Tier-level core docs (keep Tier 1 fast lean; add direction/remake guides on demand).
    for cf in tier_info.get('core_files', []):
        files.append(cf)

    # Match routes declaratively from manifest.json.
    for route in manifest['routes']:
        hit = False
        matched_label = None
        for m in route.get('media', []):
            if has_word(medium, m) or (medium and medium == normalise(m)):
                hit = True
                matched_label = route['id']
                break
        if not hit and route.get('format_kind') and brief['format']['kind'] == route['format_kind']:
            hit = True
            matched_label = 'screen'
        if not hit and route.get('brief_flag') and brief.get(route['brief_flag']) is True:
            hit = True
            matched_label = route['id']
        if not hit and route.get('text_triggers'):
            if any(has_word(full_text, phrase) for phrase in route['text_triggers']):
                hit = True
                matched_label = route['id']
        if not hit:
            continue

        matched.append(matched_label)
        groups.append(route.get('group', 'core-visual'))
        reasons.append(route['label'])
        files.extend(route.get('files', []))
        optional_files.extend(route.get('optional_files', []))
        explicit_rule_ids.update(route.get('rules', []))

    # Explicit command triggers (bolder / quieter / distill).
    if any(has_word(medium, w) for w in ('bolder', 'quieter', 'distill')):
        files.append('core/commands.md')
        reasons.append('Nudge command (bolder / quieter / distill)')

    # Intent-gated energy pass (never inferred from medium alone).
    if energetic:
        files.append('core/energy-pass.md')
        reasons.append('Energy pass triggered by brief intent/feeling')

    # Delivery placement & always-on craft guardrails for visual work (skipped for pure writing briefs).
    explicit_rule_ids.add('CD-5')
    pure_writing = bool(matched) and set(matched) == {'writing-optional'}
    if not pure_writing:
        files.insert(0, 'modules/composition/sitting-right.md')
        explicit_rule_ids.update(('CORE-11', 'COMP-19', 'COMP-23', 'EN-5', 'EN-6'))
        reasons.append('Delivery guard: balance, dead-space, and EN-5/EN-6 craft ceiling apply to visual work')

    files = list(dict.fromkeys(files))
    optional_files = [p for p in dict.fromkeys(optional_files) if p not in files]

    # Collect all canonical rule IDs defined inside the loaded files, plus explicitly cited route IDs.
    file_set = set(files)
    rule_ids = set(explicit_rule_ids & index.keys())
    for rid, (path, _) in index.items():
        if path in file_set:
            rule_ids.add(rid)
    # Include the canonical file for any explicit rule ID not yet listed (respecting energy gate).
    for rid in sorted(rule_ids):
        rpath = index[rid][0]
        if rpath == 'core/energy-pass.md' and not energetic:
            continue
        if rpath not in file_set and rpath.startswith(('modules/', 'core/')):
            # Only add if it's a module file (avoid pulling core/principles.md implicitly).
            if rpath.startswith('modules/'):
                files.append(rpath)
                file_set.add(rpath)

    # Filter hard gates relevant to this brief.
    scopes = {'all'}
    if brief['format']['kind'] == 'screen':
        scopes.add('screen')
    else:
        scopes.add('fixed')
    if brief['has_people_or_animals']:
        scopes.add('people_or_animals')
    if 'infographic' in matched:
        scopes.add('infographic')
    if '3d-optional' in matched:
        scopes.add('3d')
    if 'film-optional' in matched:
        scopes.add('film')
    if any(m in matched for m in ('logo-mark', 'brand-system', 'print-packaging-slides')):
        scopes.add('brand')
    if any(m in matched for m in ('illustration-drawing', 'photo')):
        scopes.update(('illustration', 'photo', '3d_space'))
    if 'construction-only' in matched:
        scopes.add('3d_space')
    if 'print-packaging-slides' in matched:
        scopes.add('print')

    applicable_gates = [
        g['id'] for g in manifest.get('hard_gates', [])
        if set(g['scope'].split(',')) & scopes
    ]

    taste_summary = None
    if taste:
        taste_summary = dict(
            source=taste_source,
            name=taste.get('name', 'custom'),
            english_variety=taste.get('english_variety', 'en-GB'),
            whites=(taste.get('whites') or {}).get('default', 'neutral'),
            finish_ceiling=taste.get('finish_ceiling', 'restrained'),
            avoid_typefaces=taste.get('avoid_typefaces', []),
        )

    return dict(
        schema_version=2,
        tier=tier,
        tier_label=tier_info['label'],
        roughs=tier_info['roughs'],
        max_rounds=tier_info['max_rounds'],
        matched=list(dict.fromkeys(matched)),
        groups=list(dict.fromkeys(groups)),
        energetic=energetic,
        files=files,
        optional_files=optional_files,
        rules=sorted(rule_ids),
        hard_gates=applicable_gates,
        estimated_tokens=approx_tokens(files),
        taste=taste_summary,
        reasons=reasons,
        instruction='Always-on kernel is AGENTS.md + core/kernel.md. Read the listed files for this task, use cd.py rule <ID> for single lookups, and run cd.py check on renders.',
    )


def generate_which_modules():
    """Regenerate core/which-modules.md from manifest.json so routing docs never drift."""
    manifest = load_manifest()
    lines = [
        '# Which modules to load (generated from `manifest.json`)',
        '',
        'Always load `AGENTS.md` and `core/kernel.md` (≤ 1,600 tokens). Everything else loads on demand via `python3 tools/cd.py load --brief brief.json` or `python3 tools/cd.py rule <ID>`.',
        '',
        'Do not edit this routing table by hand — edit `manifest.json` and run `python3 tools/cd.py generate-docs`.',
        '',
        '## Task routes (`core-visual` and `optional-domain`)',
        '',
        '| Route | Group | Media / Triggers | Files loaded |',
        '|---|---|---|---|',
    ]
    for r in manifest['routes']:
        grp = r.get('group', 'core-visual')
        triggers = ', '.join(r.get('media', [])[:6])
        if r.get('brief_flag'):
            triggers += f" (or `{r['brief_flag']}: true`)"
        if r.get('format_kind'):
            triggers += f" (or `format.kind: {r['format_kind']}`)"
        flist = ', '.join(f'`{f}`' for f in r.get('files', []))
        lines.append(f"| {r['label']} | `{grp}` | {triggers} | {flist} |")

    lines += [
        '',
        '## Module index',
        '',
        '| Module | Group | Entry | Extra files | Covers |',
        '|---|---|---|---|---|',
    ]
    for name, info in manifest['modules'].items():
        extras = ', '.join(f'`{Path(e).name}`' for e in info.get('extra_files', [])) or '—'
        lines.append(f"| `{name}` | `{info['group']}` | `{info['entry']}` | {extras} | {info['summary']} |")

    lines += [
        '',
        '## Energy triggers (intent-gated only)',
        '',
        '`core/energy-pass.md` loads only when the brief\'s `feeling`, `purpose`, `idea`, or `intent_tags` match an energetic intent — never from `medium` alone:',
        '',
        ', '.join(f'`{t}`' for t in manifest.get('energy_triggers', [])),
        '',
        '## Maturity',
        '',
        'The `web-ui` and `ux` modules, and the infographic recipes in `modules/layout/infographics.md`, are less mature than the rest. Blind-test Batch 9, which covers screens and infographics, is drawn and waiting to be judged.',
        '',
        '## Token budgets',
        '',
        'Run `python3 tools/check_budgets.py --loads` for live token counts. Budgets are enforced in CI on both Linux and Windows.',
        '',
    ]
    out = ROOT / 'core' / 'which-modules.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    return str(out.relative_to(ROOT).as_posix())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='command', required=True)

    bp = sub.add_parser('brief', help='Create a structured brief')
    bs = bp.add_subparsers(dest='action', required=True)
    bi = bs.add_parser('init')
    bi.add_argument('description', nargs='?', default='')
    bi.add_argument('--out', default='brief.json')

    tp = sub.add_parser('taste', help='Manage project taste profiles')
    ts = tp.add_subparsers(dest='action', required=True)
    ti = ts.add_parser('init')
    ti.add_argument('--out', default='taste.json')

    cp = sub.add_parser('check', help='Mechanical checks as JSON; missing evidence never passes')
    cp.add_argument('target')
    cp.add_argument('--brief', default='brief.json')
    cp.add_argument('--taste', help='Optional taste.json profile (auto-discovers sibling taste.json)')
    cp.add_argument('--boxes', help='Code-set text manifest [text, box, RGB]; auto-detects <stem>-boxes.json')
    cp.add_argument('--ocr-text', help='UTF-8 rendered line transcript; provenance is labelled')
    cp.add_argument('--no-ocr', action='store_true')
    cp.add_argument('--text-box', action='append', default=[])
    cp.add_argument('--observations', help='Count evidence bound to the current image SHA-256')

    rp = sub.add_parser('rule', help='Print the canonical definition of an existing rule')
    rp.add_argument('id')

    lp = sub.add_parser('load', help='Route a brief to required modules, tier, hard gates, and rules')
    lp.add_argument('--brief', default='brief.json')
    lp.add_argument('--taste', help='Optional taste.json profile')

    sp = sub.add_parser('select', help='Prepare or validate a rough-selection packet (2–8 roughs)')
    sp.add_argument('roughs', nargs='+')
    sp.add_argument('--brief', default='brief.json')
    sp.add_argument('--mode', choices=('pairwise', 'bracket', 'ranked'))
    sp.add_argument('--review')
    sp.add_argument('--owner-choice')

    comp = sub.add_parser('compose', help='Deterministically composite art, locked copy, logos, and charts')
    comp.add_argument('spec', help='Composition spec JSON')
    comp.add_argument('--out', required=True, help='Output PNG path (also writes <stem>-boxes.json)')
    comp.add_argument('--html', help='Optional standalone HTML/SVG export path')

    sub.add_parser('generate-docs', help='Regenerate core/which-modules.md from manifest.json')

    a = ap.parse_args()
    try:
        if a.command == 'brief':
            b = load_json(BRIEF)
            b['description'] = a.description
            with Path(a.out).open('x', encoding='utf-8') as out:
                out.write(json.dumps(b, indent=2, ensure_ascii=False) + '\n')
            emit(dict(path=a.out, status='created', next='Fill medium, idea, feeling, audience, purpose, success, and copy/counts.'))
            return 0
        if a.command == 'taste':
            t = load_json(TASTE_DEFAULT)
            with Path(a.out).open('x', encoding='utf-8') as out:
                out.write(json.dumps(t, indent=2, ensure_ascii=False) + '\n')
            emit(dict(path=a.out, status='created', next='Edit personal/brand preferences; universal hard gates remain in core/kernel.md.'))
            return 0
        if a.command == 'rule':
            found = rules().get(a.id.upper())
            if found is None:
                raise ValueError('unknown rule ID: ' + a.id + '; see docs/RETIRED-IDS.md for merged IDs')
            print(f'<!-- {found[0]} -->\n{found[1]}')
            return 0
        if a.command == 'load':
            brief = read_brief(a.brief)
            taste, tsrc = read_taste(a.taste, a.brief)
            emit(load_plan(brief, taste=taste, taste_source=tsrc))
            return 0
        if a.command == 'compose':
            cmd = [sys.executable, str(ROOT / 'tools' / 'compose.py'), a.spec, '--out', a.out]
            if a.html:
                cmd += ['--html', a.html]
            p = subprocess.run(cmd, capture_output=True, text=True)
            if p.returncode != 0:
                raise ValueError((p.stderr or p.stdout).strip())
            print(p.stdout.strip())
            return 0
        if a.command == 'generate-docs':
            written = generate_which_modules()
            emit(dict(status='generated', files=[written]))
            return 0
        return check(a) if a.command == 'check' else select(a)
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as e:
        emit(dict(schema_version=2, status='ERROR', passed=False, error=str(e)))
        return 2


if __name__ == '__main__':
    sys.exit(main())
