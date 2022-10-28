ans=[]
for _ in range(int(input())):
    tmp="possible"
    N,M=map(int,input().split())
    maps=[["0"*(M+1)]]
    for i in range(N):
        maps.append(list("0"+input()))
    check=0
    check2=0
    for x in range(1,N+1):
        for y in range(1,M+1):
            if maps[x][y]==".":
                if (x%2!=0 and y%2!=0) or (x%2==0 and y%2==0):
                    check=1
                else:
                    check=2
                break
            elif maps[x][y]=="#":
                if (x%2!=0 and y%2!=0) or (x%2==0 and y%2==0):
                    check=2
                else:
                    check=1
                break
    for x in range(1,N+1):
        if check2==1:
            break
        for y in range(1,M+1):
            if check==1:
                if (((x%2!=0 and y%2!=0) or (x%2==0 and y%2==0)) and maps[x][y]=="#") or \
                (((x%2!=0 and y%2==0) or (x%2==0 and y%2!=0)) and maps[x][y]=="."):
                    tmp="impossible"
                    check2=1
                    break
            elif check==2:
                if (((x%2!=0 and y%2!=0) or (x%2==0 and y%2==0)) and maps[x][y]==".") or \
                    (((x%2!=0 and y%2==0) or (x%2==0 and y%2!=0)) and maps[x][y]=="#"):
                    tmp="impossible"
                    check2=1
                    break
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))
