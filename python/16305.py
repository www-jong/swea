for m in range(int(input())):
    res=0
    N=int(input())
    li=sorted(list(map(int,input().split())))
    r=[li[N-1-i//2] if i%2==0 else li[i//2] for i in range(N)]
    print(f'#{m+1}',*r)