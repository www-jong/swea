res=[]

def func():
    
for m in range(int(input())):
    tmp=0
    N,K=map(int,input().split())
    li=sorted(list(map(int,input().split())))
    dic={}
    for i in li:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
dp=
'''