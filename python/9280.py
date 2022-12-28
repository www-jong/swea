res=[]
for m in range(int(input())):
    tmp=0
    n,m=map(int,input().split())
    park_money=[0]
    car_weight=[0]
    waiting=[]
    park=[i for i in range(1,n+1)]
    parked_car={}
    for i in range(n):
        park_money.append(int(input()))

    for i in range(m):
        car_weight.append(int(input()))
        
    for i in range(m*2):
        x=int(input())
        if x<0:# 나감
            tmp_idx=0
            for j in range(len(park)):#출차된 주차장자리를 순서에 맞게 넣기
                if parked_car[-x]<park[j]:
                    park.insert(max(j,0),parked_car[-x])
                    break
                if j==(len(park)-1):
                    park.append(parked_car[-x])
            if len(park)==0:
                park.append(parked_car[-x])
            if waiting:
                tmp+=car_weight[waiting[0]]*park_money[park[0]]
                #print(f'++ {waiting[0]}번자동차가 {park[0]}에 주차, 비용은 {car_weight[waiting[0]]*park_money[park[0]]}')
                parked_car[waiting[0]]=park[0]
                park.pop(0)
                waiting.pop(0)
        else:# 들어옴
            if len(park)!=0: #만차가 아니면
                tmp+=car_weight[x]*park_money[park[0]]
                #print(f'++ {x}번자동차가 {park[0]}에 주차, 비용은 {car_weight[x]*park_money[park[0]]}')
                parked_car[x]=park[0]
                park.pop(0)
            else:
                waiting.append(x)

    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))


'''
1,2,3,4,5,6,7,8,9,10

1,2,3,4,5 참 fir=6,7,8,9,10
4가 빠짐 -> fir=4,6,7,8,9,10
4에 참 -> fir=?   6,7,8,9,10
i) 5,3,1빠짐 -> fir=5,6,7,8,9,10 , 3,5,6,7,8,9,10   1,3,5,6,7,8,9,10
ii) 1,5,3빠짐 -> 1,6,7,8,9,10 , ???

1,2,3,4,5 참 fir=6,7,8,9,10



'''