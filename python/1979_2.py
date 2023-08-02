for m in range(int(input())):
    res=0
    N,K=map(int,input().split())
    li=[[0]*(N+1)]+[[0]+list(map(int,input().split()))+[0] for _ in range(N)]+[[0]*(N+1)]
    for x in range(1,N+1):
        for y in range(1,N+1):
            if y+K<=N+1 and sum(li[x][y:y+K])==K and sum(li[x][y-1:y+K+1])==K:
                res+=1
            if x+K<=N+1 and sum([li[x+i][y] for i in range(K)])==K and sum([li[x+i][y] for i in range(-1,K+1)])==K:
                res+=1
    print(f'{m+1} {res}')