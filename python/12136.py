for m in range(int(input())):
 N=int(input());l=list(map(int, input().split()));a=[l[0]]*N
 for i in range(1, N):a[i]=max(a[i - 1]+l[i],l[i])
 print(max(a))
