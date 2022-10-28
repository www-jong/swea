ans=[]
for m in range(int(input())):
    tmp=0
    li=input()
    li2='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(li)):
        if li[i]==li2[i]:
            tmp+=1
        else:
            break
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))