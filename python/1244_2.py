ans=[]
def tolist(num):
    
    return list(num)
def tostr(li):
    return ''.join(str(i) for i in li)

def swap(num,a,b):
    tmpli=tolist(num)
    tmpli[a],tmpli[b]=tmpli[b],tmpli[a]
    return tostr(tmpli)
for m in range(int(input())):
    tmp=""
    num,c=map(int,input().split())
    num=str(num)
    maxnum=''.join(str(i) for i in sorted(list(str(num)),reverse=True))
    check=1 if len(set(list(num)))!=len(list(num)) else 0
    idxlist=[]
    tmpnum=num
    for i in maxnum:
        for j in range(len(num)):
            if num[j]==i and j not in idxlist and num[j]!=maxnum[j]:
                idxlist.append(j)
                break
    for i in range(c):
        if tmpnum==maxnum:
            if check==1:
                continue
            tmpnum=swap(tmpnum,len(tmpnum)-2,len(tmpnum)-1)
        else:
            tmpnum=swap(tmpnum,idxlist.pop(),idxlist.pop(0))
            idxlist=[]
            for i in maxnum:
                for j in range(len(num)):
                    if tmpnum[j]==i and j not in idxlist and tmpnum[j]!=maxnum[j]:
                        idxlist.append(j)
                        break
    #print(tmpnum)
    ans.append(tmpnum)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))