for m in range(int(input())):
 s=[*input().split()]
 S,r=[],'error'
 try:
  for i in s:
   if i.isdigit():
    S+=[int(i)]
   if i=="+":S+=[S.pop()+S.pop()]
   if i=="-":S+=[-S.pop()+S.pop()]
   if i=="*":S+=[S.pop()*S.pop()]
   if i=="/":
    b=S.pop()
    S+=[S.pop()//b]
   if i=="." and len(S)==1:r=S.pop()
 except:pass
 print(f'#{m+1}',r)