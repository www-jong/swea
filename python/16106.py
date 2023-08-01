for m in range(int(input())):
    res=0
    K,N,M=map(int,input().split())
    li=list(map(int,input().split()))
    gap=[1 for i in range(M-1) if li[i+1]-li[i]>K]
    if not gap:
        fuel,idx=K,0
        while idx<N:
            if fuel==0 and idx not in li:
                idx-=1
            elif fuel==0 and idx in li:
                fuel=K
                res+=1
            else:
                idx+=1
                fuel-=1
    print(f'#{m+1} {res}')
