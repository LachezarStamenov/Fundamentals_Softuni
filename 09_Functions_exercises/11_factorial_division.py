def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return x * factorial(x - 1)


# to take input from the user for two numbers
num1 = int(input())
num2 = int(input())

# call the factorial function
result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")

# Second way! Mario Zahariev

# def factorial(num):
#     return 1 if num == 0 or num == 1 else num * factorial(num - 1)
#
#
# num1 = int(input())
# num2 = int(input())
# result = factorial(num1)/ factorial(num2)
# print(f'{result:.2f}')