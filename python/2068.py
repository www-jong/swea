res=[]
for m in range(int(input())):
    tmp=""
    li=list(map(int,input().split()))
    tmp=max(li)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))