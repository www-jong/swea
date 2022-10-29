ans=[]
so=[2]

n=10**7

for i in range(3,int(n**0.5),2):
    for s in so:
        if not i%s:
            break
    else:
        so.append(i)

for m in range(int(input())):
    tmp=1
    A=int(input())
    if A**0.5 !=int(A**0.5):
        for s in so:
            cnt = 0
            while not A%s:
                A//=s
                cnt+=1
            if cnt%2:
                tmp*=s
            if A==1 or s>A:
                break
        if A>1:
            tmp*=A
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))