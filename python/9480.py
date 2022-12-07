from collections import deque

res=0

def func(dics,N,alldics):
    global tmp
    if len(dics)==26:
        tmp+=1
        return
    for i in range(1,N+1):
        dics
for m in range(int(input())):
    tmp=0
    dic=[{}]
    N=int(input())
    for i in range(N):
        word=input()
        tmpdic={}
        for i in word:
            if i not in tmpdic:
                tmpdic[i]=1
            else:
                tmpdic[i]+=1
        dic.append(tmpdic)

    
    q=deque()
    q.append(1)
    visit

    res.append(tmp)

for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))