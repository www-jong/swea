ans=[]
for m in range(int(input())):
    tmp="possible"
    N,M=map(int,input().split())
    map=[["0"*(M+2)]]
    map.append(list("0"+input()))
    map.append("0"*(M+2))
    check=0
    for g in range(1,N):
        for i in range(1,M+1):
            tmp2=[]
            tmp3=""
            li=[(-1,1),(-1,-1),(1,-1),(1,1)]
            if map[g][i]=="#":
                for x,y in li:
                    if map[g+x][i+y]=="?":
                        map[g+x][i+y]="."
            elif map[g][i]==".":
                for x,y in li:
                    if map[g+x][i+y]=="?":
                        map[g+x][i+y]="#"
            else:
                for x,y in li:
                    if map[g+x][i+y]=="?":
            
            if "#" in tmp3 and "." in tmp3:
                tmp="impossible"
                break
            else:
            
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))