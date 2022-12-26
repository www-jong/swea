res=[]
for m in range(int(input())):
    tmp=0
    D,L,N=map(int,input().split())
    for i in range(N):
        tmp+=D*(1+i*L/100)
    res.append(int(tmp))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))