res=[]
li=[0,1]
for i in range(1,300):
    li.append(li[-1]+i)
for m in range(int(input())):
    tmp=0
    p,q=map(int,input().split())
    x1,x2,y1,y2=0,0,0,0
    for i in range(1,300):
        if p<li[i]:
            y1=i-1-(p-li[i-1])
            x1=p-li[i-1]+1
            break
    for i in range(1,300):
        if q<li[i]:
            y2=i-1-(q-li[i-1])
            x2=q-li[i-1]+1
            break
    x3,y3=x1+x2,y1+y2
    tmp=li[y3+(x3-1)]+(x3-1)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))