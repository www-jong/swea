
K,N,M=map(int,input().split())
li=list(map(int,input().split()))
gap=[1 for i in range(M-1) if li[M+1]-li[M]>K]
print(gap)