res=[]
def func(e,idx):
    global tmp
    if idx==N:
        return
    if tmp[0]>abs(level-e*2):
        tmp=[abs(level-e*2),e]
    func(e+li[idx],idx+1)
    func(e,idx+1)
for m in range(int(input())):
    tmp=[10**10,0]
    N=int(input())
    li=list(map(int,input().split()))
    level=sum(li)
    func(0,0)
    print(tmp)
    res.append(tmp[:])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))