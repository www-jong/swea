from collections import deque
d,R,I=[0,0,1,-1],range,input
for m in R(int(I())):
 N,s,l,r=int(I()),[],[],0
 v=[[0]*N for _ in R(N)]
 for i in R(N):
  t=I()
  if '2' in t:s=[i,t.index('2')]
  l.append(t)
 q=deque([s])
 while q:
  x,y=q.popleft()
  for i in R(4):
   X,Y=x+d[i],y+d[-i-1]
   if 0<=X<N and 0<=Y<N:
    if l[X][Y]=='0' and not v[X][Y]:
     v[X][Y]=1
     q.append((X,Y))
    if l[X][Y]=='3':r=1
 print(f'#{m+1}',r)