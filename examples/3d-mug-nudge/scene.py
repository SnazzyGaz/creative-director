"""scene.py: builds and renders the mug for one round.
blender -b -P scene.py -- ROUND   (1-4). Each round adds only that round's fixes."""
import bpy, bmesh, sys, math
R=int(sys.argv[sys.argv.index('--')+1])
bpy.ops.wm.read_factory_settings(use_empty=True)
S=bpy.context.scene
def srgb2lin(c): c/=255; return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def mat(name,rgb,metal,rough):
    m=bpy.data.materials.new(name); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value=(*rgb,1); b.inputs['Metallic'].default_value=metal; b.inputs['Roughness'].default_value=rough; return m
# --- model (fix 3D-4 in round 2+: segments, smooth, bevel)
seg=8 if R==1 else 48
bpy.ops.mesh.primitive_cylinder_add(vertices=seg,radius=0.04,depth=0.095,location=(0,0,0.0475))
body=bpy.context.object; body.name='mug_body'
bm=bmesh.new(); bm.from_mesh(body.data); top=max(bm.faces,key=lambda f:f.calc_center_median().z)
bmesh.ops.delete(bm,geom=[top],context='FACES'); bm.to_mesh(body.data); bm.free()
so=body.modifiers.new('wall','SOLIDIFY'); so.thickness=0.004
bpy.ops.mesh.primitive_torus_add(major_radius=0.024,minor_radius=0.0055,major_segments=(8 if R==1 else 48),minor_segments=(4 if R==1 else 16),location=(0.047,0,0.05),rotation=(math.radians(90),0,0))
handle=bpy.context.object; handle.name='mug_handle'
if R>=2:
    bv=body.modifiers.new('bevel','BEVEL'); bv.width=0.0015; bv.segments=3; bv.limit_method='ANGLE'
    for o in (body,handle):
        bpy.context.view_layer.objects.active=o; o.select_set(True); bpy.ops.object.shade_smooth(); o.select_set(False)
bpy.ops.mesh.primitive_plane_add(size=2,location=(0,0,0)); table=bpy.context.object; table.name='table'
# --- materials (fix 3D-6 in round 2+)
if R==1: mm=mat('ceramic',(1,1,1),0.5,0.15); tm=mat('table',(0,0,0),0.0,0.5)
else:    mm=mat('ceramic',tuple(srgb2lin(c) for c in (226,222,214)),0.0,0.3); tm=mat('table',tuple(srgb2lin(c) for c in (92,70,54)),0.0,0.6)
for o in (body,handle): o.data.materials.append(mm)
table.data.materials.append(tm)
# --- world / backdrop (fix 3D-5 in round 3)
w=bpy.data.worlds.new('w'); S.world=w; w.use_nodes=True
bg=w.node_tree.nodes['Background']; bg.inputs['Color'].default_value=(0.6,0.6,0.6,1) if R<3 else (0.012,0.014,0.018,1); bg.inputs['Strength'].default_value=1.0 if R<3 else 0.3
# --- camera (round 3: raised, deliberate height)
if R<3: cam_loc=(0,-0.42,0.05); look=(0,0,0.05)
else:   cam_loc=(-0.20,-0.36,0.17); look=(0.008,0,0.042)
bpy.ops.object.camera_add(location=cam_loc); cam=bpy.context.object; S.camera=cam
import mathutils
d=mathutils.Vector(look)-mathutils.Vector(cam_loc); cam.rotation_euler=d.to_track_quat('-Z','Y').to_euler(); cam.data.lens=60
# --- lights (round 1-2: one frontal light at the camera; round 3: key, fill, rim)
def area(name,loc,energy,size,aim=(0,0,0.05)):
    bpy.ops.object.light_add(type='AREA',location=loc); L=bpy.context.object; L.data.energy=energy; L.data.size=size
    dd=mathutils.Vector(aim)-mathutils.Vector(loc); L.rotation_euler=dd.to_track_quat('-Z','Y').to_euler(); return L
if R<3: area('front',(0,-0.45,0.08),60,0.3)
else:
    k=1.0 if R==3 else 0.2                       # round 4: re-balance exposure (3D-7)
    area('key',(-0.35,-0.25,0.35),40*k,0.35)    # key, upper left
    area('fill',(0.35,-0.35,0.12),10*k,0.5)     # fill, ~4:1
    area('rim',(0.15,0.35,0.25),35*k,0.2)       # rim, behind right
# --- colour management (fix 3D-7 in round 2+)
S.view_settings.view_transform='Standard' if R==1 else 'AgX'
S.view_settings.exposure=0.0
S.render.engine='CYCLES'; S.cycles.samples=48; S.cycles.use_denoising=True; S.cycles.device='CPU'
S.render.resolution_x=960; S.render.resolution_y=720
S.render.filepath=f'//round-0{R}.png'
bpy.ops.wm.save_as_mainfile(filepath=f'mug-r0{R}.blend')
bpy.ops.render.render(write_still=True)
