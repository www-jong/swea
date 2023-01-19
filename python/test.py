from itertools import combinations
def solution(answer):
    ans=eval(answer)
    dic={}
    res=1
    for item,code in ans:
        if code not in dic:
            dic[code]=1
        else:
            dic[code]+=1
    li=[]
    for i in dic.keys():
        li.append(dic[i])
        res*=dic[i]+1
    return res-1
