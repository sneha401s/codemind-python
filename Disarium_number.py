n=int(input())
l=len(str(n))
a=n
s=0
while a>0:
    d=a%10
    s=s+int(d**l)
    a=a//10
    l=l-1
if(s==n):
    print("True")
else:
    print("False")