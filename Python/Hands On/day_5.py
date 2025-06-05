a = int(input("please provide your first number"))
b = int(input("please provide your second number"))
option = input("please provide your option lcm/hcf")

hcf=1

if option=='hcf':
    for i in range(2,a+1):
        if(a%i==0 and b%i==0):
            hcf=i
    print(hcf)

elif option=='lcm':
    for i in range(2,a+1):
        if(a%i==0 and b%i==0):
            hcf=i
    lcm = (a*b)/hcf
    print(lcm)

else:
    print("choice not listed please try again")

