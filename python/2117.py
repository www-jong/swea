for m in range(int(input())):
    N,M=map(int,input().split()) # N 도시크기, M 비용
    li=[]
    homes=[]
    for i in range(N):
        tmp=list(map(int,input().split()))
        for j in range(N):
            if tmp[j]==1:
                homes.append((i,j))
        li.append(tmp)
    res=0
    for x in range(N):
        for y in range(N):
            for k in range(2*N):
                home_count=sum([1 for X,Y in homes if k>=(abs(X-x)+abs(Y-y))])
                val=home_count*M-((k+1)**2+k**2)
                if val>=0 and res<home_count:
                    res=home_count
    print(f'#{m+1}',res)
