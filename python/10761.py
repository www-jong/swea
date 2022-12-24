res=[]
for m in range(int(input())):
    tmp,tmp1,tmp2=0,1,1
    nB,nO=1,1
    Bli=[]
    Oli=[]
    li=list(map(str,input().split()))
    li2=[]
    for i in range(1,len(li),2):
        if li[i]=="B":
            Bli.append(int(li[i+1]))
            li2.append(int(li[i+1]))
        else:
            Oli.append(int(li[i+1]))
            li2.append(-int(li[i+1]))
    print(Bli)
    print(Oli)
    while li2:
        if li2[0]>0:
            tmp+=1
            if nB==Bli[0]:
                Bli.pop(0)
                li2.pop(0)
            else:
                nB=nB+(1 if Bli[0]>nB else -1)
            if Oli:
                if nO>Oli[0]:
                    nO-=1
                elif nO<Oli[0]:
                    nO+=1
        else:
            tmp+=1
            if nO==Oli[0]:
                Oli.pop(0)
                li2.pop(0)
            else:
                nO=nO+(1 if Oli[0]>nO else -1)
            if Bli:
                if nB>Bli[0]:
                    nB-=1
                elif nB<Bli[0]:
                    nB+=1

    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))