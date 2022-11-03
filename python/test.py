a=[5,4,3,2,1,4]
for i in range(10):
    a.append(a.pop(0))
print(a)