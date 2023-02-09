from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
res=[]

for m in range(int(input())):
    tmpli=[]
    tmp=""
    N=int(input())
    li=[[0]*(N+1)]
    visit=[[0]*(N+1) for i in range(N+1)]
    for i in range(N):
        li.append([0]+list(map(int,input().split())))

    for i in range(1,N+1):
        for j in range(1,N+1):
            size=[0,0,0]
            if li[i][j]!=0 and visit[i][j]==0:
                q=deque()
                q.append((i,j))
                visit[i][j]=1
                size=[size[0]+1,[i,j],[0,0]]
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 1<=nx<=N and 1<=ny<=N:
                            if li[nx][ny]!=0 and visit[nx][ny]==0:
                                visit[nx][ny]=1
                                q.append((nx,ny))
                                size[0]+=1
                                size[2]=[nx,ny] if nx>=size[2][0] and ny>=size[2][1] else size[2]
            if size[0]:
                tmpli.append([size[0],size[2][0]-size[1][0]+1,size[2][1]-size[1][1]+1])
    tmpli.sort(key=lambda x:(x[0],x[1]))
    tmp+=str(len(tmpli))+" "
    for i in tmpli:
        tmp+=str(i[1])+" "+str(i[2])+" " if i[1]!=i[2] else str(i[1])+" "
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))