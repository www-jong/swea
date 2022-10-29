ans=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    loc=[]
    checker=[i*i for i in range(0,201,20)]
    for i in range(N):
        x,y=map(int,input().split())
        cir=((x*x+y*y))
        for j in range(1,11):
            if cir<=checker[j]:
                tmp+=11-j
                break
    ans.append("#"+str(m+1)+" "+str(tmp))
print(*ans,sep="\n")