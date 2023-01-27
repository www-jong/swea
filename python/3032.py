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
    x,y=0,1
    u,v=1,0
    while a!=0:
        q,r=b//a,b%a
        m,n=x-u*q,y-v*q
        b,a,x,y,u,v=a,r,u,v,m,n
    return str(x)+" "+str(y)
for m in range(int(input())):
    tmp=""
    A,B=map(int,input().split())
    if not coprime(A,B):
        print(-1)
    else:
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

- 유클리드 호제법
두 양의 정수 a,b (a>b)에 대해 a = bq + r(0<=r<b) 이라 하면, a,b의 최대공약수는 b,r의 최대공약수와 같다
즉,  gcd(a,b) = gcd(b,r)
r = 0 이라면, a,b의 최대공약수는 b가 됨

- 유클리드 호제법(2개의 자연수 혹은 정식의 최대공약수를 구하는 알고리즘) 증명
gcd(a,b) = G, gcd(b,r) G' 이라 하자. 적당한 서로소인 정수 A,B에 대해 a= GA, b=GB가 성립
이를 a = bq + r에 대입하면 GA = GBq + r, r = G(A-Bq)이고, 여기서 G는 b와 r의 공약수이며, G는 G'의 약수임을 알 수 있음
G' = mG로 두자. 그러면 적당한 서로소인 정수 k,l에 대해 GB = G'k = Gmk, G(A-Bq) = G'l = Gml이 성립
양변을 G로 나누면 B = mk, A- Bq = ml이다.
A = ml + Bq = ml  + mkq = m(l+kq) 에서 m은 A,B의 공약수인데, gcd(A,B) = 1 이므로 항상 m = 1이고, G'=G이다.

ex) 1071과 1029의 최대공약수를 구하기
1071은 1029로 나누어 떨어지지 않기 때문에 1071을 1029로 나눈 나머지를 구함 -> 42
1029는 42로 나누어 떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구함 -> 21
42는 21로 나누어 떨어짐 -> 최대공약수 21

- 베주 항등식(Bezout's Identity)
gcd(a,b) = d 라고 할 때,
ax + by = d를 만족하는 정수 x,y가 존재한다.
d는 정수 x,y에 대하여 ax + by로 표현할 수 있는 가장 작은 정수이다.
ax + by로 표현될 수 있는 모든 정수는 d의 배수이다.


- 확장 유클리드 호제법(Extended Euclidean Algorithm)
베주 항등식에 따라 gcd(a,b) = d라고 할 때, ax + by = d를 만족하는 x,y가 존재하며, 이는 유클리드 호제법의 과정을 역으로 따라가면
찾을 수 있다. 따라서 유클리드 호제법의 과정을 따라가 봐야 하며, 두 정수 a,b에 대해 나눗셈 정리와 유클리드 호제법을 반복하면 아래와 같다.
a = bq0+r1
b=r1q1+r2
r1=r2q2+r3

'''