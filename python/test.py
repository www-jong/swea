a=0
f=0
for i in range(1,10**10,2):
    if f==0:
        a+=1/i
        f=1
    else:
        a-=1/i
        f=0
print(a*4)