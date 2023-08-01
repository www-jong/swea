res=[]
def func(x,y):
    t=0
    if 0<x:
        t+=li[x-1][y]
    if 0<y:
        t+=li[x][y-1]
    if y<M-1:
        t+=li[x][y+1]
    if x<N-1:
        t+=li[x+1][y]
    t+=li[x][y]
    return t
for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    li=[]
    for i in range(N):
        li.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(M):
            tmp=max(tmp,func(i,j))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))