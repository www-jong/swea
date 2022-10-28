ans=[]
for m in range(int(input())):
    tmp=""
    ans.append(int(input())//3)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))