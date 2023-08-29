dic=dict(zip(('A','B','C','D','E','F'),(10,11,12,13,14,15)))
def sixteen_to_binary(code):
    zero_count=0
    for i in range(len(code)):
        if code[i]!='0':
            zero_count=i
            break
    tmp=0
    idx=len(code)-1
    for i in range(len(code)-1,-1,-1):
        num=int(code[i]) if code[i].isnumeric() else int(dic[code[i]])
        tmp+=num*(16**(idx-i))
    return '0'*zero_count+bin(tmp)[2:].rstrip('0')

print(sixteen_to_binary('00000000000000000000000000000000000000000000000000000000000000000000000'))