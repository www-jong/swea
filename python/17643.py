I,R,f=input,range,int
def o(n):return''if n==0 else o(n//3)+str(n%3)
def ck(n):
 if n==0:return'0'
 t=str(f(o(n)))
 li,ch=[0]*(len(t)),0
 for i in R(len(t)-1,-1,-1):
  c=t[i]
  if c=='1':
   li[i]='1'
   if ch and i==0:li.insert(0,'1')
  elif c=='0':
   li[i],ch='01'[ch],0
  else:
   li[i],ch='10'[ch],1
   if i==0:li.insert(0,'1')
 return''.join(li)
for m in R(f(I())):
 x,y=map(f,I().split())
 s=o(f(ck(abs(x)),3)+f(ck(abs(y)),3))
 print(f"#{m+1}",'yneos'['2'in s or'0'in s::2])