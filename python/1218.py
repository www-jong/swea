res=[]
for m in range(10):
    tmp=1
    _=input()
    S=input()
    dic={'[':0,'{':0,'(':0,'<':0}
    for i in S:
        if i==')':
            if dic['(']<=0:
                tmp=0
                break
            else:
                dic['(']-=1
        elif i==']':
            if dic['[']<=0:
                tmp=0
                break
            else:
                dic['[']-=1
        elif i=='}':
            if dic['{']<=0:
                tmp=0
                break
            else:
                dic['{']-=1
        elif i=='>':
            if dic['<']<=0:
                tmp=0
                break
            else:
                dic['<']-=1
        else:
            dic[i]+=1
    if i in dic:
        if dic[i]!=0:
            tmp=0
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))