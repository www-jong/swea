res=[]
for m in range(int(input())):
    tmp=10**100
    N,A,B=map(int,input().split())
    R=0
    C=0
    CENTER=0
    for i in range(1,318):
        if i**2>N:
            CENTER=i
            break
    for i in range(1,CENTER+1):
        R=i
        C=(N//i)
        tmp=min(tmp,A*abs(R-C)+B*(N-R*C),B*(N-min(i,N//i)**2),A*abs(N-1))
        print(f'R: {R} C: {C} front: {A*abs(R-C)} back{B*(N-R*C)}')
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))
'''
A*|R-C|+B*(N-R*C)
'''