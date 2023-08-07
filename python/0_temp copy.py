I,R,f=input,range,int
def o(n):
 return ''if n==0 else o(n//3)+str(n%3)
def sol(n):
    return '' if n==0 else sol(n//3)+str(n%3)
def ck(n):
 if n==0:return '0'
 t=str(f(o(n)))
 li,ch=[0]*len(t),0
 for i in R(len(t)-1,-1,-1):
  c=t[i]
  if c=='1':li[i]='1';ch=(i==0)if ch else 1
  elif c=='0':li[i]='1' if ch else '0';ch=0
  else:li[i]='0' if ch else '1';ch=(i==0)if ch else 1
  if i==0:li.insert(0,'1')
 return ''.join(li)

def ck2(n):
    if n==0:return '0'
    t=str(int(sol(n)))
    li,ch=[0]*(len(t)),0
    for i in range(len(t)-1,-1,-1):
        c=t[i]
        if c=='1':
            if ch and i==0:li.insert(0,'1')
            li[i]='1'
        elif c=='0':
            li[i]='0'
            if ch:
                li[i]='1'
            ch=0
        else:
            if ch:li[i]='0'
            else:
                li[i]='1'
                ch=1
            if i==0:li.insert(0,'1')
    return ''.join(li)

def ck3(n):
    if n==0:return '0'
    t=str(int(sol(n)))
    li,ch=[0]*(len(t)),0
    for i in range(len(t)-1,-1,-1):
        c=t[i]
        if ch:
            if c in'01':
                li[i]='1'
                if i==0:li.insert(0,'1')
            else:li[i]='0'

        if t[i]=='1':
            if ch:
                li[i]='1'
                if i==0:li.insert(0,'1')
            else:li[i]='1'
        elif t[i]=='0':
            if ch:
                li[i]='1'
                ch=0
            else:li[i]='0'
        else:
            if ch:li[i]='0'
            else:
                li[i]='1'
                ch=1
            if i==0:li.insert(0,'1')
    return ''.join(li)

print(ck(29))
print(ck2(29))

print(ck2(325))