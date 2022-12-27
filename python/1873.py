res=[]
def shoot(x,y,z):
    global maps
    if z==1:
        for i in range(y,0,-1):
            if maps[x][i]=="#":
                break
            if maps[x][i]=="*":
                maps[x][i]="."
                break
    elif z==2:
        for i in range(x,0,-1):
            if maps[i][y]=="#":
                break
            if maps[i][y]=="*":
                maps[i][y]="."
                break
    elif z==3:
        for i in range(y,W+1):
            if maps[x][i]=="#":
                break
            if maps[x][i]=="*":
                maps[x][i]="."
                break
    elif z==4:
        for i in range(x,H+1):
            if maps[i][y]=="#":
                break
            if maps[i][y]=="*":
                maps[i][y]="."
                break

def go_move(x,y,z,order):
    global now,maps
    if order=="U":
        now[2]=2
        maps[x][y]="^"
        if x-1>=0:
            if maps[x-1][y]==".":
                now=[x-1,y,2]
                maps[x][y]="."
                maps[x-1][y]="^"
    if order=="D":
        now[2]=4
        maps[x][y]="v"
        if x+1<=H:
            if maps[x+1][y]==".":
                now=[x+1,y,4]
                maps[x][y]="."
                maps[x+1][y]="v"
    if order=="L":
        now[2]=1
        maps[x][y]="<"
        if y-1>=0:
            if maps[x][y-1]==".":
                now=[x,y-1,1]
                maps[x][y]="."
                maps[x][y-1]="<"

    if order=="R":
        now[2]=3
        maps[x][y]=">"
        if y+1<=W:
            if maps[x][y+1]==".":
                now=[x,y+1,3]
                maps[x][y]="."
                maps[x][y+1]=">"


    
for m in range(int(input())):
    tmp=""
    H,W=map(int,input().split())
    maps=[0]
    now=[0,0,0] # x,y,방향(1:왼,2:위,3:오,4:아래)
    for i in range(H):
        tmpS=[0]+list(input())
        for j in range(len(tmpS)):
            if tmpS[j]=="<":
                now=[i+1,j,1]
                break
            if tmpS[j]=="^":
                now=[i+1,j,2]
                break
            if tmpS[j]==">":
                now=[i+1,j,3]
                break
            if tmpS[j]=="v":
                now=[i+1,j,4]
                break
            
        maps.append(tmpS)
    N=int(input())
    move=input()
    print(now)
    for i in move:
        if i=="S":
            shoot(now[0],now[1],now[2])
        else:
            go_move(now[0],now[1],now[2],i)
    ch=0
    for i in maps:
        if ch==0:
            ch+=1
            continue
        if ch==1:
            print("#%d"%(m+1),end=" ")
            ch=2
        print(*i[1:],sep="")
