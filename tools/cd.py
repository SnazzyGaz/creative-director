#!/usr/bin/env python3
"""In-repo creative-director front door. See tools/brief.md for the JSON contract."""
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

ROOT = Path(__file__).resolve().parents[1]
BRIEF = ROOT / 'tools' / 'brief-template.json'
RULE_HEADING = re.compile(r'^#{2,6}\s+(?:\*\*)?([A-Z0-9][A-Z0-9]*(?:-[A-Z0-9]+)*-\d+)\b.*$', re.M)


def emit(value):
    print(json.dumps(value, indent=2, ensure_ascii=False))


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def read_brief(path, require_medium=True):
    b = load(path)
    if not isinstance(b, dict) or type(b.get('schema_version')) is not int or b.get('schema_version') != 1:
        raise ValueError('brief schema_version must be 1')
    for field in ('description', 'idea', 'feeling', 'audience', 'purpose', 'success'):
        if not isinstance(b.get(field), str):
            raise ValueError(f'brief {field} must be a string')
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


def rules():
    """Canonical root files only; ignore mirrors, notes, examples and retired IDs."""
    found = {}
    for p in sorted([*(ROOT / 'core').glob('*.md'), *(ROOT / 'modules').glob('*/*.md')]):
        text = p.read_text(encoding='utf-8')
        for m in RULE_HEADING.finditer(text):
            # End at the next heading of the same or higher level, not a subheading.
            level = len(m.group().split()[0])
            end = re.search(r'^#{1,' + str(level) + r'}\s', text[m.end():], re.M)
            block = text[m.start():m.end() + end.start() if end else len(text)].strip()
            rid = m.group(1)
            if rid in found:
                raise ValueError(f'ambiguous rule {rid}: {found[rid][0]} and {p.relative_to(ROOT)}')
            found[rid] = (str(p.relative_to(ROOT)), block)
    return found


def result(cid, status, provenance, **extra):
    return dict(id=cid, status=status, passed=status == 'PASS', provenance=provenance, **extra)


def copy_check(b, text, provenance, fallible_ocr=False):
    if text is None:
        return result('copy', 'SKIP', provenance, reason='No rendered text evidence; cannot certify CD-7.')
    # Each entry is a complete rendered line (DOM: a visible text run).
    observed = Counter(text.splitlines())
    expected = Counter({x['text']: x['count'] for x in b['copy']})
    missing = list((expected - observed).elements())
    extra = list((observed - expected).elements()) if b['exact_copy'] else [line for line, n in (observed - expected).items() if line in expected for _ in range(n)]
    return result('copy', ('FLAG' if fallible_ocr else 'FAIL') if missing or extra else 'PASS', provenance, rule='CD-7',
                  missing=missing, extra=extra, observed=dict(observed),
                  diff=list(difflib.ndiff(list(expected.elements()), text.splitlines())))


# Tesseract word confidence is 0–100; -1 denotes non-word/no confidence.
OCR_MIN_CONFIDENCE = 50


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
    rows = load(path)
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
    page = bool(re.match(r'https?://', a.target)) or Path(a.target).suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp')
    with tempfile.TemporaryDirectory(prefix='cd-check-') as tmp:
        report = Path(tmp) / 'autocheck.json'
        cmd = [sys.executable, str(ROOT / 'tools/autocheck.py'), a.target, '--json', str(report),
               '--width', str(b['format']['width']), '--height', str(b['format']['height'])]
        for box in a.text_box:
            cmd += ['--text-box', box]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
        if p.returncode not in (0, 1) or not report.exists():
            raise ValueError('autocheck failed: ' + p.stderr.strip()[-1200:])
        measured = load(report)
    text, boxes, source = None, [], 'no OCR evidence'
    fallible_ocr = False
    if page:
        text, source = measured.get('text'), 'autocheck visible DOM text (not OCR; verify image/canvas text by eye)'
        boxes = [r for t in measured.get('text_runs', []) for r in t['rects']]
    else:
        manifest = Path(a.boxes) if a.boxes else Path(a.target).with_name(Path(a.target).stem + '-boxes.json')
        if a.boxes or manifest.is_file():
            text, boxes = text_manifest(manifest)
            source = 'code-set text manifest: ' + str(manifest)
        elif not a.no_ocr and not a.ocr_text:
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
    # Counts refer to objects, not OCR word occurrences. Never pretend OCR counts bodies or cups.
    evidence = load(a.observations) if a.observations else {}
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
    emit(dict(schema_version=1, target=a.target, passed=complete and not flagged, status=status, checks=checks,
              autocheck=measured, unverified_brief_conditions=b['must_be_right'], scope='Mechanical checks only. SKIP/FLAG is not a pass; review OCR, figures, marks and intent visually.'))
    return 0 if complete else 1


def select(a):
    b = read_brief(a.brief, require_medium=False)
    if not 4 <= len(a.roughs) <= 8 or len(set(a.roughs)) != len(a.roughs):
        raise ValueError('select needs 4–8 distinct rough files')
    for path in a.roughs:
        if not Path(path).is_file():
            raise ValueError('rough not found: ' + path)
    ids = [f'R{i + 1}' for i in range(len(a.roughs))]
    packet = dict(schema_version=1, stage='fresh-context-review', brief=b,
                  roughs=dict(zip(ids, a.roughs)),
                  instruction='Same model, fresh context, no maker rationale. Compare every pair against idea, feeling and must-be-right. Name evidence and trade-off; no averaged taste scores. Show the top 2–3 to the owner of the work. Only their winner enters the fix loop. The original is better is a valid verdict.',
                  review_template=dict(same_model=True, fresh_context=True, comparisons=[dict(a='R1', b='R2', stronger='R1', reason='', trade_off='', confidence='low')], shortlist=['R1', 'R2']))
    if a.review:
        review = load(a.review)
        if not isinstance(review, dict) or not isinstance(review.get('comparisons'), list):
            raise ValueError('review needs an object with comparisons list')
        if review.get('same_model') is not True or review.get('fresh_context') is not True:
            raise ValueError('review must attest same_model and fresh_context')
        pairs = set()
        for pair in review.get('comparisons', []):
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
        if len(pairs) != len(ids) * (len(ids) - 1) // 2:
            raise ValueError('compare every pair before shortlisting')
        shortlist = review.get('shortlist', [])
        if not isinstance(shortlist, list) or not all(isinstance(x, str) for x in shortlist) or len(shortlist) not in (2, 3) or len(set(shortlist)) != len(shortlist) or not set(shortlist) <= set(ids):
            raise ValueError('shortlist must hold 2–3 distinct rough IDs')
        if a.owner_choice and a.owner_choice not in shortlist:
            raise ValueError('owner choice must be in the shortlist')
        packet.update(stage='winner-ready' if a.owner_choice else 'awaiting-owner', review=review,
                      winner=a.owner_choice, choice_provenance='caller-supplied owner choice; not inferred by this tool')
    elif a.owner_choice:
        raise ValueError('--owner-choice needs a completed --review')
    emit(packet)
    return 0


def haystack(brief):
    parts = [brief.get(key, '') or '' for key in ('description', 'idea', 'feeling', 'audience', 'purpose', 'success')]
    parts.extend(brief.get('constraints') or [])
    parts.extend(brief.get('must_be_right') or [])
    return ' '.join(str(p) for p in parts).lower()


def has_word(text, word):
    return re.search(r'(?<![a-z0-9])' + re.escape(word) + r'(?![a-z0-9])', text) is not None


ALWAYS_FILES = ('modules/composition/sitting-right.md',)
ALWAYS_RULES = ('CORE-11', 'COMP-19', 'COMP-23')


def task_routes():
    """Only the first Task/Load table is routing data, never the module index."""
    text = (ROOT / 'core/which-modules.md').read_text(encoding='utf-8')
    table = text.split('| Task | Load |', 1)[1].split('\n\n', 1)[0]
    return [tuple(cell.strip() for cell in line.strip().strip('|').split('|'))
            for line in table.splitlines() if line.startswith('|') and not line.startswith('|---')]


def normalise(text):
    return text.lower().replace('’', "'").replace('“', '"').replace('”', '"')


def task_phrases(task):
    # Phrase boundaries come from the table, not a second keyword catalogue.
    # No individual generic words (e.g. "copy", "page") are stolen from phrases.
    phrases = re.split(r'[,;()]| or | / ', normalise(task))
    return [re.sub(r'^(?:a |an |the )', '', p.strip(' "')) for p in phrases if p.strip(' "')]


def route_files(cell):
    modules = {p.name for p in (ROOT / 'modules').iterdir() if (p / 'README.md').is_file()}
    module_pattern = r'(?<![a-z0-9/-])(' + '|'.join(re.escape(m) for m in sorted(modules, key=len, reverse=True)) + r')(?![a-z0-9/-])'
    mentions = list(re.finditer(module_pattern, normalise(cell)))
    paths = [f'modules/{m.group()}/README.md' for m in mentions]
    for match in re.finditer(r'`([^`]+\.md)`', cell):
        name = match.group(1)
        if name.startswith(('core/', 'modules/')):
            path = name
        elif '/' in name:
            path = 'modules/' + name
        else:
            preceding = [m.group() for m in mentions if m.start() < match.start()]
            if not preceding:
                raise ValueError('No module context for table path: ' + name)
            path = 'modules/' + preceding[-1] + '/' + name
        if not (ROOT / path).is_file():
            raise ValueError('Unknown table path: ' + path)
        paths.append(path)
    return list(dict.fromkeys(paths))


def route_rules(cell, paths, index):
    ids = set(re.findall(r'\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d+\b', cell))
    for prefix, first, last in re.findall(r'\b([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)-(\d+)\s+(?:to|[–-])\s*(\d+)', cell):
        ids.update(f'{prefix}-{i}' for i in range(int(first), int(last) + 1))
    # Reading a module includes its rules, including shorthand such as "INF rules".
    ids.update(rid for rid, (path, _) in index.items() if path in paths)
    return sorted(ids & index.keys())


def load_plan(brief):
    medium = normalise(brief['medium'].strip())
    text = normalise(haystack(brief))
    intent = normalise(' '.join(brief.get(k, '') for k in ('feeling', 'purpose', 'idea')))
    routes = task_routes()
    energy_task = next(task for task, cell in routes if cell.startswith('`core/energy-pass.md`'))
    examples = re.search(r'\((.*?)\)', energy_task).group(1)
    energetic = any(has_word(intent, phrase) for phrase in task_phrases(examples))
    files, ids, matched, reasons = list(ALWAYS_FILES), list(ALWAYS_RULES), [], []
    index = rules()
    for task, cell in routes:
        lower_task = normalise(task)
        anatomy = 'anatomy pass CHAR-9' in cell
        writing = cell.startswith('writing (')
        screen = cell.startswith('web-ui (') and brief['format']['kind'] == 'screen'
        hit = has_word(lower_task, medium) or any(has_word(medium, phrase) for phrase in task_phrases(task)) or screen
        if anatomy and brief['has_people_or_animals']:
            hit = True
        if task == energy_task:
            hit = energetic  # never infer energy from the medium alone
        if writing:
            hit = hit or any(has_word(text, phrase) for phrase in task_phrases(task))
        if not hit:
            continue
        matched.append('writing' if writing else ('screen' if screen else medium))
        reasons.append(task)
        paths = route_files(cell)
        if task != energy_task:
            paths = [p for p in paths if p != 'core/energy-pass.md']
        row_ids = route_rules(cell, paths, index)
        # Rule-only references also resolve to their canonical files. Energy stays intent-gated.
        row_ids = [rid for rid in row_ids if index[rid][0] != 'core/energy-pass.md' or energetic]
        paths.extend(index[rid][0] for rid in row_ids)
        files.extend(paths)
        ids.extend(row_ids)
    return dict(
        schema_version=1,
        matched=list(dict.fromkeys(matched)),
        files=list(dict.fromkeys(files)),
        rules=list(dict.fromkeys(ids)),
        reasons=reasons + ['delivery: broken-balance and dead-space checks apply to every piece'],
        instruction='Read each file before making or fixing. Look up each rule with python3 tools/cd.py rule <ID>. Quote matched and rules in the critique. Skipping this list is how medium rules get missed.',
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='command', required=True)
    bp = sub.add_parser('brief', help='Create a structured brief')
    bs = bp.add_subparsers(dest='action', required=True)
    bi = bs.add_parser('init')
    bi.add_argument('description', nargs='?', default='')
    bi.add_argument('--out', default='brief.json')
    cp = sub.add_parser('check', help='Mechanical checks as JSON; missing evidence never passes')
    cp.add_argument('target')
    cp.add_argument('--brief', default='brief.json')
    cp.add_argument('--boxes', help='Code-set text manifest [text, box, RGB]; auto-detects <stem>-boxes.json beside image')
    cp.add_argument('--ocr-text', help='UTF-8 rendered line transcript; provenance is labelled')
    cp.add_argument('--no-ocr', action='store_true')
    cp.add_argument('--text-box', action='append', default=[])
    cp.add_argument('--observations', help='Count evidence bound to the current image SHA-256')
    rp = sub.add_parser('rule', help='Print the canonical definition of an existing rule')
    rp.add_argument('id')
    lp = sub.add_parser('load', help='List modules and rules this brief requires, to read before making or fixing')
    lp.add_argument('--brief', default='brief.json')
    sp = sub.add_parser('select', help='Prepare or validate a same-model fresh-context rough comparison')
    sp.add_argument('roughs', nargs='+')
    sp.add_argument('--brief', default='brief.json')
    sp.add_argument('--review')
    sp.add_argument('--owner-choice')
    a = ap.parse_args()
    try:
        if a.command == 'brief':
            b = load(BRIEF)
            b['description'] = a.description
            with Path(a.out).open('x', encoding='utf-8') as out:
                out.write(json.dumps(b, indent=2, ensure_ascii=False) + '\n')
            emit(dict(path=a.out, status='created', next='Fill the brief; description is not an inferred intent.'))
            return 0
        if a.command == 'rule':
            found = rules().get(a.id.upper())
            if found is None:
                raise ValueError('unknown rule ID: ' + a.id + '; see docs/RETIRED-IDS.md for merged IDs')
            print(f'<!-- {found[0]} -->\n{found[1]}')
            return 0
        if a.command == 'load':
            emit(load_plan(read_brief(a.brief)))
            return 0
        return check(a) if a.command == 'check' else select(a)
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as e:
        emit(dict(schema_version=1, status='ERROR', passed=False, error=str(e)))
        return 2


if __name__ == '__main__':
    sys.exit(main())
