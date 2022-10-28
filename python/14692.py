ans=[]
for m in range(int(input())):
    tmp="Bob"
    t=int(input())
    if t%2==0:
        tmp="Alice"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))