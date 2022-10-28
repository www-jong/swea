ans=[]
for m in range(int(input())):
    tmp="impossible"
    N=int(input())
    Nlist=[]
    for i in range(1,10):
        if len(str(N*i))==len(str(N)):
            Nlist.append(sorted(list(str(N*i))))
    print(Nlist)
    
    for i in range(1,len(Nlist)):
        if Nlist[0]==Nlist[i]:
            tmp="possible"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))