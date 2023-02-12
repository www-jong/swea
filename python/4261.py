res=[]
dic={'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4',
    'j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7',
    't':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
for m in range(int(input())):
    tmp=0
    S,N=map(str,input().split())
    words=map(str,input().split())
    for word in words:
        s=''
        for i in word:
            s+=dic[i]
        if s==S:
            tmp+=1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))