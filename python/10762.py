res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=sorted(list(map(int,input().split())))

    for i in li:
        tmp^=i
    if tmp!=0:
        tmp="NO"
    else:
        tmp=sum(li[1:])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))