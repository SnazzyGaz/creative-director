#!/usr/bin/env python3
"""Deterministic compositor tests: compose.py -> cd.py check end-to-end."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cd
import compose


class ComposeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_end_to_end_compose_and_cd_check(self):
        # Create an official mark PNG to place unaltered (BRAND-4).
        mark = self.root / 'mark.png'
        m = Image.new('RGBA', (120, 60), (0, 0, 0, 0))
        ImageDraw.Draw(m).rectangle([0, 0, 119, 59], fill=(220, 38, 38, 255))
        m.save(mark)

        spec = {
            'width': 1200,
            'height': 800,
            'safe_area_px': 48,
            'background': '#FFFFFF',
            'panels': [
                {'box': [48, 48, 1152, 230], 'fill': '#111827', 'opacity': 1.0, 'radius': 0}
            ],
            'marks': [
                {'path': str(mark), 'x': 960, 'y': 90, 'max_width': 140, 'max_height': 70}
            ],
            'charts': [
                {
                    'type': 'bars',
                    'box': [80, 320, 1100, 680],
                    'bar_color': '#0F766E',
                    'text_color': '#111827',
                    'data': [
                        {'label': 'Solar', 'value': 62, 'display': '62%'},
                        {'label': 'Wind', 'value': 28, 'display': '28%'},
                        {'label': 'Hydro', 'value': 10, 'display': '10%'},
                    ],
                }
            ],
            'text': [
                {'text': 'GRID REPORT 2027', 'x': 80, 'y': 88, 'size': 48, 'color': '#FFFFFF', 'font': 'bold'},
                {'text': 'Clean energy share by source', 'x': 80, 'y': 158, 'size': 24, 'color': '#F3F4F6'},
            ],
        }
        out_png = self.root / 'report.png'
        out_html = self.root / 'report.html'
        res = compose.compose_spec(spec, out_png, base_dir=self.root, html_out=out_html)
        self.assertTrue(out_png.is_file())
        self.assertTrue(out_html.is_file())
        self.assertTrue((self.root / 'report-boxes.json').is_file())
        self.assertEqual(res['lines_rendered'], 2)
        self.assertEqual(res['marks_placed'], 1)
        self.assertEqual(res['charts_drawn'], 1)
        self.assertTrue(res['safe_area_ok'])

        # Now run cd.py check against the composed PNG: copy, contrast, safe-area, and format must ALL PASS!
        brief = json.loads(cd.BRIEF.read_text(encoding='utf-8'))
        brief.update(
            medium='infographic',
            idea='Clean energy share',
            feeling='Clear factual report',
            audience='Public',
            purpose='Report',
            success='Bars and labels read clearly',
            format={'kind': 'fixed', 'width': 1200, 'height': 800},
            safe_area_px=48,
            copy=[
                {'text': 'GRID REPORT 2027', 'count': 1},
                {'text': 'Clean energy share by source', 'count': 1},
            ],
        )
        bpath = self.root / 'brief.json'
        bpath.write_text(json.dumps(brief), encoding='utf-8')
        p = subprocess.run([sys.executable, str(Path(cd.__file__)), 'check', str(out_png), '--brief', str(bpath)], capture_output=True, text=True)
        report = json.loads(p.stdout)
        by_id = {c['id']: c['status'] for c in report['checks']}
        self.assertEqual(by_id['copy'], 'PASS', report)
        self.assertEqual(by_id['contrast'], 'PASS', report)
        self.assertEqual(by_id['safe-area'], 'PASS', report)
        self.assertEqual(by_id['format'], 'PASS', report)

    def test_safe_area_violation_rejected_by_default(self):
        spec = {
            'width': 600,
            'height': 400,
            'safe_area_px': 48,
            'background': '#FFFFFF',
            'text': [{'text': 'Too close', 'x': 4, 'y': 4, 'size': 24, 'color': '#111111'}],
        }
        with self.assertRaisesRegex(ValueError, 'safe area'):
            compose.compose_spec(spec, self.root / 'bad.png')
        res = compose.compose_spec(spec, self.root / 'bad.png', allow_unsafe=True)
        self.assertFalse(res['safe_area_ok'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
