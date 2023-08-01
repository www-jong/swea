res=[]

def func(x):
    return 1 if int(x)==0 else 0
for m in range(int(input())):
    tmp=""
    N,M=map(int,input().split())
    li=[]
    for i in range(M):
        li.append(list(map(func,input().split())))
    print(li)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))