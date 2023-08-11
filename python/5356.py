R=range
for m in R(int(input())):
 i=[input()+'_'*15 for _ in R(5)]
 print(f'#{m+1}',''.join(i[y][x]for x in R(15)for y in range(5)if i[y][x]!='_'))