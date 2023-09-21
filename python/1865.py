def dfs(v,idx,val):
    global res
    if idx==N:
        res=max(val,res)
        return
    if val<=res:
        return
    for i in range(N):
        if not v[i]:
            v[i]=1
            dfs(v,idx+1,val*li[idx][i]*0.01)
            v[i]=0
for m in range(int(input())):
    N=int(input())
    li=[list(map(int,input().split())) for i in range(N)]
    res=0
    for i in range(N):
        v=[0]*N
        v[i]=1
        dfs(v,1,li[0][i]*0.01)
        v[i]=0
    print('#%d %f'%(m+1,res*100))
