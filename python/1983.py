res=[]
dd=["DO","C-","C0","C+","B-","B0","B+","A-","A0","A+"]
for m in range(int(input())):
    tmp=""
    N,K=map(int,input().split())
    li=[]
    for i in range(N):
        a,b,c=map(int,input().split())
        li.append([a*0.35+b*0.45+c*0.2,i+1])
    li.sort(key=lambda x:x[0])
    idx=0
    print(li)
    for i,v in li:
        if v==K:
            tmp=dd[idx//(N//10)]
            break
        idx+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

26.1 26.55 17.6