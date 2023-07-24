res=[]
for m in range(int(input())):
    print(f'#{m+1}')
    tmp=""
    N=int(input())
    for i in range(N):
        S=list(map(str,input().split()))
        tmp+=S[0]*(int(S[1]))
    idx=0
    for i in range(10,len(tmp),10):
        print(tmp[idx:i])
        idx=i
    if len(tmp)%10!=0:
        print(tmp[idx:])