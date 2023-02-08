res=[]
def calc(vi):
    global tmp
    tmp2=0
    types='w'
    for i in range(2,N):
        if types=='w' and vi[i]==0:
            tmp2+=(M-li[i][0])
        elif vi[i]==1:
            tmp2+=(M-li[i][1])
            types='b'
        else:
            tmp2+=(M-li[i][2])
    tmp=min(tmp2,tmp)
    
def go(idx,vi,count,stop=0):
    if idx==N:
        if count==0:
            return
        calc(vi)
        return
    if stop!=2:
        vi[idx]=1
        go(idx+1,vi,count+1,1)
    vi[idx]=0
    go(idx+1,vi,count,2 if stop==1 or stop==2 else 0)
    
for m in range(int(input())):
    tmp=10**9
    N,M=map(int,input().split())
    li=[[0,0,0] for i in range(N+1)]
    for i in range(1,N+1):
        S=input()
        for j in S:
            if j=='W':
                li[i][0]+=1
            elif j=='B':
                li[i][1]+=1
            else:
                li[i][2]+=1
    
    go(2,[0]*(N+1),0)
    tmp+=(M-li[1][0])+(M-li[N][2])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))