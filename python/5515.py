res=[]
for m in range(int(input())):
    tmp=0
    m,d=map(int,input().split())
    dic=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    dic2=[3,4,5,6,0,1,2]
    for i in range(1,m):
        d+=dic[i]
    d%=7
    tmp=dic2[d]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))