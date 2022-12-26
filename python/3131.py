res=[]
for m in range(int(input())):
    tmp="Yes"
    dic={}
    for i in range(1,10):
        for j in range(1,10):
            if i*j not in dic:
                dic[i*j]=1
    N=int(input())
    if N not in dic:
        tmp="No"
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))