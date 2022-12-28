res=[]
li=[0,1,1,1,2,2]
for i in range(6,101):
    li.append(li[i-1]+li[i-5])
for m in range(int(input())):
    tmp=0
    N=int(input())
    tmp=li[N]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))