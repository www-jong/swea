from collections import deque
dx,dy=[-1,0,1,0],[0,1,0,-1]
d=[[],[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[3,0]]
for m in range(int(input())):
    N,M,R,C,L=map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(N)]
    visit=[[0]*(M) for i in range(N)]
    q=deque()
    q.append((R,C,1))
    visit[R][C]=1
    res=1
    while q:
        x,y,c=q.popleft()
        for i in d[li[x][y]]:
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and li[nx][ny] and not visit[nx][ny] and c+1<=L and (i+2)%4 in d[li[nx][ny]]:
                visit[nx][ny]=c+1
                res+=1
                q.append((nx,ny,c+1))
    print(f'#{m+1}',res)