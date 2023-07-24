res=[]
for m in range(int(input())):
    tmp=""
    li=list(map(int,input().split()))
    li.sort()
    li[0],li[-1]=0,0
    tmp=sum(li)/(len(li)-2)
    if tmp%1>=0.5:
        tmp=int(tmp)+1
    else:
        tmp=int(tmp)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))