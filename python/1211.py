res=[]
def go(st):
    global tmp
    x,y=1,st
    count=1
    while x!=100:
        if 1<=y and li[x][y-1]==1:
            while 1<=y and li[x][y-1]==1:
                y-=1
                count+=1
        elif y<=100 and li[x][y+1]==1:
            while y<=100 and li[x][y+1]==1:
                y+=1
                count+=1
        x+=1
        count+=1
    print(f'{x}:{count}')
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
    
    res.append(tmp[0])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))