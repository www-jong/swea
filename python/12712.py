def plus(M,x,y):
    global res
    tmp=li[x][y]

    for d in range(1,M):
        if x-d>=1:tmp+=li[x-d][y]
        if x+d<=N:tmp+=li[x+d][y]
        if y-d>=1:tmp+=li[x][y-d]
        if y+d<=N:tmp+=li[x][y+d]
    res=max(tmp,res)

def ex(M,x,y):
    global res
    tmp=li[x][y]
    for d in range(1,M):
        if x-d>=1:
            if y-d>=1:tmp+=li[x-d][y-d]
            if y+d<=N:tmp+=li[x-d][y+d]
        if x+d<=N:
            if y-d>=1:tmp+=li[x+d][y-d]
            if y+d<=N:tmp+=li[x+d][y+d]
    res=max(tmp,res)

for i in range(int(input())):
    res=0
    N,M=map(int,input().split())
    li=[[0]]
    for _ in range(N):
        li.append([0]+list(map(int,input().split())))
    for x in range(1,N+1):
        for y in range(1,N+1):
            plus(M,x,y)
            ex(M,x,y)
    print(f'#{i+1} {res}')