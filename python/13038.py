ans=[]
for m in range(int(input())):
    tmp=0
    n=int(input())
    a=list(map(int,input().split()))
    tt=[32,16,8,4,2,1,0]
    alist=[a.copy()]
    co=0
    tmp=0
    for i in range(6):
        if a[0]==1:
            a.pop(0)
            gg=1
        else:
            a.pop(0)
            gg=0
        a.append(gg)
        alist.append(a.copy())
    tmpmax=[-1,0]
    for i in alist:
        gg=0
        for j in range(7):
            gg+=i[j]*tt[j]
        if gg>tmpmax[0]:
            tmpmax[0]=gg
            tmpmax[1]=i
    a=tmpmax[1]
    week=sum(a)
    if n>co and n>7:
        tmp=max((n//week*7),0)
        n=n%week
    count=0
    
    while True:
        if n==0:
            break
        count=count%7
        if a[count]==1:
            n-=1
        tmp+=1
        count+=1
#print((n-week)/week)
    print(a)
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
14일수때, 1 0 1 1 0 0 0 에서 문제
1 0 1 1 0 0 0 < 1 1 0 0 0 1 0
'''