res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=sorted(list(map(int,input().split())))
    for i in li:
        tmp+=str(i)+" "
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))