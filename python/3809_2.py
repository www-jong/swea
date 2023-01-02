ans=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=""
    lilen=0
    while lilen!=N:
        tmpli=list(map(int,input().split()))
        tmpstr=""
        for i in tmpli:
            tmpstr+=str(i)
        lilen+=len(tmpli)
        li+=tmpstr
    c=0
    while True:
        if str(c) not in li:
            tmp=c
            break
        c+=1
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))
