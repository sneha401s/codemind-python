n=int(input())
array=list(map(int,input().split()))
li=[]
for i in range(0,n):
    if(array[i]%2==0):
        li.append(array[i])
print(li[-1])