for m in range(int(input())):
    n,s=input().split()
    r=''
    for i in s:
        if i.isnumeric():
            r+=bin(int(i))[2:].zfill(4)
        else:
            r+=bin(ord(i)-55)[2:].zfill(4)
    print(f'#{m+1}',r)