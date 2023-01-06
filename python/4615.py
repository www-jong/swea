res=[]
def oselo():


for m in range(int(input())):
    tmp=""
    N,M=map(int,input().split())
    li=[[0]*(N+1) for i in range(N+1)]
    for i in range(M):
        x,y,z=map(int,input().split())
        li[x][y]="b" if z==1 else "w"
        oselo(x,y,z)
        
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))