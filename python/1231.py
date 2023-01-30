res=[]
def calc(x):
    if x:
        left_val=calc(left[x])
        right_val=calc(right[x])
        return str(left_val)+tree[x]+str(right_val)
    else:
        return ""

for m in range(10):
    tmp=""
    N=int(input())
    tree,left,right=[0]*(N+1),[0]*(N+1),[0]*(N+1)
    for i in range(N):
        S=list(map(str,input().split()))
        tree[int(S[0])]=S[1]
        if len(S)>=3:
            left[int(S[0])]=int(S[2])
        if len(S)>=4:
            right[int(S[0])]=int(S[3])
    tmp=calc(1)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))