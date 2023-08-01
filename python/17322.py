res=[]

def fac(N):
    res=1
    for i in range(2,N+1):
        res=(res*i)%p
    return res
def squ(n,k):
    if k==0:
        return 1
    elif k==1:
        return n
    tmp=squ(n,k//2)
    if k%2==0:
        return tmp*tmp%p
    else:
        return tmp*tmp*n%p
    
for m in range(int(input())):
    tmp=1
    x,y=map(int,input().split())
    if (x+y)%3!=0 or(x>((x+y)//3)*2) or(y>((x+y)//3)*2):
        res.append(0)
        continue
    n=((x+y)//3)
    k=y-n         
    p=1000000007
    top=fac(n)
    bot=fac(n-k)*fac(k)%p


    res.append(top*squ(bot,p-2)%p)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
2,1 1,2 -> 1 ,1        1행

4,2 3,3 2,4 -> 1, 2, 1  2행

6,3 5,4 4,5 3,6 ->1 3 3 1  3행

8,4 7,5 6,6 5,7 4,8  -> 1 4 6 4 1  4행

10,5  9,6 8,7 7,8 6,9 5,10   1 5 10 10 5 1   5행
            

1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1

3
6
9
12
15
'''