for m in range(int(input())):
    P,*a=map(int,input().split());d={}
    for i in a[:]:
        s,t,c=0,P,0
        while s<t:
            m,c=int((s+t)/2),c+1
            if m==i:d.add(c);break
            elif m<i:s=m
            else:t=m
    sorted(list(d));print(f'#{m+1} {d[0]}')