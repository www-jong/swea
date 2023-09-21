import heapq
d=[0,0,1,-1]
T=int(input())

for case in range(1,T+1):
    N=int(input())
    graph=[[[] for _ in range(N)] for _ in range(N)]
    li=[list(map(int,input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx,ny=x+d[i],y+d[3-i]
                if 0<=nx<N and 0<=ny<N:
                    graph[x][y].append((nx,ny,max(0,li[nx][ny]-li[x][y])+1))
    res=[[10**9]*N for _ in range(N)]
    res[0][0]=0
    q=[]
    heapq.heappush(q,(0,(0,0)))
    while q:
        dist,now=heapq.heappop(q)
        if res[now[0]][now[1]]<dist:
            continue
        for i in graph[now[0]][now[1]]:
            cost=dist+i[2]
            if cost<res[i[0]][i[1]]:
                res[i[0]][i[1]]=cost
                heapq.heappush(q,(cost,i))

    print(f'#{case}',res[N-1][N-1])