def f(power,l,v):
    global res
    if l>=N:
        res=min(res,v)
        return
    if v>res:
        return
    if power:
        f(power-1,l+1,v)
    f(li[l-1],l,v+1)
for m in range(int(input())):
    N,*li=map(int,input().split())
    res=10**8
    f(li[0],1,0)
    print(f'#{m+1}',res)