res=[]
for m in range(int(input())):
    dis=0
    N=int(input())
    speed=0
    
    for i in range(N):
        li=list(map(int,input().split()))
        if len(li)==2:
            C,G=li[0],li[1]
            speed=speed+G if C==1 else max(0,speed-G)
            dis+=speed
        else:
            dis+=speed
    res.append(dis)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))