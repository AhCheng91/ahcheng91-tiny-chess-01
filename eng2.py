def _mk(m):
 global _s,_c,ep,_f,h,ev,eq,kw,kb
 frm=m%128
 to=m//128%128
 pr=m//16384-1
 p=b[frm]
 cap=b[to]
 s=1 if p>0 else -1
 csq=-1
 if (p==1 or p==-1) and to==ep and not cap and (to & 7)!=(frm & 7):
  csq=to-16*s
  cap=b[csq]
 u.append((cap,_c,ep,_f,h,ev,eq,csq))
 if p==1 or p==-1 or cap:
  _f=0
 else:
  _f += 1
 if csq>=0:
  b[csq]=0
 if cap:
  q=1 if cap>0 else -1
  cq=csq if csq>=0 else to
  mg,eg=pv(cap,cq)
  ev -= q*mg
  eq -= q*eg
  h ^= ZP[cap+6][cq]
 mg,eg=pv(p,frm)
 ev -= s*mg
 eq -= s*eg
 h ^= ZP[p+6][frm]
 b[frm]=0
 np=pr*s if pr else p
 b[to]=np
 mg,eg=pv(np,to)
 ev += s*mg
 eq += s*eg
 h ^= ZP[np+6][to]
 if np==6:
  kw=to
 elif np==-6:
  kb=to
 if (p==6 or p==-6) and abs(to-frm)==2:
  kd=1 if to>frm else -1
  rf=frm+(3 if kd>0 else 4)*kd
  rt=frm+kd
  rp=4*s
  b[rt]=rp
  b[rf]=0
  mg,eg=pv(rp,rt)
  ev += s*mg
  eq += s*eg
  h ^= ZP[rp+6][rt]
  mg,eg=pv(rp,rf)
  ev -= s*mg
  eq -= s*eg
  h ^= ZP[rp+6][rf]
 nc=_c & CM[frm] & CM[to]
 if nc!=_c:
  h ^= ZC[_c] ^ ZC[nc]
  _c=nc
 if ep>=0:
  h ^= ZE[ep]
 ep=-1
 if (p==1 or p==-1) and abs(to-frm)==32:
  ep=(frm+to)//2
  h ^= ZE[ep]
 _s=-_s
 h ^= ZS

def _um(m):
 global _s,_c,ep,_f,h,ev,eq,kw,kb
 frm=m%128
 to=m//128%128
 pr=m//16384-1
 cap,_c,ep,_f,h,ev,eq,csq=u.pop()
 mover=-_s
 p=mover if pr else b[to]
 b[frm]=p
 b[to]=0
 if (p==6 or p==-6) and abs(to-frm)==2:
  kd=1 if to>frm else -1
  rf=frm+(3 if kd>0 else 4)*kd
  rt=frm+kd
  b[rf]=b[rt]
  b[rt]=0
 if cap:
  b[csq if csq>=0 else to]=cap
 _s=-_s
 if p==6:
  kw=frm
 elif p==-6:
  kb=frm

def _l():
 r=[]
 for m in _g(False):
  _mk(m)
  if not _a(-_s):
   r.append(m)
  _um(m)
 return r

def _u(m):
 frm=m%128
 to=m//128%128
 pr=m//16384-1
 s="abcdefgh"[frm & 7]+str((frm >> 4)+1)+"abcdefgh"[to & 7]+str((to >> 4)+1)
 if pr:
  s += "nbrq"[pr-2]
 return s

_m=(0,100,320,330,500,900,0)
_n=(0,120,320,340,540,960,0)

P_PM=(0,0,0,0,0,0,0,0,5,10,10,-20,-20,10,10,5,5,-5,-10,0,0,-10,-5,5,0,0,0,20,20,0,0,0,5,5,10,25,25,10,5,5,10,10,20,30,30,20,10,10,50,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0)
P_PE=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,10,15,15,15,15,15,15,10,20,25,25,25,25,25,25,20,40,45,45,45,45,45,45,40,70,70,70,70,70,70,70,70,0,0,0,0,0,0,0,0)
N_PM=(-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,5,5,0,-20,-40,-30,5,10,15,15,10,5,-30,-30,0,15,20,20,15,0,-30,-30,5,15,20,20,15,5,-30,-30,0,10,15,15,10,0,-30,-40,-20,0,0,0,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50)
B_PM=(-20,-10,-10,-10,-10,-10,-10,-20,-10,5,0,0,0,0,5,-10,-10,10,10,10,10,10,10,-10,-10,0,10,10,10,10,0,-10,-10,5,5,10,10,5,5,-10,-10,0,5,10,10,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-10,-10,-10,-10,-20)
R_PM=(0,0,0,5,5,0,0,0,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,5,10,10,10,10,10,10,5,0,0,0,0,0,0,0,0)
Q_PM=(-20,-10,-10,-5,-5,-10,-10,-20,-10,0,5,0,0,0,0,-10,-10,5,5,5,5,5,0,-10,0,0,5,5,5,5,0,-5,-5,0,5,5,5,5,0,-5,-10,0,5,5,5,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20)
K_PM=(20,30,10,0,0,10,30,20,20,20,0,0,0,0,20,20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30)
K_PE=(-50,-30,-30,-30,-30,-30,-30,-50,-30,-30,0,0,0,0,-30,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-20,-10,0,0,-10,-20,-30,-50,-40,-30,-20,-20,-30,-40,-50)

PM=(None,P_PM,N_PM,B_PM,R_PM,Q_PM,K_PM)
PE=(None,P_PE,N_PM,B_PM,R_PM,Q_PM,K_PE)

_pb=(0,8,14,22,32,48,70,95)

def _e():
 pw=[0]*8
 pb=[0]*8
 fw=[99]*8
 fb=[-1]*8
 bw=bb=0
 rw=[]
 rb=[]
 ksw=ksb=None
 ph=0
 for sq in range(120):
  if sq & 0x88: continue
  p=b[sq]
  if not p: continue
  f=sq & 7
  r=sq >> 4
  a=p if p>0 else -p
  if a==5: ph += 4
  elif a==4: ph += 2
  elif a==2 or a==3: ph += 1
  if a==1:
   if p>0:
    pw[f] += 1
    if r<fw[f]: fw[f]=r
   else:
    pb[f] += 1
    if r>fb[f]: fb[f]=r
  elif a==3:
   if p>0: bw += 1
   else: bb += 1
  elif a==4:
   if p>0: rw.append((r,f))
   else: rb.append((r,f))
  elif a==6:
   if p>0: ksw=(r,f)
   else: ksb=(r,f)
 if ph>24: ph=24
 sc=(ev*ph+eq*(24-ph))//24
 if bw>=2: sc += 30
 if bb>=2: sc -= 30
 for (r,f) in rw:
  if pw[f]==0:
   sc += 18 if pb[f]==0 else 9
  elif pb[f]==0:
   sc += 4
 for (r,f) in rb:
  if pb[f]==0:
   sc -= 18 if pw[f]==0 else 9
  elif pw[f]==0:
   sc -= 4
 for f in range(8):
  if pw[f]>1: sc -= 12*(pw[f]-1)
  if pb[f]>1: sc += 12*(pb[f]-1)
  if pw[f] and not (f>0 and pw[f-1]) and not (f<7 and pw[f+1]): sc -= 14
  if pb[f] and not (f>0 and pb[f-1]) and not (f<7 and pb[f+1]): sc += 14
 for f in range(8):
  if fw[f]<99:
   r=fw[f]
   ahead=0
   for ff in (f-1,f,f+1):
    if 0<=ff<8 and fb[ff]>r: ahead=1
   if not ahead: sc += _pb[r]
  if fb[f]>=0:
   r=fb[f]
   ahead=0
   for ff in (f-1,f,f+1):
    if 0<=ff<8 and fw[ff]<r: ahead=1
   if not ahead: sc -= _pb[7-r]
 kp=0
 if ksw is not None:
  r,f=ksw
  for ff in (f-1,f,f+1):
   if 0<=ff<8:
    has=0
    for rr in (r+1,r+2):
     if rr<8 and b[rr*16+ff]==1: has=1
    if not has: kp += 14
  if pw[f]==0: kp += 20
 if ksb is not None:
  r,f=ksb
  for ff in (f-1,f,f+1):
   if 0<=ff<8:
    has=0
    for rr in (r-1,r-2):
     if rr>=0 and b[rr*16+ff]==-1: has=1
    if not has: kp -= 14
  if pb[f]==0: kp -= 20
 sc -= kp*ph//24
 sc += 10*_s
 return sc
