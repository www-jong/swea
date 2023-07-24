from itertools import combinations
a=[0]*985436
c=0
for i in combinations(a,3235):
    c+=1
print(c)