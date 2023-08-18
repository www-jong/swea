from collections import deque
d=[0,0,1,-1]
for m in range(int(input())):
    N=int(input())
    li=[]
    st=[]
    end=[]
    for i in range(N):
        tmp=list(input())
        for j in range(N):
            if tmp[j]=='2':
                st=[i,j]
                tmp[j]='0'
            if tmp[j]=='3':
                tmp[j]='0'
                end=[i,j]
        li.append(tmp)
    visit=[[10**5]*N for i in range(N)]
    q=deque()
    visit[st[0]][st[1]]=0
    q.append((st[0],st[1],0))
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx=x+d[i]
            ny=y+d[3-i]
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny]>c+1 and li[nx][ny]=='0':
                    visit[nx][ny]=c+1
                    q.append((nx,ny,c+1))

    print(f'#{m+1}',visit[end[0]][end[1]]-1 if visit[end[0]][end[1]]!=10**5 else 0)