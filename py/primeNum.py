def is_prime(number):
    if number < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(number**0.5) + 1):  # Check divisors up to the square root of the number
        if number % i == 0:
            return False
    return True

# Check if a given number is prime
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
