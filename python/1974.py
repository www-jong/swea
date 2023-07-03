ans=[]
p=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
l=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
for m in range(int(input())):
    tmp=1

    li=[list(map(int,input().split())) for _ in range(9)]
    for x in range(9):
        tmpdic_x,tmpdic_y={},{}
        for y in range(9):
            if li[x][y] not in tmpdic_x:
                tmpdic_x[li[x][y]]=1
            else:
                tmp=0
                break
            if li[y][x] not in tmpdic_y:
                tmpdic_y[li[y][x]]=1
            else:
                tmp=0
                break
    for x,y in l:
        tmpdic={}
        for dx,dy in p:
            if li[x+dx][y+dy] not in tmpdic:
                tmpdic[li[x+dx][y+dy]]=1
            else:
                tmp=0
                break
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))