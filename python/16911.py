for m in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    dp=[[[10**10]*3 for _ in range(3)] for _ in range(n)]
    dp[0]=[[li[0],0,0],[0,li[0],0],[0,0,li[0]]]
    for i in range(1,n):
        for j in range(3):
            if j==0:
                c1=dp[i-1][1][1]+dp[i-1][1][2]+max(dp[i-1][1][0],li[i])
                c3=dp[i-1][2][1]+dp[i-1][2][2]+max(dp[i-1][2][0],li[i])
                if c1<c3:
                    dp[i][j]=[max(dp[i-1][1][0],li[i]),dp[i-1][1][1],dp[i-1][1][2]]
                else:
                    dp[i][j]=[max(dp[i-1][2][0],li[i]), dp[i-1][2][1],dp[i-1][2][2]]
            elif j==1:
                c1=dp[i-1][0][0]+dp[i-1][0][2]+max(dp[i-1][0][1],li[i])
                c3=dp[i-1][2][0]+dp[i-1][2][2]+max(dp[i-1][2][1],li[i])
                if c1<c3:
                    dp[i][j]=[dp[i-1][0][0],max(dp[i-1][0][1],li[i]),dp[i-1][0][2]]
                else:
                    dp[i][j]=[dp[i-1][2][0],max(dp[i-1][2][1],li[i]),dp[i-1][2][2]]
            else:
                c1=dp[i-1][0][0]+dp[i-1][0][1]+max(dp[i-1][0][2],li[i])
                c3=dp[i-1][1][0]+dp[i-1][1][1]+max(dp[i-1][1][2],li[i])
                if c1<c3:
                    dp[i][j]=[dp[i-1][0][0],dp[i-1][0][1],max(dp[i-1][0][2],li[i])]
                else:
                    dp[i][j]=[dp[i-1][1][0],dp[i-1][1][1],max(dp[i-1][1][2],li[i])]
    res=10**10
    print(dp)
    for i in dp[n-1]:
        res=min(res,sum(i))
    t=[0,0]
    for i in range(n):
        if i%2==0 and t[0]<li[i]:t[0]=li[i]
        elif i%2!=0 and t[1]<li[i]:t[1]=li[i]
    res=min(res,sum(t))
    print(f'#{m+1}',res)