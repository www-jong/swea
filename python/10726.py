res=[]
for m in range(int(input())):
    tmp="ON"
    N,M=map(int,input().split())
    li=str(bin(M))[2:]
    for i in range(len(li)-min(N,len(li)),len(li)):
        if li[i]=="0":
            tmp="OFF"
            break
    if len(li)<N:
        tmp="OFF"
    print(li)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))