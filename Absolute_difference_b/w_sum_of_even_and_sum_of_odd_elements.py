n=int(input())
array=list(map(int,input().split()))
ce=0
co=0
for i in range(0,n):
    if(array[i]%2==0):
        ce+=array[i]
    else:
        co+=array[i]
print(abs(ce-co))