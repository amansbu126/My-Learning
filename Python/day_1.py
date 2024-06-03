# defining the function to check if a number is even or odd
def evenOdd(n):
    # if remainder is 0 then num is even
    if(n==0):
        return True
    # if remainder is 1 then num is odd
    elif(n==1):
        return False
    else:
      return  evenOdd(n-2)

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is even or odd using the evenOdd function
if(evenOdd(num)):
  print(num,"Its an even number")
else:
  print(num,"Its a odd number")

#RecursionError: maximum recursion depth exceeded
#The "RecursionError: maximum recursion depth exceeded" occurs when a recursive function calls itself too many times without reaching a base case. In Python, there's a limit to how deep the recursion can go, and when that limit is reached, Python raises this error to prevent a stack overflow.

#In the code provided, the issue likely arises because the evenOdd function is being called with large numbers. Since it's subtracting 2 from the number in each recursive call, it might take many iterations to reach the base cases (0 or 1), especially for large numbers.

#To fix this issue, you can modify the code to handle larger numbers more efficiently. One way to do this is to use iteration instead of recursion. Here's the modified code using iteration: