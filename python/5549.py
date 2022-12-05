ans=[]
for m in range(int(input())):
    tmp="Odd"
    num=input()
    if int(num[-1])%2==0:
        tmp="Even"

    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))