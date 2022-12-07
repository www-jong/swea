res=[]
for m in range(int(input())):
    tmp=""
    S=set(list(input()))
    if len(S)==2:
        tmp="Yes"
    else:
        tmp="No"
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))