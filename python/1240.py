ans=[]
dic={'0001101':0,'0011001':1,'0010011':2,'0111101':3,
    '0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
for m in range(int(input())):
    tmp=""
    N,M=map(int,input().split()) # N,M=세로,가로
    li=[]
    for i in range(N):
        s=input().rstrip('0')
        if len(s)!=0:
            li.append(s)
    print(li)
    code=''
    co=0
    idx=7
    code2=[0]*(8)
    for i in range(len(li[0])-1,-1,-1):
        if co==7:
            code2[idx]=dic[code]
            idx-=1
            code=''
            co=0
        code=li[0][i]+code
        co+=1
    print(code2)
    if (sum(code2[::2])*3+sum(code2[1::2]))%10==0:
        tmp=sum(code2)
    else:
        tmp=0
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
8개숫자
홀수자리합*3 + 짝수자리합 = 10의배수

'''