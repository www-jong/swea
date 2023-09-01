from collections import deque
d=[0,0,1,-1]

for m in range(int(input())):
    N,M=map(int,input().split())
    res=0
    visit=[[3000]*M for i in range(N)]
    li=[]
    q=deque()

    '''
    for i in range(N):
        tmp=input()
        li.append(tmp)
        for j in range(M):
            if tmp[j]=='W':
                q.append((i,j,0))
                visit[i][j]=0
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<N and 0<=ny<M and li[nx][ny]=='L' and (visit[nx][ny]>c+1):
                res+=c+1
                visit[nx][ny]=c+1
                q.append((nx,ny,c+1))
    '''
    land=set()
    for i in range(N):
        tmp=input()
        b=''
        for j in range(M):
            if tmp[j]=='W':
                q.append((i,j,0))
                visit[i][j]=0
            else:
                land.add((i,j))
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if (nx,ny) in land and(visit[nx][ny]>c+1):
                res+=c+1
                visit[nx][ny]=c+1
                q.append((nx,ny,c+1))

    print(f'#{m+1}',res)
