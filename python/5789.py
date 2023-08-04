for m in range(int(input())):
    N,Q=map(int,input().split())
    li='0'*N
    for i in range(Q):
        L,R=map(int,input().split())
        li=li[:L]+str(i+1)*(R-L)+li[R:]
    print(f'#{m+1}',*li)
