res=[]
for m in range(int(input())):
    tmp=""
    S,T=map(str,input().split())
    set_S=[]
    set_T=[]
    for i in S:
        set_S.append(i)
    set_S=set(set_S)
    for i in T:
        set_T.append(i)
    set_T=set(set_T)
    
    if S==T:
        tmp="yes"
    else:
        if set_S!=set_T:
            tmp="no"
        elif
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))