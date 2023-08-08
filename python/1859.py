I=input
for m in range(int(I())):
 _,l,r=I(),[*map(int,I().split())][::-1],0;x=l[0]
 for i in l[1:]:
  if x>i:r+=x-i
  else:x=i
 print(f'#{m+1}',r)