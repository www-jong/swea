g,I,R="(){}[]",input,range
for m in R(int(I())):
 s=''.join([i for i in I()if i in g])
 for i in R(99):s=s.replace(g[i%3*2:i%3*2+2],'')
 print(f'#{m+1}',[s==''])