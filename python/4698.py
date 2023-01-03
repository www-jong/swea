res=[]
MAXNUM=1000001
so=[]
li=[1]*(MAXNUM+1)
for i in range(2,MAXNUM):
    if li[i]==1:
        for j in range(i*2,MAXNUM,i):
            li[j]=0
        so.append(i)
for m in range(int(input())):
    tmp=0
    D,A,B=map(int,input().split())
    for i in so:
        if str(D) in str(i) and (A<=i and i<=B):
            tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))