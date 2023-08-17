U=lambda:map(int,input().split())
for m in range(int(input())):
 N,M=U()
 M%=N
 print(f'#{m+1}',[*U()][M])