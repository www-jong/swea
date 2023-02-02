res=[]
for m in range(int(input())):
    tmp=0
    A,B=map(int,input().split())
    M=int('1'+(A-1)*"1"+B*"0",2)
    N=int('1'+B*"0"+(A-1)*"1",2)
    X=bin(M*N)[2:]
    for i in X:
        if i=="1":
            tmp+=1
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))