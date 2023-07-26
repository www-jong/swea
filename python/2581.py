import copy
res=[[],["*"]]
for i in range(2,37):
    if (i-1)%3==0:
        res.append(res[i-1]+res[i-1])
    elif (i-1)%3==1:
        res.append(copy.deepcopy(res[i-1]))
        for j in range(len(res[i-1])):
            res[i][j]+=" *"
    elif (i-1)%3==2:
        res.append(copy.deepcopy(res[i-1]))
        res[i].append("*"*len(res[i][-1]))

for m in range(int(input())):
    print(f'#{m+1}')
    N=int(input())
    print(*res[N],sep="\n")