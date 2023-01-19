ans=[]
for m in range(10):
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
        if order[0]=='I':
            for i in range(int(order[2])):
                code.insert(int(order[1])+i,order[3+i])
        elif order[0]=='D':
            del code[int(order[1]):int(order[1])+int(order[2])]
        elif order[0]=='A':
            for i in order[2:]:
                code.append(i)
    for i in range(10):
        tmp+=str(code[i])+' '
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))