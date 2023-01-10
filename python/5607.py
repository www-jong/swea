res=[]
fac=[0]*(1000001)
fac[1]=1
MOD=1234567891
def powcal(num,p):
    if p==0:
        return 1
    half=powcal(num,p//2)
    if p%2==0:
        return ((half%MOD)*(half%MOD))%MOD
    else:
        return (((half*num)%MOD)*(half%MOD))%MOD

for i in range(2,1000000):
    fac[i]=fac[i-1]*i%MOD
for m in range(int(input())):
    tmp=0
    N,R=map(int,input().split())
    n=1
    for i in range(1,N+1):
        n*=i
    top=fac[N]%MOD
    down=((fac[N-R]%MOD)*(fac[R]%MOD))%MOD
    down_to_top=powcal(down,MOD-2)
    tmp=(top*down_to_top%MOD)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
-모듈러 연산
a mod b = c --> a를 b로 나누었을 때 나머지가 c
모듈러는 나눗셈을 제외한 +,-,*에 대해 다음과 같은 특징을 가짐
(a mod n + b mod n) mod n = (a+b) mod n
(a mod n - b mod n) mod n = (a-b) mod n
(a mob n * b mod n) mod n = (a*b) mod n

- 합동관계
두 a,b 숫자가 n 을 mod한 결과값이 같으면 모듈러 합동관계라 할 수 있음
즉, a mob n = b mod n  --> a ≡ b (mod n) [a를 n으로 나누었을 때 나머지가 b]

- 페르마 소정리
p가 소수이고 a가 p로 나누어지지 않는 정수(서로소)이면 다음과 같은 특징을 가짐
a^p ≡ a (mod p)
a^(p-1) ≡ 1 (mod p)
a^(p-2) ≡ a^-1 (mod p)

- 예시
7C5 mod 13 (7C5를 13으로 나누었을 때 나머지 구하기)를 할 경우,
7C5 mod 13 = (7! mod 13 / (2! mod 13)*(5! mod 13)) mod 13
=(7! mod 13/ 240 mod 13) mod 13
=(7! mod 13/ 6 mod 13) mod 13
/를 *로 바꿔주기 위해 페르마소정리를 이용
a^(p-2)≡a^-1 (mod p)이므로, 1/6 mod 13 -> 6^(13-2) mod 13
즉, 7C5 mod 13 = (7! mod 13 * 6^11 mod 13) mod 13
같은논리로, NCR mod 1234567891 = N!/(N-R)!*R!

'''