ans=[]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
for m in range(int(input())):
    N=int(input())
    maps=[[0]*(N+1)]
    for i in range(N):
        maps.append([0]+list(str(input())))
    visits=[[0]*(N+1) for i in range(N+1)]
    count=0
    q=[]
    for i in range(1,N+1):
        for j in range(1,N+1):
            tmpcount=0
            if maps[i][j]=='#' and visits[i][j]==0:
                q.append((i,j))
            else:
                continue
            visits[i][j]=1
            while q:
                tmpcount+=1
                x,y=q.pop(0)
                for s in range(4):
                    nx=x+dx[s]
                    ny=y+dy[s]
                    if 0<nx<=N and 0<ny<=N:
                        if maps[nx][ny]=="#" and visits[nx][ny]==0:
                            q.append((nx,ny))
                            visits[nx][ny]=1
            if (tmpcount**(1/2))%1>0:
                count+=1
            count+=1
    tmp="no" if count!=1 else "yes"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))