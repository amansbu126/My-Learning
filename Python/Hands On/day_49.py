nums = [1,2,3,4,5,6]
new=[]
for num in nums:
    if (num % 2 == 0) != (num % 3 == 0):
        new.append(num)
print(new)