I,h=input,int
for m in range(h(I())):
 n,l=h(I()),[*map(h,I().split())]
 d=[1]*n
 for i in range(1,n):
  if l[i]>l[i-1]:d[i]+=d[i-1]
 print(f'#{m+1}',max(d))