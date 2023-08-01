res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    ch=[0,0]
    for i in input():
        if i=='1' and ch[0]==1:
            ch[1]+=1
        elif i=='1' and ch[0]==0:
            ch=[1,1]
        else:
            tmp=max(tmp,ch[1])
            ch=[0,0]
    tmp=max(tmp,ch[1])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))