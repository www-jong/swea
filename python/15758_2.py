res=[]
for m in range(int(input())):
    tmp="yes"
    S,T=map(str,input().split())
    line_S=""
    line_T=""
    count=0
    count_S=0
    count_T=0
    while count<=50:
        if S[count_S]!=T[count_T]:
            tmp="no"
            break
        else:
            count_S=0 if (count_S+1)>=len(S) else count_S
            count_T=0 if (count_T+1)>=len(T) else count_T
            count+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))