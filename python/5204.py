def func(li,n):
    global res
    if len(li)==1:
        return li
    l,r=func(li[:n//2],n//2),func(li[n//2:],n)
    if l[-1]>r[-1]:
        res+=1
    t=[]
    l_idx,r_idx=0,0
    while l_idx<len(l) and r_idx<len(r):
        if l[l_idx]<r[r_idx]:
            t.append(l[l_idx])
            l_idx+=1
        else:
            t.append(r[r_idx])
            r_idx+=1
    t+=l[l_idx:]
    t+=r[r_idx:]
    return t
for m in range(int(input())):
    res=0
    N=int(input())
    li=func(list(map(int,input().split())),N)
    print(f'#{m+1} {li[N//2]} {res}')