res=[]
for m in range(int(input())):
    tmp=0
    A,B,C=map(int,input().split())
    tmp=C//min(A,B)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))