M=30000
I=1000000
B=40000
N=0
T={}
K=[[0,0] for _ in range(80)]
H=[[0]*128 for _ in range(128)]
se=set()
RM=0
class A(Exception):pass
def o(ms,tm,pl):
 sc=[]
 for m in ms:
  f=m%128;t=m//128%128;p=m//16384-1;c=b[t]
  if (b[f]==1 or b[f]==-1) and t==ep and not c:c=1
  if m==tm:v=10000000
  elif c:
   v=1000000+10*_m[abs(c)]-_m[abs(b[f])]
   if p:v+=_m[p]
  elif p:v=900000+_m[p]
  elif m==K[pl][0]:v=800000
  elif m==K[pl][1]:v=790000
  else:v=H[f][t]
  sc.append((v,m))
 sc.sort(reverse=True)
 return [m for v,m in sc]
def q(a,b,pl):
 global N
 N+=1
 if N>B:raise A
 if _f>=100:return 0
 if h in se:return 0
 if pl>=48:return _e()*_s
 ch=_a(_s)
 if ch:st=-M+pl;bs=-M+pl;ms=_g(False)
 else:
  st=_e()*_s
  if st>=b:return st
  if st>a:a=st
  bs=st;ms=_g(True)
 ms=o(ms,0,pl if pl<80 else 79)
 ln=0
 for m in ms:
  f=m%128;t=m//128%128;p=m//16384-1
  if not ch:
   c=b[t];vi=_m[abs(c)] if c else 0
   if (b[f]==1 or b[f]==-1) and t==ep and not c:vi=100
   if p:vi+=_m[p]
   if st+vi+200<a and not p:continue
  _mk(m)
  if _a(-_s):_um(m);continue
  ln+=1;sc=-q(-b,-a,pl+1);_um(m)
  if sc>bs:bs=sc
  if bs>a:a=bs
  if a>=b:break
 if ch and ln==0:return -M+pl
 return bs
def ab(d,a,b,pl,no):
 global N,T,RM,_f,h,_s,ep
 N+=1
 if N>B:raise A
 if _f>=100:return 0
 if h in se:return 0
 ch=_a(_s)
 if ch and d>0:d+=1
 if d<=0:return q(a,b,pl)
 tt=T.get(h);tm=0
 if tt:
  td,ts,tf,m=tt;tm=m
  if td>=d:
   if ts>M-1000:ts-=pl
   elif ts<-M+1000:ts+=pl
   if tf==0:
    if pl==0:RM=m
    return ts
   if tf==1 and ts>=b:return ts
   if tf==2 and ts<=a:return ts
 if no and not ch and d>=3 and b-a>1:
  hs=False
  for sq in range(120):
   if sq&0x88:continue
   p=b[sq]
   if p*_s>0 and p!=1 and p!=-1 and p!=6 and p!=-6:hs=True;break
  if hs:
   R=3 if d>=6 else 2;oe=ep;oh=h;of=_f
   if ep>=0:h^=ZE[ep]
   ep=-1;_s=-_s;h^=ZS;_f+=1
   try:sc=-ab(d-1-R,-b,-b+1,pl+1,False)
   finally:_s=-_s;h=oh;ep=oe;_f=of
   if sc>=b:return b
 ms=_l()
 if not ms:return -M+pl if ch else 0
 ms=o(ms,tm,pl if pl<80 else 79)
 fu=False
 if d==1 and not ch:fu=_e()*_s+120<a
 bs=-M-1;bm=ms[0];oa=a
 se.add(h)
 try:
  for i,m in enumerate(ms):
   f=m%128;t=m//128%128;p=m//16384-1;c=b[t]
   ec=(b[f]==1 or b[f]==-1) and t==ep and not c
   qc=c==0 and not ec and p==0
   if fu and qc and i>0:continue
   rd=0
   if d>=3 and i>=3 and qc and not ch:rd=2 if (d<6 or i<6) else 3
   _mk(m)
   if i==0:sc=-ab(d-1,-b,-a,pl+1,True)
   else:
    if rd:
     sc=-ab(d-1-rd,-a-1,-a,pl+1,True)
     if sc>a:sc=-ab(d-1,-a-1,-a,pl+1,True)
    else:sc=-ab(d-1,-a-1,-a,pl+1,True)
    if sc>a and sc<b:sc=-ab(d-1,-b,-a,pl+1,True)
   _um(m)
   if sc>bs:bs=sc;bm=m
   if bs>a:a=bs
   if a>=b:
    if qc:
     if K[pl][0]!=m:K[pl][1]=K[pl][0];K[pl][0]=m
     H[f][t]+=d*d
    break
 finally:se.discard(h)
 if pl==0:RM=bm
 if bs>=b:fl=1
 elif bs<=oa:fl=2
 else:fl=0
 sv=bs
 if sv>M-1000:sv+=pl
 elif sv<-M+1000:sv-=pl
 if len(T)>400000:T.clear()
 T[h]=(d,sv,fl,bm)
 return bs
def think(nb):
 global B,N,RM
 B=nb;N=0;ml=_l()
 if not ml:return 0
 bs=ml[0];RM=bs
 for d in range(1,40):
  se.clear()
  try:ab(d,-I,I,0,True)
  except A:break
  bs=RM
 return bs
def post(p,o_):
 d=json.dumps(o_).encode()
 r=urllib.request.Request(os.environ.get("MAKEFUN_ENV_URL","http://127.0.0.1:8080")+p,d,{"Content-Type":"application/json"},method="POST")
 with urllib.request.urlopen(r) as x:return json.loads(x.read().decode())
def main():
 while True:
  g=post("/game",{})
  st=g.get("status")
  if st=="done":break
  while st=="your_move":
   lm=g.get("legal_moves") or [];mv=None
   try:
    load(g["fen"]);ca=uci(think(NB))
    if ca in lm:mv=ca
   except Exception:mv=None
   if mv is None:mv=lm[0] if lm else None
   if mv is None:return
   g=post("/move",{"game":g.get("game"),"move":mv});st=g.get("status")
  if st=="done":break
if __name__=="__main__":main()
