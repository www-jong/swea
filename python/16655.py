from collections import deque
for m in range(int(input())):
    V,E=map(int,input().split())
    visit=[10**5]*(V+1)
    nodes=[[] for i in range(V+1)]
    for i in range(E):
        a,b=map(int,input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    s,e=map(int,input().split())
    q=deque()
    q.append((s,0))
    while q:
        x,c=q.popleft()
        for i in nodes[x]:
            if visit[i]>c+1:
                visit[i]=c+1
                q.append((i,c+1))
    print(f'#{m+1}',visit[e] if visit[e]!=10**5 else 0)