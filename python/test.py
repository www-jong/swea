for _ in range(int(input())):
    N=int(input())
    res=[0,0]
    li=list(map(int,input().split()))
    dic={}
    for i in li:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i,j in dic.items():
        if j>res[0]:
            res=[j,i]
        elif j==res[0] and i>res[1]:
            res=[j,i]

    print(f'#{N} {res}')