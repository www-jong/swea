res=[]
for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split()) #K=가방한도
    li=[[0]]
    for i in range(N):
        V,C=map(int,input().split())
        li.append([V,C])
    dp=[[[0,0],[0,0]]]*(N+1)
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
N개의 물건
V의 부피한도내 max(C)
i)
dp=[[x,y],...]
dp[1][0]=[k,z] 1번물건을 포함한 최대가치k와 (K를 넘지않은)와 부피z
dp[1][1]= 1번물건을 포함하지 않은 최대가치k(K를 넘지않은)와 부피z

ii)
dp[1]= 부피1일때, 최대value
dp[2]= 부피2일때, 최대value

'''