res=[]
for m in range(int(input())):
    tmp=0
    N,R=map(int,input().split())
    upp=1
    down=1
    for i in range(1,N+1):
        upp*=i
    for i in range(1,N+1-R):
        down*=i
    tmp=(upp/down)%1234567891
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
페르마 소정리 필수!

'''