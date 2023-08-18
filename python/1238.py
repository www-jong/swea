from collections import deque


for m in range(10):
    lens,st=map(int,input().split())
    visit=[10**5]*(101)
    nodes=[[] for i in range(101)]
    li=list(map(int,input().split()))
    for i in range(len(li)//2):
        nodes[li[i*2]].append(li[i*2+1])
    q=deque()
    q.append((st,0))
    visit[st]=0
    while q:
        x,c=q.popleft()
        for i in nodes[x]:
            if visit[i]>c+1:
                visit[i]=c+1
                q.append((i,c+1))
    for i in range(101):
        if visit[i]==10**5:visit[i]=-1
    for i in range(100,-1,-1):
        if visit[i]==max(visit):
            print(f'#{m+1}',i)
            break
    #print(visit)