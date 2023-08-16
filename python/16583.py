def func(st,end):
    if st==end:
        return st
    mid=(st+end)//2
    le=func(st,mid)
    ri=func(mid+1,end)
    if (li[le],li[ri]) in [(2,1),(3,2),(1,3)]:
        return le
    elif li[le]==li[ri]:
        return min(le,ri)
    else:
        return ri

for m in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    res=func(0,N-1)
    print(f'#{m+1}',res+1)