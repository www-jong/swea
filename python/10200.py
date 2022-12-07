ans=[]
for m in range(int(input())):
    tmp=""
    N,A,B=map(int,input().split())
    tmp+=str(min(A,B))+" "+str(max(0,A+B-N))
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))