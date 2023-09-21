I=lambda:map(int,input().split())
for m in range(*I()):
    N,M,K=map(int,input().split())
    l,r,c=sorted([*map(int,input().split())]),0,0
    for i in l:
        c+=1
        if i//M*K<c:r=1;break
    print(f'#{m+1}',['P','Imp'][r]+'ossible')
