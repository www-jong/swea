for m in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    li.sort()
    if li[-1]!=li[-2] and sum(li[:len(li)-1])+2<=li[-1]:
        print(f"#{m+1} {(sum(li)//2)-(li[-1]-sum(li[:len(li)-1]))//2}")
    else:
        print(f"#{m+1} {sum(li)//2}")