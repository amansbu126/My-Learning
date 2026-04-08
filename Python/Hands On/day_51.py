nums = [1,2,2,3,3,3,4]

dict={}

for num in nums:
    dict[num]=dict.get(num,0)+1
#print(dict)
new=list(dict.items())
#print(new)
new.sort(key=lambda x:(x[1]),reverse=True)
#print(new)
print(new[0][0])