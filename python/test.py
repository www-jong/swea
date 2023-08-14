def func(li,idx):
    global res,t
    t.append(t)
    res+=1
    print(li)
    if idx==8:
        return
    func(li,idx+1)
    func(li+[idx],idx+1)
res=0
func([],0)

print(res)