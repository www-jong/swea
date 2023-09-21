import heapq # 다익스트라 2차원
INF=10**9
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
    graph=[[[] for _ in range(N+1)] for _ in range(N+1)]
    for x in range(1,N+1):
        for y in range(1,N+1):
            for s in range(4):
                nx=x+dx[s]
                ny=y+dy[s]
                if 1<=nx<=N and 1<=ny<=N:
                    graph[x][y].append((nx,ny,int(li[nx][ny])))
                    graph[nx][ny].append((x,y,int(li[x][y])))
                # [x][y] -> 주변칸 이동 비용
    distance=[[INF]*(N+1) for _ in range(N+1)]
    q=[]
    heapq.heappush(q,(0,1,1))
    distance[1][1]=0
    while q:
        dist,now_x,now_y=heapq.heappop(q)
        if distance[now_x][now_y]<dist:
            continue
        for i in graph[now_x][now_y]:
            cost=i[2]+dist
            if cost<distance[i[0]][i[1]]:
                distance[i[0]][i[1]]=cost
                heapq.heappush(q,(cost,i[0],i[1]))
    res.append(distance[N][N])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))