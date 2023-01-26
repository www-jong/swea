ans=[]
prime_li=[1]*(10001)
for i in range(2,101):
    if prime_li[i]==1:
        for j in range(i*2,10001,i):
            prime_li[j]=0
prime_num=[i for i in range(2,10001) if prime_li[i]==1]

def coprime(a,b):
    for i in prime_num:
        if a%i==0 and b%i==0:
            return False
    return True

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
for m in range(int(input())):
    tmp=""
    A,B=map(int,input().split())
    if not coprime(A,B):
        
    tmp=gcd(A,B)
    
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))
'''
x=(1-By)/A


A,B는 서로소
Ax + By = 1이 되는 x와 y를 구하기

확장 유클리드 방정식을 이용(유클리드 호제법)
ax+ by = c에서 c가 gcd(a,b)<-(a와b의최대공약수)일 경우에만 정수해 x,y를 가짐

두 정수 A, B의 최대공약수(GCD)를 G라고 하면 다음식이 성립
A = aG, B = bG (a와 b는 서로소)
A%B=r, A//B=q (r=나머지,q=몫)이라 하면, A=qB+r을 만족
위 두식을 이용하면 aG = bGq+rr = G(a-qb)

'''