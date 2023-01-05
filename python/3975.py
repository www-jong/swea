res=[]
for m in range(int(input())):
    tmp=""
    A,B,C,D=map(int,input().split())
    if A/B==C/D:
        tmp="DRAW"
    elif A/B>C/D:
        tmp="ALICE"
    else:
        tmp="BOB"
    res.append("#"+str(m+1)+" "+tmp)
print(*res,sep="\n")