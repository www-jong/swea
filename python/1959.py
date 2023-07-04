res=[]
for m in range(int(input())):
    tmp=-(10**10)
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    if M>=N:
        for i in range(M-N+1):
            tmp2=0
            for j in range(N):
                tmp2+=A[j]*B[j+i]
            tmp=max(tmp,tmp2)
    else:
        for i in range(N-M+1):
            tmp2=0
            for j in range(M):
                tmp2+=B[j]*A[j+i]
            tmp=max(tmp,tmp2)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))