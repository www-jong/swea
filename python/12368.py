ans=[]
for m in range(int(input())):
    tmp=0
    A,B=map(int,input().split())
    tmp=(A+B)%24
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))