res=[]

def check(li,x,y,N):
    if len(li)<1:
        return True
    else:
        for i in range(len(li)):
            if x==li[i][0] or y==li[i][1]:
                return False
            for j in range(-7,8):
                if (x,y)==(li[i][0]+j,li[i][1]+j) or (x,y)==(li[i][0]+j,li[i][1]-j) or (x,y)==(li[i][0]-j,li[i][1]+j) or (x,y)==(li[i][0]-j,li[i][1]-j):
                    return False
        return True


def func(li,N,X=1,yli=[]):
    global tmp
    if len(li)==(N):
        tmp+=1
        return
    for i in range(X,N+1):
        for j in range(1,N+1):
            if yli[j]:
                if check(li,i,j,N):
                    li.append((i,j))
                    yli[j]=False
                    func(li,N,X+1,yli)
                    yli[j]=True
                    li.pop()


for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[]
    func(li,N,1,[True]*(N+1))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
