res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    S1=(N+1)*N//2
    S2=N**2
    S3=(N+1)*N
    tmp=str(S1)+" "+str(S2)+" "+str(S3)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))