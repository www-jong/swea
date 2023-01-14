res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=list(map(int,input().split()))
    for i in range(0,N):
        for j in range(i+1,N):
            X=li[i]*li[j]
            t=-1
            for k in range(len(str(X))):
                if int(str(X)[k])<t:
                    t=-2
                    break
                else:
                    t=int(str(X)[k])
            if t!=-2:
                tmp=max(tmp,X)

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))