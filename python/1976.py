res=[]
for m in range(int(input())):
    tmp=""
    h1,m1,h2,m2=map(int,input().split())
    h=((h1+h2+(m1+m2)//60)%12)+(12 if (h1+h2+(m1+m2)//60)%12==0 else 0)
    tmp=str(h)+" "+str((m1+m2)%60)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))