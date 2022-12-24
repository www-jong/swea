res=[]
for m in range(int(input())):
    tmp=0
    D,H,M=map(int,input().split())
    M+=H*60+D*24*60
    ans=11+11*60+11*60*24
    tmp=-1 if M-ans<0 else M-ans
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))