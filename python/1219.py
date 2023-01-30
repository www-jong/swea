res=[]
def go(x):
    global tmp
    if x==99:
        tmp=1
        return
    for i in range(len(graph[x])):
        tmp_val=graph[x].pop(i)
        print(f'now{x}, i go {tmp_val}')
        go(tmp_val)
        graph[x].insert(i,tmp_val)

for m in range(10):
    tmp=0
    _,N=map(int,input().split())
    graph=[[] for i in range(N+1)]
    road=list(map(int,input().split()))
    for i in range(0,len(road),2):
        graph[road[i]].append(road[i+1])
    go(0)
    res.append(tmp)
    break
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))