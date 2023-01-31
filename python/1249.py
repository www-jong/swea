from collections import deque
res=[]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[[0]*(N+1)]
    for i in range(N):
        li.append([0]+list(input()))
    visit=[[0]*(N+1) for i in range(N+1)]
    time=[[0]*(N+1) for i in range(N+1)]
    q=deque()
    q.append((1,1))
    visit[1][1]=1
    time[1][1]=int(li[1][1])
    while q:
        x,y=q.popleft()
        now_time=int(time[x][y])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<nx<=N and 0<ny<=N:
                if visit[nx][ny]==0 or now_time+int(li[nx][ny])<time[nx][ny]:
                    q.append((nx,ny))
                    visit[nx][ny]=1
                    time[nx][ny]=now_time+int(li[nx][ny])
    tmp=time[N][N]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))