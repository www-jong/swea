p,R,I,P=[[1]*10 for _ in' '*10],range,input,print
for i in R(1,10):
 for j in R(1,i+1):p[i][j]=sum(p[i-1][j-1:j+1])
for m in R(int(I())):P(f'#{m+1}\n1');[P(*p[i][:i+2]) for i in R(int(I())-1)]