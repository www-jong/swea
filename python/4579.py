res=[]
for m in range(int(input())):
    tmp="Exist"
    S=input()
    for i in range(len(S)//2):
        if S[i]=='*' or S[len(S)-i-1]=='*':
            break
        else:
            if S[i]!=S[len(S)-i-1]:
                tmp="Not exist"
                break
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))