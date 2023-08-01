res=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for m in range(int(input())):
    tmp=""
    n=int(input())
    c=[n-1]*3
    for i in range(n-2,0,-1):
        for j in range(2):
            c.append(i)
    li=[[0]*(n) for _ in range(n)]
    li[0][0]=1
    x,y=0,0
    idx=0
    val=2
    for i in c:
        for j in range(i):
            li[x+dx[idx]][y+dy[idx]]=val
            x+=dx[idx]
            y+=dy[idx]
            val+=1
        idx+=1
        if idx==4:
            idx=0
    print(f'#{m+1}')
    for i in range(n):
        print(*li[i],sep=" ")
