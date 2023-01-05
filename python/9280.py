res=[]
for _ in range(int(input())):
    tmp=""
    n,m=map(int,input().split())
    Rli=[0]
    for i in range(n):
        Rli.append(int(input()))
        
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))