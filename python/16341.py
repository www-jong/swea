for g in range(int(input())):
    n,m=map(int,input().split())
    li=[input() for _ in range(n)]
    li.extend([''.join([li[x][y]for x in range(n)])for y in range(n)])
    print(f'#{g+1}',*[li[x][y:y+m] for x in range(n*2) for y in range(n-m+1) if li[x][y:y+m]==li[x][y:y+m][::-1]])
