R=range
for m in R(int(input())):
    N=int(input())
    li=[list(map(int,input().split())) for _ in R(N)]
    resli=[['']*3 for _ in R(N)]
    for i in R(N):
        for j in R(N):
            resli[i][0]+=str(li[N-1-j][i])
            resli[i][1]+=str(li[N-1-i][N-1-j])
            resli[i][2]+=str(li[j][N-1-i])
    print(f'#{m+1}')
    for i in R(N):
        print(*resli[i])