ans=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    loc=[]
    for i in range(N):
        x,y,s=map(int,input().split())
        loc.append((x,y,s))
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
x,y,s - > 좌표x,y  군사력 s
군주제(0개), 항복(1개), 공화제(2개이상)
'''