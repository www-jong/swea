res=[]
for m in range(int(input())):
    tmp=""
    dic={'ZRO':0,"ONE":1,"TWO":2,"THR":3,"FOR":4,"FIV":5,"SIX":6,"SVN":7,"EGT":8,"NIN":9}
    re_dic={0:'ZRO',1:'ONE',2:'TWO',3:'THR',4:'FOR',5:'FIV',6:'SIX',7:'SVN',8:'EGT',9:'NIN'}
    _,_=map(str,input().split())
    li=list(map(str,input().split()))
    li2=[]
    for i in range(len(li)):
        li2.append(dic[li[i]])
    li2.sort()
    li=[]
    for i in range(len(li2)):
        tmp+=re_dic[li2[i]]+" "
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))