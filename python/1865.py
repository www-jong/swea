res=[]
def bfs(idx,per,vi):
    global tmp
    if idx==N:
        tmp=max(per,tmp)
        return
    if per<=tmp: # per<tmp -> 시간초과,
        return
    for i in range(N):
        if not vi[i]:
            vi[i]=1
            bfs(idx+1,per*li[idx][i]*0.01,vi)
            vi[i]=0

for m in range(int(input())):
    tmp=-1
    N=int(input())
    li=[]
    visit=[0]*(N)
    for i in range(N):
        li.append(list(map(int,input().split())))
    bfs(0,1,visit)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %.6f"%(i+1,res[i]*100))