ans=[]
for m in range(10):
    tmp=0
    _=input()
    N,M=map(int,input().split())
    tmp=N**M
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))