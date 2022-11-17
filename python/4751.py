ans=[]
for m in range(int(input())):
    N=input()
    tmp=[""]*5
    tmp[0]="..#.."+".#.."*(len(N)-1)
    tmp[4]=tmp[0]
    tmp[1]=".#.#."+"#.#."*(len(N)-1)
    tmp[3]=tmp[1]
    tmp[2]="#"
    for i in N:
        tmp[2]+="."+i+".#"
    ans.append(tmp)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j])