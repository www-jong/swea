def calc(x):
    if tree[x] in "+-*/":
        left_val=calc(left[x])
        right_val=calc(right[x])
        if tree[x]=="+":
            return int(left_val)+int(right_val)
        elif tree[x]=="*":
            return int(left_val)*int(right_val)
        elif tree[x]=="-":
            return int(left_val)-int(right_val)
        else:
            return int(left_val)//int(right_val)
    else:
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
    tmp=calc(1)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))