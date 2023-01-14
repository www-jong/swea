res=[]
def dfs(idx,count):
    global max
    visit[idx]=1
    if count>max:
        max=count
    for i in li[idx]:
        if not visit[i]:
            dfs(i,count+1)
            visit[i]=0

for m in range(int(input())):
    tmp=0
    max=-1
    N,M=map(int,input().split())
    li=[[] for i in range(N+1)]
    for i in range(M):
        x,y=map(int,input().split())
        li[x].append(y)
        li[y].append(x)
    for i in range(1,N+1):
        visit=[0]*(N+1)
        dfs(i,1)
    tmp=max
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))