res=[]
for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split()) #K=가방한도
    li=[[0,0]]
    for i in range(N):
        V,C=map(int,input().split())
        li.append([V,C])
    dp=[[0]*(K+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,K+1):
            if li[i][0]<=j: # 현재 보석의 부피가 현재가방(j)보다 작은경우 
                dp[i][j]=max(dp[i-1][j],li[i][1]+dp[i-1][j-li[i][0]]) # 현재가방(j)의 최대 value는 j가방에서 현재보석을 넣지않은경우, 현재보석을 넣어 j가방무게가 된 경우중 최대값
            else:
                dp[i][j]=dp[i-1][j]
    tmp=dp[N][K]
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
N개의 물건
V의 부피한도내 max(C)
dp[i,j]= i개의 보석이 있고 배낭무게가 j일때 최적value

'''