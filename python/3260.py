res=[]
for m in range(int(input())):
    tmp=sum(list(map(int,input().split())))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))