res=[]
def to_str(x,y):
    return str(x)+'_'+str(y)
def find_mine(x,y,type=0):
    global li,check_dict
    tmps=0
    if type==0:
        for dx in range(x-1,x+2):
            for dy in range(y-1,y+2):
                if 1<=dx<=N and 1<=dy<=N:
                    if li[dx][dy]=='*':
                        tmps+=1
                    elif to_str(dx,dy) not in check_dict:
                        find_mine(dx,dy,1)
    elif type==1:
        for dx in range(x-1,x+2):
            for dy in range(y-1,y+2):
                if 1<=dx<=N and 1<=dy<=N:
                    if li[dx][dy]=='*':
                        tmps+=1

    li[x][y]=tmps
    check_dict[to_str(x,y)]=1
    if tmps==0 and type==1:
        for dx in range(x-1,x+2):
            for dy in range(y-1,y+2):
                if 1<=dx<=N and 1<=dy<=N:
                    if to_str(dx,dy) not in check_dict:
                        find_mine(dx,dy,1)

for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[[0]]
    check_dict={}
    for i in range(N):
        tmp_li=[0]+list(input())
        for j in range(1,N+1):
            if tmp_li[j]=='*':
                check_dict[to_str(i+1,j)]=1
        li.append(tmp_li)
    for x in range(1,N+1):
        for y in range(1,N+1):
            if to_str(x,y) not in check_dict:
                find_mine(x,y)
                tmp+=1
                print(f'x:{x} y:{y}')
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
02*20
13*31
2*32*
3*311
.*.00
'''