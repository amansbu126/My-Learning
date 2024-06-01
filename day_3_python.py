num = int(input("please provide the year to check if its a leap year or a non leap year"))

if (((num % 400 == 0) or (num % 4 == 0 and num % 100 != 0))):
    print(num,"its a leap year")

else:
    print(num,"its a non leap year")