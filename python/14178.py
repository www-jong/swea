ans=[]
for m in range(int(input())):
    tmp=0
    N,D=map(int,input().split())
    for i in range(1,N+1):
        if i*(1+2*D)>=N:
            tmp=i
            break
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
(x+2d)*x>=N
'''