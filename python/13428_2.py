ans=[]
def tostring(li):
    ttmp=""
    for i in li:
        ttmp+=i
    return ttmp

for m in range(int(input())):
    tmp=[]
    Nmin=''
    Nmax=''
    tt=input()
    if tt=="0":
        tmp='0 0'
        ans.append(tmp)
        continue
    N=list(str(int(tt)))
    Nlist=[tostring(N)]
    for i in range(len(N)):
        for j in range(i+1,len(N)):
            tmp=N.copy()
            tmp[i]=N[j]
            tmp[j]=N[i]
            Nlist.append(tostring(tmp))

    Nlist.sort()
    Nmax=Nlist[-1]
    for i in Nlist:
        if i[0]!='0':
            Nmin=i
            break
    tmp=Nmin+" "+Nmax
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))