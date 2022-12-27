res=[]

def func(i,now_sum):
    global tmp
    tmpp=now_sum+li[i]
    if tmpp==K:
        tmp+=1

    if i==(N-1):
        return
    if tmpp>K:
        return
    func(i+1,now_sum)
    func(i+1,tmpp)

for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split())
    li=sorted(list(map(int,input().split())))

    func(0,0)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
