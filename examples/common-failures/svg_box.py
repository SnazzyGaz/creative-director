"""svg_box.py: an SVG icon-style box in two-point perspective. Before: the two VPs sit at
different heights (planted). After: both on one horizon. Writes svg + segments csv for tools/vp.py."""
def inter(p1,p2,p3,p4):
    (x1,y1),(x2,y2),(x3,y3),(x4,y4)=p1,p2,p3,p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    a=x1*y2-y1*x2; b=x3*y4-y3*x4; return ((a*(x3-x4)-(x1-x2)*b)/d,(a*(y3-y4)-(y1-y2)*b)/d)
def along(p,vp,x): t=(x-p[0])/(vp[0]-p[0]); return (x,p[1]+t*(vp[1]-p[1]))
for tag,vpl,vpr in (("before",(-300,40),(940,220)),("after",(-300,110),(940,110))):
    fb,ft=(320,330),(320,200); lb=along(fb,vpl,150); lt=along(ft,vpl,150); rb=along(fb,vpr,500); rt=along(ft,vpr,500)
    bt=inter(lt,vpr,rt,vpl)
    E=[('L',fb,lb),('L',ft,lt),('L',rt,bt),('R',fb,rb),('R',ft,rt),('R',lt,bt),('v',fb,ft),('v',lb,lt),('v',rb,rt)]
    P=lambda p:f"{p[0]:.1f},{p[1]:.1f}"
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="400" viewBox="0 0 640 400"><rect width="640" height="400" fill="#fff"/>'
    svg+=f'<polygon points="{P(ft)} {P(lt)} {P(bt)} {P(rt)}" fill="#f3d9b1"/><polygon points="{P(fb)} {P(ft)} {P(lt)} {P(lb)}" fill="#d9a066"/><polygon points="{P(fb)} {P(ft)} {P(rt)} {P(rb)}" fill="#b97a3d"/>'
    svg+="".join(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>' for g,p,q in E)+'</svg>'
    open(f"svg-box-{tag}.svg","w").write(svg)
    open(f"svg-box-{tag}.csv","w").write("".join(f"{g},{p[0]:.1f},{p[1]:.1f},{q[0]:.1f},{q[1]:.1f}\n" for g,p,q in E))
