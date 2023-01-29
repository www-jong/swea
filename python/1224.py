def priority(a):
    if a=='*':
        return 3
    elif a=='+':
        return 2
    else:
        return 1

res=[]
for m in range(10):
    tmp=0
    N=int(input())
    stack=[]
    post=[]
    cal=[]
    S=input()
    for i in S:
        if not stack and (i in "()*+"):
            stack.append(i)
        elif stack and (i in "()*+"):
            if i=="(":
                stack.append(i)
            elif i==")":
                while stack[-1]!="(":
                    post+=stack.pop()
                stack.pop()
            else:
                while stack:
                    if priority(stack[-1])<priority(i):
                        break
                    else:
                        post+=stack.pop()
                stack.append(i)
        else:
            post+=i
    while stack:
        post+=stack.pop()
    
    for i in post:
        if i not in '*+':
            cal.append(int(i))
        elif i=='+':
            cal.append(cal.pop()+cal.pop())
        elif i=='*':
            cal.append(cal.pop()*cal.pop())
    tmp=cal.pop()
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))