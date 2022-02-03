def prime_checker(number):
    """ This is a function for finding
    if the number is prime or not!"""
    for n in range(2, (number)):
        if number % n == 0:
            return False
    return True

n = int(input("Check this number: "))

if prime_checker(n):
    print("It's a prime num.")
else:
    print("It's not a prime num.")

