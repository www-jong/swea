res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=[0]*(5)
    while N!=1:
        if N%2==0:N/=2;li[0]+=1
        if N%3==0:N/=3;li[1]+=1
        if N%5==0:N/=5;li[2]+=1
        if N%7==0:N/=7;li[3]+=1
        if N%11==0:N/=11;li[4]+=1
    print(f'#{m+1}',*li)
