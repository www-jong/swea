import math
for m in range(int(input())):
    a,b=map(int,input().split())
    res=min(a,b)
    print(f'#{m+1}',res)