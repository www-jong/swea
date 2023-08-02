res=[]
for m in range(int(input())):
    tmp=""
    _=int(input())
    N,M,K=map(int,input().split())
    li=[]
    tmp_li=[]
    res=[]
    for i in range(N):
        tmp=list(map(int,input().split()))
        res.append(tmp)
        if i==0:
            li+=tmp
        elif i==N-1:
            li+=tmp[::-1]
        else:
            tmp_li.append(tmp[0])
            li.append(tmp[-1])
    li+=tmp_li[::-1]
    for _ in range(K):
        li.insert(0,li.pop())
    print(f"#{m+1}")
    print(li)
    for i in range(N):
        if i==0:
            print(*li[:M])
        elif i==N-1:
            print(*li[len(li)-(N-2)-1:len(li)-M-(N-2)-1:-1])
        else:
            print(li[i],*res[i][1:-2],end="")
            print(li[M+i-1])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))