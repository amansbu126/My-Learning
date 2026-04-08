nums = [5, 3, 5, 2, 3, 8, 2]
d={}

for num in nums:
    d[num]=d.get(num,0)+1

transformed=[]

for num, count in d.items():
    transformed.append((-count,num))

transformed.sort()

result=[]

for count,num in transformed:
    result.append(num)
print(result)