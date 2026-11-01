"""measure.py IMG...: share of clipped pixels (any channel >= 250) and near-white flat area, plus L* stats.
Backs the 3D-7 'count clipped pixels' check."""
import sys, numpy as np
from PIL import Image
for p in sys.argv[1:]:
    a=np.asarray(Image.open(p).convert('RGB')).astype(float)
    clip=(a.max(axis=2)>=250).mean()*100
    c=a/255; lin=np.where(c<=0.04045,c/12.92,((c+0.055)/1.055)**2.4)
    Y=(lin*[0.2126,0.7152,0.0722]).sum(axis=2); L=np.where(Y>0.008856,116*np.cbrt(Y)-16,903.3*Y)
    print(f"{p}: clipped {clip:.1f}%  L* p5 {np.percentile(L,5):.0f} p50 {np.percentile(L,50):.0f} p95 {np.percentile(L,95):.0f}")
