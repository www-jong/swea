ans=[]
for m in range(int(input().rstrip())):
    tmp="Y"
    P=input().rstrip()
    Q=input().rstrip()
    co=0
    if P+"a"==Q:
        tmp="N"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))