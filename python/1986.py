res=[]
for m in range(int(input())):
    tmp=0
    N=int(input())
    for i in range(1,N+1):
        if i%2:
            ans = ans + i
        else:
            ans = ans - i
    tmp=ans
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
1 ,-2 ,3 ,-4 5
'''