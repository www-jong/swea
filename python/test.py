a=151566
b=''
for i in sorted(list(str(a)),reverse=True):
    b+=i
b=int(b)
print(b)