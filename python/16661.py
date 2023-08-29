for m in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    tree=[0]
    rtree=[0]*(N+1)
    ltree=[0]*(N+1)


    idx=1
    while idx<=N:
        tree.append(li[idx-1])
        tmp=idx
        while tmp>1:
            if tree[tmp]<tree[tmp//2]:
                tree[tmp],tree[tmp//2]=tree[tmp//2],tree[tmp]
            tmp//=2
        idx+=1
    tree.pop(0)
    print(tree)
    res=0
    while True:
        if N==1:
            break
        res+=tree[N//2-1]
        N//=2
    print(f'#{m+1}',res)
