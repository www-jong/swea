c=[[i,i+1,i+2] for i in range(8)]
for m in range(int(input())):
    li=list(map(int,input().split()))
    a,b,A,B=[],[],{},{}
    res=0
    for i in range(12):
        if i%2:
            if li[i] not in b:
                b.append(li[i])
            b.sort()
            for j in range(len(b)-2):
                if b[j:j+3] in c:
                    res=2
                    break
            if li[i] not in B:
                B[li[i]]=1
            else:
                B[li[i]]+=1
            if B[li[i]]==3:
                res=2
                break
        else:
            if li[i] not in a:
                a.append(li[i])
            a.sort()
            for j in range(len(a)-2):
                if a[j:j+3] in c:
                    res=1
                    break
            if li[i] not in A:
                A[li[i]]=1
            else:
                A[li[i]]+=1
            if A[li[i]]==3:
                res=1
                break
        if res!=0:
            break
    print(f'#{m+1}',res)