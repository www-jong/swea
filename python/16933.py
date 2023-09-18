for m in range(int(input())):
    a,b=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    B=list(map(int,input().split()))
    res=0
    for num in B:
        c=0
        st,end=0,a-1
        while st<=end:
            mid=(st+end)//2
            if A[mid]==num:
                res+=1
                break
            elif num<A[mid]:
                if c==1:
                    break
                end=mid-1
                c=1
            else:
                if c==2:
                    break
                st=mid+1
                c=2
    print(f'#{m+1} {res}')