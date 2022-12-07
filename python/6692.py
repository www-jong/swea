ans=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    for i in range(N):
        p,x=map(int,input().split())
        tmp+=p*x
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))