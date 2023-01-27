res=[]
def check_length(x,y):
    global N
    count=0
    if x-1>=0 and (x+K)<=(N+1):
        if li[x-1][y]==0 and li[x+K][y]==0:

            for i in range(K):
                count+=li[x+i][y]
            if count==K:
                return True
    return False

def check_width(x,y):
    global N
    if y-1>=0 and (y+K)<=(N+1):
        if li[x][y-1]==0 and li[x][y+K]==0:
            if sum(li[x][y:y+K])==K:
                return True
    return False

for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split())
    li=[[0]*(N+2)]
    for i in range(N):
        li.append([0]+list(map(int,input().split()))+[0])
    li.append([0]*(N+2))
    for i in range(1,N+1):
        for j in range(1,N+1):
            if check_length(i,j):
                tmp+=1
            if check_width(i,j):
                tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))