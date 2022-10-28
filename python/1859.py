ans=[]
for m in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    nowmaxval=li[-1]
    count=0
    tmp=0
    for i in range(len(li)-2,-1,-1):
        if li[i]>=nowmaxval:
            tmp+=count*nowmaxval
            nowmaxval=li[i]
            count=0
        else:
            count+=1
            tmp-=li[i]
    if count!=0:
        tmp+=count*nowmaxval
    ans.append(tmp)

for i in range(len(ans)):
    print("#%d %d"%(i+1,ans[i]))