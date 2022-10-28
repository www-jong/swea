ans=[]
for _ in range(int(input())):
    tmp="possible"
    N,M=map(int,input().split())
    maps=[["0"*(M+1)]]
    for i in range(N):
        maps.append(list("0"+input()))
    check=0
    
    for x in range(1,N+1):
        for y in range(1,M+1):
            if maps[x][y]==".":
                if y%2!=0:
                    check=1
                break
            elif maps[x][y]=="#":
                check=2
                break
    for x in range(1,N+1):
        for y in range(1,M+1):
            if check==1:
                if x%2==0 and y%2==0 and maps[x][y]!="#":
                    tmp="impossible"
                    break
            elif check==2:
                if x%2==0 and y%2==0 and maps[x][y]!=".":
                    tmp="impossible"
                    break
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))
