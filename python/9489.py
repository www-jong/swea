import sys
sys.setrecursionlimit(100000)
from collections import deque
dx,dy=[1,0,-1,0],[0,1,0,-1]

def dfs(x,y,visit,dir):
    global res
    tmp=1
    visit[x][y]=1
    for i in [0,2]:
        ndir=(dir+i)%4
        nx=x+dx[ndir]
        ny=y+dy[ndir]
        if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0 and li[nx][ny]==1:
            print(f'{nx}:{ny}, {ndir}')
            tmp+=dfs(nx,ny,visit,ndir)
    return tmp

for m in range(int(input())):
    N,M=map(int,input().split())
    li=[list(map(int,input().split())) for _ in  range(N)]
    #visit=[[0]*(M) for i in range(N)]
    res=0
    for x in range(N):
        for y in range(M):
            if li[x][y]==1:
                #print(visit)
                t1=dfs(x,y,[[0]*(M) for i in range(N)],0)
                t2=dfs(x,y,[[0]*(M) for i in range(N)],2)
                print(f'{x}:{y} - {res}:{t1}:{t2}')
                res=max(res,t1,t2)
    print(res)