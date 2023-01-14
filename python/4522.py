res=[]
for m in range(int(input())):
    tmp="Exist"
    S=input()
    for i in range(len(S)//2 if len(S)%2==0 else len(S)//2+1):
        if S[i]!=S[len(S)-1-i] and (S[i]!="?" and S[len(S)-i-1]!="?"):
            tmp="Not exist"
            break
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))