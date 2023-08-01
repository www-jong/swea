res=[]
for m in range(int(input())):
    tmp=2
    if int(input())%2!=0:
        tmp=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))