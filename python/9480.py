def apd(word):
    ress=set()
    for i in word:
        if ord(i)>=97 and ord(i)<=122:
            ress.add(i)
    return ress

def dfs(sets,idx):
    global cnt
    if idx==N:
        return
    if len(sets|words[idx])==26:
        cnt+=1
    visit[idx]=True
    dfs(sets|words[idx],idx+1)    
    visit[idx]=False
    dfs(sets,idx+1)

res=[]
for m in range(int(input())):
    cnt=0
    N=int(input())
    words=[]
    for i in range(N):
        words.append(apd(input()))

    visit=[0]*(N+1)
    dfs(set(),0)
    res.append(cnt)
    
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))