def func(li):
    if len(li)==1:
        return li
    if len(li)==0:
        return []
    g=li[0]
    return func([i for i in li if i<g])+[i for i in li if i==g]+func([i for i in li if i>g])

for m in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))


    print(func(li))
    res=func(li)[N//2]
    print(f'#{m+1} {res}')