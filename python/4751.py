for m in range(int(input())):
    s=input()
    res="..#."*len(s)+".\n"+".#.#"*len(s)+'.\n#.'+'.#.'.join()+'.#\n'+".#.#"*len(s)+'.\n#.'+'..#.'*len(s)+'.'
    print(res)