res=[]
for m in range(int(input())):
    tmp=0
    N=input()
    while len(N)>1:
        tmp=0
        for i in N:
            tmp+=int(i)
        N=str(tmp)
    tmp=N
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))