res=[]
for m in range(int(input())):
    tmp=""
    S1,S2=map(str,input().split())
    dp=[[0]*(len(S1)+1) for i in range(len(S2)+1)]

    for i in range(1,len(S2)+1):
        for j in range(1,len(S1)+1):
            if S1[j-1]==S2[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    tmp=dp[-1][-1]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))


'''
lcs 문제,
dp[i][j]= S1[i-1]번째와 S2[j-1]번째 문자까지에서 최대 공통 부분 수열
dp[i[j]는 S1[i-1]과 S2[j-1]이 같을 경우, dp[i-1][j-1]+1, 다를경우 dp[i-1][j]과 dp[i][j-1]중 최대값

'''