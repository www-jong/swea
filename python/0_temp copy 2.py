res=[]
for m in range(10):
    tmp=0
    S=input()
    stack=[]
    post=[]
    for i in S:
        if not stack and i in "()+*":
            stack.append(i)
        if stack and i in "()+*":
            
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))