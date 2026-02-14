word = input("Please provide a word ")

new = ''
for i in range(len(word)):
    if word[i] in 'aeiou':
        continue
    new+=word[i]
    
print(new)