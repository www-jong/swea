ans=[]

def func(words):
    global tmp
    for i in range(1,len(words)-1):
        tmpnums=[]
        for j in range(i+1,len(words)):
            if words[i]==words[j]:
                tmpnums.append(j)
        for endpoint in tmpnums:
            a=0
            while i+a<endpoint-a:
                if words[i+a]==words[endpoint-a]:
                    a+=1
                else:
                    a=-1
                    break
            if a!=-1:
                if tmp<(endpoint-i+1):
                    tmp=endpoint-i+1

for m in range(10):
    _=input()
    tmp=1
    li1=['1']
    li2=['0']*101

    for i in range(100):
        words=input()
        func('0'+words)
        for j in range(100):
            li2[j+1]+=words[j]    
    for i in range(1,101):
        func(li2[i])
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))