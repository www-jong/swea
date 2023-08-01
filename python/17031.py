dx,dy=[0,0,1,-1],[1,-1,0,0]
res=[]
INF=int(10**9)
def dfs(x,y):
    global graph
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny]>graph[x][y]+1+max(li[nx][ny]-li[x][y],0):
                print(f'{nx}:{ny}')
                graph[nx][ny]=graph[x][y]+1+max(li[nx][ny]-li[x][y],0)
                dfs(nx,ny)
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=[]
    for i in range(N):
        li.append(list(map(int,input().split())))

    graph=[[INF]*(N) for _ in range(N)]
    graph[0][0]=0
    dfs(0,0)
    tmp=graph[N-1][N-1]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))