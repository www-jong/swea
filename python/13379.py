res = []
def dfs(graph, node, visit, c):
    global res
    if node == co - 1:
        res = min(res,c)
        return
    if c > res:
        return

    visit[node] = True
    for i in graph[node]:
        if not visit[i]:
            dfs(graph, i, visit, c + 1)


for m in range(int(input())):
    res = 11
    M, N, L = map(int, input().split())

    gori = [(M - 1, 0)]
    for i in range(M):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:
                gori.append((i, j))
    gori.append((0, N - 1))
    co = len(gori)
    graph = [[] for i in range(co)]
    for i in range(co):
        for j in range(i + 1, co):
            lens = abs(gori[i][1] - gori[j][1]) + abs(gori[i][0] - gori[j][0])
            if lens <= L:
                graph[i].append(j)
                graph[j].append(i)
    dfs(graph, 0, [False] * (co), 0)
    print(f'#{m+1} {res}')