ans=[]
for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split())
    li=sorted(list(map(int,input().split())),reverse=True)

    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))