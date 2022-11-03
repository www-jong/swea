ans=[]
for m in range(int(input())):
    tmp=0
    L,U,X=map(int,input().split())
    tmp= 0 if L<=X and X<=U else (-1 if X>U else L-X)
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))