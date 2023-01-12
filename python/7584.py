res=[]

for m in range(int(input())):
    tmp=""
    K=int(input())-1
    while K%2!=0:
        if K%2==1:
            K=(K-1)/2
        if K%2==0:
            if K%4==0:
                tmp="0"
                break
            else:
                tmp="1"
                break
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))