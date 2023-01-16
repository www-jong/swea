res=[]
for m in range(int(input())):
    tmp=-1001
    N=int(input())
    li=[0]+list(map(int,input().split()))
    dp=[[0,0] for i in range(N+1)]
    dp[0][0]=-1001
    dp[0][1]=-1001
    for i in range(1,N+1):
        dp[i][0]=max(li[i],li[i]+dp[i-1][0])
        dp[i][1]=max(dp[i-1][0],dp[i-1][1])
        tmp=max(tmp,dp[i][0],dp[i][1])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
dp[i][0]= i번째를 포함하는 최대합,
dp[i][1]= i번째를 포함하지 않는 최대합
'''