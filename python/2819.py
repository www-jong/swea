from collections import deque
res=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(count,s,x,y):
    if count==7:
        if s not in dic:
            dic[s]=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=4 and 1<=ny<=4:
            bfs(count+1,s+str(li[nx][ny]),nx,ny)
        

for m in range(int(input())):
    tmp=0
    dic={}
    li=[[0]]
    for i in range(4):
        li.append([0]+list(map(int,input().split())))
    for i in range(1,5):
        for j in range(1,5):
            bfs(0,'',i,j)
    tmp=len(dic)

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))