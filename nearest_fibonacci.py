num=int(input())
first = 0
second = 1
third = first + second
while (third <= num):
    first = second
    second = third
    third = first + second
if (abs(third - num) >
    abs(second - num)):
    ans =  second
elif(abs(third - num) == abs(second - num)):
    print(second,third,end=" ")
else:
    ans = third
print(ans)