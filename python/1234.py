R=range
for m in R(10):
 s=input().split()[1]
 for i in R(99):s=s.replace("0123456789"[i%10]*2,'')
 print(f'#{m+1}',s)