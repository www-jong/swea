res=[]
for m in range(int(input())):
    tmp=""
    li=list(map(int,input().split()))
    tmp=li[len(li)//2]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))