import heapq
res=[]
INF=int(1e9)
def dtra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
for m in range(int(input())):
    tmp=0
    N,E=map(int,input().split())
    li=[[] for _ in range(N+1)]
    for i in range(E):
        a,b,c=map(int,input().split())
        li[a].append((b,c))
    visit=[False]*(N+1)
    distance=[INF]*(N+1)
    dtra(0)
    print(distance[N])
    
    res.append(distance[N])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))