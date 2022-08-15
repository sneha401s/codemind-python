for i in range(int(input())):
    n=int(input())
    l=list()
    while n!=0:
        r=n%2
        l.append(r)
        n=n//2
    l.reverse()
    separator=""
    print(separator.join(map(str,l)))