#!/usr/bin/env python3
"""Blind the 12 pairs. Usage: blind.py OUTDIR KEYFILE. Seed comes from the private key file (created on first run)."""
import json, random, secrets, hashlib, sys, pathlib, datetime
from PIL import Image, ImageDraw, ImageFont
W=pathlib.Path(__file__).resolve().parent; OUT=pathlib.Path(sys.argv[1]); KEY=pathlib.Path(sys.argv[2])
BRIEF={1:"Poster, calm: 'Moth Night' after-dark moth walk at a botanic garden",
2:"Poster, loud: gig poster for noise-rock band Static Choir, type-led",
3:"Illustration: ink drawing opening the short story 'The Last Keeper' (a keeper's final night before automation)",
4:"Character: Bramble the badger, mascot for a children's library reading challenge (ages 5-10)",
5:"Web page: landing hero for Crumb & Co, a small-batch sourdough bakery in Leeds",
6:"App screen: 'Today' screen for Tally, a habit tracker",
7:"Social card: announcing Tern 2.0, an open-source static site generator",
8:"3D render: shop listing hero for the 'Ridge' matte charcoal ceramic pour-over dripper",
9:"Technical drawing: two-view dimensioned L shelf bracket for a DIY instruction sheet",
10:"Logo lockup: Fernhill Coffee Roasters, an independent roaster in a hill town",
11:"Editorial spread: magazine feature 'The Night Shift: how foxes learned the city'",
12:"Game concept art: abandoned mountain observatory under snow, end of chapter 2, cozy exploration game"}
if KEY.exists(): key=json.loads(KEY.read_text())
else:
    seed=secrets.randbits(64); rng=random.Random(seed)
    key={"note":"PRIVATE answer key for examples/aesthetic-benchmark/blind-ab-01. Do not open before judging is finished.",
         "salt":secrets.token_hex(32),"seed":seed,"created":datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
         "conditions":{"rules":"core + domain modules (v0.3.1 rule set, no AES)","rules+aes":"rules + modules/aesthetic-critique (AES-0..10)"},"pairs":{}}
    for i in range(1,13):
        a=rng.choice(["rules","rules+aes"]); key["pairs"][f"{i:02d}"]={"A":a,"B":"rules+aes" if a=="rules" else "rules"}
font=lambda s,b=False: ImageFont.truetype(f"/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf",s)
def sheet(i,left,right,ll,rl,dest):
    M=760; s=min(M/left.width,M/left.height); w,h=int(left.width*s),int(left.height*s)
    g=36; top=86; bot=64; C=Image.new('RGB',(2*w+3*g,top+h+bot),'#E9E7E2'); d=ImageDraw.Draw(C)
    f=font(22); f.set_variation_by_axes([14,600]) if hasattr(f,'set_variation_by_axes') else None
    d.text((g,28),f"Pair {i:02d}   Brief: {BRIEF[i]}",fill='#1A1A1A',font=f)
    C.paste(left.resize((w,h),Image.LANCZOS),(g,top)); C.paste(right.resize((w,h),Image.LANCZOS),(2*g+w,top))
    F=font(30)
    d.text((g+w//2,top+h+16),ll,fill='#1A1A1A',font=F,anchor='ma'); d.text((2*g+w+w//2,top+h+16),rl,fill='#1A1A1A',font=F,anchor='ma')
    C.save(dest,quality=88)
M={"rules":"rules","rules+aes":"aes"}
(OUT/'images').mkdir(parents=True,exist_ok=True); (OUT/'pairs').mkdir(exist_ok=True); (OUT/'pairs-swapped').mkdir(exist_ok=True)
for i in range(1,13):
    p=key["pairs"][f"{i:02d}"]; im={}
    for side in "AB":
        src=Image.open(W/'out'/f"p{i:02d}-{M[p[side]]}.png").convert('RGB')
        dest=OUT/'images'/f"pair-{i:02d}-{side}.jpg"; src.save(dest,quality=90)   # no metadata
        p[f"{side}_sha256"]=hashlib.sha256(dest.read_bytes()).hexdigest(); im[side]=src
    sheet(i,im['A'],im['B'],'A','B',OUT/'pairs'/f"pair-{i:02d}.jpg")
    sheet(i,im['B'],im['A'],'B','A',OUT/'pairs-swapped'/f"pair-{i:02d}.jpg")
KEY.write_text(json.dumps(key,indent=1)+"\n")
h=hashlib.sha256(KEY.read_bytes()).hexdigest(); print("key sha256",h)
