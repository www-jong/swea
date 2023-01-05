res=[]
for m in range(int(input())):
    tmp="NO"
    N=int(input())
    li=[0]
    visited=[[0]*(N+1) for i in range(N+1)]
    breaker=0
    for i in range(N):
        S=input()
        li.append([0]+list(S))
    for i in range(1,N+1):
        for j in range(1,N+1):
            if li[i][j]=="o":
                if N-j>=4:
                    ch=1
                    for z in range(1,5):
                        if li[i][j+z]=="o":
                            ch+=1
                    if ch==5:
                        breaker=1
                        break
                if N-i>=4:
                    ch=1
                    for z in range(1,5):
                        if li[i+z][j]=="o":
                            ch+=1
                    if ch==5:
                        breaker=1
                        break

                if (N-i)>=4 and (N-j)>=4:
                    ch=1
                    for z in range(1,5):
                        if li[i+z][j+z]=="o":
                            ch+=1
                    if ch==5:
                        breaker=1
                        break
                if (N-i)>=4 and (j)>=5:
                    ch=1
                    for z in range(1,5):
                        if li[i+z][j-z]=="o":
                            ch+=1
                    if ch==5:
                        breaker=1
                        break
                
                if ch==0:
                    breaker=1
                    break
        if breaker==1:
            tmp="YES"
            break
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))