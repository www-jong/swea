tmp=[1]*(1000001)
res=[]
for i in range(2,1000000):
    if tmp[i]==1:
        res.append(i)
        tmp[i::i]=[0]*(1000000//i)
print(res)
print(res[-1])