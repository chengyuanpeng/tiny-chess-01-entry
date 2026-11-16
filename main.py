import os,json as j,urllib.request as r
N=10000
V={'p':100,'n':320,'b':330,'r':500,'q':900,'k':0}
Q=(1,-1,16,-16,15,17,-15,-17);D={'p':(16,),'n':(14,18,31,33,-14,-18,-31,-33),'b':Q[4:],'r':Q[:4],'q':Q,'k':Q}
n=0
def t(b,s,c):
 for d in((-15,-17)if c else(15,17)):
  x=s+d
  if x&0x88==0 and b[x]==('P' if c else 'p'):return 1
 for p in 'nk':
  for d in D[p]:
   x=s+d
   if x&0x88==0 and b[x]==(p.upper()if c else p):return 1
 for p in 'brq':
  for d in D[p]:
   x=s+d
   while not x&0x88:
    z=b[x]
    if z!='.':
     if z in((p.upper(),'Q')if c else(p,'q')):return 1
     break
    x+=d
 return 0
def h(b,c):
 return t(b,b.index('K' if c else 'k'),not c)
def g(b,c,C,E):
 O=[];P=lambda x:'q' if x//16 in(0,7)else ''
 for s,p in enumerate(b):
  if s&0x88 or p=='.' or p.isupper()!=c:continue
  T=p.lower();S=16 if c else -16
  if T=='p':
   x=s+S
   if not x&0x88 and b[x]=='.':
    O.append((s,x,P(x)))
    if s//16==(1 if c else 6):O.append((s,x+S,'')) if b[x+S]=='.' else None
   for d in(S-1,S+1):
    x=s+d
    if not x&0x88 and b[x]not in 'Kk' and(x==E or b[x]!='.' and b[x].isupper()!=c):O.append((s,x,P(x)))
  else:
   for d in D[T]:
    x=s+d
    while not x&0x88:
     z=b[x]
     if z!='.' and z.isupper()==c:break
     if z not in 'Kk':O.append((s,x,''))
     if z!='.' or T in 'nk':break
     x+=d
 R=0 if c else 112;E=not c
 if b[R+4]==('K' if c else 'k') and not h(b,c):
  for item in (('K' if c else 'k',R+6,(R+5,R+6)),('Q' if c else 'q',R+2,(R+1,R+2,R+3),(R+3,R+2))):
   q,x,I,*H=item
   H=H[0] if H else I
   if q in C and all(b[i]=='.' for i in I) and all(not t(b,i,E) for i in H):O.append((R+4,x,'c'))
 return O
def mv(b,M,c,C,E):
 s,x,p=M;z=b.copy();p0=z[s];C=z[x]
 z[s]='.'
 if p=='c':
  z[x]=p0;R=112 if s>15 else 0;a=R+(7 if x>s else 0);h=R+(5 if x>s else 3);z[h]=z[a];z[a]='.'
 else:
  if p0.lower()=='p' and x==E and C=='.':z[x-(16 if c else -16)]='.';C='p'
  z[x]=p0 if not p else('Q' if c else 'q')
 c0=C.replace('K','').replace('Q','') if p0=='K' else C.replace('k','').replace('q','') if p0=='k' else C
 for q,R in zip('KQkq',(7,0,119,112)):
  if s==R or x==R:c0=c0.replace(q,'')
 e0=(s+x)//2 if p0.lower()=='p' and abs(x-s)==32 else -1
 return z,not c,c0,e0
def L(b,c,C,E):
 k=b.index('K' if c else 'k')if('K' if c else 'k')in b else -1;a=[]
 if k<0:return a
 for M in g(b,c,C,E):
  z,_,_,_=mv(b,M,c,C,E)
  if not t(z,M[1]if M[0]==k else k,not c):a.append(M)
 return a
def ev(b,c):
 v=0
 for s,p in enumerate(b):
  if s&0x88 or p=='.':continue
  w0=p.isupper();T=p.lower();f0=s%16;R=s//16 if w0 else 7-s//16
  q=V[T]+(R*5 if T=='p' else 0)
  v+=q if w0 else -q
 return v if c else -v
def k(b,M):return V[b[M[1]].lower()]*10-V[b[M[0]].lower()] if b[M[1]]!='.' else 8000 if M[2] else 0
def s(b,c,C,E,d,a,b2,p2=0):
 global n
 n+=1
 if n>N:return ev(b,c)
 m=L(b,c,C,E)
 if not m:return -30000+p2 if h(b,c)else 0
 q=d==0;ch=h(b,c)
 if q:
  v=ev(b,c)
  if v>=b2:return v
  a=max(a,v)
 m=m if not q or ch else [M for M in m if b[M[1]]!='.' or M[2]]
 m.sort(key=lambda M:k(b,M),reverse=True)
 for M in m:
  z,c3,r2,e=mv(b,M,c,C,E);v=-s(z,c3,r2,e,max(0,d-1),-b2,-a,p2+1)
  if v>a:a=v
  if a>=b2:break
 return a
def c(f0):
 global n
 a=f0.split();b=['.']*128
 for R,R0 in enumerate(a[0].split('/')):
  x=0
  for p in R0:
   if p.isdigit():x+=int(p)
   else:b[(7-R)*16+x]=p;x+=1
 c=a[1]=='w';C=a[2]if a[2]!='-' else '';E=-1 if a[3]=='-' else(int(a[3][1])-1)*16+ord(a[3][0])-97
 m=L(b,c,C,E)
 m.sort(key=lambda M:k(b,M),reverse=True)
 if not m:return ''
 b0=m[0];n=0
 for d in range(1,30):
  o=b0;s0=-40000
  for M in m:
   z,c3,r2,e=mv(b,M,c,C,E);v=-s(z,c3,r2,e,d,-40000,-s0,1)
   if v>s0:s0=v;b0=M
   if n>=N:break
  if n>=N:b0=o;break
 return U(b0)
def U(M):
 s,x,p=M
 return chr(97+s%16)+str(s//16+1)+chr(97+x%16)+str(x//16+1)+('q' if p=='q' else '')
def O(u0,p1,b1):
 q=r.Request(u0+p1,data=j.dumps(b1).encode(),)
 return j.loads(r.urlopen(q,timeout=9).read())
def M():
 u0=os.environ['MAKEFUN_ENV_URL']
 while 1:
  g=O(u0,'/game',{})
  if g['status']=='done':break
  if g['status']=='over':continue
  M=c(g['fen']);O(u0,'/move',{'game':g['game'],'move':M})
M()
