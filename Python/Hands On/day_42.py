nums = [3, 7, 2, 9, 4, 6]
new=[]

for num in nums:
    if num%2==0:
        num*=num
        new.append(num)
        new.sort(reverse=True)
print(new)
