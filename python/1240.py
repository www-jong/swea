ans=[]
for m in range(int(input())):
    tmp=""
    N,M=map(int,input().split()) # N,M=세로,가로
    

    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
8개숫자
홀수자리합*3 + 짝수자리합 = 10의배수

'''