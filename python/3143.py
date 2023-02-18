res=[]
for m in range(int(input())):
    tmp=0
    A,B=input().split()
    idx=0
    while idx<len(A):
        if A[idx]==B[0]:
            if A[idx:len(B)+idx]==B:
                tmp+=1
                idx+=len(B)
            else:
                tmp+=1
                idx+=1
        else:
            tmp+=1
            idx+=1

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))