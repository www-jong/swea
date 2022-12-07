res=[]
for m in range(int(input())):
    tmp=""
    S=list(input())
    tmpdic={}
    for i in range(len(S)):
        if S[i] not in tmpdic:
            tmpdic[S[i]]=i
        else:
            S[tmpdic[S[i]]]=""
            del tmpdic[S[i]]
            S[i]=""
    S.sort()
    for i in S:
        tmp+=i
    if tmp=="":
        tmp="Good"
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))