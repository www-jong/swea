res=[]
def renew(li):
    t=0
    for i in range(len(li)):
        if li[i]<t:li[i]=t
        else:t=li[i]
    return li

for m in range(int(input())):
    N=int(input())
    li=[]
    for i in range(N):
        li.append(list(map(int,input().split())))
    li.sort(key=lambda x:(x[0],x[1]))
    #print(li)
    dp=[0]*25
    for i in li:
        dp[i[1]]=dp[i[0]]+1
        dp=renew(dp)
    #print(dp)
    res.append(dp[24])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
