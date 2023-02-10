from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]
res=[]
for m in range(int(input())):
    tmp=[0,[0]]
    N=int(input())
    li=[[0]*(N+1)]
    visit=[[0]*(N+1) for i in range(N+1)]
    for i in range(N):
        li.append([0]+list(map(int,input().split())))
    for i in range(1,N+1):
        for j in range(1,N+1):
            q=deque()
            q.append((i,j))
            count=[1,li[i][j]]
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 1<=nx<=N and 1<=ny<=N:
                        if li[nx][ny]==(li[x][y]+1):
                            q.append((nx,ny))
                            count[0]+=1
            if count[0]>tmp[0]:
                tmp=count
            elif count[0]==tmp[0] and count[1]<tmp[1]:
                tmp=count

    res.append(str(tmp[1])+" "+str(tmp[0]))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))