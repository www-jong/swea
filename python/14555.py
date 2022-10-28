ans=[]
for m in range(int(input())):
    tmp=0
    t=input()
    check=0
    check2=0
    for i in range(len(t)):
        g=t[i]
        if g=="(":
            check=1
        elif g=="|" and check==1:
            check=0
            tmp+=1
        elif check==1 and g==")":
            check=0
            tmp+=1
        elif check==0 and g==")":
            tmp+=1
    if check==1:
        tmp+=1
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))