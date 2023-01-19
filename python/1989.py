res=[]
for m in range(int(input())):
    tmp=1
    S=input()
    for i in range(len(S)//2):
        if S[i]!=S[len(S)-1-i]:
            tmp=0
            break
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))