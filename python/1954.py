dx,dy=[0,1,0,-1],[1,0,-1,0]
for m in range(int(input())):
    n=int(input())
    c=[n-1]+[i for i in range(n-1,0,-1) for _ in '  ']
    li=[[1]*(n) for _ in range(n)]
    x,y,idx,val=0,0,0,2
    for i in c:
        for j in range(i):
            x+=dx[idx]
            y+=dy[idx]
            li[x][y]=val
            val+=1
        idx+=1
        idx%=4
    print(f'#{m+1}')
    for i in range(n):print(*li[i],sep=" ")
