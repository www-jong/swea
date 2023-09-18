def func(val,idx):
    global res
    if idx>=12:
        res=min(res,val)
        return
    if val>res:
        return
    func(val+A[idx],idx+1)
    func(val+b,idx+1)
    func(val+c,idx+3)

for m in range(int(input())):
    a,b,c,d=map(int,input().split())
    plan=list(map(int,input().split()))
    A=[a*i for i in plan]
    res=d
    func(0,0,)
    print(f'#{m+1} {res}')