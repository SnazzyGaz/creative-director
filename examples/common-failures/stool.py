"""stool.py: blender -b -P stool.py -- before|after [--export]. --export writes stool-TAG.glb (no floor) for tools/intersect.py and skips the render. A stool: seat on four legs.
Before (planted): seat floats 12 mm above the legs, and one leg is 60 mm too long so it pokes through the seat."""
import bpy, sys, math
tag=sys.argv[sys.argv.index('--')+1]; B=tag=='before'
bpy.ops.wm.read_factory_settings(use_empty=True); S=bpy.context.scene
legh=0.43
for i,(x,y) in enumerate([(.13,.13),(-.13,.13),(.13,-.13),(-.13,-.13)]):
    h=legh+(0.06 if (B and i==0) else 0)
    bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=0.015,depth=h,location=(x,y,h/2)); bpy.context.object.name=f'leg{i}'
gap=0.012 if B else 0
bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=0.19,depth=0.03,location=(0,0,legh+gap+0.015)); bpy.context.object.name='seat'
for o in bpy.data.objects: o.select_set(True); bpy.context.view_layer.objects.active=o; bpy.ops.object.shade_smooth(); o.select_set(False)
m=bpy.data.materials.new('wood'); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value=(0.35,0.2,0.1,1); b.inputs['Roughness'].default_value=0.5
for o in list(bpy.data.objects): o.data.materials.append(m)
bpy.ops.mesh.primitive_plane_add(size=4); fl=bpy.context.object; fl.name='floor'
fm=bpy.data.materials.new('floor'); fm.use_nodes=True; fm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.5,0.5,0.52,1); fl.data.materials.append(fm)
import mathutils
bpy.ops.object.camera_add(location=(0.9,-1.2,0.75)); c=bpy.context.object; S.camera=c
c.rotation_euler=(mathutils.Vector((0,0,0.32))-c.location).to_track_quat('-Z','Y').to_euler(); c.data.lens=50
bpy.ops.object.light_add(type='AREA',location=(-1,-1,1.6)); L=bpy.context.object; L.data.energy=250; L.data.size=1
L.rotation_euler=(mathutils.Vector((0,0,0.3))-L.location).to_track_quat('-Z','Y').to_euler()
w=bpy.data.worlds.new('w'); S.world=w; w.use_nodes=True; w.node_tree.nodes['Background'].inputs['Color'].default_value=(0.05,0.05,0.06,1)
S.view_settings.view_transform='AgX'; S.render.engine='CYCLES'; S.cycles.samples=32; S.cycles.use_denoising=True
S.render.resolution_x=640; S.render.resolution_y=480; S.render.filepath=f'//stool-{tag}.png'
bpy.data.objects.remove(fl)  # check the model without the floor, then add it back for the render
if '--export' in sys.argv:
    bpy.ops.export_scene.gltf(filepath=f'stool-{tag}.glb', export_format='GLB'); sys.exit(0)
bpy.ops.wm.save_as_mainfile(filepath=f'stool-{tag}.blend')
bpy.ops.mesh.primitive_plane_add(size=4); fl=bpy.context.object; fl.data.materials.append(fm)
bpy.ops.render.render(write_still=True)
