res=[]
MAXNUM=1000001
so=[]
li=[1]*(MAXNUM+1)
for i in range(2,MAXNUM):
    if li[i]==1:
        for j in range(i*2,MAXNUM,i):
            li[j]=0
        so.append(i)
print(so)