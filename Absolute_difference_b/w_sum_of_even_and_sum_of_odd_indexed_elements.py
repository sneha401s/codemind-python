def even_odd_count(n):
    n=len(d)
    ec=0
    oc=0
    for i in range(0,n):
        if(i%2==0):
            ec=ec+d[i]
        else:
            oc=oc+d[i]
    print(ec-oc)
    return ec,oc
    
n=int(input())
d=list(map(int,input().split()))
even,odd=even_odd_count(n)