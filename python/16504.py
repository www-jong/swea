for m in range(int(input())):
    r=int(input())    
    li=list(map(int,input().split()))
    for i in range(1,100):
        li.append([li[0][j] if li[0][j]>=i else 0 for j in range(r)])
    print(li)