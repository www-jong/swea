dic={}
def func(val,li,idx):
    if idx==12:
        return
    dic[val]=set(li)
    func(val+3**idx,li+[idx],idx+1)
    func(val-3**idx,li+[idx],idx+1)
    func(val,li,idx+1)
func(0,[],0)
res=[]
for m in range(int(input())):
    tmp="yes"
    x,y=map(int,input().split())
    if x in dic and y in dic:
        x=dic[x]
        y=dic[y]
        if len(x)+len(y)!=0:
            z=set(i for i in range(1+max(x.union(y))))
            if z!=x.union(y):
                tmp="no"
    else:
        tmp="no"
    #print(z)
    #print(x.union(y))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))