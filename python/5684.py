import sys
INF=int(1e9)
res=[]
for m in range(int(input())):
    tmp=INF
    N,M=map(int,input().split())
    graph=[[INF]*(N+1) for _ in range(N+1)]
    li=[]
    for i in range(M):
        a,b,c=map(int,input().split())
        graph[a][b]=c
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(1,N+1):
        tmp=min(tmp,graph[i][i])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))