def calc(x):
    if x=="x":
        return "x"
    elif tree[x] in "+-*/":
        left_val=calc(left[x])
        right_val=calc(right[x])
        if left_val=="x" or right_val=="x":
            return "x"
        else:
            return 1
    else:
        if left[x] or right[x]:
            return "x"
        return tree[x]
res=[]
for m in range(10):
    tmp=""
    N=int(input())
    tree,left,right=[0]*(N+1),[0]*(N+1),[0]*(N+1)
    for _ in range(N):
        S=list(map(str,input().split()))
        tree[int(S[0])]=S[1]
        if len(S)>=4:
            left[int(S[0])]=int(S[2])
            right[int(S[0])]=int(S[3])
    tmp=0 if calc(1)=="x" else 1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))