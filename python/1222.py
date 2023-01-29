res=[]
for m in range(10):
    tmp=0
    N=int(input())
    S=input()
    stack=[]
    postfix=''
    cal=[]
    for i in S:
        if not stack and i=="+":
            stack.append(i)
        elif stack and i=='+':
            postfix+=stack.pop()
            stack.append(i)
        else:
            postfix+=i
    else:
        postfix+=stack.pop()

    for i in postfix:
        if i!='+':
            cal.append(int(i))
        elif i=='+':
            cal.append(cal.pop()+cal.pop())
    tmp=cal.pop()
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
주어진 계산식을 후위표기식으로
1- 숫자인 경우 바로출력
2- +기호인 경우 스택이 비었는지 확인
    2-1 - 스택이 비었을 경우 스택에 push
    2-2 - 스택이 차있을 경우 pop하고 출력
3 - 입력을 다 읽고 난 뒤, 스택의 내용을 출력
계산법
1- 숫자일 경우 스택에 push
2- +일 경우 스택의 2개 숫자를 뽑아 더하고 다시 push
3- 입력을 다 읽었을때 스택의 결과를 출력
'''