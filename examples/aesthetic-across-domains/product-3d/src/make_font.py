"""Static Josefin Sans 500 with overlaps removed: Blender's text fill breaks on a variable font's overlapping contours."""
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
import os
os.makedirs("/tmp/aad-static-fonts", exist_ok=True)
f = TTFont("../../../../fonts/art-deco-display/josefinsans/JosefinSans[wght].ttf")
instancer.instantiateVariableFont(f, {"wght": 500}, overlap=instancer.OverlapMode.REMOVE).save("/tmp/aad-static-fonts/JosefinSans-500-flat.ttf")
