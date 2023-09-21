T=int(input())
def func(x):
    global res
    for people in graph[x]:
        if not visit[people]:
            visit[people]=1
            func(people)
for case in range(1,T+1):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    visit=[0]*(N+1)
    res=0
    for _ in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,N+1):
        if not visit[i]:
            res+=1
            func(i)
    print(f'#{case}',res)