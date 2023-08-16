for m in range(10):
    n=int(input())
    s=input()
    stk=[]
    idx=0
    while idx<n:
        if s[idx].isdigit():
            stk.append(int(s[idx]))
        elif s[idx]=="*":
            a,b=stk.pop(),int(s[idx+1])
            stk.append(a*b)
            idx+=1
        else:
            idx+=1
        idx+=1

    print(f'#{m+1}',sum(stk))