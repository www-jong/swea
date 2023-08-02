res=[]
for m in range(int(input())):
    res=0
    N,M=map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(N)]
    for i in range(N+1-M):
        for j in range(N+1-M):
            res=max(res,sum([sum(li[i+k][j:j+M]) for k in range(M)]))
    print(f'#{m+1} {res}')