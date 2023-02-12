res=[]
for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    li=[]
    for i in range(N):
        li.append(list(map(int,input().split())))
    for i in range(N+1-M):
        for j in range(N+1-M):
            sums=0
            for dx in range(M):
                for dy in range(M):
                    sums+=li[i+dx][j+dy]
            tmp=max(sums,tmp)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))