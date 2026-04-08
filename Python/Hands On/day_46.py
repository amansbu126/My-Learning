nums = [5, 3, 5, 2, 3, 8, 2]

dict={}

for num in nums:
    dict[num]=dict.get(num,0)+1
new=list(dict.items())
new.sort(key=lambda x:(-x[1],x[0]))
result=[]
for item in new:
    result.append(item[0])
print(result)