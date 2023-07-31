res=[]
for m in range(int(input())):
    maxs,mins=-1,10**10
    N,M=map(int,input().split())
    li=list(map(int,input().split()))
    for i in range(N-M+1):
        if maxs<sum(li[i:i+M]):
            maxs=sum(li[i:i+M])
        if mins>sum(li[i:i+M]):
            mins=sum(li[i:i+M])
    res.append(maxs-mins)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))