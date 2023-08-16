I=input
def func(t,d):
 global r
 if t>r:return
 if len(d)==N:
  r=min(r,t)
  return
 for i in range(N):
  if i not in d:func(t+l[len(d)-1][i],d|{i})
for m in range(int(I())):N=int(I());r,l=99,[[*map(int,I().split())] for i in range(N)];func(0,set());print(f'#{m+1}',r)