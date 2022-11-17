ans=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[[0]*(N+1)]
    for i in range(N):
        tm=input()
        tmpli=[]
        for i in tm:
            tmpli.append(int(i))
        li.append([0]+tmpli)
    for i in range(1,N+1):
        tmp+=sum(li[i][(N//2+1)+1-(i if i<=(N//2+1) else N-i+1):(N//2+2)-1+(i if i<=(N//2+1) else N-i+1)])
        print('%d %d'%((N//2+1)+1-(i if i<=(N//2+1) else N-i+1),(N//2+2)-1+(i if i<=(N//2+1) else N-i+1)))
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))