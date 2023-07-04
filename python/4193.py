from collections import deque
# 파이썬 제출 불가; 문제덜품
res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    li=[list(map(int,input().split())) for _ in range(N)]
    visit=[[0]*N for _ in range(N)]
    start=list(map(int,input().split()))
    end=list(map(int,input().split()))
    
    q=deque()
    q.append(start)
    while q:
        x,y=q.popleft()
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))


'''
1 = 벽
2 = 소용돌이 0~1 x, 2 o 3~4 x

'''