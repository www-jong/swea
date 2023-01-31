from collections import deque
res=[]
dx=[1,1,0,0]
dy=[0,0,-1,1]
for m in range(10):
    tmp=0
    _=input()
    li=[]
    visit=[[0]*(100) for i in range(100)]
    for i in range(100):
        li.append(list(input()))
    visit[1][1]=1
    q=deque()
    q.append((1,1))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #print(f'nx:{nx} ny:{ny}')
            if 0<=nx<=99 and 0<=ny<=99:
                if li[nx][ny]=="3":
                    tmp=1
                    break
                if li[nx][ny]=="0" and visit[nx][ny]==0:
                    q.append((nx,ny))
                    print(f'!nx:{nx} ny:{ny}')
                    visit[nx][ny]=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))