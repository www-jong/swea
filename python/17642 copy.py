res=[]
for m in range(int(input())):
    tmp=""
    A,B=map(int,input().split())
    B,A=max(A,B),min(A,B)
    if (B-A)==1 or B<A:
        tmp=-1
    else:
        tmp=(B-A)//2
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
