import matplotlib.pyplot as plt

n=59
li=[0]
for i in range(1,n+1):
    li.append(i*(n-i))
print(li)
plt.plot(li)
plt.show()