ans=[]
for m in range(int(input())):
    tmp=""
    A,B,C,D=map(int,input().split())
    t=[0]*(101)
    tmp=len(t[max(A,C):min(B,D)])
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))