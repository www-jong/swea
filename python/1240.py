dic={'0001101':0,'0011001':1,'0010011':2,'0111101':3,
    '0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
for m in range(int(input())):
    N,M=map(int,input().split())
    li=[input().rstrip('0') for i in range(N)]
    res=0
    x=0
    g=[]
    while x<N:
        if li[x]:
            for i in range(len(li[x]),len(li[x])-56,-7):
                g.append(dic[li[x][i-7:i]])
            break
        x+=1
    print(f'#{m+1}',sum(g) if (sum(g[::2])+sum(g[1::2])*3)%10==0 else 0)