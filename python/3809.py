ans=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[]
    lilen=0
    while lilen!=N:
        tmpli=list(map(int,input().split()))
        lilen+=len(tmpli)
        li+=tmpli
    co=[0]*10
    for i in li:
        co[i]+=1
    c=0
    comin=min(co)
    while tmp==0:
        tmpco=[0]*10
        for i in str(c):
            tmpco[int(i)]+=1
        for i in range(10):
            if co[i]<tmpco[i]:
                tmp=c
                break
        c+=1
    print(tmp)
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))
