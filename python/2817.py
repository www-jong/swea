def func(g,idx):
    global res
    if g>K:
        return
    if g==K:
        res+=1
        return
    if idx>=N:
        return
    func(g+lst[idx],idx+1)
    func(g,idx+1)
for m in range(int(input())):
    N,K=map(int,input().split())
    lst=[*map(int,input().split())]
    res=0
    func(0,0)
    print(f'#{m+1}',res)