R=range
for m in R(10):
 _=input()
 li=[list(map(int,input().split()))for _ in R(100)][::-1]
 visit=[[0]*(100)for _ in R(100)]
 n=[0,li[0].index(2)]
 while n[0]<99:
  for x,y in [[0,1],[0,-1],[1,0]]:
   nx,ny=x+n[0],y+n[1]
   if -1<nx<100 and -1<ny<100 and li[nx][ny] and not visit[nx][ny]:
    n=[nx,ny]
    visit[nx][ny]=1
    break
 print(f'#{m+1} {n[1]}')