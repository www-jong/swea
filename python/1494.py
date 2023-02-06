res=[]
def comb(vi,idx,su):
    if su==N/2:
        mat(vi)
        print(vi)
        return
    for i in range(idx,N):
        vi[i]=1
        comb(vi,i+1,su+1)
        vi[i]=0

def mat(vi):
    global tmp
    A=[0,0]
    B=[0,0]
    for i in range(N):
        if vi[i]:
            A[0]+=li[i][0]
            A[1]+=li[i][1]
        else:
            B[0]+=li[i][0]
            B[1]+=li[i][1]
    tmp=min(tmp,(B[0]-A[0])**2+(B[1]-A[1])**2)

for m in range(int(input())):
    tmp=10**15
    N=int(input())
    li=[]
    visit=[]
    for i in range(N):
        li.append(list(map(int,input().split())))
    comb([0]*N,0,0)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
