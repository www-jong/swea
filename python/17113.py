for i in range(10,1,-2):
    for j in range((10-i)//2):
        print(1+j,end=" ")
    print((str(1+(10-i)//2)+" ")*i,end="")
    for j in range((10-i)//2-1,-1,-1):
        print(1+j,end=" ")
    print()

for i in range(2,11,+2):
    for j in range((10-i)//2):
        print(1+j,end=" ")
    print((str(1+(10-i)//2)+" ")*i,end="")
    for j in range((10-i)//2-1,-1,-1):
        print(1+j,end=" ")
    print()