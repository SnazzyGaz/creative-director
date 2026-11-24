#!/usr/bin/env python3
"""cd v2 front-door tests: python3 tools/tests/cd_cases.py (unittest, no paid/model calls)."""
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
        return subprocess.run([sys.executable, str(Path(cd.__file__)), *map(str, args)], capture_output=True, text=True)

    def test_help(self):
        p = self.cli('--help')
        self.assertEqual(p.returncode, 0)
        for word in ('brief', 'taste', 'rule', 'check', 'select', 'load', 'compose', 'generate-docs'):
            self.assertIn(word, p.stdout)

    def test_posix_paths_and_no_duplicates(self):
        # Regression test for Windows backslash bug in rules() and load_plan().
        for rid, (path, _) in cd.rules().items():
            self.assertNotIn('\\', path, f'Backslash in rule path for {rid}: {path}')
        data = cd.load_plan(dict(self.b, medium='poster', feeling='Bold concert'))
        for f in data['files']:
            self.assertNotIn('\\', f, f'Backslash in load_plan file: {f}')
        self.assertEqual(len(data['files']), len(set(data['files'])))

    def test_manifest_routing_precision(self):
        # Poster must load layout/typography/composition/colour-value and NOT falsely load web-ui.
        poster = dict(self.b, medium='poster', description='Harbor Night Market poster')
        data = cd.load_plan(poster)
        self.assertEqual(data['schema_version'], 2)
        self.assertEqual(data['tier'], 'directed')
        self.assertIn('poster-cover-social', data['matched'])
        self.assertIn('modules/layout/README.md', data['files'])
        self.assertIn('modules/composition/sitting-right.md', data['files'])
        self.assertNotIn('modules/web-ui/README.md', data['files'])
        self.assertIn('LAY-7', data['rules'])
        self.assertIn('COMP-23', data['rules'])

        # Screen format loads web-ui cleanly.
        screen = dict(self.b, medium='app screen', format={'kind': 'screen', 'width': 390, 'height': 844})
        sdata = cd.load_plan(screen)
        self.assertIn('modules/web-ui/README.md', sdata['files'])
        self.assertIn('UI-6', sdata['hard_gates'])
        self.assertIn('UI-10', sdata['hard_gates'])

        # Logo loads brand + logo + mark-making.
        logo = dict(self.b, medium='logo', description='One-colour mark for a survey firm')
        ldata = cd.load_plan(logo)
        self.assertIn('logo-mark', ldata['matched'])
        self.assertIn('modules/brand/logo.md', ldata['files'])
        self.assertIn('LOGO-3', ldata['rules'])

    def test_tiers_and_energy_triggers(self):
        # Fast tier omits creative-direction.md; remake tier loads first-principles.md.
        fast = cd.load_plan(dict(self.b, tier='fast'))
        self.assertEqual(fast['tier'], 'fast')
        self.assertEqual(fast['roughs'], [0, 0])
        self.assertNotIn('core/creative-direction.md', fast['files'])

        remake = cd.load_plan(dict(self.b, description='Redo this flyer from scratch'))
        self.assertEqual(remake['tier'], 'remake')
        self.assertIn('core/first-principles.md', remake['files'])

        # Energy triggers from feeling/intent_tags (including rich words like kinetic/festival), never medium alone.
        energetic = cd.load_plan(dict(self.b, medium='poster', feeling='Kinetic playful festival'))
        self.assertTrue(energetic['energetic'])
        self.assertIn('core/energy-pass.md', energetic['files'])

        quiet = cd.load_plan(dict(self.b, medium='concert poster', feeling='Quiet archival notice'))
        self.assertFalse(quiet['energetic'])
        self.assertNotIn('core/energy-pass.md', quiet['files'])

    def test_optional_domains_isolated(self):
        # Writing triggers only on explicit writing medium or writing phrases, and skips visual sitting-right guard.
        for desc in ('Website copy for an about page', 'An email reply to a customer', 'Microcopy for empty states'):
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

    def test_init_brief_and_taste_no_overwrite(self):
        out = self.root / 'new.json'
        self.assertEqual(self.cli('brief', 'init', 'One idea', '--out', out).returncode, 0)
        initial = json.loads(out.read_text(encoding='utf-8'))
        self.assertEqual(initial['description'], 'One idea')
        self.assertEqual(initial['medium'], '')
        self.assertIs(initial['has_people_or_animals'], False)
        self.assertEqual(self.cli('load', '--brief', out).returncode, 2)
        self.assertEqual(self.cli('brief', 'init', '--out', out).returncode, 2)

        tout = self.root / 'taste.json'
        self.assertEqual(self.cli('taste', 'init', '--out', tout).returncode, 0)
        self.assertEqual(self.cli('taste', 'init', '--out', tout).returncode, 2)
        t = json.loads(tout.read_text(encoding='utf-8'))
        self.assertEqual(t['whites']['default'], 'neutral')

    def test_rule_lookup_and_boundary(self):
        for rid in ('CD-7', 'CORE-2', 'FLOW-5', '3D-1', 'FILM-GEN-8', 'WRITE-1', 'WRITE-11'):
            p = self.cli('rule', rid)
            self.assertEqual(p.returncode, 0, p.stdout)
            self.assertIn(rid, p.stdout)
            self.assertIn('<!-- ', p.stdout)
        p = self.cli('rule', 'CD-1')
        self.assertIn('Have a brief', p.stdout)
        self.assertNotIn('## CD-2.', p.stdout)
        p = self.cli('rule', 'CD-7000')
        self.assertEqual(p.returncode, 2)

    def test_copy_exact_and_counts(self):
        self.b['copy'] = [{'text': 'Open 10–6.', 'count': 2}]
        self.assertEqual(cd.copy_check(self.b, 'Open 10–6.\nOpen 10–6.', 'fixture')['status'], 'PASS')
        for text in ('Open 10–6.', 'open 10–6.\nOpen 10–6.', 'Open 10–6.\nOpen 10–6.\nExtra'):
            self.assertEqual(cd.copy_check(self.b, text, 'fixture')['status'], 'FAIL')
        self.b['exact_copy'] = False
        self.assertEqual(cd.copy_check(self.b, 'Open 10–6.\nOpen 10–6.\nExtra', 'fixture')['status'], 'PASS')
        self.assertEqual(cd.copy_check(self.b, None, 'fixture')['status'], 'SKIP')

    def test_invalid_briefs_json(self):
        for change in ({'medium': ''}, {'medium': 3}, {'tier': 'huge'}, {'has_people_or_animals': 1}, {'schema_version': 4}, {'safe_area_px': -1}):
            b = copy.deepcopy(self.b)
            b.update(change)
            bad = self.write('bad.json', b)
            p = self.cli('check', self.roughs[0], '--brief', bad)
            self.assertEqual(p.returncode, 2)
            self.assertEqual(json.loads(p.stdout)['status'], 'ERROR')

    def test_proportional_select_3_roughs_and_bracket(self):
        # 3 roughs now supported cleanly (Tier 2 default)!
        p = self.cli('select', *self.roughs[:3], '--brief', self.brief)
        self.assertEqual(p.returncode, 0, p.stderr)
        pkt = json.loads(p.stdout)
        self.assertEqual(pkt['mode'], 'pairwise')
        self.assertEqual(len(pkt['roughs']), 3)

        # Honest same-session-self-review is accepted and recorded transparently.
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

        # 6 roughs defaults to bracket mode (no need for 15 pairwise essays).
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
        p6v = self.cli('select', *self.roughs[:6], '--brief', self.brief, '--review', self.write('rev6.json', rev6))
        self.assertEqual(p6v.returncode, 0, p6v.stdout)

        # Single rough still rejected.
        self.assertEqual(self.cli('select', self.roughs[0], '--brief', self.brief).returncode, 2)

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

    def test_check_json_pass_and_missing_evidence(self):
        code, r = self.mock_check(boxes=[[100, 100, 300, 150]])
        self.assertEqual(code, 0)
        self.assertTrue(r['passed'])
        for kwargs in ({'text': None}, {'complete': False}, {'count': True}, {'helper_status': 'SKIP'}, {}):
            code, r = self.mock_check(**kwargs)
            self.assertEqual(code, 1)
            self.assertFalse(r['passed'])

    def test_counts_bound_to_render(self):
        obs = dict(target_sha256=hashlib.sha256(self.roughs[0].read_bytes()).hexdigest(), counts={'cups': dict(count=3, provenance='2x crop')})
        path = self.write('counts.json', obs)
        self.assertEqual(self.mock_check(count=True, observations=path, boxes=[[100, 100, 300, 150]])[0], 0)
        obs['target_sha256'] = 'wrong'
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            self.mock_check(count=True, observations=self.write('counts.json', obs))

    def test_manifest_auto_feeds_contrast_and_priority(self):
        from PIL import Image, ImageDraw
        target = self.root / 'poster.png'
        im = Image.new('RGB', (800, 800), '#FFFFFF')
        d = ImageDraw.Draw(im)
        d.text((100, 100), 'Open', fill='#111111')
        im.save(target)
        # Manifest beside image automatically checks copy, safe-area, AND contrast (no SKIP)!
        self.write('poster-boxes.json', [['Open', [95, 95, 160, 120], [17, 17, 17]]])
        b = copy.deepcopy(self.b)
        b['copy'] = [{'text': 'Open', 'count': 1}]
        brief = self.write('poster-brief.json', b)
        p = self.cli('check', target, '--brief', brief)
        r = json.loads(p.stdout)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'safe-area')['status'], 'PASS')
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'contrast')['status'], 'PASS')

    def test_taste_warm_whites_forwarded(self):
        from PIL import Image, ImageDraw
        target = self.root / 'warm.png'
        im = Image.new('RGB', (800, 800), '#F5EEDC')  # Warm paper luma ~238, red > blue
        ImageDraw.Draw(im).rectangle([100, 100, 700, 700], outline='#222222', width=4)
        im.save(target)
        taste = self.write('taste.json', {'schema_version': 1, 'name': 'bakery', 'whites': {'default': 'warm', 'warm_reason': 'cream paper stock'}})
        p = self.cli('check', target, '--brief', self.brief, '--taste', taste, '--no-ocr')
        r = json.loads(p.stdout)
        whites = next(c for c in r['autocheck']['checks'] if c['id'] == 'whites')
        self.assertEqual(whites['status'], 'PASS')

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
        p = self.cli('check', target, '--brief', brief, '--boxes', manifest)
        r = json.loads(p.stdout)
        self.assertEqual(next(c for c in r['checks'] if c['id'] == 'copy')['status'], 'PASS')
        self.assertIn(next(c for c in r['checks'] if c['id'] == 'contrast')['status'], ('PASS', 'FAIL'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
