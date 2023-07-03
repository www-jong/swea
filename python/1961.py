for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[list(map(int,input().split())) for _ in range(N)]
    resli=[['']*3 for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            resli[i][0]+=str(li[N-1-j][i])
    print(f'#{m+1}')
    for i in range(N):
        print(*resli[i])


'''
123   741
456   852
789   963

'''