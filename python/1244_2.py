res=[]
def change(count):
    global C,ans,tmp
    if count==int(C):
        tmp=''.join(S)
        if int(tmp)>int(ans):
            ans=tmp
        return
    if int(tmp)==int(maxval):
        if (int(C)-count)%2==0:
            ans=maxval
        #else:
        #    ans=maxval[:-2]+maxval[-1]+maxval[-2]
        return
    for i in range(N):
        for j in range(i+1,N):
            S[i],S[j]=S[j],S[i]
            tmp=''.join(S)
            if (tmp,count) not in dic:
                dic[(tmp,count)]=1
                change(count+1)
            S[i],S[j]=S[j],S[i]
    
for m in range(int(input())):
    ans,tmp="0","0"
    S,C=map(str,input().split())
    S=list(S)
    N=len(S)
    maxval=''
    dic={}
    for i in sorted(S,reverse=True):
        maxval+=i
    change(0)
    res.append(ans)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))