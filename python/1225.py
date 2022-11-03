ans=[]
for m in range(2):
    tmp=""
    _=input()
    li=list(map(int,input().split()))
    c=1
    if min(li)>15:
        g=min(li)//15
        for i in range(8):
            li[i]=li[i]-15*(g-1)
    while True:
        if c==6:
            c=1
        if li[0]==0 or li[0]-c<=0:
            li[0]=0
            li.append(li.pop(0))
            break
        else:
            li[0]-=c
            li.append(li.pop(0))
        c+=1
    for i in li:
        tmp+=str(i)+" "
    
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
0 0 0 0 0 0 0 0
-1 -2 -3 -4 -5 0 0 0
0 0 0 -1 -2 -3 -4 - 5
-1 -2 -3 -5 -7 -3 -4 -5
-3 -4 -5 -1 -2 -3 -5 -7
1 2 3 4 5 -> 15
1 2 3 4 5 6 7 8
6 7 8 1 2 3 4 5
3 4 5 6 7 8 1 2
8 1 2 3 4 5 6 7
5 6 7 8 1 2 3 4
2 3 4 5 6 7 8 1
7 8 1 2 3 4 5 6
4 5 6 7 8 1 2 3
1 2 3 4 5 6 7 8
'''