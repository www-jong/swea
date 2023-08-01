res=[]
for m in range(int(input())):
    N=map(int,input().split())
    li=list(map(int,input().split()))
    res.append(max(li)-min(li))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))