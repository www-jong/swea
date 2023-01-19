res=[]
for m in range(int(input())):
    tmp=0
    P,Q,R,S,W=map(int,input().split())
    A=P*W
    B=Q if R>=W else (W-R)*S+Q
    res.append(min(A,B))
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
A사, 1리터랑 P원의 요금
B사, 기본요금 Q원, 월간 R리터이하인 경우, 기본요금. R리터보다 많을경우 추가리터 1리터당 S요금
'''