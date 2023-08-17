from collections import deque
U=lambda:map(int,input().split())
for m in range(int(input())):
    N,M=U()
    dic={}
    for i,v in enumerate([*U()]):
        dic[i+1]=v
    wha,i=deque([0]*N),1
    while len(dic)>2:
        s=wha.pop()
        if s:
            dic[s]//=2
            if not dic[s]:
                if s:
                    del dic[s]
                s=i if i<M else -1
                i+=1
        wha.appendleft(s)
    while wha[-1]==-1:wha.pop()
    print(f'#{m+1}',wha.pop()+1)