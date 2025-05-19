import random

friends = ['Aman','Shaily','Rishab','Tanya','Vivek']

#Option 1
print(random.choice(friends))

#Option 2
random_index=random.randint(0,4)
print(friends[random_index])