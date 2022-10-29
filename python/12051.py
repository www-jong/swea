ans=[]
def fac(x):
    d=2
    n=100
    while d<=x:
        if x%d==0:
            x=x/d
            if n%d==0:
                n=n/d
        else:
            d=d+1
    return n
for m in range(int(input())):
    tmp="Possible"
    N,Pd,Pg=map(int,input().split())
    if Pg==100 and Pd!=100:
        tmp="Broken"
    elif Pg==0 and Pd!=0:
        tmp="Broken"
    elif N<fac(Pd):
        tmp="Broken"
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
all = G
today = D  <= N
tooday win = Pd
all win = Pg
Pd= win/D
Pg= allwin/G

N판 -> 승률 x
ex) 15판 해서 3판 -> 3/d*100=x
즉, Pd * d / 100 == 정수를 만족해야함


'''