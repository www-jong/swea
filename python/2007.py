res=[]
for m in range(int(input())):
    tmp=""
    S=input()
    for i in range(1,11):
        li=[]
        ch=0
        j=0
        while True:
            if i*(j+1)>30:
                li.append(S[i*j:30])
                break
            li.append(S[i*j:i*(j+1)])
            j+=1

        print(li)
        print(list(set(li)))
        if len(list(set(li[:-2])))==1:
            if li[0]==li[-1]:
                ch=1
            elif li[-1] in li[0]:
                ch=1
        if ch==1:
            tmp=i
            #print(li)
            break
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))