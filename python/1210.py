res=[]
def go(st):
    x,y=1,st
    while x!=100:
        if y>=2 and li[x][y-1]==1:
            while y>=2 and li[x][y-1]==1:
                y-=1
        elif y<=99 and li[x][y+1]==1:
            while y<=99 and li[x][y+1]==1:
                y+=1
        x+=1
    if li[x][y]==2:
        return st
    else:
        return 0

for m in range(10):
    tmp=""
    _=input()
    li=[[0]*(101)]
    for i in range(100):
        li.append([0]+list(map(int,input().split())))
    for i in range(1,101):
        if li[1][i]==1:
            tmp=go(i)
            if tmp!=0:
                break
    
    res.append(tmp-1)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))