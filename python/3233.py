res=[]
for m in range(int(input())):
    tmp=0
    A,B=map(int,input().split())
    C=A//B
    for i in range(1,C+1):
        tmp+=(1+(i-1)*2)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))