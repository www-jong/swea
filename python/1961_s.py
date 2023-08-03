R,I,P=range,input,print
for m in R(int(I())):
 N=int(input());l=[list(map(int,I().split()))for _ in R(N)];r=[[l[j][i]for j in R(N)]for i in R(N)];P(f"#{m + 1}")
 for i in R(N):P(*r[i][::-1],' ',*l[-1-i][::-1],' ',*r[-1-i],sep="")