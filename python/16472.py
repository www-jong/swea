I=input
for m in range(int(I())):
 t=[]
 for i in I():
  if t and i==t[-1]:t.pop()
  else:t+=[i]
 print(f'#{m+1}',len(t))