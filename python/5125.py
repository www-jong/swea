res=[]
def func(i,score,kal):
    global tmp
    if kal>L:
        return
    if score>tmp:
        tmp=score
    if i==N:
        return
    func(i+1,score,kal)
    func(i+1,score+T[i],kal+K[i])
    
    
for m in range(int(input())):
    tmp=0
    N,L=map(int,input().split())
    T=[] #'맛에대한 점수'
    K=[] #'맛에대한 칼로리'
    for i in range(N):
        a,b=map(int,input().split())
        T.append(a)
        K.append(b)
    func(0,0,0)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))