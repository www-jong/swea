ans=[]
for m in range(2):
    tmp=""
    _,n=map(str,input().split())
    c=0
    li=list(n)
    lilen=len(li)
    while c<(lilen-1):
        if li[c]==li[c+1]:
            li.pop(c)
            li.pop(c)
            c-=1
            lilen-=2
        else:
            c+=1
    for i in li:
        tmp+=i
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))