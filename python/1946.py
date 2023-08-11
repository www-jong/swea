R,I=range,input
for m in R(int(I())):
 print(f'#{m+1}');r=''
 for i in R(int(I())):a,b=I().split();r+=a*int(b)
 [print(r[i:min(i+10,len(r))]) for i in R(0,len(r),10)]