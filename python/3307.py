res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=list(map(int,input().split()))
    dp=[1]*len(li) # dp[i]= i번째에서끝나는 최장길이
    for i in range(1,len(li)):
        for j in range(i):
            if li[j]<li[i]:
                dp[i]=max(dp[j]+1,dp[i])
    print(dp)
    res.append(max(dp))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
    