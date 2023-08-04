for m in range(int(input())):
    N=int(input())
    res=1+N*4
    for x in range(1,N+1):
        for y in range(1,N+1):
            if x*x+y*y<=N*N:res+=1
            else:
                break

    print(f'#{m+1} {res}')