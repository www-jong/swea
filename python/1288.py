res=[]
for m in range(int(input())):
    tmp=0
    dic={}
    N=input()
    i=1
    while len(dic)!=10:
        for num in str(i*int(N)):
            if num not in dic:
                dic[num]=1
        print(N)
        i+=1
    print(f'{N}, {i}')
    res.append(i)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))