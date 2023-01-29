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
        if not stack and (i=='+' or i=='*'):
            stack.append(i)
        elif stack and (i=='+' or i=='*'):
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

'''
우선순위가 들어간다
*, +, 숫자순으로 우선순위가 높음(*가 가장 높음)

중위 -> 후위
1- 숫자일 경우 바로출력
2- +,*일경우 스택이 비어있는 지확인
     2-1 - 스택이 비었을 경우 push
     2-2 - 스택이 차있을 경우
        a- 입력이 스택의 맨위값보다 우선순위 높으면 push
        b- 입력이 스택의 맨위값보다 우선순위 낮거나 같으면 스택을 pop하고 입려글 push
'''