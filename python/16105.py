res=[]
for m in range(int(input())):
    tmp=[0,0]
    N=int(input())
    dic={}
    for i in input():
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for k,v in dic.items():
        if v>tmp[1]:
            tmp=[k,v]
        elif v==tmp[1] and int(k)>int(tmp[0]):
            tmp=[k,v]
    tmp=tmp[0]+" "+str(tmp[1])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))