nums = [4, 1, 2, 1, 2,5]

dict={}
result=[]

for num in nums:
    dict[num]=dict.get(num,0)+1

print(dict)
new=list(dict.items())
print(new)
for item in new:
    if item[1]==1:
        result.append(item[0])
print(result)