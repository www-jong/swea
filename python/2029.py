res=[]
for m in range(int(input())):
    tmp=""
    a,b=map(int,input().split())
    tmp=str(a//b)+" "+str(a%b)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))