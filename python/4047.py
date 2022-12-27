res=[]
for m in range(int(input())):
    tmp=""
    dic={'S':{},'D':{},'H':{},'C':{}}
    S=input()
    for i in range(0,len(S),3):
        if S[i+1:i+3] not in dic[S[i]]:
            dic[S[i]][S[i+1:i+3]]=1
        else:
            tmp="ERROR"
            break
    if tmp!="ERROR":
        tmp=str(13-len(dic["S"]))+" "+str(13-len(dic["D"]))+" "+str(13-len(dic["H"]))+" "+str(13-len(dic["C"]))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))