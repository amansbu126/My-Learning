n=5
list=[2,3,6,6,5]
list.sort()
new=[]
seen=set()

for i in list:
    if i not in seen:
        new.append(i)
        seen.add(i)
print(new[-2])
