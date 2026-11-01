from PIL import Image, ImageDraw, ImageFont
import glob,json,shutil,os
F='/tmp/cdpush/docs/assets/src/fonts/'
def f(p,s): return ImageFont.truetype(sorted(glob.glob(F+p))[0],s)
R='/tmp/cdpush/examples/aesthetic-benchmark/reference-set/'; I=R+'images/'
A='/cursor/stores/store-ee607ef9-d24d-41fa-87cd-a3863e159c9c/grok-bot/agents/0fd271df-1064-4953-8f7a-e8ce44787f01/assets/'
key=json.load(open(R+'key.json'))['pairs']
P=[('01','moth-night-poster','Calm poster: Moth Night'),('02','static-choir-poster','Loud poster: Static Choir'),('03','last-keeper-illustration','Ink illustration: The Last Keeper'),('04','bramble-mascot','Character: Bramble the badger'),('05','crumb-co-landing','Web page: Crumb & Co bakery'),('06','tally-app','App screen: Tally habit tracker'),('07','tern-social-card','Social card: Tern 2.0'),('08','ridge-dripper-render','3D render: Ridge dripper'),('09','bracket-drawing','Technical drawing: shelf bracket'),('10','fernhill-logo','Logo lockup: Fernhill Coffee'),('11','night-shift-spread','Editorial spread: The Night Shift'),('12','observatory-concept','Game concept: snowed-in observatory')]
NS={'02':'1e16f06600084352b0c4d93ade2822634ae7f7adee013fb5d6d8d747b86edba3','05':'a9c5df04350c1c9968dace62d351dd4cbbd2cd1b2794e57556d6e171da4bd19d','08':'1286b780a216417f910c8d15c1734f01c3674ed4556ed4eba0a1aa67313e3c81','11':'7df7a42defbc69d6fda29bd34d13f8f30e605112f6da8411bdf625daad7105a0'}
os.makedirs(R+'pieces',exist_ok=True)
for n,s,name in P:
    k=key[n]; m={k['A']:'A',k['B']:'B'}; cols=[]
    if n in NS:
        dst=I+f'{n}-{s}-no-skill.jpg'; Image.open(A+NS[n]+'.jpg').convert('RGB').save(dst,quality=90); cols.append(('No skill',dst,'#A9ADBA'))
    for c,lab,col in [('rules','Creative Director rules','#F2EEE6'),('rules+aes','Rules + aesthetic layer','#E8A048')]:
        dst=I+f'{n}-{s}-{"rules" if c=="rules" else "rules-aes"}.jpg'
        src=I+f'pair-{n}-{m[c]}.jpg'
        if os.path.exists(src): os.system(f'cd {R} && git mv {src} {dst}')
        cols.append((lab,dst,col))
    W=2400 if len(cols)==3 else 1800; M,G=70,40; cw=(W-2*M-G*(len(cols)-1))//len(cols)
    ims=[Image.open(p).convert('RGB') for _,p,_ in cols]
    bh=max(int(cw*i.height/i.width) for i in ims)
    im=Image.new('RGB',(W,210+bh+70),'#14161E'); d=ImageDraw.Draw(im)
    d.text((M,50),f'{n}  {name}',font=f('Fraunces*',56),fill='#F2EEE6')
    for i,((lab,p,col),src) in enumerate(zip(cols,ims)):
        x=M+i*(cw+G); d.text((x,150),lab,font=f('InstrumentSans*',34),fill=col)
        h=int(cw*src.height/src.width); im.paste(src.resize((cw,h),Image.LANCZOS),(x,210+(bh-h)//2))
    im.save(R+f'pieces/{n}-{s}.jpg',quality=86)
shutil.copy('/workspace/transformation-sheet.png',R+'transformation-sheet.png')
