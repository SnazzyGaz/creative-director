#!/usr/bin/env python3
"""cd v2 front-door tests: python3 tools/tests/cd_cases.py (unittest, no paid/model calls).

Preserves every original v0.11 regression test (OCR TSV, confidence filtering, crops,
manifest priority, transcript mismatch, Playwright DOM copy, 40-ID integrity, JSON errors)
plus v2 manifest routing, POSIX paths, proportional selection, taste profiles, and auto contrast.
"""
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


class FrontDoorV2(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.b = json.loads(cd.BRIEF.read_text(encoding='utf-8'))
        self.b.update(medium='poster', idea='One opening', feeling='Quiet', audience='Visitors', purpose='Invite', success='Date reads')
        self.b['format'].update(width=800, height=800)
        self.brief = self.write('brief.json', self.b)
        self.roughs = [self.write(f'r{i}.png', 'rough') for i in range(6)]

    def write(self, name, data):
        p = self.root / name
        p.write_text(json.dumps(data) if not isinstance(data, str) else data, encoding='utf-8')
        return p

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(cd.__file__)), *map(str, args)],
            capture_output=True, text=True, encoding='utf-8',
        )

    def test_help(self):
        p = self.cli('--help')
        self.assertEqual(p.returncode, 0)
        for word in ('brief', 'taste', 'rule', 'check', 'select', 'load', 'compose', 'generate-docs'):
            self.assertIn(word, p.stdout)

    def test_posix_paths_and_no_duplicates(self):
        for rid, (path, _) in cd.rules().items():
            self.assertNotIn('\\', path, f'Backslash in rule path for {rid}: {path}')
        data = cd.load_plan(dict(self.b, medium='poster', feeling='Bold concert'))
        for f in data['files']:
            self.assertNotIn('\\', f, f'Backslash in load_plan file: {f}')
        self.assertEqual(len(data['files']), len(set(data['files'])))

    def test_load_from_brief_and_always_on_guardrails(self):
        poster = dict(self.b, medium='poster', description='Harbor Night Market poster')
        data = cd.load_plan(poster)
        self.assertEqual(data['schema_version'], 2)
        self.assertEqual(data['tier'], 'directed')
        self.assertIn('poster-cover-social', data['matched'])
        self.assertIn('modules/layout/README.md', data['files'])
        self.assertIn('modules/composition/sitting-right.md', data['files'])
        self.assertNotIn('modules/web-ui/README.md', data['files'])
        # Always-on guardrails (CD-5, EN-5, EN-6) must stay present even on quiet briefs!
        for rid in ('LAY-7', 'COMP-23', 'CD-5', 'EN-5', 'EN-6'):
            self.assertIn(rid, data['rules'])

        screen = dict(self.b, medium='app screen', format={'kind': 'screen', 'width': 390, 'height': 844})
        sdata = cd.load_plan(screen)
        self.assertIn('modules/web-ui/README.md', sdata['files'])
        self.assertIn('UI-6', sdata['hard_gates'])
        self.assertIn('UI-10', sdata['hard_gates'])

        logo = dict(self.b, medium='logo', description='One-colour mark for a survey firm')
        ldata = cd.load_plan(logo)
        self.assertIn('logo-mark', ldata['matched'])
        self.assertIn('modules/brand/logo.md', ldata['files'])
        self.assertIn('LOGO-3', ldata['rules'])

    def test_load_explicit_gates_and_word_boundaries(self):
        for medium, path in [
            ('infographic', 'layout/infographics.md'),
            ('packaging label', 'layout/README.md'),
            ('3d render', '3d/README.md'),
            ('video', 'film/README.md'),
            ('landing page', 'web-ui/README.md'),
        ]:
            with self.subTest(medium=medium):
                self.assertIn('modules/' + path, cd.load_plan(dict(self.b, medium=medium))['files'])
        fox = cd.load_plan(dict(self.b, medium='picture-book cover', has_people_or_animals=True, description='A fox'))
        self.assertIn('modules/character/README.md', fox['files'])
        self.assertIn('CHAR-9', fox['rules'])
        self.assertIn('modules/layout/README.md', fox['files'])
        for subject in ('girl', 'baker', 'fox'):
            self.assertIn('CHAR-9', cd.load_plan(dict(self.b, description=subject, has_people_or_animals=True))['rules'])
        # Word boundary: "discover" must NOT trigger "cover".
        self.assertNotIn('modules/layout/README.md', cd.load_plan(dict(self.b, medium='discover'))['files'])

    def test_tiers_and_energy_triggers(self):
        fast = cd.load_plan(dict(self.b, tier='fast'))
        self.assertEqual(fast['tier'], 'fast')
        self.assertEqual(fast['roughs'], [0, 0])
        self.assertNotIn('core/creative-direction.md', fast['files'])

        remake = cd.load_plan(dict(self.b, description='Redo this flyer from scratch'))
        self.assertEqual(remake['tier'], 'remake')
        self.assertIn('core/first-principles.md', remake['files'])

        energetic = cd.load_plan(dict(self.b, medium='poster', feeling='Kinetic playful festival'))
        self.assertTrue(energetic['energetic'])
        self.assertIn('core/energy-pass.md', energetic['files'])

        quiet = cd.load_plan(dict(self.b, medium='concert poster', feeling='Quiet archival notice'))
        self.assertFalse(quiet['energetic'])
        self.assertNotIn('core/energy-pass.md', quiet['files'])
        self.assertIn('EN-5', quiet['rules'])
        self.assertIn('EN-6', quiet['rules'])

    def test_writing_load_from_brief(self):
        for desc in (
            'Website copy for an about page',
            'An email reply to a customer',
            'A poster with supporting copy to draft',
            'Microcopy for empty states and error messages',
            'A reply to a customer',
            'Replies to supporters',
        ):
            with self.subTest(desc=desc):
                w = cd.load_plan(dict(self.b, medium='writing', description=desc))
                self.assertIn('modules/writing/README.md', w['files'])
                self.assertIn('optional-domain', w['groups'])
                self.assertNotIn('modules/composition/sitting-right.md', w['files'])
                self.assertTrue({f'WRITE-{i}' for i in range(1, 12)} <= set(w['rules']))
        for desc, med in (('A book cover', 'book cover'), ('A concert poster', 'poster'), ('A photograph', 'photograph')):
            v = cd.load_plan(dict(self.b, medium=med, description=desc))
            self.assertNotIn('modules/writing/README.md', v['files'])

    def test_every_manifest_route_resolves(self):
        manifest = cd.load_manifest()
        all_rules = cd.rules()
        for route in manifest['routes']:
            for f in route.get('files', []) + route.get('optional_files', []):
                self.assertTrue((cd.ROOT / f).is_file(), f'Missing route file: {f}')
            for rid in route.get('rules', []):
                self.assertIn(rid, all_rules, f'Unknown rule ID in manifest route {route["id"]}: {rid}')
        for g in manifest['hard_gates']:
            self.assertIn(g['id'], all_rules, f'Unknown hard gate ID: {g["id"]}')

    def test_forty_existing_ids(self):
        text = (cd.ROOT / 'core/principles.md').read_text(encoding='utf-8')
        selected = re.findall(r'^\| ([A-Z0-9]+(?:-[A-Z0-9]+)*-\d+) \|', text, re.M)
        ids = selected + [f'CORE-{i}' for i in range(1, 12)] + [f'FLOW-{i}' for i in range(1, 6)]
        self.assertEqual(len(ids), 40)
        self.assertEqual(len(set(ids)), 40)
        self.assertTrue(set(ids) <= cd.rules().keys())

    def test_init_and_no_overwrite(self):
        out = self.root / 'new.json'
        self.assertEqual(self.cli('brief', 'init', 'One idea', '--out', out).returncode, 0)
        initial = json.loads(out.read_text(encoding='utf-8'))
        self.assertEqual(initial['description'], 'One idea')
        self.assertEqual(initial['medium'], '')
        self.assertIs(initial['has_people_or_animals'], False)
        self.assertEqual(self.cli('load', '--brief', out).returncode, 2)
        self.assertEqual(self.cli('brief', 'init', '--out', out).returncode, 2)
        self.assertEqual(json.loads(out.read_text(encoding='utf-8'))['description'], 'One idea')

    def test_taste_init_is_genuinely_neutral(self):
        tout = self.root / 'taste.json'
        self.assertEqual(self.cli('taste', 'init', '--out', tout).returncode, 0)
        self.assertEqual(self.cli('taste', 'init', '--out', tout).returncode, 2)
        t = json.loads(tout.read_text(encoding='utf-8'))
        self.assertEqual(t['whites']['default'], 'neutral')
        self.assertEqual(t['avoid_tropes'], [])
        self.assertEqual(t['avoid_typefaces'], [])
        self.assertEqual(t['finish_ceiling'], '')

    def test_rule_lookup(self):
        for rid in ('CD-7', 'CORE-2', 'FLOW-5', '3D-1', 'FILM-GEN-8', 'WRITE-1', 'WRITE-11'):
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
        for change in (
            {'medium': ''}, {'medium': 3}, {'tier': 'huge'}, {'has_people_or_animals': 1},
            {'has_people_or_animals': 'false'}, {'schema_version': 4}, {'format': []},
            {'safe_area_px': -1}, {'copy': [{'text': 'x', 'count': -1}]}, {'constraints': 'no'},
        ):
            b = copy.deepcopy(self.b)
            b.update(change)
            bad = self.write('bad.json', b)
            p = self.cli('check', self.roughs[0], '--brief', bad)
            self.assertEqual(p.returncode, 2, p.stderr)
            self.assertEqual(json.loads(p.stdout)['status'], 'ERROR')

    def test_errors_are_json(self):
        p = self.cli('check', self.root / 'missing.png', '--brief', self.brief)
        self.assertEqual(p.returncode, 2)
        self.assertEqual(json.loads(p.stdout)['status'], 'ERROR')
        bad = self.write('not-json.json', '{bad')
        p = self.cli('check', self.roughs[0], '--brief', bad)
        self.assertEqual(p.returncode, 2)
        self.assertFalse(json.loads(p.stdout)['passed'])

    def test_select_packet_3_roughs_and_bracket(self):
        p = self.cli('select', *self.roughs[:3], '--brief', self.brief)
        self.assertEqual(p.returncode, 0, p.stderr)
        pkt = json.loads(p.stdout)
        self.assertEqual(pkt['mode'], 'pairwise')
        self.assertEqual(len(pkt['roughs']), 3)
        self.assertEqual(self.cli('select', self.roughs[0], '--brief', self.brief).returncode, 2)
        self.assertEqual(self.cli('select', *self.roughs[:3], '--brief', self.brief, '--owner-choice', 'R1').returncode, 2)

        rev3 = dict(
            context_mode='same-session-self-review',
            mode='pairwise',
            shortlist=['R1', 'R2'],
            comparisons=[
                dict(a=x, b=y, stronger=x, reason='Clearer focal point', trade_off='Tighter margins', confidence='medium')
                for x, y in itertools.combinations(['R1', 'R2', 'R3'], 2)
            ],
        )
        rfile = self.write('rev3.json', rev3)
        p = self.cli('select', *self.roughs[:3], '--brief', self.brief, '--review', rfile, '--owner-choice', 'R2')
        self.assertEqual(p.returncode, 0, p.stdout)
        out = json.loads(p.stdout)
        self.assertEqual(out['winner'], 'R2')
        self.assertEqual(out['context_mode'], 'same-session-self-review')
        self.assertEqual(self.cli('select', *self.roughs[:3], '--brief', self.brief, '--review', rfile, '--owner-choice', 'R3').returncode, 2)

        p6 = self.cli('select', *self.roughs[:6], '--brief', self.brief)
        self.assertEqual(json.loads(p6.stdout)['mode'], 'bracket')
        rev6 = dict(
            context_mode='isolated-subagent',
            mode='bracket',
            shortlist=['R1', 'R3'],
            comparisons=[
                dict(a='R1', b='R2', stronger='R1', reason='Better read', trade_off='Simpler', confidence='high'),
                dict(a='R3', b='R4', stronger='R3', reason='Stronger type', trade_off='Busier', confidence='medium'),
                dict(a='R5', b='R6', stronger='R5', reason='Cleaner grid', trade_off='Quieter', confidence='medium'),
                dict(a='R1', b='R5', stronger='R1', reason='Clearer hierarchy', trade_off='Less colour', confidence='high'),
            ],
        )
        self.assertEqual(self.cli('select', *self.roughs[:6], '--brief', self.brief, '--review', self.write('rev6.json', rev6)).returncode, 0)

    def test_select_incomplete_review_rejected(self):
        bad_ctx = dict(context_mode='bogus', mode='pairwise', shortlist=['R1', 'R2'], comparisons=[])
        self.assertEqual(self.cli('select', *self.roughs[:3], '--brief', self.brief, '--review', self.write('bctx.json', bad_ctx)).returncode, 2)
        inc = dict(context_mode='isolated-subagent', mode='pairwise', shortlist=['R1', 'R2'],
                   comparisons=[dict(a='R1', b='R2', stronger='R1', reason='x', trade_off='y', confidence='low')])
        self.assertEqual(self.cli('select', *self.roughs[:3], '--brief', self.brief, '--review', self.write('inc.json', inc)).returncode, 2)

    def mock_check(self, observations=None, boxes=None, text='Open', margin=48, count=False, complete=True, helper_status='PASS'):
        b = copy.deepcopy(self.b)
        b['copy'] = [{'text': 'Open', 'count': 1}]
        b['safe_area_px'] = margin
        b['counts'] = [{'item': 'cups', 'count': 3}] if count else []
        if not complete:
            b['idea'] = ''
        brief = self.write('mock.json', b)
        a = cd.argparse.Namespace(target=str(self.roughs[0]), brief=brief, taste=None, boxes=None, text_box=[], no_ocr=False, ocr_text=None, observations=observations)
        def helper(cmd, **kwargs):
            Path(cmd[cmd.index('--json') + 1]).write_text(json.dumps(dict(size=[800, 800], checks=[dict(id=i, status=helper_status) for i in ('contrast', 'text-size')])))
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

    def test_missing_evidence_never_passes(self):
        for kwargs in ({'text': None}, {'complete': False}, {'count': True}, {'helper_status': 'SKIP'}, {}):
            code, r = self.mock_check(**kwargs)
            self.assertEqual(code, 1)
            self.assertFalse(r['passed'])

    def test_safe_area_failure(self):
        code, r = self.mock_check(boxes=[[1, 100, 300, 150]])
        self.assertEqual(code, 1)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'safe-area')['status'], 'FAIL')

    def test_counts_bound_to_render(self):
        obs = dict(target_sha256=hashlib.sha256(self.roughs[0].read_bytes()).hexdigest(), counts={'cups': dict(count=3, provenance='2x crop')})
        path = self.write('counts.json', obs)
        self.assertEqual(self.mock_check(count=True, observations=path, boxes=[[100, 100, 300, 150]])[0], 0)
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
        self.assertEqual(boxes, [[100, 100, 160, 120]])
        self.assertIn('tesseract', source)
        with patch.object(cd.shutil, 'which', return_value=None):
            self.assertIsNone(cd.ocr_image(self.roughs[0])[0])

    def test_ocr_low_confidence_dropped(self):
        header = 'level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext\n'
        rows = ''.join(
            f'5\t1\t1\t1\t1\t{i}\t100\t100\t30\t20\t{conf}\t{text}\n'
            for i, (conf, text) in enumerate([(49.9, 'junk'), (-1, 'invalid'), (50, 'Open')], 1)
        )
        with patch.object(cd.shutil, 'which', return_value='tesseract'), patch.object(cd.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, header + rows, '')):
            text, boxes, source = cd.ocr_image(self.roughs[0])
        self.assertEqual(text, 'Open')
        self.assertEqual(boxes, [[100, 100, 130, 120]])
        self.assertIn('confidence >= 50', source)

    def image_check(self, *, manifest=None, transcript=None, ocr='Opon', boxes=None, helper_status='PASS'):
        from PIL import Image
        target = self.root / 'final.png'
        Image.new('RGB', (800, 800), 'white').save(target)
        b = copy.deepcopy(self.b)
        b['copy'] = [{'text': 'Open', 'count': 1}]
        a = cd.argparse.Namespace(target=str(target), brief=self.write('image.json', b), taste=None, boxes=manifest,
                                 text_box=[], no_ocr=False, ocr_text=transcript, observations=None)
        def helper(cmd, **kwargs):
            Path(cmd[cmd.index('--json') + 1]).write_text(json.dumps(dict(size=[800, 800], checks=[dict(id=i, status=helper_status) for i in ('contrast', 'text-size')])))
            return subprocess.CompletedProcess(cmd, 0, '', '')
        out = io.StringIO()
        with patch.object(cd.subprocess, 'run', side_effect=helper), patch.object(cd, 'ocr_image', return_value=(ocr, boxes or [[100, 100, 200, 130]], 'tesseract fixture')) as adapter, redirect_stdout(out):
            code = cd.check(a)
        return code, json.loads(out.getvalue()), adapter.call_count

    def test_ocr_mismatch_flag_and_crops(self):
        code, r, _ = self.image_check()
        self.assertEqual(code, 0)
        self.assertEqual(r['status'], 'FLAG')
        self.assertFalse(r['passed'])
        c = next(c for c in r['checks'] if c['id'] == 'copy')
        self.assertEqual(c['status'], 'FLAG')
        self.assertEqual(c['crop_boxes'], [[100, 100, 200, 130]])
        self.assertEqual(len(c['crops']), 2)
        from PIL import Image
        for crop in c['crops']:
            with Image.open(crop['path']) as im:
                self.assertLessEqual(im.width, 640)
                self.assertLessEqual(im.height, 320)
        self.assertEqual(self.image_check(boxes=[[1, 100, 200, 130]])[0], 1)
        self.assertEqual(self.image_check(helper_status='SKIP')[0], 1)

    def test_manifest_priority_and_real_mismatch(self):
        path = self.write('type.json', [['Open', [100, 100, 200, 130], [0, 0, 0]]])
        code, r, calls = self.image_check(manifest=path, transcript=self.write('wrong.txt', 'Wrong'))
        self.assertEqual(code, 0)
        self.assertEqual(calls, 0)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        self.write('type.json', [['Opon', [100, 100, 200, 130], [0, 0, 0]]])
        code, r, _ = self.image_check(manifest=path)
        self.assertEqual(code, 1)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'FAIL')
        self.write('final-boxes.json', [['Open', [1, 100, 200, 130], [0, 0, 0]]])
        code, r, calls = self.image_check()
        self.assertEqual(calls, 0)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'safe-area')['status'], 'FAIL')
        self.assertEqual(code, 1)

    def test_supplied_transcript_mismatch_fails(self):
        code, r, calls = self.image_check(transcript=self.write('wrong.txt', 'Wrong'))
        self.assertEqual(code, 1)
        self.assertEqual(calls, 0)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'FAIL')

    def test_manifest_auto_feeds_contrast(self):
        from PIL import Image, ImageDraw
        target = self.root / 'poster.png'
        im = Image.new('RGB', (800, 800), '#FFFFFF')
        ImageDraw.Draw(im).text((100, 100), 'Open', fill='#111111')
        im.save(target)
        self.write('poster-boxes.json', [['Open', [95, 95, 160, 120], [17, 17, 17]]])
        b = copy.deepcopy(self.b)
        b['copy'] = [{'text': 'Open', 'count': 1}]
        brief = self.write('poster-brief.json', b)
        r = json.loads(self.cli('check', target, '--brief', brief).stdout)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'safe-area')['status'], 'PASS')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'contrast')['status'], 'PASS')

    def test_taste_warm_whites_forwarded(self):
        from PIL import Image, ImageDraw
        target = self.root / 'warm.png'
        im = Image.new('RGB', (800, 800), '#F5EEDC')
        ImageDraw.Draw(im).rectangle([100, 100, 700, 700], outline='#222222', width=4)
        im.save(target)
        taste = self.write('taste.json', {'schema_version': 1, 'name': 'bakery', 'whites': {'default': 'warm', 'warm_reason': 'cream paper stock'}})
        r = json.loads(self.cli('check', target, '--brief', self.brief, '--taste', taste, '--no-ocr').stdout)
        self.assertEqual(next(c for c in r['autocheck']['checks'] if c['id'] == 'whites')['status'], 'PASS')

    def test_allotment_real_manifest(self):
        from PIL import Image
        target = cd.ROOT / 'examples/aesthetic-across-domains/poster/after.png'
        manifest = target.parent / 'src/after-boxes.json'
        lines = ['Hollin Lane Allotments', 'SEED', 'SWAP', 'Sat 13 March 2027',
                 '10:00 to 13:00, in the hut', 'Bring spare seeds and take some home.',
                 'Envelopes provided. Free. Tea in the hut.']
        b = copy.deepcopy(self.b)
        with Image.open(target) as im:
            b['format'].update(width=im.width, height=im.height)
        b['copy'] = [dict(text=line, count=1) for line in lines]
        brief = self.write('allotment.json', b)
        r = json.loads(self.cli('check', target, '--brief', brief, '--boxes', manifest).stdout)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        self.assertIn(next(c for c in r['checks'] if c['id'] == 'contrast')['status'], ('PASS', 'FAIL'))

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
