words = ["apple", "banana", "pear", "kiwi"]

result = sorted(words, key=lambda w: (-len(w), w))

print(result)
