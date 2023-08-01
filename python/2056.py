res=[]
for m in range(int(input())):
    s=input()
    tmp=s
    if s[4]=="1":
        if s[5]=="1":
            if int(s[6:])>30 or int(s[6:])<1:
                tmp=-1
        elif s[5]=="2":
            if int(s[6:])>31 or int(s[6:])<1:
                tmp=-1
        else:
            tmp=-1
    elif s[4]=="0":
        if s[5] in ["1","3","4","5","7","8"]:
            if int(s[6:])>31 or int(s[6:])<1:
                tmp=-1
        elif s[5]=="2":
            if int(s[6:])>28 or int(s[6:])<1:
                tmp=-1
        elif s[5] in ["4","6","9"]:
            if int(s[6:])>30 or int(s[6:])<1:
                tmp=-1
        else:
            tmp=-1
    else:
        tmp=-1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))