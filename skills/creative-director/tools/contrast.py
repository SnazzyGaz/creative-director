"""WCAG 2.x contrast ratio for colour pairs (alpha composited over a given ground)."""
import sys
def hex2rgb(h): h=h.lstrip('#'); return [int(h[i:i+2],16)/255 for i in (0,2,4)]
def lin(c): return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def L(rgb): r,g,b=map(lin,rgb); return 0.2126*r+0.7152*g+0.0722*b
def over(fg,a,bg): return [f*a+b*(1-a) for f,b in zip(fg,bg)]
def ratio(a,b): la,lb=sorted([L(a),L(b)],reverse=True); return (la+0.05)/(lb+0.05)
if __name__=='__main__':
    for line in sys.stdin:
        if not line.strip() or line.startswith('#'): continue
        name,fg,bg,need=line.split('|')
        def parse(s):
            s=s.strip()
            if '@' in s:  # colour@alpha@ground
                c,a,g=s.split('@'); return over(hex2rgb(c),float(a),parse(g))
            return hex2rgb(s)
        r=ratio(parse(fg),parse(bg)); need=float(need)
        print(f'{name.strip():40s} {r:5.2f}:1  need {need}:1  {"PASS" if r>=need else "FAIL"}')
