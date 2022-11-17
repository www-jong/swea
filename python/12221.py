ans=[]
for m in range(int(input())):
    tmp=0
    A,B=map(int,input().split())
    if A>=10 or B>=10:
        tmp=-1
    else:
        tmp=A*B
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))