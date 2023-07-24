res=[]

for m in range(int(input())):
    tmp=1.0
    N,R=map(int,input().split())
    for i in range(max(N-R,R)+1,N+1):
        tmp*=i
        tmp%=1234567891
    for i in range(2,min(N-R,R)+1):
        tmp/=i
    tmp%=1234567891
    if N==0:tmp=0
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))