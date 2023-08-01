dx,dy=[0,0,1,-1],[1,-1,0,0]
res=[]
INF=int(10**9)
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=[]
    for i in range(N):
        li.append(list(map(int,input().split())))

    graph=[[INF]*(N) for _ in range(N)]
    graph[0][0]=0
    q=[]
    q.append((0,0))
    while q:
        x,y=q.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]>1+graph[x][y]+max(li[nx][ny]-li[x][y],0):
                    graph[nx][ny]=1+graph[x][y]+max(li[nx][ny]-li[x][y],0)
                    q.append((nx,ny))
    tmp=graph[N-1][N-1]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))