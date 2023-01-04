res=[]
MAXNUM=1000
so=[]
sodic={}
li=[1]*(MAXNUM+1)
for i in range(2,MAXNUM):
    if li[i]==1:
        for j in range(i*2,MAXNUM,i):
            li[j]=0
        so.append(i)
        sodic[i]=1
for m in range(int(input())):
    tmp=0
    minus_tmp=0
    all_compare_tmp=0
    N=int(input())
    dic={}
    for i in so:
        for j in so:
            for z in so:
                if (i+j+z)>N:
                    break
                elif (i+j+z)==N:
                    checker=0
                    for o in (str(i)+str(j)+str(z),str(i)+str(z)+str(j),str(j)+str(i)+str(z),str(j)+str(z)+str(i),str(z)+str(i)+str(j),str(z)+str(j)+str(i)):
                        if o not in dic:
                            dic[o]=1
                            checker=1
                    if checker==1:
                        print(f'i:{i}, j:{j}, z:{z}')
                        tmp+=1
                    
    print(f'tmp : {tmp} minus_tmp : {minus_tmp} all,, {all_compare_tmp}')
    res.append(tmp-minus_tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))