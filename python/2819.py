d=[0,0,1,-1]
def f(v,idx,x,y):
    if idx==7:
        res.add(v)
        return
    for k in range(4):
        nx,ny=x+d[k],y+d[3-k]
        if 0<=nx<4 and 0<=ny<4:
            f(v+li[nx][ny],idx+1,nx,ny)


for m in range(int(input())):
    res=set()
    li=[list(input().split()) for i in range(4)]
    for i in range(4):
        for j in range(4):
            f(li[i][j],1,i,j)
    print(f'#{m+1}',len(res))