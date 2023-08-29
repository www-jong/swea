dx,dy=[0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,1,-1]
for m in range(int(input())):
    N,M=map(int,input().split());N+=1
    li=[[0]*(N) for i in range(N)]
    for x in range(2):
        for y in range(2):
            li[N//2+x][N//2+y]=1if(x+y)%2else 2
    for i in range(M):
        a,b,c=map(int,input().split())
        li[a][b]=c
        for k in range(8):
            stk=[]
            g=1
            while True:
                nx,ny=a+dx[k]*g,b+dy[k]*g
                try:
                    if li[nx][ny]==(1if c==2 else 2):
                        stk.append((nx,ny))
                    else:
                        if li[nx][ny]==c:
                            while stk:
                                x,y=stk.pop()
                                li[x][y]=c
                        break
                except:
                    break
                g+=1
    r=0
    for i in range(N):
        r+=li[i].count(1)
    print(f'#{m+1}',r,M+4-r)