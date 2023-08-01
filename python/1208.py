res=[]
def flatten():
    idx=0
    while True:
        if idx==99 or boxs[idx]<=boxs[idx+1]:
            break
        else:
            boxs[idx],boxs[idx+1]=boxs[idx+1],boxs[idx]
            idx+=1
    idx=99
    while True:
        if idx==0 or boxs[idx]>=boxs[idx-1]:
            break
        else:
            boxs[idx],boxs[idx-1]=boxs[idx-1],boxs[idx]
            idx-=1

for m in range(10):
    tmp=""
    dumps=int(input())
    boxs=list(map(int,input().split()))
    boxs.sort()
    for _ in range(dumps):
        boxs[0]+=1
        boxs[99]-=1
        flatten()
    res.append(boxs[99]-boxs[0])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))