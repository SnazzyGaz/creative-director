"""Perfume bottle product shot. Run: blender -b -P scene.py -- before|after OUT.png|OUT-product.blend [samples] [font]
Same model both times; only light, camera, materials and world change."""
import bpy, sys, math, os
from mathutils import Vector
argv = sys.argv[sys.argv.index("--") + 1:]
MODE, OUT = argv[0], argv[1]
SAMPLES = int(argv[2]) if len(argv) > 2 else 128
FONT = argv[3] if len(argv) > 3 else "/tmp/aad-static-fonts/JosefinSans-500-flat.ttf"  # static, overlaps removed (see make_font.py)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.samples = SAMPLES; sc.cycles.use_denoising = True
sc.cycles.max_bounces = 16; sc.cycles.transmission_bounces = 16; sc.cycles.glossy_bounces = 8
sc.render.resolution_x, sc.render.resolution_y = 1080, 1350
sc.render.film_transparent = False

def mat(name, **p):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    for k, v in p.items():
        b.inputs[k].default_value = v
    return m

def obj_add(o, m):
    o.data.materials.append(m); return o

# The before keeps the round-1 model (base block through the glass floor, label and text floating
# 0.1-0.3 mm off the glass, unwelded text mesh); the after uses the fixed one (3D-1, see critique.md).
FIXED = MODE != "before"
# --- model (units: metres; bottle 60 x 32 x 85 mm body) ---
W, D, Hb = 0.060, 0.032, 0.085
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, Hb / 2))
glass = bpy.context.object; glass.scale = (W, D, Hb); bpy.ops.object.transform_apply(scale=True)
bv = glass.modifiers.new("bevel", "BEVEL"); bv.width = 0.004; bv.segments = 6
so = glass.modifiers.new("solid", "SOLIDIFY"); so.thickness = 0.004; so.offset = -1
glass.modifiers.new("sub", "SUBSURF").levels = 1
bpy.ops.object.shade_smooth()
# thick glass base block
# sits on the inside of the 4 mm glass floor (z 4-14 mm), not through it
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.004 + 0.005 if FIXED else 0.007))
base = bpy.context.object; base.scale = (W - 0.0084, D - 0.0084, 0.010) if FIXED else (W - 0.008, D - 0.008, 0.010); bpy.ops.object.transform_apply(scale=True)
base.modifiers.new("bevel", "BEVEL").width = 0.002
# liquid
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, (0.014 if FIXED else 0.012) + 0.058 / 2))
liq = bpy.context.object; liq.scale = (W - 0.0084, D - 0.0084, 0.058); bpy.ops.object.transform_apply(scale=True)
lb = liq.modifiers.new("bevel", "BEVEL"); lb.width = 0.002; lb.segments = 4
bpy.ops.object.shade_smooth()
# neck and cap
bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.008, location=(0, 0, Hb + 0.004))
neck = bpy.context.object
bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=0.0145, depth=0.030, location=(0, 0, Hb + 0.008 + 0.015))
cap = bpy.context.object
cb = cap.modifiers.new("bevel", "BEVEL"); cb.width = 0.0015; cb.segments = 4
bpy.ops.object.shade_smooth()
# label: thin plate with the name
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -D / 2 - (0.0002 if FIXED else 0.0003), 0.046))
label = bpy.context.object; label.scale = (0.036, 0.0004, 0.020); bpy.ops.object.transform_apply(scale=True)
bpy.ops.object.text_add(location=(0, -D / 2 - (0.00042 if FIXED else 0.0008), 0.0475), rotation=(math.radians(90), 0, 0))
t1 = bpy.context.object; t1.data.body = "SALTMARSH"; t1.data.align_x = "CENTER"; t1.data.size = 0.0042
t1.data.font = bpy.data.fonts.load(FONT)
t1.data.space_character = 1.25; t1.data.extrude = 0.0
bpy.ops.object.text_add(location=(0, -D / 2 - (0.00042 if FIXED else 0.0008), 0.0405), rotation=(math.radians(90), 0, 0))
t2 = bpy.context.object; t2.data.body = "No. 2"; t2.data.align_x = "CENTER"; t2.data.size = 0.0040
t2.data.font = t1.data.font; t2.data.extrude = 0.0
# text to mesh, then weld and drop loose bits so model-qa sees clean geometry
import bmesh
for i, t in enumerate((t1, t2) if FIXED else ()):
    bpy.ops.object.select_all(action="DESELECT"); t.select_set(True); bpy.context.view_layer.objects.active = t
    bpy.ops.object.convert(target="MESH")
    bm = bmesh.new(); bm.from_mesh(t.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bmesh.ops.dissolve_degenerate(bm, dist=1e-7, edges=bm.edges)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
    bm.to_mesh(t.data); bm.free()
if FIXED:
    t1, t2 = [o for o in bpy.data.objects if o.name.startswith("Text")][:2]

# backdrop sweep: floor plane + curved wall
bpy.ops.mesh.primitive_plane_add(size=1.0, location=(0, 0.1, 0))
floor0 = bpy.context.object; floor0.scale = (3, 1.6, 1); bpy.ops.object.transform_apply(scale=True)
floor = bpy.context.object
bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="DESELECT"); bpy.ops.object.mode_set(mode="OBJECT")
for v in floor.data.vertices:
    v.select = v.co.y > 0
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.8)})
bpy.ops.object.mode_set(mode="OBJECT")
fb = floor.modifiers.new("bevel", "BEVEL"); fb.width = 0.25; fb.segments = 24; fb.limit_method = "ANGLE"
bpy.ops.object.shade_smooth()

def area(name, loc, rot, size, energy, color=(1, 1, 1), shape="RECTANGLE", sy=None, spread=180):
    bpy.ops.object.light_add(type="AREA", location=loc, rotation=[math.radians(r) for r in rot])
    l = bpy.context.object; l.name = name; l.data.energy = energy; l.data.color = color
    l.data.shape = shape; l.data.size = size; l.data.size_y = sy or size; l.data.spread = math.radians(spread)
    return l

def look_at(o, target):
    d = Vector(target) - o.location
    o.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()

world = bpy.data.worlds.new("w"); sc.world = world; world.use_nodes = True
bg = world.node_tree.nodes["Background"]

if MODE == "before":
    # what a bot usually sets up: default-ish glass, grey sweep, one light from the camera side, 50 mm, eye level
    obj_add(glass, mat("glass", **{"Base Color": (1, 1, 1, 1), "Transmission Weight": 1.0, "Roughness": 0.0, "IOR": 1.45}))
    obj_add(base, glass.data.materials[0]); obj_add(neck, glass.data.materials[0])
    obj_add(liq, mat("liquid", **{"Base Color": (1.0, 0.75, 0.3, 1), "Transmission Weight": 1.0, "Roughness": 0.0, "IOR": 1.36}))
    obj_add(cap, mat("cap", **{"Base Color": (0.8, 0.65, 0.3, 1), "Metallic": 1.0, "Roughness": 0.25}))
    obj_add(label, mat("label", **{"Base Color": (0.95, 0.95, 0.95, 1), "Roughness": 0.5}))
    tm = mat("text", **{"Base Color": (0.1, 0.1, 0.1, 1)}); obj_add(t1, tm); obj_add(t2, tm)
    obj_add(floor, mat("sweep", **{"Base Color": (0.6, 0.6, 0.6, 1), "Roughness": 0.6}))
    bg.inputs[0].default_value = (0.8, 0.8, 0.8, 1); bg.inputs[1].default_value = 0.35
    l = area("key", (0.0, -0.45, 0.35), (0, 0, 0), 0.25, 9); look_at(l, (0, 0, 0.05))
    sc.view_settings.view_transform = "Standard"
    bpy.ops.object.camera_add(location=(0, -0.40, 0.07)); cam = bpy.context.object
    cam.data.lens = 50; look_at(cam, (0, 0, 0.065))
else:
    # low-key: dark sweep, two tall strip lights behind and to the sides draw the glass edges (dark-field),
    # one large soft key from upper left for the cap and liquid, faint fill; glossy dark floor for a reflection
    obj_add(glass, mat("glass", **{"Base Color": (1, 1, 1, 1), "Transmission Weight": 1.0, "Roughness": 0.02, "IOR": 1.5}))
    obj_add(base, glass.data.materials[0]); obj_add(neck, glass.data.materials[0])
    lm = mat("liquid", **{"Base Color": (0.98, 0.66, 0.30, 1), "Transmission Weight": 1.0, "Roughness": 0.0, "IOR": 1.36})
    obj_add(liq, lm)
    obj_add(cap, mat("cap", **{"Base Color": (0.05, 0.05, 0.05, 1), "Metallic": 0.0, "Roughness": 0.35, "Coat Weight": 0.6}))
    obj_add(label, mat("label", **{"Base Color": (0.88, 0.85, 0.78, 1), "Roughness": 0.7}))
    tm = mat("text", **{"Base Color": (0.06, 0.06, 0.06, 1), "Roughness": 0.6}); obj_add(t1, tm); obj_add(t2, tm)
    obj_add(floor, mat("sweep", **{"Base Color": (0.015, 0.015, 0.014, 1), "Roughness": 0.12, "Specular IOR Level": 0.5}))
    bg.inputs[0].default_value = (0, 0, 0, 1); bg.inputs[1].default_value = 0.0
    warm = (1.0, 0.9, 0.78)
    l = area("rim_left", (-0.12, 0.09, 0.075), (0, 0, 0), 0.02, 16, warm, "RECTANGLE", 0.14, 30); look_at(l, (0, 0, 0.075))
    l = area("rim_right", (0.12, 0.09, 0.075), (0, 0, 0), 0.02, 12, warm, "RECTANGLE", 0.14, 30); look_at(l, (0, 0, 0.075))
    l = area("key", (-0.22, -0.16, 0.34), (0, 0, 0), 0.16, 1.6, warm, "RECTANGLE", None, 35); look_at(l, (0, 0, 0.07))
    l = area("back_glow", (0, 0.35, 0.06), (0, 0, 0), 0.12, 9, (1.0, 0.80, 0.58), "DISK"); look_at(l, (0, 0.9, 0.14))
    l = area("fill", (0.35, -0.40, 0.12), (0, 0, 0), 0.4, 0.35); look_at(l, (0, 0, 0.06))
    # glow card behind the bottle: seen only through the glass (camera rays off), so the liquid glows
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0.16, 0.038), rotation=(math.radians(90), 0, 0))
    card = bpy.context.object; card.scale = (0.05, 0.05, 1)
    cm = bpy.data.materials.new("card"); cm.use_nodes = True; nt = cm.node_tree
    em = nt.nodes.new("ShaderNodeEmission"); em.inputs[0].default_value = (1.0, 0.86, 0.68, 1); em.inputs[1].default_value = 1.2
    tc = nt.nodes.new("ShaderNodeTexCoord"); sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    mr = nt.nodes.new("ShaderNodeMapRange"); mr.inputs[3].default_value = 1.6; mr.inputs[4].default_value = 0.35
    nt.links.new(tc.outputs["Generated"], sep.inputs[0]); nt.links.new(sep.outputs[1], mr.inputs[0])
    nt.links.new(mr.outputs[0], em.inputs[1])   # brighter at the bottom of the liquid, fading up
    nt.links.new(em.outputs[0], nt.nodes["Material Output"].inputs[0]); card.data.materials.append(cm)
    card.visible_camera = False; card.visible_glossy = False; card.visible_diffuse = False
    sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
    bpy.ops.object.camera_add(location=(0.05, -0.62, 0.040)); cam = bpy.context.object
    cam.data.lens = 85; look_at(cam, (0.0, 0, 0.075))
    cam.data.shift_y = 0.07    # bottle low in frame: room above for the name
sc.camera = cam
if OUT.endswith("-product.blend"):   # bottle only, for model-qa: drop backdrop, glow card and lights
    for o in list(bpy.data.objects):
        if o.type != "MESH" or o.name.startswith("Plane"):
            bpy.data.objects.remove(o)
if OUT.endswith(".blend"):   # save the scene for model-qa instead of rendering
    bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(OUT)); sys.exit(0)
sc.render.filepath = OUT
bpy.ops.render.render(write_still=True)
