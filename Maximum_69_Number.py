n=int(input())
s=str(n)
if '6' not in s:
    print(s)
else:
    nlist=list(s)
    nlist[nlist.index('6')]='9'
    print(int(''.join(nlist)))