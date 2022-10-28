def checker(x,y):
    for i in range(1,9):
        if map[x][i]=="O" and i!=y:
            return True
        if map[i][y]=='O'and i!=x:
            return True
    return False
ans=[]
for m in range(int(input())):
    map=[[0]*9]
    tmp="yes"
    co=0
    li=[]
    for i in range(8):
        t=input()
        for g in range(8):
            if t[g]=='O':
                co+=1
                li.append((len(map),g+1))
        t=[0]+list(t)
        map.append(t)
    if co!=8:
        tmp="no"
    else:
        for x,y in li:
            if checker(x,y):
                tmp="no"
                break
            
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))