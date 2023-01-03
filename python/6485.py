res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=[0]*5001
    for i in range(N):
        A,B=map(int,input().split())
        for j in range(A,B+1):
            li[j]+=1
    P=int(input())
    for i in range(P):
        tmpnum=int(input())
        tmp+=" "+str(li[tmpnum])
    tmp=tmp[1:]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))