"""intersect.py: parts that cut into each other, and parts that float (3D-1, 3D-2 build checks).

python3 tools/intersect.py MODEL.(glb|gltf|obj|stl|ply) [--up y|z] [--unit m|cm|mm] [--tol MM] [--near MM]

Parts = the file's separate objects (GLB/OBJ nodes); a single-object file is split
into connected pieces. Reports, in mm:
  INTERSECT  two parts share volume (watertight parts: exact boolean volume via
             manifold3d; otherwise the depth of A's vertices inside B). Says when a
             part passes right through the other.
  FLOATING   a part with no contact (gap <= --tol, or an intersection, which is
             already reported) to the ground or to a part that is itself supported.
  GAP        two parts closer than --near but not touching: a near-miss that usually
             means they were meant to meet.
Ground = the lowest point of the model along --up (default: y for glTF, z otherwise).
Exit code 1 if anything is found. Needs: pip install trimesh rtree manifold3d
"""
import sys, argparse, itertools
import numpy as np, trimesh

def parts(path):
    sc = trimesh.load(path, force='scene')
    out = []
    for node in sc.graph.nodes_geometry:
        T, g = sc.graph[node]
        m = sc.geometry[g].copy(); m.apply_transform(T)
        m.merge_vertices(merge_tex=True, merge_norm=True)   # split normals/UVs break watertightness
        out.append((node, m))
    if len(out) == 1:
        pieces = out[0][1].split(only_watertight=False)
        if len(pieces) > 1: out = [(f'piece{i}', p) for i, p in enumerate(pieces)]
    return out

def overlap(a, b, tol):
    """Shared volume and depth (model units) of a inside b, or None."""
    lo = np.maximum(a.bounds[0], b.bounds[0]); hi = np.minimum(a.bounds[1], b.bounds[1])
    if (hi - lo).min() <= tol: return None              # boxes don't overlap by more than tol
    if a.is_watertight and b.is_watertight:
        try:
            i = trimesh.boolean.intersection([a, b], engine='manifold')
            if i.is_empty or i.volume <= 0: return None
            ext = i.extents
            if ext.min() <= tol: return None              # touching faces, not a cut
            return dict(volume=float(i.volume), depth=float(ext.min()), box=ext)
        except Exception: pass
    d = trimesh.proximity.signed_distance(b, a.vertices)  # > 0 inside b
    if d.max() <= tol: return None
    return dict(volume=None, depth=float(d.max()), box=None)

def gap(a, b, n=3000):
    pts = np.vstack([a.vertices, a.sample(n)])
    _, d, _ = trimesh.proximity.closest_point(b, pts)
    pts2 = np.vstack([b.vertices, b.sample(n)])
    _, d2, _ = trimesh.proximity.closest_point(a, pts2)
    return float(min(d.min(), d2.min()))

def passes_through(a, b, ax):
    return a.bounds[0][ax] < b.bounds[0][ax] and a.bounds[1][ax] > b.bounds[1][ax]

def main():
    p = argparse.ArgumentParser(); p.add_argument('model'); p.add_argument('--up')
    p.add_argument('--unit', default='m'); p.add_argument('--tol', type=float, default=1.0)
    p.add_argument('--near', type=float, help='near-miss distance, mm (default 5%% of model size)')
    a = p.parse_args()
    up = {'x': 0, 'y': 1, 'z': 2}[a.up or ('y' if a.model.lower().endswith(('.glb', '.gltf')) else 'z')]
    k = {'m': 1000, 'cm': 10, 'mm': 1}[a.unit]           # model units -> mm
    P = parts(a.model); tol = a.tol / k
    allv = np.vstack([m.vertices for _, m in P]); size = float(np.ptp(allv, 0).max())
    near = (a.near / k) if a.near else 0.05 * size
    ground = float(allv[:, up].min())
    print(f'{a.model}: {len(P)} parts, size {size*k:.0f} mm, up axis {"xyz"[up]}, tol {a.tol} mm, near-miss < {near*k:.1f} mm')
    found = 0; touch = {i: set() for i in range(len(P))}; cut = {i: set() for i in range(len(P))}; gaps = {}
    for (i, (na, A)), (j, (nb, B)) in itertools.combinations(enumerate(P), 2):
        o = overlap(A, B, tol) or overlap(B, A, tol)
        if o:
            cut[i].add(j); cut[j].add(i); found += 1
            thr = [f'{x} passes right through {y} (sticks out {(X.bounds[1][up] - Y.bounds[1][up])*k:.1f} mm above it)'
                   for x, X, y, Y in ((na, A, nb, B), (nb, B, na, A)) if passes_through(X, Y, up)]
            vol = f'{o["volume"]*k**3/1000:.1f} cm3 shared, ' if o['volume'] is not None else ''
            print(f'[INTERSECT] {na} x {nb}: {vol}{o["depth"]*k:.1f} mm deep' + ('; ' + '; '.join(thr) if thr else ''))
            continue
        g = gap(A, B); gaps[(i, j)] = g
        if g <= tol: touch[i].add(j); touch[j].add(i)
    for i in cut: touch[i] |= cut[i]
    grounded = {i for i, (_, m) in enumerate(P) if m.vertices[:, up].min() - ground <= tol}
    sup, todo = set(grounded), list(grounded)
    while todo:
        for j in touch[todo.pop()]:
            if j not in sup: sup.add(j); todo.append(j)
    for i, (n, m) in enumerate(P):
        if i in sup: continue
        found += 1
        cand = [(g, j) for (x, y), g in gaps.items() for j in ((y,) if x == i else (x,) if y == i else ()) if j in sup]
        why = f'nearest supported part {P[min(cand)[1]][0]} is {min(cand)[0]*k:.1f} mm away' if cand else 'no supported part nearby'
        print(f'[FLOATING] {n}: {(m.vertices[:, up].min() - ground)*k:.1f} mm above the ground, {why}')
    for (i, j), g in sorted(gaps.items()):
        if tol < g < near:
            found += 1; print(f'[GAP] {P[i][0]} - {P[j][0]}: {g*k:.1f} mm apart (near-miss: meant to touch?)')
    print('OK: no intersections, nothing floating, no near-miss gaps' if not found else f'{found} finding(s)')
    sys.exit(1 if found else 0)

if __name__ == '__main__':
    main()
