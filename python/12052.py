res=[]
def check(x,y):
    if x<(N-1) and y<(M-1):
        for i in range(2):
            for j in range(2):
                if li[x+i][y+j]!='#':
                    return False
        return True
    else:
        return False

for m in range(int(input())):
    tmp="YES"
    N,M=map(int,input().split())
    li=[]
    for i in range(N):
        li.append(list(input()))
    for i in range(N):
        for j in range(M):
            if li[i][j]=='#':
                if i<(N-1) and j<(M-1):
                    if check(i,j):
                        for k in range(2):
                            for m in range(2):
                                li[i+k][j+m]='.'
                else:
                    tmp="NO"
                    break
        if tmp=="NO":
            break
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))