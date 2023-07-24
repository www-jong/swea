res=[]
for m in range(int(input())):
    tmp=""
    print(f'#{m+1}')
    N=int(input())
    li=[[0]*(N) for i in range(N)]
    li[0][0]=1
    for i in range(N):
        for j in range(i+1):
            if j==0 or j==i:
                li[i][j]=1
            else:
                li[i][j]=li[i-1][j-1]+li[i-1][j]
            print(li[i][j],end=" ")
        print()
