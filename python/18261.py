def func(i):
    global visit
    for x in graph[i]:
        if not visit[x]:
            visit[x]=1
            func(x)

T=int(input())
for case in range(1,T+1):
    res=0
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    visit=[0]*(N+1)
    li=list(map(int,input().split()))
    for i in range(M):
        graph[li[i*2]].append(li[i*2+1])
        graph[li[i*2+1]].append(li[i*2])
    for i in range(1,N+1):
        if not visit[i]:
            res+=1
            func(i)

    print(f'#{case}',res)