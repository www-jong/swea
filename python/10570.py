ans=[]
def check(li):
    for i in range(len(li)-len(li)//2):
        if li[i]!=li[len(li)-i-1]:
            return 0
    return 1

for m in range(int(input())):
    tmp=0
    A,B=map(int,input().split())
    for i in range(1,34):
        if i**2<A or i**2>B:
            continue
        if check(list(str(i)))+check(list(str(i**2)))==2:
            tmp+=1
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))