x,y=map(int,input().split())
if (x+y)%3!=0:
    print(0)
h=((x+y)//3)
w=y-h+1
print(h,w)