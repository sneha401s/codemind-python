n=int(input())
array=list(map(int,input().split()))
summ=0
for i in range(0,n):
    if(array[i]%2==0):
        summ+=array[i]
print(summ)