res=[]
for m in range(int(input())):
    tmp=0
    X=int(input())
    li=[{1,2,5},{10,20,25,50},{100,125,200,250,500}]
    for i in li[0]:
        if i<=X:
            tmp+=1
    for i in li[1]:
        if i<=X:
            tmp+=1
    for i in li[2]:
        if i<=X:
            tmp+=1
    if X>=1000:
        tmp+=5*(len(str(X))-4)
        for i in li[2]:
            if i*(10**(len(str(X))-3))<=X:
                tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))