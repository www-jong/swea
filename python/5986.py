res=[]
MAXNUM=1000
so=[]
sodic={}
li=[1]*(MAXNUM+1)
for i in range(2,MAXNUM):
    if li[i]==1:
        for j in range(i*2,MAXNUM,i):
            li[j]=0
        so.append(i)
        sodic[i]=1
for m in range(int(input())):
    tmp=0
    N=int(input())
    if N/3%1==0 and sodic[N//3]:
        tmp+=1
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))