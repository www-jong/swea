def func(r):
    global res
    if len(r)==N:
        t=0
        tmp_idx=r[0]
        for i in r[1:]:
            t+=li[tmp_idx][i]
            tmp_idx=i
        res=min(res,t+li[r[-1]][1])
        return
    for i in range(1,N+1):
        if i not in r:
            func(r+[i])

for m in range(int(input())):
    N=int(input())
    nodes=[i for i in range(N+1)]
    li=[[0]]
    res=10**9
    g=[[] for i in range(N+1)]
    for i in range(N):
        tmp=[0]+list(map(int,input().split()))
        for j in range(N):
            g[i+1].append((j+1,tmp[j]))
        li.append(tmp)
    func([1])
    print(f'#{m+1}',res)