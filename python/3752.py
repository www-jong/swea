res=[]
for m in range(int(input())):
    tmp_res=1
    N=int(input())
    li=list(map(int,input().split()))
    sli=list(set(li))
    tmp_res+=len(li)-len(sli)
    tmp_res+=int((len(sli)+1)*(len(sli)/2)) if len(sli)!=1 else 1
    print(f'{len(li)-len(sli)} {int((len(sli)+1)*(len(sli)/2))}')
    res.append(tmp_res)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
2 2 3 5

0
2
3
4
5
7
9
12

'''