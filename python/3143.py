for m in range(int(input())):
    a,b=input().split()
    print(f'#{m+1} {len(b.replace(a,""))}')