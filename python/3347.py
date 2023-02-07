res=[]
for m in range(int(input())):
    tmp=[0,0]
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    vote=[0]*(N)
    for i in B:
        for j in range(N):
            if A[j]<=i:
                vote[j]+=1
                break
    for i in range(N):
        if tmp[0]<vote[i]:
            tmp=[vote[i],i]
    res.append(tmp[1]+1)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))