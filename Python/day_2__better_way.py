num1 = int(input("please provide the first number"))
num2 = int(input("please provide the first number"))

operator = input("please select + operator for addition or * for muliplication")

if operator=='*':
  result = num1 * num2

elif operator=='+':
  result = num1 + num2

else:
  print('Oh ho i am sorry you have selected incorrect operator' )
  exit()

print("Result:", result)