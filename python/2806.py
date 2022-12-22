res=[]

def check(li,N):


def func(li,N,X=1):
    global res
    if len(li)==N:
        res+=1
        return
    for i in range(X,N+1):
        for j in range(1,N+1):
            if check(li,N):
                li.append((i,j))
                func(li,N,X+1)
                li.pop()


for m in range(int(input())):
    tmp=""
    res=0    
    N=int(input())
    li=[]
    func(li,N,1)

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
