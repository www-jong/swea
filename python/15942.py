res = []
for m in range(int(input())):
    tmp = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    idx = 0
    check = 0
    while True:

        if idx == len(A):
            break
        if A[0]>K:
            tmp=-1
            break
        if K > A[idx]:
            if check == 1:
                K += A.pop(idx)
                check=0
                tmp += 1
            else:
                idx += 1
        elif K==A[idx]:
            K+=A.pop(idx)
            tmp+=1
        else:
            check=1
            idx-=1

    res.append(tmp-1)
for i in range(len(res)):
    print("#%d %s" % (i + 1, res[i]))