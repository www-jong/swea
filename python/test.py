dic={'슈퍼E':[66000,17325],'멜로시라':[130000,31500],'세럼':[99000,25500],'스킨':[88000,22500],
    '폼클':[48000,12000],'마스크':[65000,15750]}
for item in dic:
    value=dic[item][0]
    point=dic[item][1]
    print(f'{item} : {point}, {value} -> {point/value}')
print('---------------')

total_value=0
total_point=0
cart=[['슈퍼E',2],['멜로시라',1],['스킨',1],['마스크',1]]
items=''
for item,count in cart:
    if count==0:
        continue
    total_value+=dic[item][0]*count
    total_point+=dic[item][1]*count
    items+=item+' '+str(count)+'개, '
print(items)
print(f'총금액 : {total_value}, 총 PV : {total_point}')
    
'''
슈퍼E [66000,17325]
멜로시라 [130000,31500]
세럼 [99000,25500]
스킨 [88000,22500]
폼클 [48000,12000]
마스크 [65000,15750]
'''