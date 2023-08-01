for m in range(10):
    n=int(input())
    boxs=list(map(int,input().split()))
    for _ in range(n):
        boxs[0]+=1
        boxs[-1]-=1
        boxs.sort()
    print(f'#{m+1} {boxs[-1]-boxs[0]}')