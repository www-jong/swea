for m in range(int(input())):
    N,M,K=map(int,input().split())
    li,res,c=sorted(list(map(int,input().split()))),0,0
    for i in li:
        c+=1
        if i//M*K<c:
            res=1
            break

    print(f'#{m+1}',['P','Imp'][res]+'ossible')
