for m in range(int(input())):
    ans=[]
    tmp="TAK"
    N=int(input())
    bp=[]
    for _ in range(min(3,N)):
        x,y,z=map(float,input().split())
        bp.append([x,y,z])
    if N<=3:
        ans.append("#"+str(m+1)+" TAK")
    else:
        x1,y1,z1=bp[0]
        x2,y2,z2=bp[1]
        x3,y3,z3=bp[2]
        A=y1*(z2-z3)+y2*(z3-z1)+y3*(z1-z2)
        B=z1*(x2-x3)+z2*(x3-x1)+z3*(x1-x2)
        C=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
        D=x1*(y2*z3-y3*z2)+x2*(y3*z1-y1*z3)+x3*(y1*z2-y2*z1)
        for _ in range(N-3):
            x,y,z=map(float,input().split())
            if (A*x+B*y+C*z)!=D:
                tmp="NIE"
                break
        ans.append("#"+str(m+1)+" "+str(tmp))
    print(*ans)