res=[]
def binary_search(val):
    st=0
    end=val
    while st<=end:
        mid=(st+end)//2
        if mid**3==val:
            return mid
        elif mid**3<val:
            st=mid+1
        else:
            end=mid-1
    return -1

for m in range(int(input())):
    tmp=""
    N=int(input())
    tmp=binary_search(N)
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))