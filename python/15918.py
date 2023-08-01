res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    c={}
    li=list(map(int,input().split()))
    for i in li:
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
    li2=[]
    for k,v in c.items():
        li2.append([k,v])
    li2.sort(key=lambda x:x[0])
    for a,b in li2:
        tmp+=str(a)+":"+str(b)+" "
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))