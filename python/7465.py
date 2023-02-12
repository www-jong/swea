from collections import deque
res=[]

def bfs(st):
    q=deque()
    q.append(st)
    visit[st]=1
    while q:
        now=q.popleft()
        for node in li[now]:
            if not visit[node]:
                q.append(node)
                visit[node]=1

for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    li=[[] for i in range(N+1)]
    visit=[0]*(N+1)
    for i in range(M):
        A,B=map(int,input().split())
        li[A].append(B)
        li[B].append(A)
    
    for i in range(1,N+1):
        if not visit[i]:
            bfs(i)
            tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))