ans=[]
for m in range(int(input().rstrip())):
    tmp="Y"
    P=input().rstrip()
    Q=input().rstrip()
    co=0
    for i in range(len(P)):
        if ord(P[i])>ord(Q[i]):
            tmp="N"
            break
        elif ord(P[i])<ord(Q[i]):
            break
        co+=1
    if Q[0:len(P)]==P and (len(Q)-len(P))==1 and Q[-1]=='a':
        tmp="N"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))