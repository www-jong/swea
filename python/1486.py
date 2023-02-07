res=[]
def check(height,vi,idx):
    global B,tmp
    if height>=B:
        tmp=min(tmp,height-B)
        print(vi)
        return
    for i in range(idx,N):
        vi[i]=1
        check(height+li[i],vi,i+1)
        vi[i]=0

for m in range(int(input())):
    tmp=200000
    N,B=map(int,input().split())
    li=list(map(int,input().split()))
    visit=[0]*(N)
    check(0,visit,0)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))