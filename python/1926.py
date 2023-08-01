n=int(input())
for i in range(1,n+1):
    c=0
    for j in str(i):
        if int(j)%3==0 and j!="0":
            print("-",end="")
            c=1
    if c==0:
        print(i,end=" ")
    else:
        print(" ",end="")