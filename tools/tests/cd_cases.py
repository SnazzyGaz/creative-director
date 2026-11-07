#!/usr/bin/env python3
"""cd front-door tests: python3 tools/tests/cd_cases.py (unittest, no paid/model calls)."""
from contextlib import redirect_stdout
import copy
import hashlib
import io
import itertools
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cd


class FrontDoor(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.b = json.loads(cd.BRIEF.read_text())
        self.b.update(idea='One opening', feeling='Quiet', audience='Visitors', purpose='Invite', success='Date reads')
        self.b['format'].update(width=800, height=800)
        self.brief = self.write('brief.json', self.b)
        self.roughs = [self.write(f'r{i}.png', 'rough') for i in range(4)]

    def write(self, name, data):
        p = self.root / name
        p.write_text(json.dumps(data) if not isinstance(data, str) else data)
        return p

    def cli(self, *args):
        return subprocess.run([sys.executable, str(Path(cd.__file__)), *map(str, args)], capture_output=True, text=True)

    def test_help(self):
        p = self.cli('--help')
        self.assertEqual(p.returncode, 0)
        for word in ('brief', 'rule', 'check', 'select'):
            self.assertIn(word, p.stdout)

    def test_init_and_no_overwrite(self):
        out = self.root / 'new.json'
        self.assertEqual(self.cli('brief', 'init', 'One idea', '--out', out).returncode, 0)
        self.assertEqual(json.loads(out.read_text())['description'], 'One idea')
        self.assertEqual(self.cli('brief', 'init', '--out', out).returncode, 2)
        self.assertEqual(json.loads(out.read_text())['description'], 'One idea')

    def test_rule_lookup(self):
        for rid in ('CD-7', 'CORE-2', 'FLOW-5', '3D-1', 'FILM-GEN-8'):
            with self.subTest(rid=rid):
                p = self.cli('rule', rid)
                self.assertEqual(p.returncode, 0, p.stdout)
                self.assertIn(rid, p.stdout)
                self.assertIn('<!-- ', p.stdout)
        p = self.cli('rule', 'CD-7000')
        self.assertEqual(p.returncode, 2)
        self.assertFalse(json.loads(p.stdout)['passed'])

    def test_rule_boundary(self):
        p = self.cli('rule', 'CD-1')
        self.assertIn('Have a brief', p.stdout)
        self.assertNotIn('## CD-2.', p.stdout)

    def test_forty_existing_ids(self):
        text = (cd.ROOT / 'core/principles.md').read_text()
        selected = re.findall(r'^\| ([A-Z0-9]+(?:-[A-Z0-9]+)*-\d+) \|', text, re.M)
        ids = selected + [f'CORE-{i}' for i in range(1, 12)] + [f'FLOW-{i}' for i in range(1, 6)]
        self.assertEqual(len(ids), 40)
        self.assertEqual(len(set(ids)), 40)
        self.assertTrue(set(ids) <= cd.rules().keys())

    def test_copy_exact_and_counts(self):
        self.b['copy'] = [{'text': 'Open 10–6.', 'count': 2}]
        self.assertEqual(cd.copy_check(self.b, 'Open 10–6.\nOpen 10–6.', 'fixture')['status'], 'PASS')
        for text in ('Open 10–6.', 'open 10–6.\nOpen 10–6.', 'Open 10–6.\nOpen 10–6.\nExtra'):
            self.assertEqual(cd.copy_check(self.b, text, 'fixture')['status'], 'FAIL')
        self.b['exact_copy'] = False
        self.assertEqual(cd.copy_check(self.b, 'Open 10–6.\nOpen 10–6.\nExtra', 'fixture')['status'], 'PASS')
        self.assertEqual(cd.copy_check(self.b, 'Open 10–6.\nOpen 10–6.\nOpen 10–6.', 'fixture')['status'], 'FAIL')
        self.assertEqual(cd.copy_check(self.b, None, 'fixture')['status'], 'SKIP')

    def test_invalid_briefs_json(self):
        for change in ({'schema_version': 4}, {'format': []}, {'safe_area_px': -1}, {'copy': [{'text': 'x', 'count': -1}]}, {'constraints': 'no'}):
            b = copy.deepcopy(self.b)
            b.update(change)
            bad = self.write('bad.json', b)
            p = self.cli('check', self.roughs[0], '--brief', bad)
            self.assertEqual(p.returncode, 2, p.stderr)
            self.assertEqual(json.loads(p.stdout)['status'], 'ERROR')

    def test_select_packet(self):
        p = self.cli('select', *self.roughs, '--brief', self.brief)
        self.assertEqual(p.returncode, 0, p.stderr)
        packet = json.loads(p.stdout)
        self.assertEqual(len(packet['roughs']), 4)
        self.assertEqual(packet['stage'], 'fresh-context-review')
        self.assertIn('Same model', packet['instruction'])
        self.assertEqual(self.cli('select', *self.roughs[:3], '--brief', self.brief).returncode, 2)
        self.assertEqual(self.cli('select', *self.roughs, '--brief', self.brief, '--owner-choice', 'R1').returncode, 2)

    def review(self):
        return dict(same_model=True, fresh_context=True, shortlist=['R1', 'R2'],
                    comparisons=[dict(a=x, b=y, stronger=x, reason='The idea reads sooner', trade_off='Less space for the setting', confidence='medium') for x, y in itertools.combinations(['R1', 'R2', 'R3', 'R4'], 2)])

    def test_select_review_and_choice(self):
        review = self.write('review.json', self.review())
        p = self.cli('select', *self.roughs, '--brief', self.brief, '--review', review)
        self.assertEqual(json.loads(p.stdout)['stage'], 'awaiting-owner')
        p = self.cli('select', *self.roughs, '--brief', self.brief, '--review', review, '--owner-choice', 'R2')
        self.assertEqual(json.loads(p.stdout)['winner'], 'R2')
        self.assertEqual(self.cli('select', *self.roughs, '--brief', self.brief, '--review', review, '--owner-choice', 'R3').returncode, 2)

    def test_incomplete_review_and_wrong_context(self):
        for field in ('comparisons', 'same_model', 'fresh_context'):
            r = self.review()
            r[field] = r[field][:1] if field == 'comparisons' else False
            p = self.cli('select', *self.roughs, '--brief', self.brief, '--review', self.write('r.json', r))
            self.assertEqual(p.returncode, 2, p.stderr)

    def mock_check(self, observations=None, boxes=None, text='Open', margin=48, count=False, complete=True, helper_status='PASS'):
        b = copy.deepcopy(self.b)
        b['copy'] = [{'text': 'Open', 'count': 1}]
        b['safe_area_px'] = margin
        b['counts'] = [{'item': 'cups', 'count': 3}] if count else []
        if not complete:
            b['idea'] = ''
        brief = self.write('mock.json', b)
        a = cd.argparse.Namespace(target=str(self.roughs[0]), brief=brief, text_box=[], no_ocr=False, ocr_text=None, observations=observations)
        def helper(cmd, **kwargs):
            Path(cmd[cmd.index('--json') + 1]).write_text(json.dumps(dict(size=[800, 800], checks=[dict(id=i, status=helper_status) for i in ('contrast', 'text-size') ])))
            return subprocess.CompletedProcess(cmd, 0, '', '')
        out = io.StringIO()
        with patch.object(cd.subprocess, 'run', side_effect=helper), patch.object(cd, 'ocr_image', return_value=(text, boxes or [], 'fixture OCR')), redirect_stdout(out):
            code = cd.check(a)
        return code, json.loads(out.getvalue())

    def test_check_json_pass(self):
        code, r = self.mock_check(boxes=[[100, 100, 300, 150]])
        self.assertEqual(code, 0)
        self.assertTrue(r['passed'])
        self.assertTrue({'copy', 'counts', 'contrast', 'text-size', 'safe-area', 'format'} <= {c['id'] for c in r['checks']})
        self.assertTrue(all({'id', 'status', 'passed', 'provenance'} <= c.keys() for c in r['checks']))

    def test_missing_evidence_never_passes(self):
        for kwargs in ({'text': None}, {'complete': False}, {'count': True}, {'helper_status': 'SKIP'}, {}):
            code, r = self.mock_check(**kwargs)
            self.assertEqual(code, 1)
            self.assertFalse(r['passed'])

    def test_safe_area_and_copy_failures(self):
        for kwargs, cid in (({'boxes': [[1, 100, 300, 150]]}, 'safe-area'), ({'text': 'Opon'}, 'copy')):
            code, r = self.mock_check(**kwargs)
            self.assertEqual(code, 1)
            self.assertEqual(next(c for c in r['checks'] if c['id'] == cid)['status'], 'FAIL')

    def test_counts_bound_to_render(self):
        obs = dict(target_sha256=hashlib.sha256(self.roughs[0].read_bytes()).hexdigest(), counts={'cups': dict(count=3, provenance='2x crop, three ticks')})
        path = self.write('counts.json', obs)
        code, r = self.mock_check(count=True, observations=path, boxes=[[100, 100, 300, 150]])
        self.assertEqual(code, 0)
        obs['counts']['cups']['count'] = 4
        self.assertEqual(self.mock_check(count=True, observations=self.write('counts.json', obs))[0], 1)
        obs['target_sha256'] = 'wrong'
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            self.mock_check(count=True, observations=self.write('counts.json', obs))

    def test_ocr_tsv_adapter(self):
        header = 'level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext\n'
        rows = '5\t1\t1\t1\t1\t1\t100\t100\t30\t20\t95\tOpen\n5\t1\t1\t1\t1\t2\t140\t100\t20\t20\t90\tnow.\n'
        with patch.object(cd.shutil, 'which', return_value='/usr/bin/tesseract'), patch.object(cd.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, header + rows, '')):
            text, boxes, source = cd.ocr_image(self.roughs[0])
        self.assertEqual(text, 'Open now.')
        self.assertEqual(boxes, [[100, 100, 130, 120], [140, 100, 160, 120]])
        self.assertIn('tesseract', source)
        with patch.object(cd.shutil, 'which', return_value=None):
            self.assertIsNone(cd.ocr_image(self.roughs[0])[0])

    def test_errors_are_json(self):
        p = self.cli('check', self.root / 'missing.png', '--brief', self.brief)
        self.assertEqual(p.returncode, 2)
        self.assertEqual(json.loads(p.stdout)['status'], 'ERROR')
        bad = self.write('not-json.json', '{bad')
        p = self.cli('check', self.roughs[0], '--brief', bad)
        self.assertEqual(p.returncode, 2)
        self.assertFalse(json.loads(p.stdout)['passed'])

    def test_real_image_json(self):
        fixture = Path(cd.__file__).parent / 'tests/fixtures/autocheck/even.png'
        p = self.cli('check', fixture, '--brief', self.brief, '--no-ocr')
        self.assertEqual(p.returncode, 1, p.stderr)
        r = json.loads(p.stdout)
        self.assertFalse(r['passed'])
        self.assertEqual(r['autocheck']['mode'], 'image')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'text-size')['status'], 'SKIP')

    def test_real_dom_copy(self):
        try:
            import playwright  # noqa
        except ImportError:
            self.skipTest('page checks require playwright and chromium')
        html = self.write('page.html', '<html><body style="margin:100px;background:white;color:black;font:24px Arial"><p>Open</p></body></html>')
        b = copy.deepcopy(self.b)
        b['format']['kind'] = 'screen'
        b['copy'] = [{'text': 'Open', 'count': 1}]
        brief = self.write('page.json', b)
        p = self.cli('check', html, '--brief', brief)
        self.assertEqual(p.returncode, 0, p.stderr + p.stdout)
        r = json.loads(p.stdout)
        self.assertTrue(r['passed'])
        self.assertEqual(r['autocheck']['text'], 'Open')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        b['copy'][0]['text'] = 'open'
        p = self.cli('check', html, '--brief', self.write('page.json', b))
        self.assertEqual(p.returncode, 1)
        self.assertEqual(next(c for c in json.loads(p.stdout)['checks'] if c['id'] == 'copy')['status'], 'FAIL')


if __name__ == '__main__':
    unittest.main(verbosity=2)
