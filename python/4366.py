for m in range(int(input())):
    double=input()
    three=input()
    a,b=[],[]
    for i in range(len(double)):
        a.append(int(double[:i]+('0'if double[i]=='1' else '1')+double[i+1:],2))
    for i in range(len(three)):
        b.append(int(three[:i] + ('0' if three[i] == '1' else '1') + three[i + 1:], 3))
        b.append(int(three[:i] + ('2' if three[i] == '1' else '1') + three[i + 1:], 3))
        b.append(int(three[:i] + ('1' if three[i] == '2' else '2') + three[i + 1:], 3))
        b.append(int(three[:i] + ('0' if three[i] == '2' else '2') + three[i + 1:], 3))
        b.append(int(three[:i] + ('1' if three[i] == '0' else '0') + three[i + 1:], 3))
        b.append(int(three[:i] + ('2' if three[i] == '0' else '0') + three[i + 1:], 3))

    for i in a:
        if i in b:
            print(f'#{m+1}',i)
            break