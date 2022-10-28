import sys
sys.setrecursionlimit(5000)
def func(n,xsum,ysum,root):
    global glo,tmp
    if len(li[n])==0:
        return
    for B,x,y in li[n]:
        nowsum=(xsum+x)*(ysum+y)
        if B in root:
            continue
        elif B==2:
            if tmp>nowsum:
                tmp=nowsum
        else:
            if nowsum<=tmp:
                func(B,xsum+x,ysum+y,root+[B])
    

for p in range(int(input())):
    try:
        N,M=map(int,input().split())
        li=[[] for i in range(N+1)]
        tmp=10**9
        for i in range(M):
            a,b,c,d=map(int,input().split())
            if a+b==3:
                tmp=c*d
            li[a].append((b,c,d))
            li[b].append((a,c,d))
        root=[1]
        if M!=0:
            func(1,0,0,root)
            if tmp<10**8:
                print('#%d %d'%(p+1,tmp))
            else:
                print('#%d -1'%(p+1))
        else:
            print('#%d -1'%(p+1))
    except:
        print('#%d -1'%(p+1))