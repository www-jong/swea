R,I=range,input
for m in R(10):res,n=0,int(I());l=[I()for _ in R(8)];l.extend([''.join([l[x][y]for x in R(8)])for y in R(8)]);print(f'#{m+1} {sum([1 for x in R(16)for y in R(9-n)if l[x][y:y+n]==l[x][y+n-1:(y-1)if y!=0 else(None):-1]])}')