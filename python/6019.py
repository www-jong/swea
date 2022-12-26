res=[]
for m in range(int(input())):
    tmp=""
    D,A,B,F=map(int,input().split())
    end_time=D/(A+B)
    tmp=end_time*F
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))