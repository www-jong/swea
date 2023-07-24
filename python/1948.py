res=[]
dd=[31,28,31,30,31,30,31,31,30,31,30,31]
for m in range(int(input())):
    tmp=""
    a,b,c,d,=map(int,input().split())
    aa=sum(dd[:a-1])+b
    bb=sum(dd[:c-1])+d
    tmp=bb-aa
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))