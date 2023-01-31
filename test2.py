dic={'슈퍼E':[66000,17325],'멜로시라':[130000,31500],'세럼':[99000,25500],'스킨':[88000,22500],
    '폼클렌져':[48000,12000],'마스크':[65000,15750],'아이크림':[120000,31500],'오리지널크림':[245000,65250],
    '마스크세트':[300000,72690],'이너케어':[300000,78750],'아이업 골든타임':[260000,45500]}
minpv=105000
cart_list=[]
overlap_checker={}

def cart_read(items_series,type=0):
    items_txt=""
    tmp_items_names=[]
    for i in  items_series[0]:
        tmp_items_names.append(i)
    for i in sorted(tmp_items_names):
        items_txt+=i+" "+str(items_series[0][i])+"개,"
    items_txt=items_txt.rstrip(",")
    if type==0:
        items_txt+=" "+str(items_series[1])+"원 "+str(items_series[2])+"pv"
    return items_txt


def search(item_list,money,now_pv):
    if money>=500000 or now_pv>=120000:
        return
    if now_pv>=minpv:
        if cart_read([item_list.copy(),money,now_pv],1) in overlap_checker:
            return
        cart_list.append([item_list.copy(),money,now_pv])
        overlap_checker[cart_read([item_list.copy(),money,now_pv],1)]=1
        return
    for item in dic:
        value=dic[item][0]
        point=dic[item][1]
        if item in item_list:
            item_list[item]+=1
        else:
            item_list[item]=1
        search(item_list,money+value,now_pv+point)
        if item_list[item]==1:
            del item_list[item]
        else:
            item_list[item]-=1

search({},0,0)
cart_list.sort(key=lambda x:x[1])
print(f'총 방법 수 : {len(cart_list)}')
f=open("./list.txt",'w',encoding="utf-8")
for i in cart_list:
    tmp_str=cart_read(i)
    f.write(tmp_str+"\n")
f.close()
