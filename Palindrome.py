n=int(input())
sum=0
t=n
while n>0:
    d=n%10
    sum=sum*10+d
    n=n//10
if(t==sum):
    print("True")
else:
    print("False")