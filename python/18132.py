def back(li,idx):
    global tmp
    if sum(li)==K and len(li)==N:
        tmp+=1
        return
    if sum(li)>K or idx>12:
        return
    back(li+[idx],idx+1)
    back(li,idx+1)
res=[]
for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split())
    back([],1)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))