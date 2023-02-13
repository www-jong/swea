res=[]
for m in range(int(input())):
    tmp=0
    idx=0
    N=int(input())
    li=sorted(list(map(int,input().split())),reverse=True)
    for i in range(len(li)):
        if idx!=2:
            tmp+=li[i]
            idx+=1
        else:
            idx=0
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))