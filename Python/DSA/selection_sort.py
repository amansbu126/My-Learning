arr=[13,46,24,52,20,9]
print("Before sorting:",arr)
result=[]

for i in range(len(arr)-1):#working as a n-2 only beacuse in python range work as n-1
    min=i
    temp=0
    for j in range(i,len(arr)):
        if arr[j]<arr[min]:
            min=j
    arr[i], arr[min] = arr[min], arr[i] #swap

print("After sorting:",arr)