res=[]
def check(value,upvalue,sets,ch=0):
    count=0
    if ch==0:
        for i in range(value,li[-1]+1,upvalue):
            if i in sets:
                count+=1
            else:
                return -1
        return count
    else:
        se=set()
        for i in range(value,li[-1]+1,upvalue):
            if i in sets:
                se.add(i)
        return se


for m in range(int(input())):
    tmp=0
    N=int(input())
    li=[]
    se={}
    for i in range(N):
        tmpday=(int(input())-1)
        if tmpday==0:
            continue
        li.append(tmpday)
    
    se=set(li)
    print("처리할 배들 : ",se)
    while len(se)!=0:
        if len(se)==1:
            tmp+=1
            break
        idx=0
        nowcount=check(li[idx],li[idx],se)
        if nowcount==-1:
            pass
        maxcount=[li[idx],nowcount]
        se=se-check(0,maxcount[0],se,1)
        li=list(se)
        tmp+=1

        print(f'첫배 : {maxcount[0]}, 처리된 배들 {maxcount[1]}, 남은양 {se}')
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))