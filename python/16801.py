import heapq
res=[]
for m in range(int(input())):
    tmp=""
    N,K=map(int,input().split())
    people=sorted(list(map(int,input().split())))
    food=sorted(list(map(int,input().split())),reverse=True)
    mins=people[0]
    decrease=0
    idx=0
    hp1=[]
    hp2=[]
    for i in range(N):
        if people[i]==mins:
            heapq.heappush(hp2,(people[i]*food[i],people[i],food[i]))
        else:
            if idx==0:
                idx=i
            heapq.heappush(hp1,(people[i]*food[i],people[i],food[i]))
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))