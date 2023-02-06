res=[]
def go(st):
    global tmp
    x,y=st,1
    count=1
    while x!=100:
        if 2<=y and li[x][y-1]==1:
            while 2<=y and li[x][y-1]==1:
                y-=1
                count+=1
        elif y<=99 and li[x][y+1]==1:
            while y<=99 and li[x][y+1]==1:
                y+=1
                count+=1
        x+=1
        count+=1
    if count<=tmp[1]:
        tmp=[st,count]

for m in range(10):
    tmp=[0,10**9]
    _=input()
    li=[[0]*(101)]
    for i in range(100):
        li.append([0]+list(map(int,input().split())))
    for i in range(1,101):
        if li[1][i]==1:
            go(i)
    
    res.append(tmp[0]-1)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))