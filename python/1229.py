res=[]
for m in range(10):
    tmp=""
    N=int(input())
    code=list(map(int,input().split()))
    S=int(input())
    orders=list(map(str,input().split()))
    idx=0
    while idx<len(orders):
        if orders[idx]=='I':
            for i in range(int(orders[idx+2])):
                code.insert(int(orders[idx+1])+i,int(orders[idx+3+i]))
            idx+=int(orders[idx+2])+3
        else:
            del code[int(orders[idx+1]):int(orders[idx+1])+int(orders[idx+2])]
            idx+=3
    for i in range(10):
        tmp+=str(code[i])+" "
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))