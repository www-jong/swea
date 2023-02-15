res=[]
for m in range(int(input())):
    tmp=0
    S=input()
    dic={'c':0,'r':0,'o':0,'a':0,'k':0}
    for i in S:
        if dic['k']<dic['a'] or dic['a']<dic['o'] or dic['o']<dic['r'] or dic['r']<dic['c']:
            tmp=-1
            break
        if i=='c':
            dic[i]+=1
        elif i=='r':
            dic[i]+=1
        elif i=='o':
            dic[i]+=1
        elif i=='a':
            dic[i]+=1
        elif i=='k':
            dic[i]+=1
            
    if tmp!=-1:

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))