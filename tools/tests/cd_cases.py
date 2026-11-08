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
        self.b.update(medium='poster', idea='One opening', feeling='Quiet', audience='Visitors', purpose='Invite', success='Date reads')
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
        for word in ('brief', 'rule', 'check', 'select', 'load'):
            self.assertIn(word, p.stdout)

    def test_load_from_brief(self):
        poster = dict(self.b)
        poster['description'] = 'Harbor Night Market poster: a lantern over water'
        self.write('poster.json', poster)
        data = json.loads(self.cli('load', '--brief', self.root / 'poster.json').stdout)
        self.assertEqual(data['schema_version'], 1)
        self.assertIn('poster', data['matched'])
        self.assertIn('LAY-7', data['rules'])
        self.assertIn('modules/layout/README.md', data['files'])
        self.assertIn('COMP-23', data['rules'])
        self.assertIn('modules/composition/sitting-right.md', data['files'])

        screen = dict(self.b)
        screen['description'] = 'Bakery pickup confirmation'
        screen['format'] = {'kind': 'screen', 'width': 390, 'height': 844}
        self.write('screen.json', screen)
        data = json.loads(self.cli('load', '--brief', self.root / 'screen.json').stdout)
        self.assertIn('screen', data['matched'])
        self.assertIn('LAY-10', data['rules'])
        self.assertIn('COMP-23', data['rules'])

        logo = dict(self.b)
        logo['medium'] = 'logo'
        logo['description'] = 'A one-colour logo for a survey firm'
        self.write('logo.json', logo)
        data = json.loads(self.cli('load', '--brief', self.root / 'logo.json').stdout)
        self.assertIn('logo', data['matched'])
        self.assertIn('LOGO-3', data['rules'])
        self.assertIn('modules/brand/logo.md', data['files'])

    def test_writing_load_from_brief(self):
        for description in ('Website copy for an about page',
                            'An email reply to a customer',
                            'A poster with supporting copy to draft',
                            'Microcopy for empty states and error messages',
                            'A reply to a customer', 'Replies to supporters'):
            with self.subTest(description=description):
                brief = dict(self.b, description=description)
                path = self.write('writing.json', brief)
                result = self.cli('load', '--brief', path)
                self.assertEqual(result.returncode, 0, result.stderr)
                data = json.loads(result.stdout)
                self.assertIn('writing', data['matched'])
                self.assertIn('modules/writing/README.md', data['files'])
                self.assertTrue({f'WRITE-{i}' for i in range(1, 12)} <= set(data['rules']))
        for description in ('A book cover', 'A concert poster', 'A photograph'):
            with self.subTest(description=description):
                data = cd.load_plan(dict(self.b, description=description))
                self.assertNotIn('writing', data['matched'])
                self.assertNotIn('modules/writing/README.md', data['files'])

    def test_init_and_no_overwrite(self):
        out = self.root / 'new.json'
        self.assertEqual(self.cli('brief', 'init', 'One idea', '--out', out).returncode, 0)
        initial = json.loads(out.read_text())
        self.assertEqual(initial['description'], 'One idea')
        self.assertEqual(initial['medium'], '')
        self.assertIs(initial['has_people_or_animals'], False)
        self.assertEqual(self.cli('load', '--brief', out).returncode, 2)
        self.assertEqual(self.cli('brief', 'init', '--out', out).returncode, 2)
        self.assertEqual(json.loads(out.read_text())['description'], 'One idea')

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
        for change in ({'medium': ''}, {'medium': 3}, {'has_people_or_animals': 1}, {'has_people_or_animals': 'false'}, {'schema_version': 4}, {'format': []}, {'safe_area_px': -1}, {'copy': [{'text': 'x', 'count': -1}]}, {'constraints': 'no'}):
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
        a = cd.argparse.Namespace(target=str(self.roughs[0]), brief=brief, boxes=None, text_box=[], no_ocr=False, ocr_text=None, observations=observations)
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
        for kwargs, cid in (({'boxes': [[1, 100, 300, 150]]}, 'safe-area'),):
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
        self.assertEqual(boxes, [[100, 100, 160, 120]])
        self.assertIn('tesseract', source)
        with patch.object(cd.shutil, 'which', return_value=None):
            self.assertIsNone(cd.ocr_image(self.roughs[0])[0])

    def test_ocr_low_confidence_dropped(self):
        header = 'level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext\n'
        rows = ''.join(f'5\t1\t1\t1\t1\t{i}\t100\t100\t30\t20\t{conf}\t{text}\n'
                       for i, (conf, text) in enumerate([(49.9, 'junk'), (-1, 'invalid'), (50, 'Open')], 1))
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
        a = cd.argparse.Namespace(target=str(target), brief=self.write('image.json', b), boxes=manifest,
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
        self.assertFalse(r['passed'])  # FLAG is not certified PASS, but is not exit 1.
        c = next(c for c in r['checks'] if c['id'] == 'copy')
        self.assertEqual(c['status'], 'FLAG')
        self.assertEqual(c['crop_boxes'], [[100, 100, 200, 130]])
        self.assertEqual(len(c['crops']), 2)  # extra line + overview for missed text
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
        self.assertIn(str(path), next(c for c in r['checks'] if c['id'] == 'copy')['provenance'])
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

    def test_allotment_real_manifest(self):
        from PIL import Image
        target = cd.ROOT / 'examples/aesthetic-across-domains/poster/after.png'
        manifest = target.parent / 'src/after-boxes.json'
        lines = ['Hollin Lane Allotments', 'SEED', 'SWAP', 'Sat 13 March 2027',
                 '10:00 to 13:00, in the hut', 'Bring spare seeds and take some home.',
                 'Envelopes provided. Free. Tea in the hut.']
        self.assertEqual([row[0] for row in cd.load(manifest)], lines)
        b = copy.deepcopy(self.b)
        with Image.open(target) as im:
            b['format'].update(width=im.width, height=im.height)
        b['copy'] = [dict(text=line, count=1) for line in lines]
        brief = self.write('allotment.json', b)
        p = self.cli('check', target, '--brief', brief, '--boxes', manifest)
        self.assertIn(p.returncode, (0, 1), p.stdout + p.stderr)
        r = json.loads(p.stdout)
        c = next(c for c in r['checks'] if c['id'] == 'copy')
        self.assertEqual(c['status'], 'PASS')
        self.assertIn(str(manifest), c['provenance'])
        self.assertNotIn('tesseract', c['provenance'])
        # Image font-size/contrast evidence can still be incomplete; not an OCR failure.
        self.assertTrue(all(c['id'] != 'copy' for c in r['checks'] if c['status'] != 'PASS'))

    def test_load_every_task_row(self):
        # Independent fixtures in table order. A new task row must add a fixture.
        fixtures = [
            ('drawing', 'technical-drawing illustration composition colour-value', ''),
            ('balance', 'composition colour-value', ''),
            ('palette', 'colour-value', ''),
            ('animal', 'character technical-drawing illustration', ''),
            ('construction errors only', 'technical-drawing', ''),
            ('poster', 'layout typography composition illustration colour-value brand', ''),
            ('packaging', 'layout typography brand', ''),
            ('infographic', 'layout typography illustration character brand', 'modules/layout/infographics.md'),
            ('signage', 'layout typography', ''),
            ('wordmark', 'typography layout web-ui', ''),
            ('brand guide', 'brand', 'core/brand-intake.md'),
            ('landing page', 'web-ui typography brand lookbook', ''),
            ('checkout', 'ux web-ui', ''),
            ('whole product', 'web-ui ux', ''),
            ('3d render', '3d illustration', ''),
            ('3d as reference for a drawing', '3d technical-drawing', ''),
            ('logo', 'brand illustration web-ui', 'modules/brand/logo.md modules/brand/logo-notes.md modules/brand/mark-making.md modules/brand/clever-marks.md'),
            ('storyboard', 'illustration film', 'modules/illustration/notes.md modules/film/story.md modules/film/review.md'),
            ('video', 'film composition colour-value typography character', 'modules/film/story.md modules/film/review.md modules/film/edit.md modules/film/crossover.md'),
            ('clip made or altered by a video model', 'film character brand', 'modules/film/generated.md'),
            ('distinctive feel', 'aesthetic-critique', ''),
            ('from-scratch concepts', 'lookbook', ''),
            ('poster', '', 'core/energy-pass.md'),
            ('bolder', '', 'core/commands.md'),
            ('remake from scratch', 'aesthetic-critique brand', 'core/first-principles.md'),
            ('writing', 'writing', ''),
            ('photograph', 'photo character illustration brand', ''),
            ('image from an ai image model', 'illustration technical-drawing photo brand character', ''),
        ]
        routes = cd.task_routes()
        self.assertEqual(len(fixtures), len(routes))
        for (medium, modules, extra), (task, _) in zip(fixtures, routes):
            with self.subTest(task=task):
                b = dict(self.b, medium=medium, has_people_or_animals=(medium == 'animal'))
                if 'core/energy-pass.md' in extra:
                    b['feeling'] = 'Joyful brass-band concert'
                data = cd.load_plan(b)
                self.assertIn(task, data['reasons'])
                expected = {f'modules/{m}/README.md' for m in modules.split()} | set(extra.split())
                self.assertTrue(expected <= set(data['files']), expected - set(data['files']))
                self.assertTrue(all((cd.ROOT / p).is_file() for p in data['files']))
                self.assertTrue(set(data['rules']) <= cd.rules().keys())

    def test_load_explicit_gates_and_word_boundaries(self):
        for medium, path in [('infographic', 'layout/infographics.md'), ('packaging label', 'layout/README.md'),
                             ('3d render', '3d/README.md'), ('video', 'film/README.md'), ('landing page', 'web-ui/README.md')]:
            with self.subTest(medium=medium):
                self.assertIn('modules/' + path, cd.load_plan(dict(self.b, medium=medium))['files'])
        fox = cd.load_plan(dict(self.b, medium='picture-book cover', has_people_or_animals=True, description='A fox'))
        self.assertIn('modules/character/README.md', fox['files'])
        self.assertIn('CHAR-9', fox['rules'])
        self.assertIn('modules/layout/README.md', fox['files'])
        for subject in ('girl', 'baker', 'fox'):
            self.assertIn('CHAR-9', cd.load_plan(dict(self.b, description=subject, has_people_or_animals=True))['rules'])
        concert = cd.load_plan(dict(self.b, feeling='Joyful brass-band concert poster'))
        self.assertIn('core/energy-pass.md', concert['files'])
        self.assertNotIn('core/energy-pass.md', cd.load_plan(dict(self.b, medium='concert poster'))['files'])
        self.assertNotIn('modules/layout/README.md', cd.load_plan(dict(self.b, medium='discover'))['files'])
        for description, medium in [('A book cover', 'book cover'), ('A concert poster', 'poster'), ('A photograph', 'photograph')]:
            self.assertNotIn('modules/writing/README.md', cd.load_plan(dict(self.b, medium=medium, description=description))['files'])
        self.assertIn('WRITE-11', cd.load_plan(dict(self.b, medium='writing'))['rules'])


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
