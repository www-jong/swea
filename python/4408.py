for m in range(int(input())):
    N=int(input())
    li=[0]*401
    for i in range(N):
        a,b=sorted(map(int,input().split()))
        for j in range(((a-1)//2)*2+1,(b+1)//2*2+1):
            li[j]+=1
    print(f'#{m+1}',max(li))