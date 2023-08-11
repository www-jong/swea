#1 1 2 3 5 8 13 
li=[]
for i in range(5):
    n=int(input())
    li.append(n)

fi=[0,1]
for i in range(2,max(li)+1):
    fi.append(fi[i-1]+fi[i-2])
for i in li:
    print(fi[i])