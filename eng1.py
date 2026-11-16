import json,os,urllib.request,random

BS=160
b=[0]*BS
_s=1
_c=0
ep=-1
_f=0
h=0
ev=0
eq=0
kw=4
kb=116
u=[]

KN=(33,31,18,14,-14,-18,-31,-33)
BD=(15,17,-15,-17)
RD=(1,-1,16,-16)
KD=(1,-1,16,-16,15,17,-15,-17)

CM=[15]*128
CM[0]=13
CM[7]=14
CM[4]=12
CM[112]=7
CM[119]=11
CM[116]=3

_R=random.Random(20240601)
ZP=[[_R.getrandbits(64) for _ in range(128)] for _ in range(13)]
ZC=[_R.getrandbits(64) for _ in range(16)]
ZC[0]=0
ZE=[_R.getrandbits(64) for _ in range(128)]
ZS=_R.getrandbits(64)

def pv(p,sq):
 t=p if p>0 else -p
 i=(sq >> 4)*8+(sq & 7)
 if p<0:
  i=63-i
 return (_m[t]+PM[t][i],_n[t]+PE[t][i])

def load(f):
 global b,_s,_c,ep,_f,h,ev,eq,kw,kb,u
 b=[0]*BS
 u=[]
 rows=f.split()[0].split('/')
 mp={'p': -1,'n': -2,'b': -3,'r': -4,'q': -5,'k': -6,
  'P': 1,'N': 2,'B': 3,'R': 4,'Q': 5,'K': 6}
 for ri,row in enumerate(rows):
  fi=0
  rk=7-ri
  for ch in row:
   if ch.isdigit():
    fi += int(ch)
   else:
    b[rk*16+fi]=mp[ch]
    fi += 1
 fs=f.split()
 _s=1 if fs[1]=='w' else -1
 _c=0
 for ch in fs[2]:
  if ch=='K': _c |= 1
  elif ch=='Q': _c |= 2
  elif ch=='k': _c |= 4
  elif ch=='q': _c |= 8
 ep=-1
 if fs[3]!='-':
  ep=(ord(fs[3][0])-97)+(ord(fs[3][1])-49)*16
 _f=int(fs[4])
 h=0
 ev=0
 eq=0
 for sq in range(120):
  if sq & 0x88:
   continue
  p=b[sq]
  if not p:
   continue
  h ^= ZP[p+6][sq]
  s=1 if p>0 else -1
  mg,eg=pv(p,sq)
  ev += s*mg
  eq += s*eg
  if p==6: kw=sq
  elif p==-6: kb=sq
 h ^= ZC[_c]
 if ep>=0: h ^= ZE[ep]
 if _s<0: h ^= ZS

def _a(s):
 return att(kw if s>0 else kb,-s)

def att(sq,by):
 if by>0:
  for d in (-15,-17):
   t=sq+d
   if not t & 0x88 and b[t]==1: return True
 else:
  for d in (15,17):
   t=sq+d
   if not t & 0x88 and b[t]==-1: return True
 for d in KN:
  t=sq+d
  if not t & 0x88 and b[t]==2*by: return True
 for d in BD:
  t=sq+d
  while not t & 0x88:
   q=b[t]
   if q:
    if q==3*by or q==5*by: return True
    break
   t += d
 for d in RD:
  t=sq+d
  while not t & 0x88:
   q=b[t]
   if q:
    if q==4*by or q==5*by: return True
    break
   t += d
 for d in KD:
  t=sq+d
  if not t & 0x88 and b[t]==6*by: return True
 return False

def _g(caps=False):
 r=[]
 s=_s
 for sq in range(120):
  if sq & 0x88: continue
  p=b[sq]
  if p==0 or p*s<=0: continue
  a=p if p>0 else -p
  if a==1:
   t=sq+16*s
   if not t & 0x88 and b[t]==0:
    if (t >> 4)==(7 if s>0 else 0):
     for pr in (5,4,3,2): r.append(sq+t*128+(pr+1)*16384)
    elif not caps:
     r.append(sq+t*128+16384)
     if (sq >> 4)==(1 if s>0 else 6) and b[sq+32*s]==0:
      r.append(sq+(t+16*s)*128+16384)
   for d in (15,17):
    t=sq+d*s
    if t & 0x88: continue
    q=b[t]
    if q*s<0:
     if (t >> 4)==(7 if s>0 else 0):
      for pr in (5,4,3,2): r.append(sq+t*128+(pr+1)*16384)
     else:
      r.append(sq+t*128+16384)
    elif t==ep and q==0:
     r.append(sq+t*128+16384)
   continue
  if a==6:
   for d in KD:
    t=sq+d
    if t & 0x88: continue
    q=b[t]
    if q*s>0: continue
    if caps and q==0: continue
    r.append(sq+t*128+16384)
   if not caps:
    if s==1 and b[4]==6:
     if _c & 1 and b[5]==0 and b[6]==0 and b[7]==4 and not att(4,-1) and not att(5,-1) and not att(6,-1):
      r.append(4+6*128+16384)
     if _c & 2 and b[3]==0 and b[2]==0 and b[1]==0 and b[0]==4 and not att(4,-1) and not att(3,-1) and not att(2,-1):
      r.append(4+2*128+16384)
    elif s==-1 and b[116]==-6:
     if _c & 4 and b[117]==0 and b[118]==0 and b[119]==-4 and not att(116,1) and not att(117,1) and not att(118,1):
      r.append(116+118*128+16384)
     if _c & 8 and b[115]==0 and b[114]==0 and b[113]==0 and b[112]==-4 and not att(116,1) and not att(115,1) and not att(114,1):
      r.append(116+114*128+16384)
   continue
  if a==2:
   ds=KN
  elif a==3:
   ds=BD
  elif a==4:
   ds=RD
  else:
   ds=BD+RD
  if a in (3,4,5):
   for d in ds:
    t=sq+d
    while not t & 0x88:
     q=b[t]
     if q==0:
      if not caps: r.append(sq+t*128+16384)
     else:
      if q*s<0: r.append(sq+t*128+16384)
      break
     t += d
  else:
   for d in ds:
    t=sq+d
    if t & 0x88: continue
    q=b[t]
    if q*s>0: continue
    if caps and q==0: continue
    r.append(sq+t*128+16384)
 return r
