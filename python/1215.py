ans=[]
def check(li):
    for i in range(len(li)-len(li)//2):
        if li[i]!=li[len(li)-i-1]:
            return 0
    return 1
for m in range(10):
    tmp=0
    N=int(input())
    maps=[[0]]
    for i in range(8):
        g=list("0"+input())
        maps.append(g)
    for i in range(1,9):
        for j in range(1,9):
            if j<=(9-N):
                tmp+=check(maps[i][j:j+N])
            if i<=(9-N):
                tmpli=[]
                for p in range(i,i+N):
                    tmpli.append(maps[p][j])
                tmp+=check(tmpli)
    if N==1:
        tmp//=2
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))