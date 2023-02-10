res=[]
for m in range(int(input())):
    tmp=0
    S=input()
    stick=0
    idx=0
    while idx<len(S)-1:
        if S[idx]=="(" and S[idx+1]==")":
            tmp+=stick
            idx+=1
        elif S[idx]=="(":
            stick+=1
            tmp+=1
        else:
            stick-=1
        idx+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))