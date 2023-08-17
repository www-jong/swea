for m in' '*10:
 N,l,c,g=int(input()),[*map(int, input().split())],0,1
 while l[c-1]>0:
  l[c]-=g
  g,c=g%5+1,(c+1)%8
 l[c-1]=0
 k=l[c:]+l[:c]
 print(f'#{N}',*k)

