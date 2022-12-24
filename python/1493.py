res=[]
for m in range(int(input())):
    tmp=""
    p,q=map(int,input().split())
    li=[0,1]
    for i in range(1,200):
        li.append(li[-1]+i)
    x1,x2,y1,y2=0,0,0,0
    for i in range(1,200):
        if p<li[i]:
            y1=i-1
            print('y1 : %d'%(y1))
            for j in range(1,li[i]+1):
                if p==(li[i-1]+j-1):
                    x1=j
                    y1-=(j-1)
                    print('x1 : %d'%(x1))
                    break
            break
    for i in range(1,200):
        if q<li[i]:
            y2=i-1
            print('y2 : %d'%(y2))
            for j in range(1,li[i]+1):
                if q==(li[i-1]+j-1):
                    x2=j
                    y2-=(j-1)
                    print('x2 : %d'%(x2))
                    break
            break
    print("%d,%d : %d,%d"%(x1,y1,x2,y2))
    print(li)
    x3,y3=x1+x2,y1+y2
    print('x3 %d :y3 %d'%(x3,y3))
    tmp=li[y3]+x3
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))