from collections import deque
dx=[0,1,0,-1] # 동,남,서,북 (시계방향)
dy=[1,0,-1,0]
def bfs(st_x,st_y,dir,cur,tar_x,tar_y):
    visit=[[[10**3]*4 for _ in range(N)] for _ in range(N)]
    q=deque()
    q.append((st_x,st_y,dir,cur))
    plag=1
    
    if st_x==0 and st_y==0:
        plag=0
    else:
        pass
        #visit[st_x][st_y]=
    while q:
        x,y,dir,cur=q.popleft()
        for i in [0,1]:
            if not plag and i==1:
                plag=1
                continue
            ncur=cur+(1 if i==1 else 0)
            nx=x+dx[(dir+i)%4]
            ny=y+dy[(dir+i)%4]
            ndir=(dir+i)%4
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny][ndir]>ncur:
                    visit[nx][ny][ndir]=ncur
                    q.append((nx,ny,ndir,ncur))
    
    for i in visit:
        print(i)
    print('------')

    return visit[tar_x][tar_y]
for m in range(int(input())):
    N=int(input())
    li=[]
    target=[]
    for i in range(N):
        tmp=list(map(int,input().split()))
        for j in range(N):
            if tmp[j]!=0:
                target.append([tmp[j],i,j])
        li.append(tmp)
    target.sort(key=lambda x:x[0])
    q=deque()
    st_x,st_y,dir,cur=0,0,0,0
    data=[10**5]*4
    tmp_count=1
    plag=0
    for _,tar_x,tar_y in target:
        if not plag:
            data=bfs(0,0,0,0,tar_x,tar_y)
            plag=1
        else:
            tmp_data=data[:]
            data=[10**5]*4
            for i in range(4):
                t_data=bfs(st_x,st_y,i,tmp_data[i],tar_x,tar_y)
                print(f'tt:{t_data}')
                dd=t_data[:]
                for j in range(4):
                    data[i]=min(data[i],dd[i])
        st_x,st_y=tar_x,tar_y
        print('@@@@@@@@@@@@@@@@@@')
        print(tmp_count,data)
        tmp_count+=1
    print(data)

