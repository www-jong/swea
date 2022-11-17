ans=[]
for m in range(10):
    tmp=0
    n=int(input())
    li=[[0]*101]
    for i in range(100):
        li.append([0]+list(map(int,input().split())))
    
    for i in range(1,101):
        ch1,ch2=0,0
        co=0
        for j in range(1,101):
            if li[j][i]==0:
                continue
            if li[j][i]!=0 and ch1==0:
                if li[j][i]==1:
                    ch1=1
                else:
                    pass
                    #ch1=2
            elif li[j][i]==ch1:
                co+=1
            else:
                tmp+=1
                ch1=0
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))
'''
1=N, 2=S
N이 위, S가 아래
'''