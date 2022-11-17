ans=[]
for m in range(2):
    tmp=0
    _=input()
    check=input()
    li=input()
    ch=0
    for i in li:
        if i==check[0] and ch==0:
            ch=1
        elif ch!=0:
            if i==check[ch]:
                ch+=1
            else:
                if i==check[0]:
                    ch=1
                else:
                    ch=0
        if ch==len(check):
            tmp+=1
            ch=0
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))