#!/usr/bin/env python3
"""Zero-dependency, workspace-sandboxed stdio MCP server for creative-director v2.

Security model:
  All file reads and writes are strictly confined to --workspace (or CD_MCP_WORKSPACE,
  defaulting to the current working directory). Path traversal (..), arbitrary absolute
  paths outside the workspace, and http(s) URLs (unless --allow-urls) are rejected.

Run directly:
  python3 tools/mcp_server.py --workspace /path/to/project
Or after `pip install -e .`:
  cd-mcp --workspace /path/to/project
"""
import argparse
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stdin, 'reconfigure'):
    sys.stdin.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import cd  # noqa: E402
import compose  # noqa: E402
import contrast  # noqa: E402

SERVER_INFO = {
    'name': 'creative-director',
    'version': cd.load_manifest().get('version', '2.0.0-alpha.1'),
}
PROTOCOL_VERSION = '2024-11-05'
URL_RE = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*://')

TOOLS = [
    {
        'name': 'cd_load_plan',
        'description': 'Route a structured brief to its proportional tier, required modules, hard gates, and canonical rule IDs.',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'brief': {'type': 'object', 'description': 'Brief object matching tools/brief-template.json (must include nonempty medium).'},
                'taste_path': {'type': 'string', 'description': 'Optional path to taste.json inside the workspace.'},
            },
            'required': ['brief'],
        },
    },
    {
        'name': 'cd_get_rule',
        'description': 'Return the canonical definition, check, fix, evidence grade, and sources for a rule ID (e.g. CD-7, UI-6, CHAR-9).',
        'inputSchema': {
            'type': 'object',
            'properties': {'rule_id': {'type': 'string'}},
            'required': ['rule_id'],
        },
    },
    {
        'name': 'cd_check',
        'description': 'Run deterministic mechanical checks (autocheck, exact copy, safe area, contrast, counts, format) against a render inside the workspace.',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'target': {'type': 'string', 'description': 'Path inside workspace to rendered image or HTML file.'},
                'brief_path': {'type': 'string', 'description': 'Path inside workspace to brief.json.'},
                'taste_path': {'type': 'string', 'description': 'Optional path inside workspace to taste.json.'},
                'boxes_path': {'type': 'string', 'description': 'Optional path inside workspace to text manifest JSON.'},
                'observations_path': {'type': 'string', 'description': 'Optional path inside workspace to SHA-256 bound count observations.'},
                'no_ocr': {'type': 'boolean', 'default': False},
            },
            'required': ['target', 'brief_path'],
        },
    },
    {
        'name': 'cd_compose',
        'description': 'Deterministically composite an art plate, panels, official logo marks, accurate bar charts, and locked typography into a PNG plus <stem>-boxes.json manifest inside the workspace.',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'spec': {'type': 'object', 'description': 'Composition specification object (all file paths confined to workspace).'},
                'out_path': {'type': 'string', 'description': 'Output PNG path inside the workspace.'},
                'html_path': {'type': 'string', 'description': 'Optional standalone HTML export path inside the workspace.'},
                'allow_unsafe': {'type': 'boolean', 'default': False},
            },
            'required': ['spec', 'out_path'],
        },
    },
    {
        'name': 'cd_lookbook_find',
        'description': 'Search the 415 curated visual looks by use, mood, colour, or similarity (LOOK-1..3).',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'use': {'type': 'string'},
                'mood': {'type': 'string'},
                'colour': {'type': 'string', 'description': 'Comma-separated hex colours, e.g. "#c5040f,#ed6322".'},
                'like': {'type': 'string', 'description': 'Look ID for nearest neighbours, e.g. "LB-010".'},
                'avoid': {'type': 'string'},
                'max_out': {'type': 'integer', 'default': 3},
                'limit': {'type': 'integer', 'default': 6},
            },
        },
    },
    {
        'name': 'cd_font_find',
        'description': 'Search the 107 free font families (OFL/Apache) by mood, genre, or theme.',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'mood': {'type': 'string'},
                'genre': {'type': 'string'},
                'theme': {'type': 'string'},
                'limit': {'type': 'integer', 'default': 6},
            },
        },
    },
    {
        'name': 'cd_contrast',
        'description': 'Compute WCAG 2.1 luminance contrast ratio and AA/AAA pass flags for two hex colours.',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'fg': {'type': 'string', 'description': 'Foreground hex colour, e.g. "#111827".'},
                'bg': {'type': 'string', 'description': 'Background hex colour, e.g. "#FFFFFF".'},
            },
            'required': ['fg', 'bg'],
        },
    },
]

RESOURCES = [
    {'uri': 'creative-director://kernel', 'name': 'Always-on Kernel', 'mimeType': 'text/markdown', 'description': 'AGENTS.md + core/kernel.md.'},
    {'uri': 'creative-director://manifest', 'name': 'Declarative Manifest', 'mimeType': 'application/json', 'description': 'manifest.json: modules, routes, tiers, hard gates.'},
    {'uri': 'creative-director://taste/default', 'name': 'Default Taste Profile', 'mimeType': 'application/json', 'description': 'Neutral taste.default.json starter profile.'},
]


def resolve_safe_path(raw_path, workspace: Path, *, write: bool = False, allow_urls: bool = False, allow_repo_fonts: bool = False):
    """Confine every filesystem path to the configured workspace root."""
    if not isinstance(raw_path, str) or not raw_path.strip() or '\x00' in raw_path:
        raise ValueError('path must be a nonempty string without NUL bytes')
    if URL_RE.match(raw_path):
        if allow_urls and not write and raw_path.startswith(('http://', 'https://')):
            return raw_path
        raise ValueError(f'URL targets are disabled by default (pass --allow-urls to permit): {raw_path}')
    p = Path(raw_path)
    resolved = (workspace / p).resolve() if not p.is_absolute() else p.resolve()
    if resolved.is_relative_to(workspace):
        return str(resolved)
    if allow_repo_fonts and not write:
        fonts_dir = (ROOT / 'fonts').resolve()
        if resolved.is_relative_to(fonts_dir):
            return str(resolved)
    raise ValueError(f'path outside MCP workspace ({workspace}): {raw_path}')


def sanitize_compose_spec(spec, workspace: Path):
    if not isinstance(spec, dict):
        raise ValueError('spec must be an object')
    clean = json.loads(json.dumps(spec))
    bg = clean.get('background')
    if isinstance(bg, dict) and bg.get('image'):
        bg['image'] = resolve_safe_path(bg['image'], workspace, write=False)
    for mark in clean.get('marks', []):
        if isinstance(mark, dict) and mark.get('path'):
            mark['path'] = resolve_safe_path(mark['path'], workspace, write=False)
    for item in clean.get('text', []):
        if isinstance(item, dict) and item.get('font'):
            fval = str(item['font'])
            # Allow simple logical font names ("bold", "InstrumentSans") or verified paths inside workspace/repo fonts.
            if '/' in fval or '\\' in fval or fval.lower().endswith(('.ttf', '.otf', '.ttc')):
                item['font'] = resolve_safe_path(fval, workspace, write=False, allow_repo_fonts=True)
    return clean


def call_tool(name, args, workspace: Path, allow_urls: bool = False):
    args = args or {}
    if name == 'cd_load_plan':
        b = dict(cd.load_json(cd.BRIEF))
        b.update(args['brief'])
        if not isinstance(b.get('medium'), str) or not b['medium'].strip():
            raise ValueError('brief.medium must be a nonempty string')
        tpath = resolve_safe_path(args['taste_path'], workspace, write=False) if args.get('taste_path') else None
        taste, tsrc = cd.read_taste(tpath)
        return cd.load_plan(b, taste=taste, taste_source=tsrc)

    if name == 'cd_get_rule':
        rid = str(args['rule_id']).upper()
        found = cd.rules().get(rid)
        if not found:
            raise ValueError(f'unknown rule ID: {rid}')
        return {'id': rid, 'path': found[0], 'text': found[1]}

    if name == 'cd_check':
        target = resolve_safe_path(args['target'], workspace, write=False, allow_urls=allow_urls)
        brief_path = resolve_safe_path(args['brief_path'], workspace, write=False)
        taste_path = resolve_safe_path(args['taste_path'], workspace, write=False) if args.get('taste_path') else None
        boxes_path = resolve_safe_path(args['boxes_path'], workspace, write=False) if args.get('boxes_path') else None
        obs_path = resolve_safe_path(args['observations_path'], workspace, write=False) if args.get('observations_path') else None
        ns = cd.argparse.Namespace(
            target=target,
            brief=brief_path,
            taste=taste_path,
            boxes=boxes_path,
            ocr_text=None,
            no_ocr=bool(args.get('no_ocr', False)),
            text_box=[],
            observations=obs_path,
        )
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cd.check(ns)
        data = json.loads(buf.getvalue())
        data['exit_code'] = code
        return data

    if name == 'cd_compose':
        safe_spec = sanitize_compose_spec(args['spec'], workspace)
        out_path = resolve_safe_path(args['out_path'], workspace, write=True)
        html_path = resolve_safe_path(args['html_path'], workspace, write=True) if args.get('html_path') else None
        return compose.compose_spec(
            safe_spec,
            out_path,
            base_dir=workspace,
            html_out=html_path,
            allow_unsafe=bool(args.get('allow_unsafe', False)),
        )

    if name == 'cd_lookbook_find':
        cmd = [sys.executable, str(TOOLS_DIR / 'lookbook_find.py')]
        for flag, key in (('--use', 'use'), ('--mood', 'mood'), ('--colour', 'colour'),
                          ('--like', 'like'), ('--avoid', 'avoid'), ('--max-out', 'max_out'), ('--limit', 'limit')):
            if args.get(key) is not None:
                cmd += [flag, str(args[key])]
        p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=30)
        if p.returncode != 0:
            raise ValueError((p.stderr or p.stdout).strip())
        return {'results': p.stdout.strip()}

    if name == 'cd_font_find':
        cmd = [sys.executable, str(TOOLS_DIR / 'font_find.py')]
        for flag, key in (('--mood', 'mood'), ('--genre', 'genre'), ('--theme', 'theme'), ('--limit', 'limit')):
            if args.get(key) is not None:
                cmd += [flag, str(args[key])]
        p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=30)
        if p.returncode != 0:
            raise ValueError((p.stderr or p.stdout).strip())
        return {'results': p.stdout.strip()}

    if name == 'cd_contrast':
        r = contrast.ratio(contrast.hex2rgb(args['fg']), contrast.hex2rgb(args['bg']))
        return {
            'fg': args['fg'],
            'bg': args['bg'],
            'ratio': round(r, 2),
            'aa_normal': r >= 4.5,
            'aa_large': r >= 3.0,
            'aaa_normal': r >= 7.0,
        }

    raise ValueError(f'unknown tool: {name}')


def read_resource(uri):
    if uri == 'creative-director://kernel':
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8') + '\n\n---\n\n' + (ROOT / 'core/kernel.md').read_text(encoding='utf-8')
        return {'uri': uri, 'mimeType': 'text/markdown', 'text': text}
    if uri == 'creative-director://manifest':
        return {'uri': uri, 'mimeType': 'application/json', 'text': (ROOT / 'manifest.json').read_text(encoding='utf-8')}
    if uri == 'creative-director://taste/default':
        return {'uri': uri, 'mimeType': 'application/json', 'text': (ROOT / 'taste.default.json').read_text(encoding='utf-8')}
    raise ValueError(f'unknown resource URI: {uri}')


def handle_message(msg, workspace: Path, allow_urls: bool = False):
    method = msg.get('method')
    mid = msg.get('id')
    params = msg.get('params') or {}

    if mid is None and method in ('notifications/initialized', 'notifications/cancelled'):
        return None

    try:
        if method == 'initialize':
            res = {
                'protocolVersion': PROTOCOL_VERSION,
                'capabilities': {'tools': {}, 'resources': {}},
                'serverInfo': SERVER_INFO,
            }
        elif method == 'ping':
            res = {}
        elif method == 'tools/list':
            res = {'tools': TOOLS}
        elif method == 'tools/call':
            data = call_tool(params.get('name'), params.get('arguments'), workspace=workspace, allow_urls=allow_urls)
            res = {'content': [{'type': 'text', 'text': json.dumps(data, indent=2, ensure_ascii=False)}], 'isError': False}
        elif method == 'resources/list':
            res = {'resources': RESOURCES}
        elif method == 'resources/read':
            res = {'contents': [read_resource(params.get('uri'))]}
        else:
            return {'jsonrpc': '2.0', 'id': mid, 'error': {'code': -32601, 'message': f'Method not found: {method}'}}
        return {'jsonrpc': '2.0', 'id': mid, 'result': res}
    except Exception as exc:
        if method == 'tools/call':
            return {
                'jsonrpc': '2.0',
                'id': mid,
                'result': {'content': [{'type': 'text', 'text': json.dumps({'error': str(exc)})}], 'isError': True},
            }
        return {'jsonrpc': '2.0', 'id': mid, 'error': {'code': -32602, 'message': str(exc)}}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workspace', default=os.environ.get('CD_MCP_WORKSPACE', '.'),
                    help='Project directory to confine all file reads/writes (default: CD_MCP_WORKSPACE or cwd)')
    ap.add_argument('--allow-urls', action='store_true', help='Allow http(s) URL targets in cd_check')
    a = ap.parse_args(argv)
    workspace = Path(a.workspace).resolve()
    if not workspace.is_dir():
        sys.stderr.write(f'MCP workspace directory does not exist: {workspace}\n')
        return 2

    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as exc:
            resp = {'jsonrpc': '2.0', 'id': None, 'error': {'code': -32700, 'message': f'Parse error: {exc}'}}
        else:
            resp = handle_message(msg, workspace=workspace, allow_urls=a.allow_urls)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + '\n')
            sys.stdout.flush()
    return 0


if __name__ == '__main__':
    sys.exit(main())
