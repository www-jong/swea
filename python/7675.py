res=[]
tmp_N=0
for m in range(int(input())):
    tmp=""
    N=int(input())
    count_N=0
    words=[]
    tmp_words=""
    while count_N!=N:
        ttmp=input()
        print(f'count : {count_N}')
        for i in ttmp:
            if i=="!" or i=="." or i=="?":
                words.append(tmp_words)
                count_N+=1
                tmp_words=""
            else:
                tmp_words+=i
    for line in words:
        names=0
        for word in list(map(str,line.split())):
            if ord(word[0])>=65 and ord(word[0])<=90:
                check=0
                for i in word[1:]:
                    if ord(i)<=96 or ord(i)>=123:
                        check=1
                        break
                if check==0:
                    names+=1
        tmp+=str(names)+" "

    print(words)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))