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


def read_brief(path):
    b = load(path)
    if not isinstance(b, dict) or type(b.get('schema_version')) is not int or b.get('schema_version') != 1:
        raise ValueError('brief schema_version must be 1')
    for field in ('description', 'idea', 'feeling', 'audience', 'purpose', 'success'):
        if not isinstance(b.get(field), str):
            raise ValueError(f'brief {field} must be a string')
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


def copy_check(b, text, provenance):
    if text is None:
        return result('copy', 'SKIP', provenance, reason='No rendered text evidence; cannot certify CD-7.')
    # Each entry is a complete rendered line (DOM: a visible text run).
    observed = Counter(text.splitlines())
    expected = Counter({x['text']: x['count'] for x in b['copy']})
    missing = list((expected - observed).elements())
    extra = list((observed - expected).elements()) if b['exact_copy'] else [line for line, n in (observed - expected).items() if line in expected for _ in range(n)]
    return result('copy', 'FAIL' if missing or extra else 'PASS', provenance, rule='CD-7',
                  missing=missing, extra=extra, observed=dict(observed),
                  diff=list(difflib.ndiff(list(expected.elements()), text.splitlines())))


def ocr_image(target):
    if not shutil.which('tesseract'):
        return None, [], 'tesseract unavailable; install it or supply --ocr-text'
    p = subprocess.run(['tesseract', str(target), 'stdout', 'tsv'], capture_output=True, text=True, timeout=90)
    if p.returncode:
        raise ValueError('tesseract failed: ' + p.stderr.strip())
    groups = {}
    boxes = []
    for row in csv.DictReader(io.StringIO(p.stdout), delimiter='\t', quoting=csv.QUOTE_NONE):
        if row['level'] != '5' or not row['text'].strip():
            continue
        key = tuple(row[k] for k in ('page_num', 'block_num', 'par_num', 'line_num'))
        groups.setdefault(key, []).append(row['text'])
        x, y, w, h = (int(row[k]) for k in ('left', 'top', 'width', 'height'))
        boxes.append([x, y, x + w, y + h])
    return '\n'.join(' '.join(words) for words in groups.values()), boxes, 'tesseract TSV on current render (fallible; verify visually)'


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
    if page:
        text, source = measured.get('text'), 'autocheck visible DOM text (not OCR; verify image/canvas text by eye)'
        boxes = [r for t in measured.get('text_runs', []) for r in t['rects']]
    elif not a.no_ocr:
        text, boxes, source = ocr_image(a.target)
    if a.ocr_text:
        text, source = Path(a.ocr_text).read_text(encoding='utf-8').rstrip('\n'), 'supplied render transcript: ' + a.ocr_text
    if a.text_box:
        for box in a.text_box:
            vals = [int(v) for v in box.split(':')[0].split(',')]
            if len(vals) != 4 or vals[0] < 0 or vals[1] < 0 or vals[2] <= vals[0] or vals[3] <= vals[1]:
                raise ValueError('text boxes require x0,y0,x1,y1 within the frame')
            boxes.append(vals)
    missing_intent = [k for k in ('idea', 'feeling', 'audience', 'purpose', 'success') if not b[k].strip()]
    checks = [result('brief-intent', 'SKIP' if missing_intent else 'PASS', 'structured brief; not an aesthetic judgement', missing=missing_intent), copy_check(b, text, source)]
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
                         'visible DOM/OCR text boxes plus supplied text boxes; non-text key elements still need visual review',
                         rule='LAY-5', margin_px=margin, outside=bad, measured_boxes=len(boxes)))
    checks.append(result('format', 'PASS' if [width, height] == [b['format']['width'], b['format']['height']] else 'FAIL',
                         'autocheck rendered size', expected=b['format'], observed=[width, height]))
    passed = all(c['passed'] for c in checks) and not any(c['status'] == 'FAIL' for c in measured['checks'])
    emit(dict(schema_version=1, target=a.target, passed=passed, status='PASS' if passed else 'FAIL', checks=checks,
              autocheck=measured, unverified_brief_conditions=b['must_be_right'], scope='Mechanical checks only. SKIP/FLAG is not a pass; review OCR, figures, marks and intent visually.'))
    return 0 if passed else 1


def select(a):
    b = read_brief(a.brief)
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
    cp.add_argument('--ocr-text', help='UTF-8 rendered line transcript; provenance is labelled')
    cp.add_argument('--no-ocr', action='store_true')
    cp.add_argument('--text-box', action='append', default=[])
    cp.add_argument('--observations', help='Count evidence bound to the current image SHA-256')
    rp = sub.add_parser('rule', help='Print the canonical definition of an existing rule')
    rp.add_argument('id')
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
        return check(a) if a.command == 'check' else select(a)
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as e:
        emit(dict(schema_version=1, status='ERROR', passed=False, error=str(e)))
        return 2


if __name__ == '__main__':
    sys.exit(main())
