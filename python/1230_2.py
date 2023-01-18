ans=[]
for m in range(1):
    tmp=''
    N=int(input())
    code=list(map(int,input().split()))
    M=int(input())
    tmp_order=list(map(str,input().split()))
    orders=[]
    tmps=[]
    i=0

    for i in tmp_order:
        if i=='I' or i=='D' or i=='A':
            orders.append(tmps)
            tmps=[]
            tmps.append(i)
        else:
            tmps.append(i)
    orders.pop(0)
    for order in orders:
        if order[1]>10:
            continue
        else:
            if order[0]=='D':
                
    for i in range(10):
        tmp+=str(code[i])+' '
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))