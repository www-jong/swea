res=[]
for m in range(int(input())):
    tmp=""
    S=input()
    H=int(input())
    li=list(map(int,input().split()))
    dic={}
    for i in li:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i in range(len(S)):
        if i in dic:
            tmp+="-"*dic[i]
        tmp+=S[i]
    if len(S) in dic:
        tmp+=dic[len(S)]*"-"
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))