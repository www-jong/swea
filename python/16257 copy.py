for m in range(int(input())):
    res=0
    N=int(input())
    li=[[0]*(10) for _ in range(10)]
    for i in range(N):
        r1,c1,r2,c2,color=map(int,input().split())
        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                if li[x][y]!=color and li[x][y]!=0:
                    res+=1
                li[x][y]=color
    print(f'#{m+1} {res}')