res=[]
for m in range(int(input())):
    tmp=""
    N,Q=map(int,input().split())
    li=[0]*(N+1)
    for i in range(1,Q+1):
        L,R=map(int,input().split())
        for j in range(L,R+1):
            li[j]=i
    for i in li:
        tmp+=str(i)+" "
    res.append(tmp[2:-1])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))