res=[]


for m in range(int(input())):
    tmp=10**13
    N=int(input())
    for i in range(1,int(((N**(0.5))//1))+1):
        if N%i==0 and tmp>i+N//i:
            tmp=i+N//i
    res.append(tmp-2)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))