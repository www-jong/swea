res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=list(map(int,input().split()))
    for i in range(max(li),0,-1):
        co=-1
        flag=0
        for j in range(N):
            if li[j]>=i:
                if flag==1:
                    pass
                else:
                    flag=1
                    co=0
            else:
                co+=1
        tmp=max(tmp,co)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))