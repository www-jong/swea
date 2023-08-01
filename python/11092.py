res=[]
for m in range(int(input())):
    maxs_idx,mins_idx=[-1,0],[-1,0]
    N=int(input())
    li=list(map(int,input().split()))
    maxs,mins=max(li),min(li)
    for i in range(N):
        if maxs==li[i]:
            if maxs_idx[0]==-1:
                maxs_idx[0]=i
            maxs_idx[1]=i
        if mins==li[i]:
            if mins_idx[0]==-1:
                mins_idx[0]=i
            mins_idx[1]=i
    res.append(abs(maxs_idx[1]-mins_idx[0]))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))