#!/usr/bin/env python3
"""Stdio JSON-RPC 2.0 + workspace-sandbox security tests for tools/mcp_server.py."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOLS_DIR = Path(__file__).resolve().parents[1]
SERVER = TOOLS_DIR / 'mcp_server.py'


class McpServerTests(unittest.TestCase):
    def rpc(self, messages, workspace):
        payload = '\n'.join(json.dumps(m) for m in messages) + '\n'
        p = subprocess.run(
            [sys.executable, str(SERVER), '--workspace', str(workspace)],
            input=payload, capture_output=True, text=True, encoding='utf-8', timeout=30,
        )
        self.assertEqual(p.returncode, 0, p.stderr)
        return [json.loads(line) for line in p.stdout.splitlines() if line.strip()]

    def test_handshake_tools_and_resources(self):
        with tempfile.TemporaryDirectory() as td:
            resps = self.rpc([
                {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {}},
                {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
                {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'},
                {'jsonrpc': '2.0', 'id': 3, 'method': 'resources/list'},
                {'jsonrpc': '2.0', 'id': 4, 'method': 'resources/read', 'params': {'uri': 'creative-director://kernel'}},
            ], workspace=td)
            self.assertEqual(len(resps), 4)
            self.assertEqual(resps[0]['result']['serverInfo']['name'], 'creative-director')
            tool_names = {t['name'] for t in resps[1]['result']['tools']}
            self.assertTrue({'cd_load_plan', 'cd_get_rule', 'cd_check', 'cd_compose', 'cd_lookbook_find', 'cd_font_find', 'cd_contrast'} <= tool_names)
            uris = {r['uri'] for r in resps[2]['result']['resources']}
            self.assertIn('creative-director://kernel', uris)
            self.assertIn('Creative Director Kernel', resps[3]['result']['contents'][0]['text'])

    def test_tool_calls_inside_workspace(self):
        with tempfile.TemporaryDirectory() as td:
            resps = self.rpc([
                {'jsonrpc': '2.0', 'id': 10, 'method': 'tools/call', 'params': {'name': 'cd_get_rule', 'arguments': {'rule_id': 'CD-7'}}},
                {'jsonrpc': '2.0', 'id': 11, 'method': 'tools/call', 'params': {'name': 'cd_contrast', 'arguments': {'fg': '#111827', 'bg': '#FFFFFF'}}},
                {'jsonrpc': '2.0', 'id': 12, 'method': 'tools/call', 'params': {'name': 'cd_load_plan', 'arguments': {'brief': {'medium': 'poster', 'feeling': 'Bold festival'}}}},
                {'jsonrpc': '2.0', 'id': 13, 'method': 'tools/call', 'params': {
                    'name': 'cd_compose',
                    'arguments': {
                        'out_path': 'card.png',
                        'spec': {'width': 600, 'height': 400, 'safe_area_px': 40, 'background': '#FFFFFF',
                                 'text': [{'text': 'MCP TEST', 'x': 60, 'y': 80, 'size': 32, 'color': '#111111'}]},
                    },
                }},
                {'jsonrpc': '2.0', 'id': 14, 'method': 'tools/call', 'params': {'name': 'cd_lookbook_find', 'arguments': {'use': 'poster', 'mood': 'bold', 'limit': 3}}},
            ], workspace=td)
            rule_data = json.loads(resps[0]['result']['content'][0]['text'])
            self.assertEqual(rule_data['id'], 'CD-7')
            self.assertEqual(rule_data['path'], 'core/creative-direction.md')

            c_data = json.loads(resps[1]['result']['content'][0]['text'])
            self.assertTrue(c_data['aa_normal'])
            self.assertGreater(c_data['ratio'], 15.0)

            plan = json.loads(resps[2]['result']['content'][0]['text'])
            self.assertTrue(plan['energetic'])
            self.assertNotIn('modules/web-ui/README.md', plan['files'])

            comp = json.loads(resps[3]['result']['content'][0]['text'])
            self.assertEqual(comp['status'], 'OK')
            self.assertTrue((Path(td) / 'card.png').is_file())

            lb = json.loads(resps[4]['result']['content'][0]['text'])
            self.assertIn('LB-', lb['results'])

    def test_workspace_sandbox_blocks_escapes_and_urls(self):
        with tempfile.TemporaryDirectory() as outer:
            ws = Path(outer) / 'project'
            ws.mkdir()
            outside_file = Path(outer) / 'secret.json'
            outside_file.write_text('{"secret": true}', encoding='utf-8')
            escape_out = Path(outer) / 'escaped.png'

            resps = self.rpc([
                # Path traversal write escape
                {'jsonrpc': '2.0', 'id': 20, 'method': 'tools/call', 'params': {
                    'name': 'cd_compose',
                    'arguments': {'out_path': '../escaped.png', 'spec': {'width': 200, 'height': 200, 'background': '#FFFFFF'}},
                }},
                # Absolute path write escape
                {'jsonrpc': '2.0', 'id': 21, 'method': 'tools/call', 'params': {
                    'name': 'cd_compose',
                    'arguments': {'out_path': str(escape_out), 'spec': {'width': 200, 'height': 200, 'background': '#FFFFFF'}},
                }},
                # Read escape via taste_path
                {'jsonrpc': '2.0', 'id': 22, 'method': 'tools/call', 'params': {
                    'name': 'cd_load_plan',
                    'arguments': {'brief': {'medium': 'poster'}, 'taste_path': str(outside_file)},
                }},
                # Read escape inside compose background image
                {'jsonrpc': '2.0', 'id': 23, 'method': 'tools/call', 'params': {
                    'name': 'cd_compose',
                    'arguments': {'out_path': 'ok.png', 'spec': {'width': 200, 'height': 200, 'background': {'image': '../secret.json'}}},
                }},
                # URL blocked by default (anti-SSRF)
                {'jsonrpc': '2.0', 'id': 24, 'method': 'tools/call', 'params': {
                    'name': 'cd_check',
                    'arguments': {'target': 'http://127.0.0.1:8080/', 'brief_path': 'brief.json'},
                }},
            ], workspace=ws)

            for r in resps:
                self.assertTrue(r['result']['isError'], f'Expected sandbox rejection, got: {r}')
                msg = json.loads(r['result']['content'][0]['text'])['error']
                self.assertTrue('outside MCP workspace' in msg or 'URL targets are disabled' in msg, msg)
            self.assertFalse(escape_out.exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
