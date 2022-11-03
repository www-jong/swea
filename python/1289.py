ans=[]
for m in range(int(input())):
    c=0
    N=input()
    tmp="0"*len(N)
    g=0
    for i in N:
        if i=="0":
            g+=1
        else:
            break
    for i in range(g,len(N)):
        if N==tmp:
            break
        else:
            if N[i]==tmp[i]:
                continue
            if N[i]!="0":
                tmp=(tmp[0:i])+"1"*(len(N)-i)
            else:
                tmp=(tmp[0:i])+"0"*(len(N)-i)
            c+=1
    ans.append(c)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))