ans=[]
def func(a):
    if int(a)<40:
        a=40
    return int(a)
for m in range(int(input())):
    tmp=0
    li=list(map(func,input().split()))
    tmp=sum(li)//len(li)
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))