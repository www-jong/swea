def apd(word):
    ress=set()
    for i in word:
        if ord(i)>=97 and ord(i)<=122:
            ress.add(i)
    return ress
print(apd('apple'))
print(apd('apple')|apd('tree'))