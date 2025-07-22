a = [1, 1, 2]

new = []
seen = set()

for num in a:
    if num not in seen:
        new.append(num)
        seen.add(num)
print(new)