def go(x):
    global co
    for i in graph[x]:
        co+=1
        go(i)
for m in range(int(input())):
    E,N=map(int,input().split())
    li=list(map(int,input().split()))
    graph=[[] for i in range(max(li)+1)]
    for i in range(E):
        graph[li[i*2]].append(li[i*2+1])
    co=1
    go(N)
    print(f'#{m+1}',co)