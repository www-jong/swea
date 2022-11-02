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
    tmpnum=num
    for i in range(c):
        if tmpnum==maxnum:
            if check==1:
                continue
            tmpnum=swap(tmpnum,len(tmpnum)-2,len(tmpnum)-1)
        else:
            minidx=len(tmpnum)-1
            idx=0
            maxnum=tmpnum[minidx]
            while True:
                print('%d %d'%(idx,minidx))
                if minidx==0:
                    break
                if idx==minidx:
                    idx=0
                    minidx-=1
                    continue
                if maxnum>tmpnum[idx]:
                    tmpnum=swap(tmpnum,minidx,idx)
                    print('swap!')
                    break
                idx+=1

    tmp=tmpnum    
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))