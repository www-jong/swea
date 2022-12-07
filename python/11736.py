res=[]
for m in range(int(input())):
    tmp=0
    _=input()
    li=list(map(int,input().split()))
    di={min(li):0,max(li):0}
    for i in range(1,len(li)-1):
        if li[i]!=min(li[i-1:i+2]) and li[i]!=max(li[i-1:i+2]):
            tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))