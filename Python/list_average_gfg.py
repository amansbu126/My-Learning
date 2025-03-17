arr=[5,0,0,0]
new_list=[]
cnt=0
res=0
for number in arr:
  if number>=0:
    new_list.append(number)
print(new_list)
cnt=int(len(new_list))
print(cnt)
for i in new_list:
  res=(i+res)
print(res/cnt)