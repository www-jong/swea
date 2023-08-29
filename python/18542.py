def dfs(x):
    global idx
    if ltree[x]:dfs(ltree[x])
    nodes[x]=idx
    idx+=1
    if rtree[x]:dfs(rtree[x])

for m in range(int(input())):
    N=int(input())
    li=[i for i in range(N+1)]
    nodes=[i for i in range(N+1)]
    tree=[[] for i in range(N+1)]
    ltree=[0]*(N+1)
    rtree=[0]*(N+1)
    for i in range(1,N+1):
        if i*2<=N:
            tree[i].append(i*2)
            ltree[i]=i*2
        if i*2+1<=N:
            tree[i].append(i*2+1)
            rtree[i]=i*2+1
    idx=1
    dfs(1)
    print(f'#{m+1}',nodes[1],nodes[N//2])