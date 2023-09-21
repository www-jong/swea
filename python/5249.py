def find(a):
    if nodes[a]==a:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

T=int(input())
for case in range(1,T+1):
    V,E=map(int,input().split())
    li=[]
    res=0
    nodes=[i for i in range(V+1)]
    for _ in range(E):
        a,b,c=map(int,input().split())
        li.append((c,a,b))

    li.sort(key=lambda x:x[0])
    for c,a,b in li:
        if find(a)!=find(b):
            res+=c
            union(a,b)
    print(f'#{case}',res)