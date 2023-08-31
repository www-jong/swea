for m in range(int(input())):
    N,M=map(int,input().split())
    w=sorted(list(map(int,input().split())),reverse=True)
    t=sorted(list(map(int,input().split())),reverse=True)
    res=0
    idx=0
    t_idx=0
    while idx<N and t_idx<M:
        if t[t_idx]>=w[idx]:
            res+=w[idx]
            t_idx+=1
        idx+=1
    print(f'#{m+1}',res)