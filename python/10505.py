ans=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=list(map(int,input().split()))
    for i in li:
        if i<=sum(li)/len(li):
            tmp+=1
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))