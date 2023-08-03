res=[]
for m in range(int(input())):
    tmp='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    res.append(tmp[:int(input())])
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))