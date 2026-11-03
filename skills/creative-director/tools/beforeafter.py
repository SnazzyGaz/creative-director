"""beforeafter.py BEFORE AFTER OUT.png [label_before] [label_after] [crop_h]"""
import sys
from PIL import Image, ImageDraw, ImageFont
b,a,out=sys.argv[1:4]; lb=sys.argv[4] if len(sys.argv)>4 else 'Before'; la=sys.argv[5] if len(sys.argv)>5 else 'After'
ch=int(sys.argv[6]) if len(sys.argv)>6 else None
ims=[]
for p in (b,a):
    im=Image.open(p).convert('RGB')
    if ch: im=im.crop((0,0,im.width,min(ch,im.height)))
    ims.append(im.resize((800,round(im.height*800/im.width))))
h=max(i.height for i in ims); pad=40
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
except Exception: f=ImageFont.load_default()
s=Image.new('RGB',(800*2+30,h+pad),'white'); d=ImageDraw.Draw(s)
for k,(im,l) in enumerate(zip(ims,(lb,la))):
    x=k*830; s.paste(im,(x,pad)); d.text((x+4,8),l,fill='black',font=f)
s.save(out)
