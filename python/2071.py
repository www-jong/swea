res=[]
for m in range(int(input())):
    tmp=""
    li=list(map(int,input().split()))
    tmp=sum(li)//10
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))