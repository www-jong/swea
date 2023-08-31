for m in range(int(input())):
    N=int(input())
    li=[]
    for i in range(N):
        a,b=map(int,input().split())
        li.append((a,b))
    li.sort(key=lambda x:(-x[0],x[1]))
    res=0
    now=24
    for x,y in li:
        if y<=now:
            res+=1
            now=x
    print(f'#{m+1}',res)
    print(li)