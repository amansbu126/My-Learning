num = int(input("please enter a number to get its factorial"))
Result =1

if num < 0:
    print("sorry, factorial does not exist for negative numbers")
elif num ==0:
    print("the factorial of 0 is 1")
else:
    for i in range(num,1,-1):
        Result = Result*i

    print("the factorial of",num,"is",Result)

    