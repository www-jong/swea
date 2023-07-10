import sys
sys.setrecursionlimit(10**9)
res=[]

def get_dist(li):
    global tmp
    tmp_cost=get_cost(company,customers[li[0]])+get_cost(home,customers[li[-1]])
    for m in range(N-1):
        tmp_cost+=get_cost(customers[li[m]],customers[li[m+1]])
    tmp=min(tmp,tmp_cost)
    
def get_cost(start,end):
    return abs(start[0]-end[0])+abs(start[1]-end[1])
 
def btk(now_order):
    if len(now_order)==N:
        get_dist(now_order)
        return
    for k in range(N):
        if visit[k]==False:
            visit[k]=True
            btk(now_order+[k])
            visit[k]=False
for _ in range(int(input())):
    tmp=10**10
    N=int(input())
    tmp_li=list(map(int,input().split()))
    company=tmp_li[:2]
    home=tmp_li[2:4]
    customers=[]
    homes=[]
    for i in range(2,N+2):
        x=tmp_li[i*2]
        y=tmp_li[i*2+1]
        customers.append([x,y])
    visit=[False]*(N)
    btk([])
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))