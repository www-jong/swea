ans=[]
for m in range(int(input())):
    tmp=""
    S=input()
    e={"a":0,"e":0,"i":0,"o":0,"u":0}
    for i in S:
        if i not in e:
            tmp+=i
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))