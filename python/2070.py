res=[]
for m in range(int(input())):
    tmp=""
    li=list(map(int,input().split()))
    if li[0]>li[1]:
        tmp=">"
    elif li[0]==li[1]:
        tmp="="
    else:
        tmp="<"
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))