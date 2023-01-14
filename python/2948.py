res=[]
for m in range(int(input())):
    tmp=0
    N,M=map(int,input().split())
    A=set(list(map(str,input().split())))
    B=set(list(map(str,input().split())))
    tmp=len(A)-len(A-B)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))