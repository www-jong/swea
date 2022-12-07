res=[]
for m in range(int(input())):
    tmp=""
    maxs=-1
    li=[[0]*16 for i in range(6)]
    for i in range(5):
        words=list(input())
        maxs=max(maxs,len(words))
        for j in range(len(words)):
            li[i+1][j]=words[j]
    for i in range(maxs):
        for j in range(1,6):
            tmp+="" if li[j][i]==0 else li[j][i]
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))