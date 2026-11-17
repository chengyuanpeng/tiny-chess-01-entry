import os,json as j,urllib.request as r
N=10000
V=dict(p=100,n=320,b=330,r=500,q=900,k=0)
Q=(1,-1,16,-16,15,17,-15,-17);D=dict(p=(16,),n=(14,18,31,33,-14,-18,-31,-33),b=Q[4:],r=Q[:4],q=Q,k=Q);n=0
def t(b,s,c):
 P,A,K='PNK'if c else'pnk';B,R=('BQ','RQ')if c else('bq','rq')
 for d in((-15,-17)if c else(15,17)):
  x=s+d
  if x&136<1 and b[x]==P:return 1
 for p,ds in((A,D['n']),(K,Q)):
  for d in ds:
   x=s+d
   if x&136<1 and b[x]==p:return 1
 for ds,zs in((D['b'],B),(D['r'],R)):
  for d in ds:
   x=s+d
   while x&136<1 and b[x]=='.':x+=d
   if x&136<1 and b[x] in zs:return 1
 return 0
def h(b,c):return t(b,b.index('K'if c else'k'),not c)
def g(b,c,C,E):
 O=[];P=lambda x:'q'if not x//16%7 else'';S=32*c-16
 for s,p in enumerate(b):
  if s&136 or p=='.'or p.isupper()!=c:continue
  T=p.lower()
  if T=='p':
   x=s+S
   if x&136<1 and b[x]=='.':
    O.append((s,x,P(x)))
    if s//16==(1 if c else 6)and b[x+S]=='.':O.append((s,x+S,''))
   for d in(S-1,S+1):
    x=s+d
    if x&136<1 and b[x]not in'Kk'and(x==E or b[x]!='.'and b[x].isupper()!=c):O.append((s,x,P(x)))
  else:
   for d in D[T]:
    x=s+d
    while x&136<1:
     z=b[x]
     if z!='.'and z.isupper()==c:break
     if z not in'Kk':O.append((s,x,''))
     if z!='.'or T in'nk':break
     x+=d
 R=112-112*c
 if b[R+4]==('K'if c else'k')and not h(b,c):
  for i in 0,1:
   q=('KQ'if c else'kq')[i];x=R+6-4*i;I=range(R+5,R+7)if i<1 else range(R+1,R+4);H=(R+5,R+6)if i<1 else(R+3,R+2)
   if q in C and all(b[j]=='.'for j in I)and all(not t(b,j,not c)for j in H):O.append((R+4,x,'c'))
 return O
def mv(b,M,c,C,E):
 s,x,p=M;z=b.copy();u=z[x];v=z[s];z[s]='.'
 if p=='c':
  z[x]=v;R=112 if s>15 else 0;a=R+(7 if x>s else 0);h=R+(5 if x>s else 3);z[h]=z[a];z[a]='.'
 else:
  if v.lower()=='p'and x==E and u=='.':z[x-(16 if c else-16)]='.'
  z[x]=v if not p else('Q'if c else'q')
 C=''.join(q for q,R in zip('KQkq',(7,0,119,112))if q in C and(v not in'Kk'or(q in'KQ')!=(v=='K'))and s!=R and x!=R)
 return z,not c,C,(s+x)//2 if v.lower()=='p'and abs(x-s)==32 else-1
def L(b,c,C,E):
 K='K'if c else'k';k=b.index(K)if K in b else-1;a=[]
 if k<0:return a
 ch=h(b,c);P=set()
 if not ch:
  for d in Q:
   x=k+d
   while x&136<1 and b[x]=='.':x+=d
   if x&136<1 and b[x].isupper()==c:P.add(x)
 for M in g(b,c,C,E):
  x,y,p=M
  if ch or x==k or x in P or b[x].lower()=='p'and y==E and b[y]=='.':
   z,_,_,_=mv(b,M,c,C,E)
   if not t(z,y if x==k else k,not c):a.append(M)
  else:a.append(M)
 return a
def ev(b,c):
 v=0
 for s,p in enumerate(b):
  if s&136 or p=='.':continue
  w=p.isupper();T=p.lower();R=s//16 if w else 7-s//16;q=V[T]+(R*5 if T=='p'else 0);v+=q if w else-q
 return v if c else-v
def k(b,M):return V[b[M[1]].lower()]*10-V[b[M[0]].lower()]if b[M[1]]!='.'else 8000 if M[2]else 0
def s(b,c,C,E,d,a,b2,p2=0):
 global n
 n+=1
 if n>N:return ev(b,c)
 m=L(b,c,C,E)
 if not m:return-30000+p2 if h(b,c)else 0
 q=d==0;ch=h(b,c)
 if q:
  v=ev(b,c)
  if v>=b2:return v
  a=max(a,v)
 m=m if not q or ch else[M for M in m if b[M[1]]!='.'or M[2]];m.sort(key=lambda M:k(b,M),reverse=True)
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
 c=a[1]=='w';C=a[2]if a[2]!='-'else'';E=-1 if a[3]=='-'else(int(a[3][1])-1)*16+ord(a[3][0])-97
 m=L(b,c,C,E);m.sort(key=lambda M:k(b,M),reverse=True)
 if not m:return''
 b0=m[0];n=0
 for d in range(1,30):
  o=b0;v0=-40000
  for M in m:
   z,c3,r2,e=mv(b,M,c,C,E);v=-s(z,c3,r2,e,d,-40000,40000,1)
   if v>v0:v0=v;b0=M
   if n>=N:break
  if n>=N:b0=o;break
 return U(b0)
def U(M):
 s,x,p=M
 return chr(97+s%16)+str(s//16+1)+chr(97+x%16)+str(x//16+1)+('q'if p=='q'else'')
def O(u0,p1,b1):return j.loads(r.urlopen(r.Request(u0+p1,data=j.dumps(b1).encode()),timeout=9).read())
def M():
 u0=os.environ['MAKEFUN_ENV_URL']
 while 1:
  g=O(u0,'/game',{})
  if g['status']=='done':break
  if g['status']=='over':continue
  M=c(g['fen']);O(u0,'/move',{'game':g['game'],'move':M})
M()
