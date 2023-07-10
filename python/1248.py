from collections import deque
res=[]

def find(a,val=[],dic={}):
    if nodes[a]==a:
        if nodes[a] not in dic:
            dic[nodes[a]]=1
        return a,[nodes[a]]+val,dic
    else:
        nodes[a],val,dic=find(nodes[a],val,dic)
        if a not in dic:
            dic[a]=1
        return nodes[a],[a]+val,dic

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

def tree_count(N):
    count=0
    if left_tree[N]!=0:
        count+=tree_count(left_tree[N])+1
    if right_tree[N]!=0:
        count+=tree_count(right_tree[N])+1
    return count
for m in range(int(input())):
    tmp=[0,0]
    V,E,A,B=map(int,input().split())
    nodes=[i for i in range(V+1)]
    li=[]
    left_tree=[0]*(V+1)
    right_tree=[0]*(V+1)
    tmp_li=list(map(int,input().split()))
    for i in range(E):
        nodes[tmp_li[i*2+1]]=tmp_li[i*2]
        if left_tree[tmp_li[i*2]]==0:
            left_tree[tmp_li[i*2]]=tmp_li[i*2+1]
        else:
            right_tree[tmp_li[i*2]]=tmp_li[i*2+1]

    A_mom,A_moms,A_dic=find(A)
    B_mom,B_moms,B_dic=find(B)
    for i in B_moms:
        if i in A_moms:
            tmp[0]=i
            break
    tmp[1]=tree_count(tmp[0])+1
    res.append(str(tmp[0])+" "+str(tmp[1]))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))