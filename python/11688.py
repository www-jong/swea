ans=[]
for m in range(int(input())):
    tmp=[1,1]
    Root=input()

    for i in Root:
        if i=="L":
            tmp[1]=tmp[0]+tmp[1]
        else:
            tmp[0]=tmp[0]+tmp[1]
    tmp=str(tmp[0])+" "+str(tmp[1])
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))

'''
         1
    2          3
  4   5     6     7
8 9 10 11 12 13 14 15 

n (n%2)+1 
'''