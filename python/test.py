def comb(x2,y2):
    x=((x2+y2)//3)
    y=y2-x   
    #xCy
    x,y=max(x,y),min(x,y)
    res=1
    for i in range(min(x-y,y)):
        res*=(x-i)
        res/=(min(x-y,y)-i)
        res%=1000000007
    return int(res)

def comb2(x2,y2):
    x=((x2+y2)//3)
    y=y2-x    
    #xCy
    x,y=max(x,y),min(x,y)
    res=1
    for i in range(min(x-y,y)):
        res*=(x-i)
        res/=(min(x-y,y)-i)
    res%=1000000007
    return int(res)
def perm(x,y):

    #xPy
    x,y=max(x,y),min(x,y)
    res=1
    for i in range(1,y-x):
        res*=i
calc={
    'permutation':perm,
    'combination':comb,
    'combination2':comb2
    
}
print(calc['combination'](999999,999999))
print(calc['combination2'](999999,999999))
