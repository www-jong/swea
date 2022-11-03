ans=[]
for m in range(int(input())):
    tmp=""
    s=int(input())
    tmp=(("1/"+str(s)+" ")*s).rstrip()
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))