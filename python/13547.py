ans=[]
for m in range(int(input())):
    tmp="NO"
    S=input()
    co=0
    for i in S:
        if i=="o":
            co+=1
    if (15-len(S))+co>=8:
        tmp="YES"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))