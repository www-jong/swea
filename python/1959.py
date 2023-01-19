res=[]
for m in range(int(input())):
    tmp=-(10**10)
    N,M=map(int,input().split())
    A=[0]+list(map(int,input().split()))
    B=[0]+list(map(int,input().split()))
    N,M=(M,N) if N>M else (N,M)
    A,B=(B,A) if len(A)>len(B) else (A,B)
    print(f'A : {A}')
    print(f'B : {B}')
    for i in range(M-N+1):
        tmp_val=0
        for j in range(1,N+1):
            tmp_val+=A[j]*B[j+i]
            print(f'tmp_val:{tmp_val}, A[j]:{A[j]}, B[j+i]:{B[j+i]} ')
        tmp=max(tmp_val,tmp)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))