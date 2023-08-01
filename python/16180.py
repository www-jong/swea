res=[]
for m in range(int(input())):
    tmp=[0,0]
    c={}
    N=input()
    for i in input():
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
    for k,v in c.items():
        if v>tmp[1]:
            tmp=[k,v]
        elif v==tmp[1] and int(k)>int(tmp[0]):
            tmp=[k,v]
    tmp=tmp[0]+" "+str(tmp[1])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))