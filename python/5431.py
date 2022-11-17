ans=[]
for m in range(int(input())):
    tmp=""
    N,K=map(int,input().split())
    li=[i for i in range(1,N+1)]
    ch=list(map(int,input().split()))
    for i in ch:
        li[i-1]=0
    for i in li:
        if i!=0:
            tmp+=str(i)+" "
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))