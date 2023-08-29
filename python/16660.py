for m in range(int(input())):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    for i in range(M):
        a,b=map(int,input().split())
        tree[a]=b
    for i in range(M,0,-1):
        if not tree[i]:
            tree[i]=tree[i*2]+(tree[i*2+1] if i*2+1<=N else 0)

    print(f'#{m+1}',tree[L])