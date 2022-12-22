res=[]

def func(li,N,X,yli):
    global tmp
    i=X
    if len(li)==(N):
        tmp+=1
        return
    for j in range(1,N+1):
        ch=0
        if yli[j]:
            if len(li)>=1:
                for x,y in li:
                    
                    for k in range(-N,N):
                        if (x,y)==(i+k,j+k) or (x,y)==(i+k,j-k) or (x,y)==(i-k,j+k) or (x,y)==(i-k,j-k):
                            ch=1
                            break
                    if ch==1:
                        break
            if ch==0:
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
