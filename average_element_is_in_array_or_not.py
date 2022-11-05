n=int(input())
array=list(map(int,input().split()))
avrg=sum(array)//n
if avrg in array:
    print("True")
else:
    print("False")