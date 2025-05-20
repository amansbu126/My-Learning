import random

letters=['a','A','b','B','c','C','d','D','e','E','f','F','g','G',
'h','H','i','I','j','J','k','K','l','L','m','M','n','N',
'o','O','p','P','q','Q','r','R','s','S','t','T','u','U',
'v','V','w','W','x','X','y','Y','z','Z']

numbers=[0,1,2,3,4,5,6,7,8,9]

special=['!','@','#','$','%','^','&','*','?','~']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_special = int(input("How many special would you like in your password?\n"))

my_letters=[]
for i in range(0,nr_letters):
    new_string=random.choice(letters)
    my_letters.append(new_string)

my_numbers=[]
for i in range(0,nr_numbers):
    new_numbers=random.choice(numbers)
    my_numbers.append(new_numbers)
b= list(map(str,my_numbers))

my_special=[]
for i in range(0,nr_special):
    new_special=random.choice(special)
    my_special.append(new_special)

concatenated_string=""
for lst in [my_letters,b,my_special]:
    for s in lst:
        concatenated_string+=s
print(f"Your password is:{concatenated_string}")