ans=[]
for m in range(int(input())):
    tmp=""
    li={'MON':1,'TUE':2,'WED':3,'THU':4,'FRI':5,'SAT':6,'SUN':0}
    S=input()
    tmp=7-li[S]
    ans.append(tmp)
for i in range(len(ans)):
    print("#%d %s"%(i+1,ans[i]))