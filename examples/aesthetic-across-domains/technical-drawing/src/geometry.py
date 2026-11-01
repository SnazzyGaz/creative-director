"""Nest box parts as convex polyhedra (mm). Shared by the before and after drawings."""
import numpy as np
T = 15  # board thickness

def box(x0, x1, y0, y1, z0, z1):
    v = np.array([[x0,y0,z0],[x1,y0,z0],[x1,y1,z0],[x0,y1,z0],[x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1]], float)
    return v

def ztop(y):  # sloped top of the sides: 200 at the front face (y=T) to 250 at the back (y=150-T)
    return 200 + (y - T) * 50 / (150 - 2 * T)

def side(x0, x1):
    y0, y1 = T, 150 - T
    return np.array([[x0,y0,T],[x1,y0,T],[x1,y1,T],[x0,y1,T],[x0,y0,ztop(y0)],[x1,y0,ztop(y0)],[x1,y1,ztop(y1)],[x0,y1,ztop(y1)]], float)

def roof():
    x0, x1, y0, y1 = -12, 162, -35, 165
    zb = lambda y: ztop(y) if True else 0
    return np.array([[x0,y0,zb(y0)],[x1,y0,zb(y0)],[x1,y1,zb(y1)],[x0,y1,zb(y1)],
                     [x0,y0,zb(y0)+T],[x1,y0,zb(y0)+T],[x1,y1,zb(y1)+T],[x0,y1,zb(y1)+T]], float)

FACES = [(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]  # outward with z-up right-handed

# name, vertices, explode direction (unit), explode distance, part number, description, qty, size
PARTS = [
    ("base",  box(0,150,0,150,0,T),            (0,0,-1), 150, 1, "Base", 1, "150 x 150"),
    ("front", box(0,150,0,T,T,200),            (0,-1,0), 110, 2, "Front, 32 mm hole", 1, "150 x 185"),
    ("back",  box(0,150,150-T,150,T,250),      (0,1,0), 90, 3, "Back", 1, "150 x 235"),
    ("left",  side(0,T),                       (-1,0,0), 110, 4, "Side, left", 1, "120 x 185-235"),
    ("right", side(150-T,150),                 (1,0,0), 90, 5, "Side, right", 1, "120 x 185-235"),
    ("roof",  roof(),                          (0,0,1), 110, 6, "Roof", 1, "174 x 200"),
]
HOLE = dict(centre=(75, 0, 150), r=16)   # on the front face (y=0)
SCREWS = 8  # 4 x 30 mm through the front and back into the sides, 4 through the base; drawn on the front and base explode lines
