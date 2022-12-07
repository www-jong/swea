res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=list(map(str,input().split()))
    if N%2==0:
        for i in range(N//2):
            tmp+=li[i]+" "
            tmp+=li[i+N//2]+" "
    else:
        for i in range(N//2):
            tmp+=li[i]+" "
            tmp+=li[i+N//2+1]+" "
        tmp+=li[N//2]
        
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
123 456

14 25 36


1234 567
1 5 2 6 3 7 4
'''