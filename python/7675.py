res=[]
for m in range(int(input())):
    tmp=""
    N=int(input())
    words=list(map(str,input().split('!').split('?').split('.')))
    print(words)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))