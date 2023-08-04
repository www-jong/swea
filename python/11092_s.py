i=input
for m in range(int(i())):N=int(i());l=[*map(int,i().split())];print(f'#{m+1} {abs(N-l[::-1].index(max(l))-l.index(min(l)))}')
    