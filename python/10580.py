res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[]
    for _ in range(N):
        a,b=map(int,input().split())
        for fir,end in li:
            if (fir<=a and b<=end) or (a<=fir and end<=b):
                tmp+=1
        li.append((a,b))
                
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))