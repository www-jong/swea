def g(x):
 global y
 if r[x]:g(r[x])
 y+=t[x]
 if l[x]:g(l[x])
for m in range(10):
 t,r,l,y=[0]*101,[0]*101,[0]*101,''
 for i in range(int(input())):
  e=input().split()
  try:
   a=int(e[0])
   t[a]=e[1]
   r[a]=int(e[2])
   l[a]=int(e[3])
  except:pass
 g(1)
 print(f'#{m+1}',y)