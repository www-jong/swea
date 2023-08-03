res=[]
for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split())
    li=list(map(int,input().split()))
    r=[[0]*N for i in range(N)]
    for x in range(N):
        r[x][x]=li[x]
        for y in range(x+1,N):
            r[x][y]=r[x][y-1]+li[y]
            if r[x][y]==K:tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))