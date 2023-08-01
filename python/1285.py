res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    re=[10000000,0]
    li=list(map(int,input().split()))
    for i in li:
        if abs(i)<re[0]:
            re=[abs(i),1]
        elif abs(i)==re[0]:
            re[1]+=1
    tmp=str(re[0])+" "+str(re[1])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))