decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/'
      ]
res=[]
for m in range(int(input())):
    tmp=""
    ress=''
    word=list(input())
    for i in range(len(word)):
        num=decode.index(word[i])
        bnum=str(bin(num)[2:])
        while len(bnum)<6:
            bnum='0'+bnum
        ress+=bnum
    for i in range(len(word)*6//8):
        e=int(ress[i*8:i*8+8],2)
        tmp+=chr(e)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))