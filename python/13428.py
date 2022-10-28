ans=[]
for m in range(int(input())):
    tmp=[]
    N=list(str(int(input())))
    if len(N)==1 and N[0]==0:
        tmp.append("0 0")
        continue
    Nmax=-1
    Nmin=10
    Nmaxlo=-1
    Nminlo=-1
    Nsormax=sorted(N,reverse=True)
    Nsormin=sorted(N)
    Nsorzeromin='d'
    for i in range(len(N)):
        if int(N[i])>Nmax and N[i]!=Nsormax[i]:
            Nmax=int(N[i])
            Nmaxlo=i
        if int(N[i])<Nmin and N[i]!=Nsormin[i]:
            Nmin=int(N[i])
            Nminlo=i
    Nsormax=''
    Nsormin=''
    co=0
    for i in range(len(N)):
        if int(N[i])<Nmax and co==0:
            Nsormax=Nsormax+str(Nmax)
            Nmax=int(N[i])
            co=1
        elif co==1 and i==Nmaxlo:
            co=-1
            Nsormax=Nsormax+str(Nmax)
        else:
            Nsormax=Nsormax+N[i]
    co=0
    print('Nmin %d Nminlo %d'%(Nmin,Nminlo))
    for i in range(len(N)):
        if int(N[i])>Nmin and co==0:
            if Nmin==0 and i==0:
                Nsormin=Nsormin+N[i]
                continue
            Nsormin=Nsormin+str(Nmin)
            Nmin=int(N[i])
            co=1
        elif co==1 and i==Nminlo:
            co=-1
            Nsormin=Nsormin+str(Nmin)
        else:
            Nsormin=Nsormin+N[i]
    tmp=Nsormin+" "+Nsormax
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))