def factorial(x):
    if x == 0:
        return 1
    return x*factorial(x-1)

x = int(input("Enter the number whose factorial is to be found"))

if x < 0:
    print('Please entewr positive numbers')
else:
    print("the factorail of number",x,"is",factorial(x))
