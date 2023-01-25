res=[]
def change(idx,count):
    global C,tmp
    if count==C:
        tmp=
    
for m in range(int(input())):
    tmp=0
    S,C=map(str,input().split())
    maxval=''
    for i in sorted(list(str(S)),reverse=True):
        maxval+=i
    change(S,int(C))
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))