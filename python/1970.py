res=[]
for m in range(int(input())):
    tmp=""
    print(f'#{m+1}')
    N=int(input())
    for i in [50000,10000,5000,1000,500,100,50,10]:
        if N//i>=1:
            print(N//i,end=" ")
            N=N-i*(N//i)
        else:
            print(0,end=" ")
    print()
