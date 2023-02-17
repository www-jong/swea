res=[]
for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    li=[[0]*(N) for i in range(M)]
    for i in range(M):
        for j in range(N):
           if li[i][j]==0:
            li[i][j]=1
            tmp+=1
            if i+2<M:
                li[i+2][j]=-1
            if j+2<N:
                li[i][j+2]=-1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))