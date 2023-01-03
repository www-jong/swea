res=[]
for m in range(int(input())):
    tmp=""
    S=input()
    N=S[0]

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
N: 기립박수를 하고 있는 사람이 아무도 없을 때(0명일때) 기립박수를 하는 사람의 수
S[i]= 기립박수를 하고있는 사람이 i-1명이상일 때 박수를 하는 사람의 수
마지막 문자는 0이 아님
'''