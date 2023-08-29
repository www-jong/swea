for m in range(10):
    n=int(input())
    li=[list(map(int,input().split())) for _ in range(n)]
    res=0
    for y in range(n):
        t=''
        for x in range(n):
            t+=str(li[x][y])
        res+=t.replace('0','').count('12')
    print(f'#{m+1}',res)