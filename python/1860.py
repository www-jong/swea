res=[]
for m in range(int(input())):
    tmp="Possible"
    N,M,K=map(int,input().split())
    li=sorted(list(map(int,input().split())))
    
    for i in range(N):
        now_boongs=(li[i]//M)*K
        now_people=i+1
        if now_boongs-now_people<0:
            tmp="Impossible"
            break
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))