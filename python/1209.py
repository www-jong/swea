def ch(a,b):
    return li[a]-li[b]

ans=[]
for m in range(1,11):
    dd=int(input())
    li=[0]+list(map(int,input().split()))
    tmp=0
    for i in range(3,len(li)-2):
        a,b,c,d=ch(i,i-2),ch(i,i-1),ch(i,i+1),ch(i,i+2)
        if b<=0 and c<=0:
            continue
        if a>0 and b>0 and c>0 and d>0:
            tmp+=min(a,b,c,d)

    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %d"%(i+1,ans[i]))

