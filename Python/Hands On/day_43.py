nums = [5, 3, 5, 2, 3, 8, 2]
new=[]

for num in nums:
    if num not in new:
        new.append(num)
new.sort()
print(new)