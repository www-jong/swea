res=[]

def func(li):
    global sm,ans
    if len(li)==3:
        if li[0]>li[1] or li[1]>li[2]:
            return
        tt=0
        for i in li:
            tt+=ans[i]
        sm.append(tt)

        return
    for i in range(1,8):
        if i not in li:
            li.append(i)
            func(li)
            li.pop()

for m in range(int(input())):
    tmp=0
    ans=list(map(int,input().split()))
    ans.sort(reverse=True)
    ans=[0]+ans
    sm=[]
    func([])
    tmp=sorted(list(set(sm)),reverse=True)[4]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))



'''
10 9 3 2 1


'''