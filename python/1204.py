res=[]
for m in range(int(input())):
    tmp=""
    s=input()
    li=list(map(int,input().split()))
    dic={}
    for i in li:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    ress=[0,0]
    for k,v in dic.items():
        print(f'!{k} : {v}')
        if v>ress[1]:
            ress=[k,v]
        elif v==ress[1] and k>ress[0]:
            ress=[k,v]
    tmp=ress[0]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))