"""intersect_cases.py: synthetic scenes plus the stool from examples/common-failures for tools/intersect.py.
python3 tools/tests/intersect_cases.py"""
import os, sys, subprocess, tempfile
import trimesh
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '..', 'intersect.py')

def box(ext, z0, xy=(0, 0)):   # metres, z-up, bottom at z0
    b = trimesh.creation.box(ext); b.apply_translation((xy[0], xy[1], z0 + ext[2] / 2)); return b

def scene(path, meshes):
    s = trimesh.Scene()
    for n, m in meshes: s.add_geometry(m, node_name=n, geom_name=n)
    s.export(path)

# (name, meshes, file ext, extra args, expected tags)
TAB = lambda top_z: [('top', box((.6, .4, .03), top_z))] + [(f'leg{i}', box((.04, .04, .4), 0, (x, y)))
                     for i, (x, y) in enumerate([(.25, .15), (-.25, .15), (.25, -.15), (-.25, -.15)])]
CASES = [
    ('table, top resting on legs', TAB(.4), 'glb', ['--up', 'z'], set()),
    ('table, top sunk 10 mm into legs', TAB(.39), 'glb', ['--up', 'z'], {'INTERSECT'}),
    ('table, top floating 5 mm', TAB(.405), 'glb', ['--up', 'z'], {'FLOATING', 'GAP'}),
    ('table, top floating 0.5 mm (under tol)', TAB(.4005), 'glb', ['--up', 'z'], set()),
    ('cup floating 40 mm (beyond near-miss)', [('saucer', box((.15, .15, .01), 0)), ('cup', box((.08, .08, .09), .05))], 'glb', ['--up', 'z', '--near', '20'], {'FLOATING'}),
    ('one STL, two pieces, one sunk in', [('m', trimesh.util.concatenate([box((.2, .2, .2), 0), box((.1, .1, .1), .15)]))], 'stl', [], {'INTERSECT'}),
]

def tags(out): return {t for t in ('INTERSECT', 'FLOATING', 'GAP') if f'[{t}]' in out}

if __name__ == '__main__':
    tmp = tempfile.mkdtemp(); ok_n = 0; rows = []
    for i, (name, ms, ext, args, want) in enumerate(CASES):
        p = os.path.join(tmp, f'c{i}.{ext}')
        if ext == 'stl': ms[0][1].export(p)
        else: scene(p, ms)
        rows.append((name, p, args, want))
    cf = os.path.join(HERE, '..', '..', 'examples', 'common-failures')
    rows += [('stool before (examples/common-failures)', os.path.join(cf, 'stool-before.glb'), [], {'INTERSECT', 'GAP'}),
             ('stool after (examples/common-failures)', os.path.join(cf, 'stool-after.glb'), [], set())]
    for name, p, args, want in rows:
        out = subprocess.run([sys.executable, TOOL, p] + args, capture_output=True, text=True).stdout
        got = tags(out); ok = got == want; ok_n += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name:42s} want {sorted(want)} got {sorted(got)}")
        if not ok: print(out)
    print(f'\n{ok_n}/{len(rows)} passed'); sys.exit(0 if ok_n == len(rows) else 1)
