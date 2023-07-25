res=[]

for m in range(int(input())):
    tmp=0
    x,y=map(int,input().split())
    if (x+y)%3!=0:
        res.append(0)
        continue
    h=((x+y)//3)
    w=y-h+1            # h C (w-1) 문제.
    
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))

'''
2,1 1,2 -> 1 ,1        1행

4,2 3,3 2,4 -> 1, 2, 1  2행

6,3 5,4 4,5 3,6 ->1 3 3 1  3행

8,4 7,5 6,6 5,7 4,8  -> 1 4 6 4 1  4행

10,5  9,6 8,7 7,8 6,9 5,10   1 5 10 10 5 1   5행
            

1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1

3
6
9
12
15
'''