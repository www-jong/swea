res=[]
for m in range(10):
    tmp=""
    N=int(input())
    code=list(map(int,input().split()))
    S=int(input())
    order=list(map(str,input().split()))
    idx=0
    order_len=len(order)
    while idx<len(order):
        for i in range(int(order[idx+2])):
            code.insert(int(order[idx+1])+i,order[idx+3+i])
            print(f'{order[idx+1+i]} {order[idx+3+i]} ')
        idx=idx+3+int(order[idx+2])
    for i in code[0:10]:
        tmp+=str(i)+" "
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))