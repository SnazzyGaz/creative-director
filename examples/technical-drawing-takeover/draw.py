"""draw.py: makes the two test drawings for this example with known geometry.
round-01 has planted errors; round-02 is constructed. Writes segments-rNN.csv
(true edge endpoints from the drawing code) for tools/vp.py fit."""
import math, numpy as np
from PIL import Image, ImageDraw
W,H=1200,800
def inter(p1,p2,p3,p4):
    (x1,y1),(x2,y2),(x3,y3),(x4,y4)=p1,p2,p3,p4
    d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    a=x1*y2-y1*x2; b=x3*y4-y3*x4
    return ((a*(x3-x4)-(x1-x2)*b)/d,(a*(y3-y4)-(y1-y2)*b)/d)
def along(p,vp,x):  # point on line p->vp at given x
    t=(x-p[0])/(vp[0]-p[0]); return (x,p[1]+t*(vp[1]-p[1]))
def ell(cx,cy,a,b,rot=0,lemon=False,n=200):
    pts=[]
    for i in range(n):
        t=2*math.pi*i/n; x=a*math.cos(t)
        y=b*math.sin(t)*(abs(math.sin(t))**0 if not lemon else 1)
        if lemon: y=b*math.copysign(1-(math.cos(t))**2,math.sin(t))
        r=math.radians(rot); pts.append((cx+x*math.cos(r)-y*math.sin(r),cy+x*math.sin(r)+y*math.cos(r)))
    return pts
def box(vpl,vpr,fb,ft,xl,xr,lean_l=0,lean_r=0):
    lb=along(fb,vpl,xl); lt=along(ft,vpl,xl+lean_l)
    rb=along(fb,vpr,xr); rt=along(ft,vpr,xr+lean_r)
    bt=inter(lt,vpr,rt,vpl)
    return dict(fb=fb,ft=ft,lb=lb,lt=lt,rb=rb,rt=rt,bt=bt)
def render(name,B,mug,horizon_y=None):
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); k=(20,20,20)
    E=[('L',B['fb'],B['lb']),('L',B['ft'],B['lt']),('L',B['rt'],B['bt']),
       ('R',B['fb'],B['rb']),('R',B['ft'],B['rt']),('R',B['lt'],B['bt']),
       ('v',B['fb'],B['ft']),('v',B['lb'],B['lt']),('v',B['rb'],B['rt'])]
    for g,p,q in E: d.line([p,q],fill=k,width=4)
    top,base,axis_pts=mug
    li=min(range(len(top)),key=lambda i:top[i][0]); ri=max(range(len(top)),key=lambda i:top[i][0])
    bl=min(range(len(base)),key=lambda i:base[i][0]); br=max(range(len(base)),key=lambda i:base[i][0])
    d.polygon(top+base,fill='white'); d.polygon([top[li],top[ri],base[br],base[bl]],fill='white')
    d.polygon(base,fill='white')
    d.line(top+[top[0]],fill=k,width=4)
    # visible front half of base + sides
    d.line(base[:len(base)//2+1],fill=k,width=4)
    li=min(range(len(top)),key=lambda i:top[i][0]); ri=max(range(len(top)),key=lambda i:top[i][0])
    bl=min(range(len(base)),key=lambda i:base[i][0]); br=max(range(len(base)),key=lambda i:base[i][0])
    d.line([top[li],base[bl]],fill=k,width=4); d.line([top[ri],base[br]],fill=k,width=4)
    im.save(name+'.png')
    with open('segments-r'+name.split('-')[1]+'.csv','w') as f:
        for g,p,q in E: f.write(f"{g},{p[0]:.1f},{p[1]:.1f},{q[0]:.1f},{q[1]:.1f}\n")
def topc(B): return inter(B['ft'],B['bt'],B['lt'],B['rt'])  # diagonals cross at the lid's centre
# round 01: planted errors
B1=box((-350,60),(1500,260),(560,700),(575,470),260,860,lean_l=20,lean_r=-6)
cx,cy=topc(B1); top1=ell(cx,cy-150,95,34,rot=12,lemon=True); base1=ell(cx+8,cy-10,95,22,rot=12)
render('round-01',B1,(top1,base1,None))
# round 02: constructed, horizon y=150, verticals vertical, ellipses true, base fuller than top
B2=box((-350,150),(1500,150),(560,700),(560,470),260,860)
cx,cy=topc(B2); top2=ell(cx,cy-140,95,30); base2=ell(cx,cy,95,38)
render('round-02',B2,(top2,base2,None))
