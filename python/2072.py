for m in range(int(input())):
    sum=0
    li=list(map(int,input().split()))
    for i in li:
        if i%2!=0:
            sum+=i
    print("#%d %d"%(m+1,sum))