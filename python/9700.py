ans=[]
for m in range(int(input())):
    tmp="YES"
    p,q=map(float,input().split())
    if (1-p)*q>=p*q*(1-q):
        tmp="NO"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
s1 = (1-p)*q
s2 = p*q*(1-q)

'''