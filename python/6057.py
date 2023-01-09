res=[]
for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    li=[[0]*(51) for i in range(51)]
    for i in range(M):
        x,y=map(int,input().split())
        li[x][y]=1
        li[y][x]=1
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if li[i][j] and li[j][k] and li[k][i]:
                    tmp+=1

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))