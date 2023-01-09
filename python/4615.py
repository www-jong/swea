res=[]
def oselo(x,y,z): # z==2 : 백, z==1: 흑
    global li,global_black,global_white
    vec=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for vec_x,vec_y in vec:
        tmpli=[]
        dx=x
        dy=y
        NOW_COLOR=-1
        while NOW_COLOR!=0:
            dx+=vec_x
            dy+=vec_y
            if dx>=len(li[0]) or dy>=len(li[0]) or dx==0 or dy==0:
                break
            NOW_COLOR=li[dx][dy]
            if NOW_COLOR==z:
                for re_x,re_y in tmpli:
                    li[re_x][re_y]=NOW_COLOR
                    if NOW_COLOR==1:
                        global_white-=1
                        global_black+=1
                    else:
                        global_black-=1
                        global_white+=1
                break
            elif NOW_COLOR==0:
                break
            else:
                tmpli.append((dx,dy))




for m in range(int(input())):
    tmp=""
    global_white=2
    global_black=2
    N,M=map(int,input().split())
    li=[[0]*(N+1) for i in range(N+1)]
    li[N//2][N//2]=2
    li[N//2][N//2+1]=1
    li[N//2+1][N//2]=1
    li[N//2+1][N//2+1]=2
    
    for i in range(M):
        x,y,z=map(int,input().split())
        if z==1:
            li[x][y]=1  # b
            global_black+=1
        else:
            li[x][y]=2
            global_white+=1
        oselo(x,y,z)
        for i in li[1:]:
            print(i[1:])
    tmp=str(global_black)+" "+str(global_white)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))