from collections import deque
d=[0,0,1,-1]
for m in range(int(input())):
    N=int(input())
    li=[list(map(int,input().split())) for i in range(N)]
    v=[[-1]*N for i in range(N)]
    q=deque()
    q.append((0,0))
    v[0][0]=li[0][0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<N and 0<=ny<N:
                if (v[nx][ny]==-1) or (v[x][y]+li[nx][ny]<v[nx][ny]):
                    v[nx][ny]=v[x][y]+li[nx][ny]
                    q.append((nx,ny))
    print(f'#{m+1}',v[N-1][N-1])