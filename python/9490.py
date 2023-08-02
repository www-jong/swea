res=[]
dn=[[1,0],[-1,0],[0,1],[0,-1],[0,0]]
def gets(x,y):
    t=-li[x][y]
    for i in range(-li[x][y],li[x][y]+1):
        if 0<=x+i<N:
            t+=li[x+i][y]
        if 0<=y+i<M:
            t+=li[x][y+i]
    return t

for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(M):
            tmp=max(tmp,gets(x,y))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))