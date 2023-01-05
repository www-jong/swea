res=[]
for m in range(int(input())):
    tmp="Exist"
    S=input()
    null_value={}
    for i in range(len(S)//2 if len(S)%2==0 else len(S)//2+1):
        print(f'{i}번째, ',end="")
        if S[i]!=S[len(S)-1-i] and (S[i]=="?" or S[len(S)-i-1]=="?"):
            tmp="Not exist"
            print(f'No, {S[i]}:{i} , {S[len(S)-i-1]}:{len(S)-i-1}')
            break
        else:
            print('yes')
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
4 ->(0,1,2,3) , 0,1
5 ->(0,1,2,3,4) , 0,1,2
'''