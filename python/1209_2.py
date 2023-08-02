for m in range(10):
    _ = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    res = max(sum([li[i][i] for i in range(100)]), sum([li[i][99 - i] for i in range(100)]))
    for dn in range(100):
        res = max(res, sum(li[dn]))
        res = max(res, sum([li[i][dn] for i in range(100)]))
    print(f'#{m+1} {res}')